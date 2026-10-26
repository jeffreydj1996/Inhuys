#!/usr/bin/env python3
"""Tekstcontrole voor content/*.md: aanspreekvorm, Engels, plaatshouders, meta-lengtes, verplichte koppen, 7-woord-overlap met oude productteksten (data/raw) en fabrikantteksten (data/bron-teksten).
Gebruik: python3 tools/check_tekst.py content/producten/<handle>.md [...]   Exit 1 bij één of meer FOUT-regels. Alleen foutregels worden geprint, plus één OK-regel per schoon bestand."""
import re, sys, os, glob, json, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U_RE = re.compile(r"\b(u|uw)\b"); EN_RE = re.compile(r"\b(the|and|with|chair|sofa|dining|your|our|seater|lounge chair)\b", re.I)
FAB_RE = re.compile(r"(Fijn voor wie houdt van een interieur dat klopt in detail|Tijdloos ontwerp dat gemakkelijk combineert|InHuys selectie:|Upgrade uw)", re.I)
PRODUCT_KOPPEN = ["## Varianten en prijzen", "## Beschrijving", "### Zo werkt het in de ruimte", "### Materiaal en maakwijze", "### Combineren", "## Specificaties (metavelden `inhuys.*`)", "## Advies van InHuys", "## Veelgestelde vragen"]

def woorden(t): return re.findall(r"[a-zà-ü0-9']+", re.sub(r"<[^>]+>", " ", html.unescape(t)).lower())
def shingles(t, n=7):
    w = woorden(t); return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}
def oude_teksten():
    s = set()
    for f in glob.glob(os.path.join(ROOT, "data", "raw", "products-*.json")):
        for e in json.load(open(f, encoding="utf-8"))["data"]["products"]["edges"]:
            s |= shingles(e["node"].get("descriptionHtml") or "")
    for f in glob.glob(os.path.join(ROOT, "data", "bron-teksten", "*.txt")):
        s |= shingles(open(f, encoding="utf-8", errors="ignore").read())
    return s

def proza(md):
    """Alleen de lopende tekst: geen tabellen, codes, bronkolommen of bijlagen."""
    out = []
    skip = False
    for ln in md.split("\n"):
        if ln.startswith("## Beelden") or ln.startswith("## Opmerking") or ln.startswith("## Aan te vullen"): skip = True
        if ln.startswith("## ") and not (ln.startswith("## Beelden") or ln.startswith("## Opmerking") or ln.startswith("## Aan te vullen")): skip = False
        if skip or ln.startswith("|") or ln.startswith("Handle:") or ln.startswith("Tags:") or ln.startswith("Categorie:") or ln.startswith("Collecties:"): continue
        out.append(re.sub(r"`[^`]*`", "", ln))
    return "\n".join(out)

def controleer(path, oud):
    md = open(path, encoding="utf-8").read(); fouten = []
    tekst = proza(md)
    for m in re.finditer(r"^Meta-titel \((\d+)\): (.*?)\s*$", md, re.M):
        n = len(m.group(2).strip())
        if n > 60: fouten.append(f"meta-titel {n} tekens (max 60)")
    for m in re.finditer(r"^Meta-description \((\d+)\): (.*?)\s*$", md, re.M):
        n = len(m.group(2).strip())
        if n > 160: fouten.append(f"meta-description {n} tekens (max 160)")
        if n < 120: fouten.append(f"meta-description {n} tekens (min 120)")
    for m in U_RE.finditer(tekst): fouten.append(f"u-vorm: '...{tekst[max(0, m.start()-30):m.end()+20].strip()}...'"); break
    en = EN_RE.findall(tekst)
    if len(en) >= 3: fouten.append(f"Engels in de tekst: {sorted(set(x.lower() for x in en))[:5]}")
    if FAB_RE.search(md): fouten.append("sjabloon- of fabrikantzin uit de oude teksten")
    ph = re.findall(r"\[(AANVULLEN|VANAF-PRIJS|OPENINGSTIJDEN)[^\]]*\]", tekst)
    if ph: fouten.append(f"plaatshouder in lopende tekst: {ph[0]}")
    if "Handle: `/products/" in md:
        for k in PRODUCT_KOPPEN:
            if k not in md: fouten.append(f"kop ontbreekt: {k}")
        faq = len(re.findall(r"^\*\*.+\*\*\s*$", md, re.M))
        if faq < 3: fouten.append(f"FAQ heeft {faq} vragen (min 3)")
        if not re.search(r"^\*\*Zin onder de titel:\*\* \S", md, re.M): fouten.append("zin onder de titel ontbreekt")
        w = len(woorden(tekst))
        if w < 250: fouten.append(f"lopende tekst {w} woorden (min 250)")
    overlap = shingles(tekst) & oud
    if overlap: fouten.append(f"{len(overlap)} zinsdelen van 7 woorden komen uit oude product- of fabrikantteksten, bv. '{sorted(overlap)[0]}'")
    return fouten

if __name__ == "__main__":
    oud = oude_teksten(); totaal = 0
    for p in sys.argv[1:]:
        if os.path.basename(p) in ("overzicht.md", "README.md"): continue
        f = controleer(p, oud); totaal += len(f)
        print(f"OK   {p}" if not f else "\n".join(f"FOUT {p}: {x}" for x in f))
    sys.exit(1 if totaal else 0)
