#!/usr/bin/env python3
"""Zet een productbestand uit content/producten/<handle>.md om naar productSet-variabelen (data/out/productSet-<handle>.json) en een redirectregel.
Bron van de beelden en huidige alt-teksten: data/raw/products-*.json (export vóór fase 2) plus data/alt-origineel.json.
Gebruik: python3 tools/md_naar_vars.py content/producten/<handle>.md [meer bestanden]   (uitvoer in data/out/, redirects in data/out/redirects-<handle>.csv)
Regels: specificatiewaarden met [AANVULLEN] worden niet naar Shopify gestuurd; alt-teksten van bestaande beelden blijven ongewijzigd (Shopify deelt bestanden)."""
import json, re, sys, glob, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "out")
SPEC_KEYS = ["afmetingen", "zithoogte", "zitdiepte", "gewicht", "materiaal_frame", "materiaal_bekleding", "afwerking", "set_inhoud", "onderhoud", "herkomst", "levertijd", "garantie"]

def bronproducten():
    by = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "data", "raw", "products-*.json"))):
        for e in json.load(open(f, encoding="utf-8"))["data"]["products"]["edges"]:
            n = e["node"]
            imgs = [{"url": m["node"]["image"]["url"], "w": m["node"]["image"].get("width"), "alt": m["node"].get("alt")} for m in n["media"]["edges"] if m["node"].get("image")]
            by[n["handle"]] = {"images": imgs, "title": n["title"]}
    alt = json.load(open(os.path.join(ROOT, "data", "alt-origineel.json"), encoding="utf-8"))
    for h, m in alt.items():
        if h in by:
            for im in by[h]["images"]:
                if im["url"] in m: im["alt"] = m[im["url"]]
    return by

def rt(paragraphs):
    ch = []
    for p in paragraphs:
        if isinstance(p, tuple):
            ch.append({"type": "paragraph", "children": [{"type": "text", "value": p[0], "bold": True}, {"type": "text", "value": " " + p[1]}]})
        else:
            ch.append({"type": "paragraph", "children": [{"type": "text", "value": p}]})
    return json.dumps({"type": "root", "children": ch}, ensure_ascii=False)

def parse(md):
    lines = md.split("\n")
    d = {"title": lines[0].lstrip("# ").strip(), "options": [], "variants": [], "specs": {}, "advies": [], "faq": [], "tags": [], "collections": []}
    m = re.search(r"Handle: `/products/([^`]+)`.*?Merk: (.+?) · Producttype: (.+?)\s*$", md, re.M); d["handle"], d["vendor"], d["ptype"] = m.group(1), m.group(2).strip(), m.group(3).strip()
    m = re.search(r"^Tags: (.*?)\s*$", md, re.M); d["tags"] = [t.strip() for t in m.group(1).split(",") if t.strip()] if m else []
    m = re.search(r"^Categorie: (gid://\S+)", md, re.M); d["category"] = m.group(1) if m else None
    m = re.search(r"^Collecties: (.*?)\s*$", md, re.M); d["collections"] = [c.strip() for c in m.group(1).split(",") if c.strip().startswith("gid://")] if m else []
    m = re.search(r"^Meta-titel \(\d+\): (.*?)\s*$", md, re.M); d["seo_title"] = m.group(1).strip()
    m = re.search(r"^Meta-description \(\d+\): (.*?)\s*$", md, re.M); d["seo_desc"] = m.group(1).strip()
    m = re.search(r"^\*\*Zin onder de titel:\*\* (.*?)\s*$", md, re.M); d["short"] = m.group(1).strip()
    sec = {}; cur = None
    for ln in lines:
        if ln.startswith("## "): cur = ln[3:].strip(); sec[cur] = []
        elif cur: sec[cur].append(ln)
    # varianten
    rows = [r for r in sec["Varianten en prijzen"] if r.startswith("|")]
    head = [c.strip() for c in rows[0].strip("|").split("|")]
    opt_names = head[:head.index("Prijs")]
    d["options"] = [(n, []) for n in opt_names]
    for r in rows[2:]:
        cells = [c.strip() for c in r.strip("|").split("|")]
        ov = dict(zip(opt_names, cells[:len(opt_names)]))
        price = cells[len(opt_names)].replace("€", "").strip().replace(".", "").replace(",", ".")
        sku = cells[len(opt_names) + 1]; sku = None if sku in ("-", "") else sku
        srch = cells[len(opt_names) + 2].strip("`")
        for i, n in enumerate(opt_names):
            if ov[n] not in d["options"][i][1]: d["options"][i][1].append(ov[n])
        d["variants"].append((ov, price, sku, srch))
    # beschrijving
    b = sec["Beschrijving"]; parts = {}; k = None
    for ln in b:
        if ln.startswith("### "): k = ln[4:].strip(); parts[k] = []
        elif k and ln.strip(): parts[k].append(ln.strip())
    d["beschrijving"] = [(k, " ".join(v)) for k, v in parts.items()]
    # specs
    for r in [r for r in sec.get("Specificaties (metavelden `inhuys.*`)", []) if r.startswith("|")][2:]:
        cells = [c.strip() for c in r.strip("|").split("|")]
        if len(cells) >= 2 and cells[0] in SPEC_KEYS: d["specs"][cells[0]] = cells[1]
    d["advies"] = [ln.strip() for ln in sec.get("Advies van InHuys", []) if ln.strip()]
    q = None
    for ln in sec.get("Veelgestelde vragen", []):
        s = ln.strip()
        if s.startswith("**") and s.endswith("**"): q = s.strip("*").strip()
        elif q and s: d["faq"].append((q, s)); q = None
    return d

