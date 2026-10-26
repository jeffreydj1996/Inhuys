#!/usr/bin/env python3
"""PreToolUse-hook voor mcp__Shopify__graphql_mutation. Leest de tool-aanroep op stdin (JSON van Claude Code) en blokkeert (exit 2)
alles wat live objecten kan raken. Toegestaan zijn alleen mutaties op concepten en op de thema-kopie. Ontgrendelen: INHUYS_GOLIVE=1 in de omgeving (alleen de eigenaar).
Droge test: python3 tools/guard_shopify.py --test"""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDS = os.path.join(ROOT, "data", "ids.json")
TOEGESTAAN = {"productSet", "productUpdate", "productCreate", "pageCreate", "pageUpdate", "collectionCreate", "collectionUpdate",
              "articleCreate", "articleUpdate", "themeFilesUpsert", "metafieldDefinitionCreate", "menuCreate", "menuUpdate", "fileUpdate"}
VERBODEN_RE = re.compile(r"(delete|publish|unpublish|archive|urlredirect|themepublish|themecreate|themeupdate|inventory|pricelist|discount|customer|order|fulfillment|webhook|bulkoperation|stagedupload)", re.I)
THEMA_KOPIE = "gid://shopify/OnlineStoreTheme/210233098579"

def concept_ids():
    try: d = json.load(open(IDS, encoding="utf-8"))
    except Exception: return set(), set()
    ids, files = set(), set()
    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "bestanden_eigen" and isinstance(v, list): files.update(v)
                else: walk(v)
        elif isinstance(o, list):
            for x in o: walk(x)
        elif isinstance(o, str) and o.startswith("gid://shopify/"): ids.add(o)
    walk(d); return ids, files

def veldnamen(query):
    body = re.sub(r"fragment\s+\w+\s+on\s+\w+\s*\{.*", "", query, flags=re.S)
    body = re.sub(r"^\s*mutation[^{]*\{", "", body.strip(), flags=re.S)
    namen = set()
    depth = 0
    for m in re.finditer(r"([A-Za-z_]\w*)\s*(?::\s*([A-Za-z_]\w*))?\s*(\(|\{)|(\{)|(\})", body):
        if m.group(5): depth -= 1; continue
        if m.group(4): depth += 1; continue
        if depth == 0:
            namen.add(m.group(2) or m.group(1))
        if m.group(3) == "{": depth += 1
    return namen

def controleer(query, variables, env):
    fouten = []
    if env.get("INHUYS_GOLIVE") == "1": return fouten
    for n in veldnamen(query):
        if n not in TOEGESTAAN or VERBODEN_RE.search(n): fouten.append(f"mutatie '{n}' is niet toegestaan zonder INHUYS_GOLIVE=1")
    if VERBODEN_RE.search(query) and not fouten: fouten.append("de mutatietekst bevat een verboden term (delete/publish/redirect/...)")
    ids, files = concept_ids()
    def walk(o, pad=""):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "status" and str(v).upper() == "ACTIVE": fouten.append(f"{pad}.status ACTIVE: producten blijven DRAFT")
                if k in ("isPublished", "published", "publishedOnCurrentPublication") and v is True: fouten.append(f"{pad}.{k} true: niets wordt gepubliceerd")
                if k in ("themeId", "id") and isinstance(v, str) and v.startswith("gid://shopify/OnlineStoreTheme/") and v != THEMA_KOPIE: fouten.append(f"thema {v} is niet de werkkopie")
                if k == "id" and isinstance(v, str) and v.startswith("gid://shopify/") and "Theme" not in v and v not in ids and v not in files: fouten.append(f"{pad}.id {v} staat niet in data/ids.json als concept")
                walk(v, f"{pad}.{k}")
        elif isinstance(o, list):
            for i, x in enumerate(o): walk(x, f"{pad}[{i}]")
    walk(variables or {})
    if "fileUpdate" in query:
        for f in re.findall(r"gid://shopify/(?:MediaImage|GenericFile|Video)/\d+", json.dumps(variables or {})):
            if f not in files: fouten.append(f"fileUpdate op {f}: bestand is gedeeld met live producten; alleen bestanden uit ids.json 'bestanden_eigen'")
    return sorted(set(fouten))

def main():
    if "--test" in sys.argv:
        ids, _ = concept_ids()
        proef = [("themePublish", 'mutation { themePublish(id: "gid://shopify/OnlineStoreTheme/210233098579") { theme { id } } }', {}, True),
                 ("delete", 'mutation($id: ID!) { productDelete(input: {id: $id}) { deletedProductId } }', {"id": "gid://shopify/Product/1"}, True),
                 ("active", 'mutation($p: ProductSetInput!) { productSet(input: $p) { product { id } } }', {"p": {"status": "ACTIVE", "title": "x"}}, True),
                 ("vreemd id", 'mutation($p: ProductSetInput!) { productSet(input: $p) { product { id } } }', {"p": {"id": "gid://shopify/Product/10447090057555", "status": "DRAFT"}}, True),
                 ("publishable", 'mutation { publishablePublish(id: "gid://shopify/Product/1", input: []) { userErrors { message } } }', {}, True),
                 ("redirect", 'mutation { urlRedirectCreate(urlRedirect: {path: "/a", target: "/b"}) { userErrors { message } } }', {}, True),
                 ("concept ok", 'mutation($p: ProductSetInput!) { productSet(input: $p, synchronous: true) { product { id } userErrors { message } } }', {"p": {"title": "Proef", "status": "DRAFT"}}, False),
                 ("thema-kopie ok", 'mutation($t: ID!, $f: [OnlineStoreThemeFilesUpsertFileInput!]!) { themeFilesUpsert(themeId: $t, files: $f) { userErrors { message } } }', {"t": THEMA_KOPIE, "f": []}, False)]
        goed = 0
        for naam, q, v, verwacht_blok in proef:
            f = controleer(q, v, {}); blok = bool(f)
            print(("OK  " if blok == verwacht_blok else "MIS ") + f"{naam:14} geblokkeerd={blok} {f[:1]}"); goed += blok == verwacht_blok
        print(f"{goed} van {len(proef)} tests goed; concept-id's bekend: {len(ids)}"); sys.exit(0 if goed == len(proef) else 1)
    try: data = json.load(sys.stdin)
    except Exception: sys.exit(0)
    if data.get("tool_name") != "mcp__Shopify__graphql_mutation": sys.exit(0)
    ti = data.get("tool_input") or {}
    fouten = controleer(ti.get("query") or ti.get("mutation") or "", ti.get("variables") or {}, os.environ)
    if fouten:
        sys.stderr.write("GEBLOKKEERD door tools/guard_shopify.py:\n- " + "\n- ".join(fouten) + "\nAlleen concepten en de thema-kopie mogen wijzigen. Live wijzigingen alleen door de eigenaar met INHUYS_GOLIVE=1.\n")
        sys.exit(2)
    sys.exit(0)

if __name__ == "__main__": main()
