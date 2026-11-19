#!/usr/bin/env python3
"""Controle op de hele winkel na een verse uitlezing: dubbele producten, gewijzigde varianten en volledigheid.
Invoer: het logboek van een lezer die alle producten heeft gelezen (products { nodes { id handle title status vendor totalInventory
mediaCount{count} resourcePublicationsCount{count} variants(first:10){nodes{title sku price inventoryQuantity}} } }).
Gebruik: python3 -I tools/controle_producten.py <lezer.output> <JJJJ-MM-DD>
Uitvoer: data/orderchamp/voorraad-<datum>.csv, data/orderchamp/varianten-<datum>.json, analyse/11-dubbele-producten.md,
data/orderchamp/verificatie/varianten-afwijkingen-<datum>.txt, data/orderchamp/verificatie/volledigheid-<datum>.txt.
Draai eerst `python3 -I tools/md_naar_vars.py content/producten/*.md` zodat data/out actueel is. Wijzigt niets in Shopify."""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DROPSHIP = ("Pole To Pole", "Jupiduu - Designed for Kids")
BEHEER = "https://admin.shopify.com/store/in-huys/products/"

def lees(pad):
    P = {}
    def vind(o):
        if isinstance(o, dict):
            if str(o.get("id", "")).startswith("gid://shopify/Product/") and "variants" in o: P[o["id"]] = o
            for v in o.values(): vind(v)
        elif isinstance(o, list):
            for x in o: vind(x)
    for line in open(pad, encoding="utf-8", errors="ignore"):
        try: d = json.loads(line)
        except Exception: continue
        c = (d.get("message") or {}).get("content")
        for x in c if isinstance(c, list) else []:
            if not isinstance(x, dict) or x.get("type") != "tool_result": continue
            cc = x.get("content")
            for t in ([cc] if isinstance(cc, str) else [y.get("text", "") for y in cc if isinstance(y, dict)]):
                m = re.search(r"\{.*\}", t, re.S)
                if not m: continue
                try: vind(json.loads(m.group(0)))
                except Exception: continue
    return P

