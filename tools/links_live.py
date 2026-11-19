#!/usr/bin/env python3
"""Zet de productlinks in content/producten/*.md goed tegenover wat op de winkel bereikbaar is.
Een link naar een product dat live is (of live gaat) wijst naar de handle die dat product in Shopify heeft; een link naar een product
dat concept blijft, weg kan of niet bestaat verdwijnt (de tekst blijft staan). Markdown-links en <a href> in de beschrijving, het advies
en de FAQ; de sectie "Opmerking" blijft ongemoeid.
Gebruik: python3 -I tools/links_live.py data/orderchamp/varianten-<datum>.json [--naar-live gids.txt] [--naar-concept gids.txt] [--droog]
(gids.txt: één gid per regel of "handle gid"). Schrijft de lijst gewijzigde bestanden naar data/tmp/links-gewijzigd.txt."""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def gids(pad):
    return {w for line in open(pad, encoding="utf-8") for w in line.split() if w.startswith("gid://")} if pad else set()

def main():
    a = sys.argv[1:]; droog = "--droog" in a
    arg = lambda n: a[a.index(n) + 1] if n in a else None
    V = json.load(open(a[0], encoding="utf-8"))                       # shop-handle -> {gid, status, varianten}
    ids = json.load(open(os.path.join(ROOT, "data", "ids.json"), encoding="utf-8"))
    op, af = gids(arg("--naar-live")), gids(arg("--naar-concept"))
    shop = {v["gid"]: h for h, v in V.items()}
    live = {v["gid"] for v in V.values() if v["status"] == "ACTIVE"} | op
    live -= af
    onze = {h: g for h, g in {**ids.get("producten", {}), **ids.get("live_tekst", {})}.items()}
    def doel(naam):                                                    # naam in een link -> shop-handle als live, anders None
        g = V[naam]["gid"] if naam in V else onze.get(naam)
        return shop.get(g) if g in live else None
    gewijzigd, weg, om = [], 0, 0
    for h, g in sorted(onze.items()):
        p = os.path.join(ROOT, "content", "producten", f"{h}.md")
        if not os.path.exists(p) or g not in shop or g not in live: continue   # alleen teksten van producten die live zijn of gaan
        s = open(p, encoding="utf-8").read(); kop, sep, rest = s.partition("## Opmerking")
        tel = [0, 0]
        def md(m):
            d = doel(m.group(2))
            if d is None: tel[0] += 1; return m.group(1)
            if d != m.group(2): tel[1] += 1
            return f"[{m.group(1)}](/products/{d})"
        def html(m):
            d = doel(m.group(1))
            if d is None: tel[0] += 1; return m.group(2)
            if d != m.group(1): tel[1] += 1
            return f'<a href="/products/{d}">{m.group(2)}</a>'
        nieuw = re.sub(r"\[([^\]]+)\]\(/products/([a-z0-9-]+)\)", md, kop)
        nieuw = re.sub(r'<a href="/products/([a-z0-9-]+)">(.*?)</a>', html, nieuw)
        if nieuw != kop:
            gewijzigd.append(h); weg += tel[0]; om += tel[1]
            if not droog: open(p, "w", encoding="utf-8").write(nieuw + sep + rest)
    os.makedirs(os.path.join(ROOT, "data", "tmp"), exist_ok=True)
    open(os.path.join(ROOT, "data", "tmp", "links-gewijzigd.txt"), "w", encoding="utf-8").write("".join(f"{h} {onze[h]}\n" for h in gewijzigd))
    print(f"{len(gewijzigd)} bestanden {'zouden wijzigen' if droog else 'gewijzigd'}: {weg} links weg, {om} links omgezet naar de live handle")
    for h in gewijzigd: print(" ", h, "(live)" if onze[h] in live else "(concept)")

if __name__ == "__main__": main()
