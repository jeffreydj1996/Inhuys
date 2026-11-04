#!/usr/bin/env python3
"""Haalt bronpagina's van fabrikanten en dealers op via de proxy (curl) en drukt alleen feitregels af.

Gebruik:
  python3 -I tools/bron_ophalen.py sku <sku> [<model>]   poletopole.nl: specificaties per SKU (sitemap -> productpagina -> extraFields)
  python3 -I tools/bron_ophalen.py url <url> [<model>]   willekeurige pagina; bij een Shopify-productpagina ook /products/<handle>.json

Met <model> wordt de platte brontekst toegevoegd aan data/bron-teksten/<model>.txt. Dat bestand dient alleen
voor de 7-woord-overlapcontrole van check_tekst.py; de schrijver krijgt het nooit te zien.
Exit 2: host onbereikbaar (netwerkpolicy of niet-bestaand). Exit 1: SKU niet op poletopole.nl.
"""
import datetime
import html
import json
import os
import re
import subprocess
import sys
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRONMAP = os.path.join(ROOT, "data", "bron-teksten")
SITEMAPS = [
    "https://poletopole.nl/sitemap/products.xml?locale=en-GB",
    "https://poletopole.nl/sitemap/products.xml?locale=nl-NL",
]
VANDAAG = datetime.date.today().isoformat()
MAX_REGELS = 40

# Regels die een feit kunnen bevatten: een maat, gewicht of een kernwoord in NL/EN/DE.
FEIT_RE = re.compile(
    r"\d[\d.,]*\s?(?:cm|mm|kg)\b|"
    r"\b(?:hoogte|breedte|diepte|lengte|zithoogte|zitdiepte|zitbreedte|gewicht|materia|onderhoud|reinig|afmeting|"
    r"leeftijd|belasting|montage|height|width|depth|length|seat|weight|material|cleaning|care|load|assembl|"
    r"ma(?:ß|ss)e|abmessung|sitzh|pflege|alter|jahre|years|belastbar)\w*",
    re.I,
)
# Veldnamen van poletopole.nl naar de rijen van data/feiten/<model>.md.
VELDEN = {
    "Product Width": "breedte",
    "Product Depth": "diepte",
    "Product Height": "hoogte",
    "Product Length": "lengte",
    "Product Weight": "gewicht",
    "Seat Height": "zithoogte",
    "Seat Depth": "zitdiepte",
    "Seat Width": "zitbreedte",
    "Seat Thickness": "zitdikte",
    "Armrest Height": "armleuninghoogte",
    "Maximum Load": "maximale belasting",
    "Materials": "materialen",
    "Fabric": "stof",
    "Cleaning Instructions": "onderhoud (origineel, Engels)",
    "Country of Origin": "land van herkomst",
    "Fire Repellent": "brandvertragend",
    "Original Box Contents": "doosinhoud",
    "Original Box Packing (Width / Depth / Height / Weight / Volume)": "doos (b / d / h / gewicht / volume)",
    "Backrest Height": "rugleuninghoogte",
    "Armrest Width": "armleuningbreedte",
    "Fabric and Composition": "stof en samenstelling",
    "Color": "kleur",
}
# Velden van poletopole.nl die geen productfeit zijn.
RUIS = {"Barcode", "SKU", "HS Code", "Recycling Instructions", "Original Box Quantity", "product path", "filter color", "display order"}


def haal(url):
    """Haalt een URL op met curl (proxy en CA-bundel komen uit de omgeving). Stopt met exit 2 bij een onbereikbare host."""
    r = subprocess.run(
        ["curl", "-sS", "-L", "--max-time", "40", "-A", "Mozilla/5.0 (compatible; InHuys-onderzoek)", "-w", "\n%{http_code}", url],
        capture_output=True, text=True, errors="replace",
    )
    body, _, code = r.stdout.rpartition("\n")
    if r.returncode != 0 or code in ("", "000"):
        print(f"ONBEREIKBAAR: {urlparse(url).netloc} · {r.stderr.strip()[:140]}")
        sys.exit(2)
    return body, code


def platte_tekst(h):
    h = re.sub(r"<(script|style|noscript|svg|template)[^>]*>.*?</\1>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<br\s*/?>|</(?:p|div|li|tr|td|th|h\d|table|dt|dd|section)>", "\n", h, flags=re.I)
    t = html.unescape(re.sub(r"<[^>]+>", " ", h))
    regels = [re.sub(r"[ \t ]+", " ", r).strip() for r in t.splitlines()]
    return "\n".join(r for r in regels if r)


def feitregels(tekst):
    """Regels met een feit; een kort label zonder cijfer (tabelkop als 'Zithoogte') wordt aan de volgende regel geplakt."""
    regels = tekst.splitlines()
    gezien, uit, i = set(), [], 0
    while i < len(regels):
        r = regels[i]
        if len(r) <= 40 and not re.search(r"\d", r) and FEIT_RE.search(r) and i + 1 < len(regels) and len(regels[i + 1]) <= 80 and regels[i + 1].lower() != r.lower():
            r = f"{r}: {regels[i + 1]}"
            i += 1
        i += 1
        if len(r) < 4 or not FEIT_RE.search(r):
            continue
        k = r.lower()
        if k in gezien:
            continue
        gezien.add(k)
        uit.append(r[:200])
        if len(uit) >= MAX_REGELS:
            break
    return uit