def main():
    logboek, datum = sys.argv[1], sys.argv[2]
    P = lees(logboek)
    if not P: raise SystemExit("geen producten gevonden in het logboek")
    ids = json.load(open(os.path.join(ROOT, "data", "ids.json"), encoding="utf-8"))
    prod, live = ids.get("producten", {}), ids.get("live_tekst", {})
    onze = {g: h for h, g in prod.items()}; onze.update({g: h for h, g in live.items()})   # gid -> onze (geplande) handle
    var = lambda n: n["variants"]["nodes"]
    voorraad = lambda n: n.get("totalInventory") or 0
    oc = os.path.join(ROOT, "data", "orderchamp"); ver = os.path.join(oc, "verificatie"); os.makedirs(ver, exist_ok=True)
    # 0. uitlezing vastleggen
    rows = sorted(";".join([n["handle"], g, n["status"], n["vendor"], str(voorraad(n)), str(len(var(n))), str(n["mediaCount"]["count"]),
                            str(n["resourcePublicationsCount"]["count"]), n["title"].replace(";", ",")]) for g, n in P.items())
    open(os.path.join(oc, f"voorraad-{datum}.csv"), "w", encoding="utf-8").write("handle;gid;status;vendor;voorraad;varianten;beelden;publicaties;titel\n" + "\n".join(rows) + "\n")
    json.dump({n["handle"]: {"gid": g, "status": n["status"], "varianten": var(n)} for g, n in P.items()},
              open(os.path.join(oc, f"varianten-{datum}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # 1. dubbelen: dezelfde SKU in meer dan één product
    # eigen concepten (door ons aangemaakt, niet van Orderchamp): nooit het product dat blijft
    import csv
    notitie = {r["handle"]: (r.get("opmerking") or "") for r in csv.DictReader(open(os.path.join(ROOT, "data", "status.csv"), encoding="utf-8"), delimiter=";")}
    eigen_g = {g for h, g in prod.items() if g in P and (h.endswith("-eigen") or "Orderchamp-concept gezet" not in notitie.get(h, ""))}
    per_sku = {}
    for g, n in P.items():
        if g in eigen_g: continue
        for v in var(n):
            if v.get("sku"): per_sku.setdefault(str(v["sku"]), []).append((g, v))
    groepen = {}
    for sku, lst in per_sku.items():
        gs = sorted({g for g, _ in lst})
        if len(gs) > 1: groepen.setdefault(tuple(gs), []).append(sku)
    def score(g):   # wat blijft: live, dan meeste varianten (samengevoegd), dan meeste voorraad, dan onze inhoud
        n = P[g]; return (n["status"] == "ACTIVE", len(var(n)), voorraad(n), g in onze)
    L = [f"# Dubbele producten · stand {datum}", "",
         "Dezelfde SKU staat in meer dan één product. Per groep: het product dat blijft en de producten die weg kunnen. Niets is verwijderd; de eigenaar ruimt op, bij voorkeur in de Orderchamp-app zodat het product niet opnieuw wordt aangemaakt.", "",
         "Keuze \"blijft\": live gaat voor concept, daarna het product met de meeste varianten (het samengevoegde), daarna de meeste voorraad.", ""]
    weg = {}
    for i, (gs, skus) in enumerate(sorted(groepen.items(), key=lambda kv: P[max(kv[0], key=score)]["handle"]), 1):
        blijft = max(gs, key=score)
        L += [f"## {i}. {P[blijft]['title']}", "", f"Gedeelde SKU's: {', '.join(sorted(skus))}", "", "| Advies | Handle | Status | Voorraad | Varianten | Onze tekst | Beheer |", "|---|---|---|---|---|---|---|"]
        for g in sorted(gs, key=score, reverse=True):
            n = P[g]; adv = "blijft" if g == blijft else "kan weg"
            if g != blijft: weg[g] = blijft
            L.append(f"| {adv} | `{n['handle']}` | {n['status']} | {voorraad(n)} | {len(var(n))} | {'ja' if g in onze else 'nee'} | {BEHEER}{g.split('/')[-1]} |")
        L.append("")
    eigen = sorted((h, g) for h, g in prod.items() if g in eigen_g)
    L += ["## Eigen concepten uit fase 2 (geen Orderchamp-koppeling)", "",
          "Deze concepten zijn door ons aangemaakt vóór de Orderchamp-werkwijze. Het Orderchamp-product draagt nu de inhoud; het eigen concept kan weg.", "",
          "| Handle | Status | Voorraad | Beheer |", "|---|---|---|---|"]
    for h, g in sorted(eigen): L.append(f"| `{P[g]['handle']}` | {P[g]['status']} | {voorraad(P[g])} | {BEHEER}{g.split('/')[-1]} |")
    L.append("")
    open(os.path.join(ROOT, "analyse", "11-dubbele-producten.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    json.dump({P[g]["handle"]: P[b]["handle"] for g, b in weg.items()}, open(os.path.join(ver, f"kan-weg-{datum}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # 2. gewijzigde varianten tegenover onze bestanden
    afw = []
    for g, h in sorted(onze.items(), key=lambda kv: kv[1]):
        if g not in P or g in eigen_g: continue
        p = os.path.join(ROOT, "data", "out", f"productSet-{h}.json")
        if not os.path.exists(p): continue
        md = sorted((str(a.get("sku")), f'{float(a["price"]):.2f}') for a in json.load(open(p, encoding="utf-8"))["variants"])
        o = [(v["title"], str(v["sku"]), f'{float(v["price"]):.2f}', v["inventoryQuantity"]) for v in var(P[g])]
        if md != sorted((s, pr) for _, s, pr, _ in o):
            afw.append(f"{h} ({P[g]['status']}{', kan weg' if g in weg else ''}): tekst {md} | Orderchamp {o}")
    open(os.path.join(ver, f"varianten-afwijkingen-{datum}.txt"), "w", encoding="utf-8").write("\n".join(afw) + ("\n" if afw else ""))
    # 3. volledigheid
    zonder_met, zonder_nul = [], []
    for g, n in sorted(P.items(), key=lambda kv: kv[1]["handle"]):
        if n["vendor"] not in DROPSHIP or (g in onze and g not in eigen_g) or g in eigen_g: continue
        (zonder_met if voorraad(n) > 0 else zonder_nul).append(f"{n['handle']};{g};{n['status']};{n['vendor']};{voorraad(n)};{'kan weg' if g in weg else ''};{n['title']}")
    open(os.path.join(ver, f"volledigheid-{datum}.txt"), "w", encoding="utf-8").write(
        "# met voorraad, zonder onze inhoud\n" + "\n".join(zonder_met) + "\n# zonder voorraad, zonder onze inhoud\n" + "\n".join(zonder_nul) + "\n")
    st = {}
    for n in P.values(): st[(n["vendor"] in DROPSHIP, n["status"])] = st.get((n["vendor"] in DROPSHIP, n["status"]), 0) + 1
    print(f"{len(P)} producten; Orderchamp-merken: " + ", ".join(f"{s} {c}" for (d, s), c in sorted(st.items()) if d) + "; overig: " + ", ".join(f"{s} {c}" for (d, s), c in sorted(st.items()) if not d))
    print(f"dubbelen: {len(groepen)} groepen, {len(weg)} producten kunnen weg (waarvan {sum(1 for g in weg if g in onze)} met onze tekst); groepen waar het blijvende product geen tekst heeft: {sum(1 for gs in groepen if max(gs, key=score) not in onze)}; eigen concepten: {len(eigen)}")
    print(f"gewijzigde varianten: {len(afw)} (waarvan {sum(1 for a in afw if 'kan weg' in a.split(':')[0])} op de weg-lijst)")
    print(f"zonder onze inhoud: {len(zonder_met)} met voorraad, {len(zonder_nul)} zonder voorraad")

if __name__ == "__main__": main()
