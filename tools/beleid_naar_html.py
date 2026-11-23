#!/usr/bin/env python3
"""Zet een beleidstekst uit content/beleid/<naam>.md om naar HTML voor shopPolicyUpdate (alleen het deel na de eerste '---').
Kopjes (##, ###), alinea's, genummerde en gewone lijsten, **vet**, [links](url) en tabellen. Regels met [AANVULLEN] worden weggelaten.
Gebruik: python3 -I tools/beleid_naar_html.py content/beleid/<naam>.md > data/out/beleid-<naam>.html"""
import html, re, sys

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', t)

def main():
    s = open(sys.argv[1], encoding="utf-8").read()
    s = s.split("\n---\n", 1)[1] if "\n---\n" in s else s
    uit, lijst, alinea, tabel = [], None, [], []
    def sluit():
        nonlocal lijst, alinea, tabel
        if alinea: uit.append("<p>" + inline(" ".join(alinea)) + "</p>"); alinea = []
        if lijst: uit.append(f"</{lijst}>"); lijst = None
        if tabel:
            rijen = [[c.strip() for c in r.strip("|").split("|")] for r in tabel if not re.match(r"^\|[\s|:-]+\|$", r)]
            uit.append("<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in rijen[0]) + "</tr></thead><tbody>"
                       + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rijen[1:]) + "</tbody></table>")
            tabel = []
    for r in s.split("\n"):
        r = r.rstrip()
        if "[AANVULLEN" in r: continue
        if not r: sluit(); continue
        if r.startswith("|"):
            if alinea or lijst: sluit()
            tabel.append(r); continue
        if tabel: sluit()
        m = re.match(r"^(#{2,4})\s+(.*)", r)
        if m: sluit(); n = len(m.group(1)); uit.append(f"<h{n}>{inline(m.group(2))}</h{n}>"); continue
        m = re.match(r"^\s*(\d+\.|[-*])\s+(.*)", r)
        if m:
            soort = "ol" if m.group(1)[0].isdigit() else "ul"
            if alinea: sluit()
            if lijst != soort:
                if lijst: uit.append(f"</{lijst}>")
                uit.append(f"<{soort}>"); lijst = soort
            uit.append(f"<li>{inline(m.group(2))}</li>"); continue
        if lijst: sluit()
        alinea.append(r.strip())
    sluit()
    print("\n".join(uit))

if __name__ == "__main__": main()
