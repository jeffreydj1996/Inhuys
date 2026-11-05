#!/usr/bin/env python3
"""Vergelijkt uitgelezen Shopify-producten (JSON met per gid: handle, title, productType, tags, category{id}, seo, descriptionHtml,
metafields{nodes[{key,type,value}]}, metafield{value} voor descriptor.short_description) byte-voor-byte met data/out/productSet-<handle>.json.
Gebruik: python3 -I tools/verifieer_overzetting.py <nodes.json> [verschillen.txt]"""
import json, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
nodes = json.load(open(sys.argv[1], encoding="utf-8"))
uit = open(sys.argv[2], "w", encoding="utf-8") if len(sys.argv) > 2 else sys.stdout
tot_fout = 0
for gid, n in sorted(nodes.items(), key=lambda kv: kv[1].get("handle", "")):
    h = n.get("handle"); p = os.path.join(ROOT, "data", "out", f"productSet-{h}.json")
    if not os.path.exists(p): print(f"{h}: geen variabelenbestand", file=uit); tot_fout += 1; continue
    v = json.load(open(p, encoding="utf-8")); fouten = []
    def chk(naam, verwacht, gevonden):
        if verwacht != gevonden: fouten.append(f"  {naam}: verwacht {str(verwacht)[:200]!r} | gevonden {str(gevonden)[:200]!r}")
    chk("title", v["title"], n.get("title")); chk("productType", v["productType"], n.get("productType"))
    chk("tags", sorted(v["tags"]), sorted(n.get("tags") or [])); chk("category", v.get("category"), (n.get("category") or {}).get("id"))
    chk("seo.title", v["seo"]["title"], (n.get("seo") or {}).get("title")); chk("seo.description", v["seo"]["description"], (n.get("seo") or {}).get("description"))
    chk("descriptionHtml", v["descriptionHtml"], n.get("descriptionHtml"))
    mf = {m["key"]: m for m in (n.get("metafields") or {}).get("nodes", [])}
    for m in v["metafields"]:
        if m["namespace"] == "descriptor":
            chk("descriptor.short_description", m["value"], (n.get("metafield") or {}).get("value")); continue
        g = mf.get(m["key"])
        if not g: fouten.append(f"  inhuys.{m['key']}: ontbreekt"); continue
        chk(f"inhuys.{m['key']}.type", m["type"], g.get("type"))
        vw, gv = m["value"], g.get("value")
        if m["type"] == "rich_text_field":
            try: vw, gv = json.loads(vw), json.loads(gv)
            except Exception: pass
        chk(f"inhuys.{m['key']}", vw, gv)
    extra = set(mf) - {m["key"] for m in v["metafields"] if m["namespace"] == "inhuys"}
    if extra: fouten.append(f"  extra inhuys-metavelden in Shopify: {sorted(extra)}")
    print(f"{h}: status {n.get('status')}, " + ("gelijk" if not fouten else f"{len(fouten)} afwijking(en)"), file=uit)
    for f in fouten: print(f, file=uit)
    tot_fout += len(fouten)
print(f"totaal {len(nodes)} producten, {tot_fout} afwijkingen", file=uit)