def build(d, by):
    base = d["title"].split(" (")[0]
    html = "".join(f"<h3>{k}</h3><p>{v}</p>" for k, v in d["beschrijving"])
    files, seen, alts = [], set(), {}
    for (ov, price, sku, srch) in d["variants"]:
        if srch in seen: continue
        seen.add(srch)
        it = by.get(srch)
        if not it: raise SystemExit(f"bronproduct onbekend in data/raw: {srch}")
        for i, im in enumerate(it["images"], 1):
            f = {"originalSource": im["url"], "contentType": "IMAGE"}
            if im.get("alt"): f["alt"] = im["alt"]
            files.append(f)
            if i == 1: alts[srch] = im.get("alt")
    variants = []
    for (ov, price, sku, srch) in d["variants"]:
        it = by[srch]
        v = {"optionValues": [{"optionName": k, "name": val} for k, val in ov.items()], "price": price, "inventoryItem": {"tracked": False}}
        if sku: v["sku"] = sku
        if it["images"]:
            v["file"] = {"originalSource": it["images"][0]["url"], "contentType": "IMAGE"}
            if alts[srch]: v["file"]["alt"] = alts[srch]
        variants.append(v)
    mfs = [{"namespace": "descriptor", "key": "short_description", "type": "single_line_text_field", "value": d["short"]}]
    for k in SPEC_KEYS:
        v = d["specs"].get(k)
        if v and "[AANVULLEN" not in v: mfs.append({"namespace": "inhuys", "key": k, "type": "single_line_text_field", "value": v})
    mfs.append({"namespace": "inhuys", "key": "advies", "type": "rich_text_field", "value": rt(d["advies"])})
    mfs.append({"namespace": "inhuys", "key": "faq", "type": "rich_text_field", "value": rt([(q, a) for q, a in d["faq"]])})
    inp = {"title": d["title"], "handle": d["handle"], "status": "DRAFT", "vendor": d["vendor"], "productType": d["ptype"], "tags": d["tags"], "category": d["category"],
           "descriptionHtml": html, "seo": {"title": d["seo_title"], "description": d["seo_desc"]},
           "productOptions": [{"name": name, "position": i + 1, "values": [{"name": v} for v in vals]} for i, (name, vals) in enumerate(d["options"])],
           "variants": variants, "files": files, "metafields": mfs}
    if d["collections"]: inp["collections"] = d["collections"]
    if not inp["category"]: inp.pop("category")
    return inp

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    by = bronproducten()
    for path in sys.argv[1:]:
        md = open(path, encoding="utf-8").read()
        if "Handle: `/products/" not in md:
            print(f"overgeslagen (geen productbestand): {path}"); continue
        d = parse(md)
        inp = build(d, by)
        out = os.path.join(OUT, f"productSet-{d['handle']}.json")
        json.dump(inp, open(out, "w", encoding="utf-8"), ensure_ascii=False)
        red = os.path.join(OUT, f"redirects-{d['handle']}.csv")
        seen = []
        for (_, _, _, srch) in d["variants"]:
            if srch not in seen and srch != d["handle"]: seen.append(srch)
        open(red, "w", encoding="utf-8").write("oude_handle;nieuwe_handle\n" + "".join(f"{s};{d['handle']}\n" for s in seen))
        print(f"{d['handle']}: {len(inp['variants'])} varianten, {len(inp['files'])} beelden, {len(inp['metafields'])} metavelden, {len(seen)} redirects -> {os.path.relpath(out, ROOT)}")
