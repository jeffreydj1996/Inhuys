#!/usr/bin/env python3
"""Feiten uit de eigen Shopify-export voor een model: per bronproduct titel, status, prijs, SKU, aantal beelden en beeldbreedte.
Gebruik: python3 -I tools/varianten.py <zoekwoord in titel of handle> [...]   bv. python3 -I tools/varianten.py panda
Uitvoer: markdown-tabel om in data/feiten/<model>.md te plakken (sectie 'Bronproducten')."""
import json, glob, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
zoek = [z.lower() for z in sys.argv[1:]]
print("| bronhandle | titel | status | prijs | sku | beelden | breedte px |")
print("|---|---|---|---|---|---|---|")
for f in sorted(glob.glob(os.path.join(ROOT, "data", "raw", "products-*.json"))):
    for e in json.load(open(f, encoding="utf-8"))["data"]["products"]["edges"]:
        n = e["node"]
        t = (n["title"] + " " + n["handle"]).lower()
        if not any(z in t for z in zoek):
            continue
        imgs = [m["node"]["image"] for m in n["media"]["edges"] if m["node"].get("image")]
        for v in n["variants"]["edges"]:
            v = v["node"]
            breedte = min((i.get("width") or 0) for i in imgs) if imgs else 0
            print(f"| `{n['handle']}` | {n['title']} | {n['status']} | € {str(v['price']).replace('.', ',')} | {v.get('sku') or '-'} | {len(imgs)} | {breedte} |")
