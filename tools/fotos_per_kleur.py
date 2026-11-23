#!/usr/bin/env python3
"""Kaart van foto's per kleur voor actieve producten met meer dan één variant.
Per variant: welk bestaand beeld van het product bij die kleur hoort (zelfde bestand als op een ander product met dezelfde SKU),
of welke beelden van dat andere product moeten worden toegevoegd, of "geen bron".
Invoer: data/orderchamp/media-<datum>.json ({gid: productknoop} met media, variants, options), uit een lezer-uitlezing.
Gebruik: python3 -I tools/fotos_per_kleur.py data/orderchamp/media-<datum>.json
Uitvoer: data/orderchamp/fotos-per-kleur.json en analyse/17-varianten-fotos.md."""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def bestand(url):
    return re.sub(r"(_\d+x\d+[^.]*)?(\.[a-z]+)(\?.*)?$", r"\2", url.rsplit("/", 1)[-1]).lower() if url else ""

def main():
    P = json.load(open(sys.argv[1], encoding="utf-8"))
    per_sku = {}
    for g, p in P.items():
        for v in p["variants"]["nodes"]:
            if v.get("sku"): per_sku.setdefault(str(v["sku"]), []).append(g)
    beelden = lambda p: [(m["id"], (m.get("image") or {}).get("url", "")) for m in p["media"]["nodes"] if m.get("mediaContentType") == "IMAGE"]
    kaart, regels = {}, ["# Foto's per kleur · stand 23 november 2026", "", "Per actief product met meerdere varianten: welke foto bij welke variant hoort en wat er moet gebeuren.", "",
                         "| Product | Variant | SKU | Actie | Bron |", "|---|---|---|---|---|"]
    for g, p in sorted(P.items(), key=lambda kv: kv[1]["handle"]):
        vs = p["variants"]["nodes"]
        if p["status"] != "ACTIVE" or len(vs) < 2: continue
        eigen = beelden(p); eigen_b = {bestand(u): i for i, u in eigen}
        item = {"handle": p["handle"], "product": g, "varianten": []}
        for v in vs:
            r = {"variant": v["id"], "titel": v["title"], "sku": v.get("sku"), "voorraad": v.get("inventoryQuantity"), "gekoppeld": bool(v["media"]["nodes"])}
            bronnen = [o for o in per_sku.get(str(v.get("sku")), []) if o != g]
            # een bron met meerdere varianten (samengevoegd of ons eigen fase 2-concept) bevat de foto's van alle kleuren; alleen een losse kleur telt
            enkel = [o for o in bronnen if len(P[o]["variants"]["nodes"]) == 1]
            if enkel or bronnen: bronnen = enkel
            treffer = None
            for o in bronnen:
                for _, u in beelden(P[o]):
                    if bestand(u) in eigen_b: treffer = eigen_b[bestand(u)]; break
                if treffer: break
            if treffer:
                r.update(actie="koppelen", media=treffer, bron="eigen beeld")
            elif bronnen:
                o = max(bronnen, key=lambda x: len(beelden(P[x])))
                r.update(actie="toevoegen en koppelen", bron=P[o]["handle"], urls=[u for _, u in beelden(P[o])][:6])
            else:
                r.update(actie="geen bron", bron="")
            if r["gekoppeld"] and r["actie"] == "koppelen": r["actie"] = "al gekoppeld"
            item["varianten"].append(r)
        # eigen set via de kleur in de alt-tekst
        K = json.load(open(os.path.join(ROOT, "data", "orderchamp", "kleurnamen.json"), encoding="utf-8"))
        alts = [(m["id"], (m.get("alt") or "").lower()) for m in p["media"]["nodes"]]
        gebruikt0 = {r.get("media") for r in item["varianten"]}
        for r in item["varianten"]:
            if r["gekoppeld"]: r["actie"] = "al gekoppeld"; continue
            if r["actie"] != "geen bron": continue
            kleur = K["waarden"].get(r["titel"], r["titel"])
            woorden = K["zoekwoorden"].get(kleur, [kleur.lower()])
            for i, a in alts:
                if i not in gebruikt0 and any(w in a for w in woorden):
                    r.update(actie="koppelen", media=i, bron="eigen beeld (kleur in alt)"); gebruikt0.add(i); break
        # eerste set zonder bron-match: als precies één variant 'geen bron' heeft en het product eigen beelden heeft die nergens gekoppeld zijn, toewijzen
        open_v = [r for r in item["varianten"] if r["actie"] == "geen bron"]
        gebruikt = {r.get("media") for r in item["varianten"]}
        vrij = [i for i, _ in eigen if i not in gebruikt]
        if len(open_v) == 1 and vrij and not any(r["actie"] == "koppelen" for r in item["varianten"]):
            open_v[0].update(actie="koppelen", media=vrij[0], bron="eigen beeld (enige set)")
        kaart[g] = item
        regels += [f"| `{p['handle']}` | {r['titel']} | {r['sku']} | {r['actie']} | {r.get('bron','')} |" for r in item["varianten"]]
    json.dump(kaart, open(os.path.join(ROOT, "data", "orderchamp", "fotos-per-kleur.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    tel = {}
    for it in kaart.values():
        for r in it["varianten"]: tel[r["actie"]] = tel.get(r["actie"], 0) + 1
    regels += ["", "Totalen: " + ", ".join(f"{k} {v}" for k, v in sorted(tel.items()))]
    open(os.path.join(ROOT, "analyse", "17-varianten-fotos.md"), "w", encoding="utf-8").write("\n".join(regels) + "\n")
    print(len(kaart), "producten;", tel)

if __name__ == "__main__": main()
