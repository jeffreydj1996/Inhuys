#!/usr/bin/env python3
"""Statusregister per model in data/status.csv (puntkomma). Kolommen: handle;model;feiten;tekst;controle;concept;gid;datum;opmerking
Gebruik: python3 tools/status.py show            toon het register
         python3 tools/status.py set <handle> <kolom>=<waarde> [...]   bijwerken of toevoegen (datum wordt gezet); gid= werkt data/ids.json bij"""
import csv, sys, os, json, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(ROOT, "data", "status.csv"); IDS = os.path.join(ROOT, "data", "ids.json")
KOL = ["handle", "model", "feiten", "tekst", "controle", "concept", "gid", "datum", "opmerking"]
def lees():
    if not os.path.exists(CSV): return []
    return list(csv.DictReader(open(CSV, encoding="utf-8"), delimiter=";"))
def schrijf(rows):
    with open(CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=KOL, delimiter=";"); w.writeheader(); w.writerows(rows)
if __name__ == "__main__":
    rows = lees()
    if len(sys.argv) < 2 or sys.argv[1] == "show":
        print(";".join(KOL)); [print(";".join(r.get(k, "") for k in KOL)) for r in rows]; sys.exit(0)
    if sys.argv[1] == "set":
        h = sys.argv[2]; r = next((x for x in rows if x["handle"] == h), None)
        if not r: r = {k: "" for k in KOL}; r["handle"] = h; rows.append(r)
        for kv in sys.argv[3:]:
            k, v = kv.split("=", 1); r[k] = v
            if k == "gid" and v.startswith("gid://shopify/Product/"):
                d = json.load(open(IDS, encoding="utf-8")); d.setdefault("producten", {})[h] = v
                json.dump(d, open(IDS, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        r["datum"] = datetime.date.today().isoformat(); schrijf(rows); print("bijgewerkt:", ";".join(r.get(k, "") for k in KOL))
