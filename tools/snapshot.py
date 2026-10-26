#!/usr/bin/env python3
"""Vergelijkt twee momentopnames van live objecten (formaat van data/snapshots/*.txt: secties met regels 'ID naam updatedAt').
De momentopname zelf maakt de lezer-agent met de query in tools/gql/snapshot.graphql en schrijft hij naar data/snapshots/snapshot-<datum>.txt.
Gebruik: python3 tools/snapshot.py data/snapshots/voor.txt data/snapshots/na.txt   Exit 1 als een bestaand live object een andere updatedAt heeft."""
import sys, re
def lees(p):
    d = {}; sec = None
    for ln in open(p, encoding="utf-8"):
        ln = ln.rstrip("\n")
        if not ln or ln.startswith("#"): continue
        if re.fullmatch(r"[A-Z_]+", ln): sec = ln; d[sec] = {}; continue
        parts = ln.split(" ")
        if sec and len(parts) >= 2: d[sec][parts[0]] = (" ".join(parts[1:-1]), parts[-1])
    return d
a, b = lees(sys.argv[1]), lees(sys.argv[2]); fouten = 0
for sec in a:
    for k, (naam, upd) in a[sec].items():
        if k not in b.get(sec, {}): print(f"VERDWENEN {sec} {k} {naam}"); fouten += 1
        elif b[sec][k][1] != upd: print(f"GEWIJZIGD {sec} {k} {naam}: {upd} -> {b[sec][k][1]}"); fouten += 1
    for k, (naam, upd) in b.get(sec, {}).items():
        if k not in a[sec]: print(f"NIEUW     {sec} {k} {naam}")
print("identiek" if not fouten else f"{fouten} live objecten gewijzigd of verdwenen"); sys.exit(1 if fouten else 0)
