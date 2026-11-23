#!/usr/bin/env python3
"""Controle op de live winkel (alleen lezen, via /products/<handle>.js): per actief product
- of elke variant een featured_image heeft en of die per kleur verschilt (alleen bij meer dan één variant);
- of er nog machinevertaalde kleur- of optienamen staan (data/orderchamp/kleurnamen.json, sleutels 'waarden' en 'opties').
Handles komen uit de laatste uitlezing (data/orderchamp/media-<datum>.json) voor de gids onder live_actief in data/ids.json.
Gebruik: python3 -I tools/winkel_controle.py data/orderchamp/media-<datum>.json [uitvoer.txt]
Uitzonderingen (bekend, geen fout): data/orderchamp/winkel-uitzonderingen.json {handle: [varianttitel, ...]}"""
import json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    P = json.load(open(sys.argv[1], encoding="utf-8"))
    ids = json.load(open(os.path.join(ROOT, "data", "ids.json"), encoding="utf-8"))
    K = json.load(open(os.path.join(ROOT, "data", "orderchamp", "kleurnamen.json"), encoding="utf-8"))
    slecht_w, slecht_o = set(K["waarden"]), set(K.get("opties", {}))
    pu = os.path.join(ROOT, "data", "orderchamp", "winkel-uitzonderingen.json")
    uitz = json.load(open(pu, encoding="utf-8")) if os.path.exists(pu) else {}
    regels, tel = [], {"producten": 0, "fotos_fout": 0, "namen_fout": 0, "onbereikbaar": 0}
    for g in sorted(ids.get("live_actief", []), key=lambda x: P.get(x, {}).get("handle", x)):
        h = P.get(g, {}).get("handle")
        if not h: regels.append(f"{g}: niet in de uitlezing"); tel["onbereikbaar"] += 1; continue
        r = subprocess.run(["curl", "-s", "--max-time", "20", f"https://www.in-huys.nl/products/{h}.js"], capture_output=True, text=True)
        try: d = json.loads(r.stdout)
        except Exception: regels.append(f"{h}: geen productdata op de winkel"); tel["onbereikbaar"] += 1; continue
        tel["producten"] += 1
        namen = [o["name"] for o in d["options"] if o["name"] in slecht_o] + [v for o in d["options"] for v in o["values"] if v in slecht_w]
        if namen: regels.append(f"{h}: machinevertaalde namen {namen}"); tel["namen_fout"] += 1
        vs = d["variants"]
        if len(vs) < 2: continue
        fi = [((v.get("featured_image") or {}).get("src") or "").split("?")[0].rsplit("/", 1)[-1] for v in vs]
        bekend = set(uitz.get(h, []))
        leeg = [v["title"] for v, f in zip(vs, fi) if not f and v["title"] not in bekend]
        gevuld = [f for f in fi if f]
        dubbel = len(set(gevuld)) < len(gevuld)
        if leeg or dubbel:
            tel["fotos_fout"] += 1
            regels.append(f"{h}: " + (f"zonder foto {leeg} " if leeg else "") + ("zelfde foto bij meerdere varianten " + str([(v['title'], f[:24]) for v, f in zip(vs, fi)]) if dubbel else ""))
    tekst = "\n".join(regels + ["", "Totalen: " + ", ".join(f"{k} {v}" for k, v in tel.items())]) + "\n"
    if len(sys.argv) > 2: open(sys.argv[2], "w", encoding="utf-8").write(tekst)
    print(tekst[-2000:])

if __name__ == "__main__": main()