def bewaar_brontekst(model, url, tekst):
    if not model:
        return
    os.makedirs(BRONMAP, exist_ok=True)
    pad = os.path.join(BRONMAP, f"{model}.txt")
    with open(pad, "a", encoding="utf-8") as f:
        f.write(f"\n\n## {url} · {VANDAAG}\n{tekst}\n")
    print(f"Brontekst toegevoegd aan {os.path.relpath(pad, ROOT)} ({len(tekst)} tekens)")


def titel_van(h):
    m = re.search(r"<title[^>]*>(.*?)</title>", h, flags=re.S | re.I)
    return re.sub(r"\s+", " ", html.unescape(m.group(1))).strip() if m else ""


def zoek_sku(sku):
    for sm in SITEMAPS:
        body, _ = haal(sm)
        m = re.search(rf"<loc>([^<]*/product/{re.escape(sku)}/[^<]*)</loc>", body)
        if m:
            return html.unescape(m.group(1))
    return None


def modus_sku(sku, model):
    url = zoek_sku(sku)
    if not url:
        print(f"niet op poletopole.nl: SKU {sku} staat niet in de product-sitemap (en-GB, nl-NL). Gebruik de dealers uit analyse/09-bronnen-per-merk.md.")
        sys.exit(1)
    h, code = haal(url)
    paren = re.findall(r'"originalKey":"((?:[^"\\]|\\.)*)","key":"(?:[^"\\]|\\.)*","originalValue":"((?:[^"\\]|\\.)*)"', h)
    print(f"# Feiten van poletopole.nl · SKU {sku}")
    print(f"Bron: {url} · HTTP {code} · geraadpleegd {VANDAAG}")
    print(f"Titel: {titel_van(h)}")
    if not paren:
        print("Geen extraFields gevonden op de pagina; controleer de pagina met de modus url.")
        sys.exit(1)
    velden = {}
    for k, v in paren:
        k = json.loads(f'"{k}"')
        v = json.loads(f'"{v}"').strip()
        if k in RUIS or not v:
            continue
        velden.setdefault(k, [])
        if v not in velden[k]:
            velden[k].append(v)
    print("\n| feit | waarde | bron | datum |\n|---|---|---|---|")
    for k, vs in velden.items():
        print(f"| {VELDEN.get(k, k)} | {', '.join(vs)[:200]} | {url} | {VANDAAG} |")
    # Letterlijke fabrikanttekst (beschrijving en onderhoud) alleen naar het bronbestand voor de overlapcontrole.
    stukken = re.findall(r'"preface":"((?:[^"\\]|\\.)*)"', h)
    tekst = "\n".join(json.loads(f'"{s}"') for s in dict.fromkeys(stukken))
    tekst += "\n" + "\n".join(", ".join(vs) for k, vs in velden.items() if k == "Cleaning Instructions")
    bewaar_brontekst(model, url, tekst.strip())


def shopify_json(url):
    """Geeft (titel, vendor, platte body, varianten) als de URL een Shopify-productpagina is, anders None."""
    u = urlparse(url)
    m = re.match(r"^(?:/[a-z]{2}(?:-[a-z]{2})?)?/products/([^/?#]+)", u.path)
    if not m:
        return None
    body, code = haal(f"{u.scheme}://{u.netloc}/products/{m.group(1)}.json")
    try:
        p = json.loads(body)["product"]
    except (ValueError, KeyError, TypeError):
        return None
    varianten = [(v.get("title"), v.get("weight"), v.get("weight_unit"), v.get("price")) for v in p.get("variants", [])]
    return p.get("title", ""), p.get("vendor", ""), platte_tekst(p.get("body_html") or ""), varianten


def modus_url(url, model):
    h, code = haal(url)
    tekst = platte_tekst(h)
    print(f"# Bron: {url} · HTTP {code} · geraadpleegd {VANDAAG}")
    print(f"Titel: {titel_van(h)}")
    sj = shopify_json(url)
    if sj:
        titel, vendor, body, varianten = sj
        print(f"Shopify-product: {titel} · merk: {vendor}")
        for t, w, eenheid, prijs in varianten[:12]:
            print(f"  variant: {t} · gewicht {w} {eenheid} · prijs {prijs}")
        tekst = body + "\n" + tekst
    regels = feitregels(tekst)
    print(f"\nFeitregels ({len(regels)}, max {MAX_REGELS}):")
    for r in regels:
        print(f" - {r}")
    if not regels:
        print(" (geen regels met maten, gewicht, materiaal of onderhoud gevonden)")
    bewaar_brontekst(model, url, tekst)


def main(argv):
    if len(argv) < 2 or argv[0] not in ("sku", "url"):
        print(__doc__)
        sys.exit(64)
    model = argv[2] if len(argv) > 2 else None
    if model and not re.fullmatch(r"[a-z0-9-]+", model):
        print("model: alleen kleine letters, cijfers en koppeltekens (bestandsnaam in data/bron-teksten/)")
        sys.exit(64)
    if argv[0] == "sku":
        if not re.fullmatch(r"\d{10,14}", argv[1]):
            print("sku: 10 tot 14 cijfers, bijvoorbeeld 871917285905")
            sys.exit(64)
        modus_sku(argv[1], model)
    else:
        if not argv[1].startswith("https://"):
            print("url: begin met https://")
            sys.exit(64)
        modus_url(argv[1], model)


if __name__ == "__main__":
    main(sys.argv[1:])
