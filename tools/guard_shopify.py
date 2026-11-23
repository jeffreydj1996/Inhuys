#!/usr/bin/env python3
"""PreToolUse-hook voor mcp__Shopify__graphql_mutation. Leest de tool-aanroep op stdin (JSON van Claude Code) en blokkeert (exit 2)
alles wat live objecten kan raken. Toegestaan zijn alleen mutaties op concepten en op de thema-kopie. Ontgrendelen: INHUYS_GOLIVE=1 in de omgeving (alleen de eigenaar).
Droge test: python3 tools/guard_shopify.py --test"""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDS = os.path.join(ROOT, "data", "ids.json")
DROPSHIP_MERKEN = {"Pole To Pole", "Jupiduu - Designed for Kids"}
TOEGESTAAN = {"productSet", "productUpdate", "productCreate", "pageCreate", "pageUpdate", "collectionCreate", "collectionUpdate",
              "articleCreate", "articleUpdate", "themeFilesUpsert", "metafieldDefinitionCreate", "menuCreate", "menuUpdate", "fileUpdate"}
VERBODEN_RE = re.compile(r"(delete|publish|unpublish|archive|urlredirect|themepublish|themecreate|themeupdate|inventory|pricelist|discount|customer|order|fulfillment|webhook|bulkoperation|stagedupload)", re.I)
THEMA_KOPIE = "gid://shopify/OnlineStoreTheme/210233098579"

TESTMODUS = False
LIVE_TEKST_VELDEN = {"id", "title", "descriptionHtml", "seo", "productType", "tags", "category", "metafields", "collectionsToJoin"}

