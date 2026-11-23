#!/usr/bin/env python3
"""Controleert analyse/redirects.csv: dubbelen, kringen/ketens, onbekende doelen, ontbrekende regels.
Gebruik: python3 -I tools/redirects_check.py [--fix]   (--fix: platslaan van ketens en exacte dubbelen weg)"""
import csv, json, sys
from collections import Counter
R = "analyse/redirects.csv"
rows = list(csv.reader(open(R, encoding="utf-8"), delimiter=";"))
kop, regels = rows[0], [r for r in rows[1:] if r]
ids = json.load(open("data/ids.json", encoding="utf-8"))
var = json.load(open("data/orderchamp/varianten-2026-11-19.json", encoding="utf-8"))
gepland = {**ids["producten"], **ids["live_tekst"]}
gid2plan = {g: h for h, g in gepland.items()}
oude = Counter(r[0] for r in regels)
doel = {}
for r in regels: doel.setdefault(r[0], set()).add(r[1])
uit = {}
seen, ex = set(), []
for r in regels:
    k = tuple(r[:3])
    if k in seen: ex.append(r)
    seen.add(k)
uit["dubbel_exact"] = ex
uit["dubbel_strijdig"] = sorted(h for h, d in doel.items() if len(d) > 1)
uit["zelfverwijzing"] = [r for r in regels if r[0] == r[1]]
uit["keten"] = [r for r in regels if r[1] in oude and r[0] != r[1]]
bekend = set(gepland) | set(var) | {f"/collections/{h}" for h in ids.get("collecties", {})} | {"/collections/all"}
uit["oude_is_geplande_handle"] = [r for r in regels if r[0] in gepland and gepland[r[0]] != var.get(r[0], {}).get("gid")]
uit["onbekend_doel"] = [r for r in regels if r[1] not in bekend]
uit["ontbrekend"] = []
for h, v in var.items():
    if v["status"] != "ACTIVE": continue
    p = gid2plan.get(v["gid"])
    if h in oude: continue
    if p is None: uit["ontbrekend"].append((h, "geen geplande handle")); continue
    if p != h and h not in oude: uit["ontbrekend"].append((h, p))
if "--fix" in sys.argv:
    doelmap = {r[0]: r[1] for r in regels}
    def eind(h):
        n = 0
        while h in doelmap and doelmap[h] != h and n < 10: h, n = doelmap[h], n + 1
        return h
    nieuw, s = [], set()
    for r in regels:
        r = [r[0], eind(r[1]), r[2]]
        if tuple(r) in s: continue
        s.add(tuple(r)); nieuw.append(r)
    with open(R, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";", lineterminator="\n"); w.writerow(kop); w.writerows(nieuw)
    print("hersteld:", len(regels), "->", len(nieuw), "regels")
print("regels:", len(regels))
for k, v in uit.items(): print(f"{k}: {len(v)}"); [print("  ", x) for x in v[:50]]
