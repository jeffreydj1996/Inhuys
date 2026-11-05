#!/usr/bin/env python3
"""Haalt de ruwe graphql_query-resultaten (productknopen met descriptionHtml) uit het logboek van een lezer-agent
(/tmp/claude-0/.../tasks/<agentId>.output, JSONL) en schrijft ze als {gid: knoop} naar een JSON-bestand, zonder overtypen.
Gebruik: python3 -I tools/nodes_uit_logboek.py <agent.output> <uit.json>   (daarna tools/verifieer_overzetting.py)"""
import json, re, sys
nodes = {}
def vind(o):
    if isinstance(o, dict):
        if "descriptionHtml" in o and str(o.get("id", "")).startswith("gid://shopify/Product/"): nodes[o["id"]] = o
        for v in o.values(): vind(v)
    elif isinstance(o, list):
        for x in o: vind(x)
for line in open(sys.argv[1], encoding="utf-8", errors="ignore"):
    try: d = json.loads(line)
    except Exception: continue
    inhoud = (d.get("message") or {}).get("content")
    for c in inhoud if isinstance(inhoud, list) else []:
        if not isinstance(c, dict) or c.get("type") != "tool_result": continue
        cont = c.get("content")
        for t in ([cont] if isinstance(cont, str) else [x.get("text", "") for x in cont if isinstance(x, dict)]):
            m = re.search(r"\{.*\}", t, re.S)
            if not m: continue
            try: vind(json.loads(m.group(0)))
            except Exception: continue
json.dump(nodes, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False)
print(f"{len(nodes)} producten -> {sys.argv[2]}")