def concept_ids():
    """Gids uit data/ids.json: concepten (alles behalve live_niet_aanraken en live_tekst), eigen bestanden, live-blokkade, live-tekst."""
    try: d = json.load(open(IDS, encoding="utf-8"))
    except Exception: return set(), set(), set(), set()
    ids, files, live_blok, live_tekst = set(), set(), set(), set()
    def gids(o, doel):
        if isinstance(o, dict):
            for v in o.values(): gids(v, doel)
        elif isinstance(o, list):
            for x in o: gids(x, doel)
        elif isinstance(o, str) and o.startswith("gid://shopify/"): doel.add(o)
    for k, v in d.items():
        if k == "bestanden_eigen" and isinstance(v, list): files.update(v)
        elif k == "live_niet_aanraken": gids(v, live_blok)
        elif k == "live_tekst": gids(v, live_tekst)
        else: gids(v, ids)
    return ids, files, live_blok, live_tekst

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
    # Regel 2c (besluit eigenaar): de gids onder 'naar_live' in data/ids.json mogen op ACTIVE en gepubliceerd worden; niets anders in dezelfde mutatie.
    try: naar_live = set(json.load(open(IDS, encoding="utf-8")).get("naar_live", []))
    except Exception: naar_live = set()
    if TESTMODUS: naar_live = set(env.get("_TEST_NAAR_LIVE", "").split())
    if naar_live:
        nm = veldnamen(query); vs = list((variables or {}).values())
        prod = set(re.findall(r"gid://shopify/Product/\d+", json.dumps(variables or {}) + query))
        if prod and prod <= naar_live:
            if nm == {"productUpdate"} and all(isinstance(p, dict) and set(p) == {"id", "status"} and str(p["status"]).upper() == "ACTIVE" for p in vs): return []
            if nm == {"publishablePublish"} and not re.search(r"(delete|unpublish|archive|urlredirect|theme|inventory|price|discount)", query, re.I): return []
    # Regel 2d (besluit eigenaar 23 november 2026, /goal fase A en B): alleen de mutaties onder 'fase_ab.mutaties' in data/ids.json,
    # en themeFilesUpsert op het live thema alleen voor de bestanden onder 'fase_ab.live_thema_bestanden'. Niets anders in dezelfde mutatie.
    try: fab = json.load(open(IDS, encoding="utf-8")).get("fase_ab", {}) or {}
    except Exception: fab = {}
    if TESTMODUS: fab = json.loads(env.get("_TEST_FASE_AB", "{}"))
    fab_mut, fab_best = set(fab.get("mutaties", [])), set(fab.get("live_thema_bestanden", []))
    nm0 = veldnamen(query)
    if fab_mut and nm0 and nm0 <= fab_mut and not re.search(r"(delete|archive|inventory|price|discount|themepublish|urlredirect)", query, re.I):
        if nm0 == {"themeFilesUpsert"}:
            namen_best = set(re.findall(r'"filename":\s*"([^"]+)"', json.dumps(variables or {})))
            if namen_best and namen_best <= fab_best: return []
        else:
            return []
    for t in set(re.findall(r"gid://shopify/OnlineStoreTheme/\d+", json.dumps(variables or {}) + query)):
        if t != THEMA_KOPIE: fouten.append(f"thema {t} is niet de werkkopie")
    for n in veldnamen(query):
        if n not in TOEGESTAAN or VERBODEN_RE.search(n): fouten.append(f"mutatie '{n}' is niet toegestaan zonder INHUYS_GOLIVE=1")
    if VERBODEN_RE.search(query) and not fouten: fouten.append("de mutatietekst bevat een verboden term (delete/publish/redirect/...)")
    ids, files, live_blok, live_tekst = concept_ids()
    namen = veldnamen(query)
    # Alleen gids die als 'id' (het object dat gemuteerd wordt) in de variabelen staan tellen; een verwijzing in een metaveld-waarde niet.
    def id_waarden(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("id", "themeId") and isinstance(v, str): yield v
                yield from id_waarden(v)
        elif isinstance(o, list):
            for x in o: yield from id_waarden(x)
    mutatie_ids = set(id_waarden(variables or {})) | set(re.findall(r"gid://shopify/[A-Za-z]+/\d+", query))
    for g in live_blok:
        if g in mutatie_ids: fouten.append(f"{g} is live (live_niet_aanraken) en wordt nooit aangeraakt")
    # Besluit eigenaar: de gids onder 'live_naar_concept' mogen van ACTIVE naar DRAFT, met uitsluitend id en status DRAFT.
    try: naar_concept = set(json.load(open(IDS, encoding="utf-8")).get("live_naar_concept", []))
    except Exception: naar_concept = set()
    if TESTMODUS: naar_concept = set(env.get("_TEST_NAAR_CONCEPT", "").split())  # alleen in --test, nooit vanuit de echte omgeving
    ids -= naar_concept
    nc_in_input = [g for g in naar_concept if g in mutatie_ids]
    if nc_in_input:
        if namen != {"productUpdate"}: fouten.append("naar concept: alleen productUpdate is toegestaan")
        for p in (variables or {}).values():
            if isinstance(p, dict) and (set(p) != {"id", "status"} or str(p.get("status")).upper() != "DRAFT"): fouten.append("naar concept: alleen id en status DRAFT zijn toegestaan")
        if not fouten: ids = ids | set(nc_in_input)
    live_in_input = [g for g in live_tekst if g in mutatie_ids and g not in naar_concept]   # een dubbel dat naar concept gaat valt onder de regel hierboven
    if live_in_input:
        # Besluit eigenaar 19 november 2026: tekst op de live producten uit 'live_tekst' mag zonder omgevingsvariabele; alleen de velden hieronder.
        if namen != {"productUpdate"}: fouten.append("live product: alleen productUpdate is toegestaan met INHUYS_LIVE_TEKST=1")
        else:
            for p in (variables or {}).values():
                if isinstance(p, dict) and set(p) - LIVE_TEKST_VELDEN: fouten.append(f"live product: velden niet toegestaan: {sorted(set(p) - LIVE_TEKST_VELDEN)}")
        if not fouten: ids = ids | set(live_in_input)
    if namen & {"productSet", "productCreate"}:
        for v in re.findall(r'"vendor":\s*"([^"]*)"', json.dumps(variables or {})):
            if v in DROPSHIP_MERKEN: fouten.append(f"vendor '{v}' loopt via Orderchamp: nooit zelf aanmaken, alleen productUpdate op het geïmporteerde concept")
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
        ids, _, _, _ = concept_ids()
        globals()["TESTMODUS"] = True
        LIVE ="gid://shopify/Product/999999999999"
        _orig = concept_ids
        globals()["concept_ids"] = lambda: (_orig()[0], _orig()[1], _orig()[2], _orig()[3] | {LIVE})
        upd = 'mutation($p: ProductUpdateInput!) { productUpdate(product: $p) { product { id } userErrors { message } } }'
        proef = [("live tekst zo", upd, {"p": {"id": LIVE, "title": "x"}}, False, {}),
                 ("naar concept ok", upd, {"p": {"id": "gid://shopify/Product/888888888888", "status": "DRAFT"}}, False, {"_TEST_NAAR_CONCEPT": "gid://shopify/Product/888888888888"}),
                 ("naar concept actief", upd, {"p": {"id": "gid://shopify/Product/888888888888", "status": "ACTIVE"}}, True, {"_TEST_NAAR_CONCEPT": "gid://shopify/Product/888888888888"}),
                 ("naar concept extra", upd, {"p": {"id": "gid://shopify/Product/888888888888", "status": "DRAFT", "title": "x"}}, True, {"_TEST_NAAR_CONCEPT": "gid://shopify/Product/888888888888"}),
                 ("ander live concept", upd, {"p": {"id": "gid://shopify/Product/888888888888", "status": "DRAFT"}}, True, {}),
                 ("naar live ok", upd, {"p": {"id": "gid://shopify/Product/777777777777", "status": "ACTIVE"}}, False, {"_TEST_NAAR_LIVE": "gid://shopify/Product/777777777777"}),
                 ("naar live publiceren", 'mutation($id: ID!, $in: [PublicationInput!]!) { publishablePublish(id: $id, input: $in) { userErrors { message } } }', {"id": "gid://shopify/Product/777777777777", "in": [{"publicationId": "gid://shopify/Publication/1"}]}, False, {"_TEST_NAAR_LIVE": "gid://shopify/Product/777777777777"}),
                 ("naar live ander", upd, {"p": {"id": "gid://shopify/Product/666666666666", "status": "ACTIVE"}}, True, {"_TEST_NAAR_LIVE": "gid://shopify/Product/777777777777"}),
                 ("naar live extra", upd, {"p": {"id": "gid://shopify/Product/777777777777", "status": "ACTIVE", "title": "x"}}, True, {"_TEST_NAAR_LIVE": "gid://shopify/Product/777777777777"}),
                 ("beleid ok", 'mutation($p: ShopPolicyInput!) { shopPolicyUpdate(shopPolicy: $p) { userErrors { message } } }', {"p": {"type": "REFUND_POLICY", "body": "<p>x</p>"}}, False, {"_TEST_FASE_AB": '{"mutaties": ["shopPolicyUpdate"]}'}),
                 ("beleid zonder", 'mutation($p: ShopPolicyInput!) { shopPolicyUpdate(shopPolicy: $p) { userErrors { message } } }', {"p": {"type": "REFUND_POLICY", "body": "<p>x</p>"}}, True, {}),
                 ("live thema bestand ok", 'mutation($t: ID!, $f: [OnlineStoreThemeFilesUpsertFileInput!]!) { themeFilesUpsert(themeId: $t, files: $f) { userErrors { message } } }', {"t": "gid://shopify/OnlineStoreTheme/1", "f": [{"filename": "templates/product.json", "body": {"type": "TEXT", "value": "{}"}}]}, False, {"_TEST_FASE_AB": '{"mutaties": ["themeFilesUpsert"], "live_thema_bestanden": ["templates/product.json"]}'}),
                 ("live thema ander bestand", 'mutation($t: ID!, $f: [OnlineStoreThemeFilesUpsertFileInput!]!) { themeFilesUpsert(themeId: $t, files: $f) { userErrors { message } } }', {"t": "gid://shopify/OnlineStoreTheme/1", "f": [{"filename": "layout/theme.liquid", "body": {"type": "TEXT", "value": "x"}}]}, True, {"_TEST_FASE_AB": '{"mutaties": ["themeFilesUpsert"], "live_thema_bestanden": ["templates/product.json"]}'}),
                 ("live status", upd, {"p": {"id": LIVE, "status": "DRAFT"}}, True, {}),
                 ("live varianten", upd, {"p": {"id": LIVE, "variants": []}}, True, {}),
                 ("live tekst ok", upd, {"p": {"id": LIVE, "title": "x", "descriptionHtml": "<p>x</p>", "metafields": []}}, False, {"INHUYS_LIVE_TEKST": "1"}),
                 ("live handle", upd, {"p": {"id": LIVE, "handle": "x"}}, True, {"INHUYS_LIVE_TEKST": "1"}),
                 ("verwijzing ok", upd, {"p": {"id": "gid://shopify/Product/10447099593043", "metafields": [{"namespace": "inhuys", "key": "hoofdproduct", "type": "product_reference", "value": LIVE}]}}, False, {}),
                 ("live menu", 'mutation($id: ID!) { menuUpdate(id: $id, title: "x", items: []) { menu { id } } }', {"id": "gid://shopify/Menu/291696738643"}, True, {}),
                 ("themePublish", 'mutation { themePublish(id: "gid://shopify/OnlineStoreTheme/210233098579") { theme { id } } }', {}, True),
                 ("delete", 'mutation($id: ID!) { productDelete(input: {id: $id}) { deletedProductId } }', {"id": "gid://shopify/Product/1"}, True),
                 ("active", 'mutation($p: ProductSetInput!) { productSet(input: $p) { product { id } } }', {"p": {"status": "ACTIVE", "title": "x"}}, True),
                 ("vreemd id", 'mutation($p: ProductSetInput!) { productSet(input: $p) { product { id } } }', {"p": {"id": "gid://shopify/Product/10447090057555", "status": "DRAFT"}}, True),
                 ("publishable", 'mutation { publishablePublish(id: "gid://shopify/Product/1", input: []) { userErrors { message } } }', {}, True),
                 ("redirect", 'mutation { urlRedirectCreate(urlRedirect: {path: "/a", target: "/b"}) { userErrors { message } } }', {}, True),
                 ("orderchamp", 'mutation($p: ProductSetInput!) { productSet(input: $p) { product { id } } }', {"p": {"title": "x", "status": "DRAFT", "vendor": "Pole To Pole"}}, True),
                 ("concept ok", 'mutation($p: ProductSetInput!) { productSet(input: $p, synchronous: true) { product { id } userErrors { message } } }', {"p": {"title": "Proef", "status": "DRAFT"}}, False),
                 ("thema-kopie ok", 'mutation($t: ID!, $f: [OnlineStoreThemeFilesUpsertFileInput!]!) { themeFilesUpsert(themeId: $t, files: $f) { userErrors { message } } }', {"t": THEMA_KOPIE, "f": []}, False)]
        goed = 0
        for naam, q, v, verwacht_blok, *rest in proef:
            f = controleer(q, v, rest[0] if rest else {}); blok = bool(f)
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
