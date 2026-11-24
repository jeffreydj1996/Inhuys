#!/usr/bin/env python3
"""Controle op de live winkel (alleen lezen, via /products/<handle>.js): per actief product
- of elke variant een featured_image heeft en of die per kleur verschilt (alleen bij meer dan één variant);
- of er nog machinevertaalde kleur- of optienamen staan (data/orderchamp/kleurnamen.json, sleutels 'waarden' en 'opties').
Handles komen uit de laatste uitlezing (data/orderchamp/media-<datum>.json) voor de gids onder live_actief in data/ids.json.
Gebruik: python3 -I tools/winkel_controle.py data/orderchamp/media-<datum>.json [uitvoer.txt] [--thema <thema-id>]
Met --thema <id> (alleen lezen, Playwright): opent de voorvertoning ?preview_theme_id=<id> (eerst de homepage, zodat de cookie staat; Shopify.theme.id moet kloppen),
haalt de productpagina's op van de actieve producten met machinenamen (uit de .js-controle) en meldt elke sleutel uit kleurnamen.json die in de zichtbare tekst
(document.body.innerText, inclusief opties van selecteerlijsten) staat als optienaam of -waarde: een regel die de sleutel is, begint met 'sleutel:', of de sleutel
tussen ' / ' of voor ' - €' heeft. Elke treffer daar is een fout van het thema. Eén seconde tussen pagina's.
Uitzonderingen (bekend, geen fout): data/orderchamp/winkel-uitzonderingen.json {handle: [varianttitel, ...]}"""
import json, os, re, subprocess, sys, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def thema_controle(thema, handles, sleutels):
    """Zichtbare tekst van de voorvertoning per productpagina; geeft (regels, aantal fouten, aantal pagina's)."""
    from playwright.sync_api import sync_playwright
    chrome = "/usr/bin/google-chrome"
    regels, fout, n = [], 0, 0
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=chrome if os.path.exists(chrome) else None, args=["--no-sandbox"])
        pg = b.new_context(viewport={"width": 1280, "height": 900}).new_page()
        pg.goto(f"https://www.in-huys.nl/?preview_theme_id={thema}", wait_until="load")
        tid = str(pg.evaluate("Shopify.theme.id"))
        if tid != str(thema): b.close(); return [f"voorvertoning toont thema {tid} in plaats van {thema}"], 1, 0
        for h in handles:
            time.sleep(1)
            r = pg.goto(f"https://www.in-huys.nl/products/{h}", wait_until="load"); time.sleep(1)
            if r is None or r.status != 200 or str(pg.evaluate("Shopify.theme.id")) != str(thema): regels.append(f"{h}: pagina niet op thema {thema} (status {getattr(r, 'status', None)})"); fout += 1; continue
            n += 1
            tekst = pg.evaluate("""() => document.body.innerText + '\\n' + [...document.querySelectorAll('select option')].map(o => o.textContent.trim()).join('\\n')""")
            gevonden = [k for k in sleutels if re.search(r"(?:^|: |\s/\s)" + re.escape(k) + r"(?::)?(?:$| / | - €)", tekst, re.M)]
            if gevonden: regels.append(f"{h}: machinenamen in zichtbare tekst van het thema {gevonden}"); fout += 1
        b.close()
    return regels, fout, n

def main():
    thema = None
    if "--thema" in sys.argv:
        i = sys.argv.index("--thema"); thema = sys.argv[i + 1]; del sys.argv[i:i + 2]
    P = json.load(open(sys.argv[1], encoding="utf-8"))
    ids = json.load(open(os.path.join(ROOT, "data", "ids.json"), encoding="utf-8"))
    K = json.load(open(os.path.join(ROOT, "data", "orderchamp", "kleurnamen.json"), encoding="utf-8"))
    slecht_w, slecht_o = set(K["waarden"]), set(K.get("opties", {}))
    pu = os.path.join(ROOT, "data", "orderchamp", "winkel-uitzonderingen.json")
    uitz = json.load(open(pu, encoding="utf-8")) if os.path.exists(pu) else {}
    regels, tel = [], {"producten": 0, "fotos_fout": 0, "namen_fout": 0, "onbereikbaar": 0}
    met_namen = []
    for g in sorted(ids.get("live_actief", []), key=lambda x: P.get(x, {}).get("handle", x)):
        h = P.get(g, {}).get("handle")
        if not h: regels.append(f"{g}: niet in de uitlezing"); tel["onbereikbaar"] += 1; continue
        r = subprocess.run(["curl", "-s", "--max-time", "20", f"https://www.in-huys.nl/products/{h}.js"], capture_output=True, text=True)
        try: d = json.loads(r.stdout)
        except Exception: regels.append(f"{h}: geen productdata op de winkel"); tel["onbereikbaar"] += 1; continue
        tel["producten"] += 1
        namen = [o["name"] for o in d["options"] if o["name"] in slecht_o] + [v for o in d["options"] for v in o["values"] if v in slecht_w]
        if namen: regels.append(f"{h}: machinevertaalde namen {namen}"); tel["namen_fout"] += 1; met_namen.append(h)
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
    if thema:
        r2, f2, n2 = thema_controle(thema, met_namen, sorted(slecht_w | slecht_o))
        regels += [f"[thema {thema}] " + x for x in r2]; tel["thema_paginas"] = n2; tel["thema_fout"] = f2
    tekst = "\n".join(regels + ["", "Totalen: " + ", ".join(f"{k} {v}" for k, v in tel.items())]) + "\n"
    if len(sys.argv) > 2: open(sys.argv[2], "w", encoding="utf-8").write(tekst)
    print(tekst[-2000:])

if __name__ == "__main__": main()
