#!/usr/bin/env python3
"""Productaudit Inhuys · fase 1. Leest de ruwe Admin API-exports (alleen-lezen) en schrijft CSV's + samenvatting."""
import json, re, csv, sys, glob, html, collections, statistics
from pathlib import Path

DATA = Path(sys.argv[1]); OUT = Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)

def strip_html(s):
    s = re.sub(r'<br\s*/?>', ' ', s or '', flags=re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

products = []
for f in sorted(glob.glob(str(DATA / 'products-*.json'))):
    d = json.load(open(f))
    products += [e['node'] for e in d['data']['products']['edges']]
cols = [e['node'] for e in json.load(open(DATA / 'collections.json'))['data']['collections']['edges']]

SPEC_RE = re.compile(r'\b(\d+([.,]\d+)?\s?(cm|mm|kg)|afmeting|hoogte|breedte|diepte|lengte|diameter|zithoogte|materiaal|gewicht)\b', re.I)
U_RE = re.compile(r'\b(u|uw)\b', re.I); JE_RE = re.compile(r'\b(je|jouw|jij)\b', re.I)
EN_RE = re.compile(r'\b(the|and|with|chair|sofa|dining|your|our)\b', re.I)
TEMPLATE_RE = re.compile(r'(Fijn voor wie houdt van een interieur dat klopt in detail|Tijdloos ontwerp dat gemakkelijk combineert met verschillende stijlen|InHuys selectie|verzonden via een zorgvuldig geselecteerde partner)', re.I)
DIM_RE = re.compile(r'\d+([.,]\d+)?\s?(cm|mm)\b|Ø|zithoogte|afmeting', re.I)
MATERIAL_RE = re.compile(r'\b(materia(al|len)|hout|eiken|staal|metaal|stof|boucl|velvet|fluweel|linnen|katoen|marmer|travertin|steen|keramiek|glas|leer|rotan|teak|mango)\b', re.I)
GARBLED_RE = re.compile(r'(voorzitter|aangevoerd|wouten|loterij|schiereiland|\bchair\b|\bsofa\b|seater|dining|lounge chair|\bcream\b|\bblack\b|\bgold\b|\bwhite\b|stoelcr|\bset of\b)', re.I)
FILENAME_ALT = re.compile(r'(\.(jpe?g|png|webp)|^img[_ -]?\d|^dsc|_\d{3,}|^\d+$)', re.I)

desc_counter = collections.Counter()
rows = []
for p in products:
    text = strip_html(p.get('descriptionHtml'))
    words = len(text.split()) if text else 0
    desc_counter[text[:200]] += 1 if words else 0
for p in products:
    text = strip_html(p.get('descriptionHtml'))
    words = len(text.split()) if text else 0
    media = [m['node'] for m in p['media']['edges']]
    images = [m for m in media if m['mediaContentType'] == 'IMAGE']
    alt_missing = sum(1 for m in images if not (m.get('alt') or '').strip())
    alt_filename = sum(1 for m in images if (m.get('alt') or '') and FILENAME_ALT.search(m['alt']))
    variants = [v['node'] for v in p['variants']['edges']]
    prices = [float(v['price']) for v in variants if v.get('price') is not None]
    mfs = [m['node'] for m in p['metafields']['edges']]
    spec_mfs = [m for m in mfs if m['namespace'] in ('shopify', 'custom', 'descriptor', 'inhuys') and not m['key'].startswith('related')]
    specs_in_text = bool(SPEC_RE.search(text))
    specs = bool(spec_mfs) or specs_in_text
    seo = p.get('seo') or {}
    mt = (seo.get('title') or '').strip(); md = (seo.get('description') or '').strip()
    u_hits = len(U_RE.findall(text)); je_hits = len(JE_RE.findall(text)); en_hits = len(EN_RE.findall(text))
    aanspreek = 'u' if u_hits > je_hits and u_hits else ('je' if je_hits else ('engels' if en_hits >= 3 else '-'))
    colls = [c['node']['title'] for c in p['collections']['edges']]
    sjabloon = bool(TEMPLATE_RE.search(text))
    m_fab = re.search(r'klopt in detail:\s*(.+?)(?:\.|$)', text)
    fabrikantzin = (m_fab.group(1).strip()[:120] if m_fab else '')
    afmetingen = bool(DIM_RE.search(text)) or any(o['name'].lower() in ('maat','diameter') for o in p.get('options') or [])
    materiaal = bool(MATERIAL_RE.search(text)) or any(m['key'] in ('material','decoration-material','furniture-fixture-material','upholstery-material') for m in spec_mfs)
    titel_rommel = bool(GARBLED_RE.search(p['title']))
    alts = {(m.get('alt') or '').strip() for m in images}
    alt_identiek = len(images) > 1 and len(alts) == 1
    min_w = min([(m.get('image') or {}).get('width') or 0 for m in images], default=0)
    cat = (p.get('category') or {}).get('fullName') or ''
    dup = desc_counter[text[:200]] - 1 if words else 0
    complete_fields = all([p.get('vendor'), p.get('productType'), cat])
    if not images or words < 20:
        score = 'D'
    elif sjabloon or not afmetingen or not materiaal or aanspreek in ('u', 'engels') or titel_rommel:
        score = 'C'
    elif not (mt and md) or alt_missing or alt_identiek or len(images) < 3 or min_w < 1000 or not complete_fields:
        score = 'B'
    else:
        score = 'A'
    rows.append({
        'id': p['id'].split('/')[-1], 'titel': p['title'], 'handle': p['handle'], 'status': p['status'],
        'gepubliceerd': 'ja' if p.get('publishedAt') else 'nee',
        'merk': p.get('vendor') or '', 'producttype': p.get('productType') or '', 'categorie': cat,
        'tags': '|'.join(p.get('tags') or []), 'collecties': '|'.join(colls),
        'prijs_min': f"{min(prices):.2f}" if prices else '', 'prijs_max': f"{max(prices):.2f}" if prices else '',
        'varianten': len(variants), 'opties': '|'.join(o['name'] for o in p.get('options') or [] if o['name'] != 'Title'),
        'beschrijving_woorden': words, 'aanspreekvorm': aanspreek, 'beschrijving_identiek_aan_n_andere': dup,
        'meta_titel': 'ja' if mt else 'nee', 'meta_titel_lengte': len(mt),
        'meta_description': 'ja' if md else 'nee', 'meta_description_lengte': len(md),
        'afbeeldingen': len(images), 'alt_ontbreekt': alt_missing, 'alt_is_bestandsnaam': alt_filename,
        'specificaties': 'metavelden' if spec_mfs else ('in tekst' if specs_in_text else 'nee'),
        'sjabloontekst': 'ja' if sjabloon else 'nee', 'fabrikantzin_ingeplakt': fabrikantzin,
        'afmetingen': 'ja' if afmetingen else 'nee', 'materiaal_benoemd': 'ja' if materiaal else 'nee',
        'titel_vertaalfout_of_engels': 'ja' if titel_rommel else 'nee', 'alt_identiek_per_product': 'ja' if alt_identiek else 'nee',
        'kleinste_afbeelding_px': min_w,
        'spec_metavelden': '|'.join(f"{m['namespace']}.{m['key']}" for m in spec_mfs),
        'template': p.get('templateSuffix') or '', 'aangemaakt': p['createdAt'][:10], 'bijgewerkt': p['updatedAt'][:10],
        'score': score,
    })

fields = list(rows[0].keys())
with open(OUT / 'producten.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fields, delimiter=';'); w.writeheader(); w.writerows(rows)

crows = []
for c in cols:
    text = strip_html(c.get('descriptionHtml')); words = len(text.split()) if text else 0
    rs = c.get('ruleSet')
    rules = ' OF '.join if (rs and rs.get('appliedDisjunctively')) else ' EN '.join
    rule_txt = rules(f"{r['column']} {r['relation']} '{r['condition']}'" for r in rs['rules']) if rs else 'handmatig'
    u_hits = len(U_RE.findall(text)); je_hits = len(JE_RE.findall(text))
    crows.append({'id': c['id'].split('/')[-1], 'titel': c['title'], 'handle': c['handle'], 'type': 'automatisch' if rs else 'handmatig',
                  'regels': rule_txt, 'producten': c['productsCount']['count'], 'beschrijving_woorden': words,
                  'aanspreekvorm': 'u' if u_hits > je_hits and u_hits else ('je' if je_hits else '-'),
                  'meta_titel': 'ja' if (c.get('seo') or {}).get('title') else 'nee',
                  'meta_description': 'ja' if (c.get('seo') or {}).get('description') else 'nee',
                  'afbeelding': 'ja' if c.get('image') else 'nee', 'sortering': c['sortOrder'], 'template': c.get('templateSuffix') or '',
                  'bijgewerkt': c['updatedAt'][:10]})
with open(OUT / 'collecties.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(crows[0].keys()), delimiter=';'); w.writeheader(); w.writerows(crows)

# ---------- samenvatting ----------
def pct(n, d): return f"{(100*n/d):.0f}%" if d else '-'
def table(headers, data):
    out = ['| ' + ' | '.join(headers) + ' |', '|' + '---|' * len(headers)]
    out += ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in data]
    return '\n'.join(out)

L = []
act = [r for r in rows if r['status'] == 'ACTIVE']; dr = [r for r in rows if r['status'] == 'DRAFT']; ar = [r for r in rows if r['status'] == 'ARCHIVED']
L.append('## Totalen\n'); L.append(table(['Status', 'Aantal'], [['Actief (live)', len(act)], ['Concept', len(dr)], ['Gearchiveerd', len(ar)], ['Totaal', len(rows)]]))

def missing_table(sub, label):
    n = len(sub)
    d = [
        ['Beschrijving ontbreekt of < 20 woorden', sum(r['beschrijving_woorden'] < 20 for r in sub)],
        ['Beschrijving < 80 woorden', sum(r['beschrijving_woorden'] < 80 for r in sub)],
        ['Beschrijving in u-vorm', sum(r['aanspreekvorm'] == 'u' for r in sub)],
        ['Beschrijving (deels) Engels', sum(r['aanspreekvorm'] == 'engels' for r in sub)],
        ['Beschrijving identiek aan een ander product', sum(r['beschrijving_identiek_aan_n_andere'] > 0 for r in sub)],
        ['Meta-titel ontbreekt', sum(r['meta_titel'] == 'nee' for r in sub)],
        ['Meta-description ontbreekt', sum(r['meta_description'] == 'nee' for r in sub)],
        ['Geen afbeelding', sum(r['afbeeldingen'] == 0 for r in sub)],
        ['Minder dan 3 afbeeldingen', sum(r['afbeeldingen'] < 3 for r in sub)],
        ['Minstens één alt-tekst ontbreekt', sum(r['alt_ontbreekt'] > 0 for r in sub)],
        ['Alle alt-teksten ontbreken', sum(r['alt_ontbreekt'] == r['afbeeldingen'] and r['afbeeldingen'] > 0 for r in sub)],
        ['Sjabloontekst (gegenereerde standaardzinnen)', sum(r['sjabloontekst'] == 'ja' for r in sub)],
        ['Fabrikantzin letterlijk ingeplakt', sum(bool(r['fabrikantzin_ingeplakt']) for r in sub)],
        ['Geen afmetingen in tekst of opties', sum(r['afmetingen'] == 'nee' for r in sub)],
        ['Materiaal niet benoemd', sum(r['materiaal_benoemd'] == 'nee' for r in sub)],
        ['Titel met vertaalfout of Engels', sum(r['titel_vertaalfout_of_engels'] == 'ja' for r in sub)],
        ['Alle alt-teksten per product identiek', sum(r['alt_identiek_per_product'] == 'ja' for r in sub)],
        ['Kleinste afbeelding < 1000 px', sum(0 < r['kleinste_afbeelding_px'] < 1000 for r in sub)],
        ['Geen specificaties (metavelden of in tekst)', sum(r['specificaties'] == 'nee' for r in sub)],
        ['Geen specificatie-metavelden', sum(r['specificaties'] != 'metavelden' for r in sub)],
        ['Productcategorie (Shopify-taxonomie) ontbreekt', sum(not r['categorie'] for r in sub)],
        ['Producttype ontbreekt', sum(not r['producttype'] for r in sub)],
        ['Merk (vendor) ontbreekt', sum(not r['merk'] for r in sub)],
        ['Geen tags', sum(not r['tags'] for r in sub)],
        ['In geen enkele collectie', sum(not r['collecties'] for r in sub)],
        ['Alleen in Bestsellers/Homepage/Adviezen', sum(bool(r['collecties']) and set(r['collecties'].split('|')) <= {'Bestsellers', 'Homepage', 'Adviezen'} for r in sub)],
    ]
    return table(['Ontbreekt of onvoldoende', f'{label} (n={n})', '%'], [[a, b, pct(b, n)] for a, b in d])

L.append('\n## Wat ontbreekt per product · live producten\n'); L.append(missing_table(act, 'Actief'))
L.append('\n## Wat ontbreekt per product · concepten\n'); L.append(missing_table(dr, 'Concept'))

sc = collections.Counter(r['score'] for r in act); scd = collections.Counter(r['score'] for r in dr)
L.append('\n## Score\n'); L.append(table(['Score', 'Actief', 'Concept'], [[s, sc.get(s, 0), scd.get(s, 0)] for s in 'ABCD']))

def group(key, sub, top=None):
    c = collections.Counter((r[key] or '(leeg)') for r in sub)
    items = c.most_common(top)
    return table([key, 'Aantal'], items)
L.append('\n## Merken (vendor) · alle producten\n'); L.append(group('merk', rows))
L.append('\n## Merken (vendor) · live\n'); L.append(group('merk', act))
L.append('\n## Producttypes · alle producten\n'); L.append(group('producttype', rows))
L.append('\n## Productcategorie (Shopify-taxonomie) · alle producten\n'); L.append(group('categorie', rows))
L.append('\n## Aanspreekvorm in beschrijvingen · alle producten met tekst\n'); L.append(group('aanspreekvorm', [r for r in rows if r['beschrijving_woorden'] >= 20]))

def buckets(sub):
    b = collections.OrderedDict([('< €50', 0), ('€50 – €150', 0), ('€150 – €500', 0), ('€500 – €1.500', 0), ('€1.500 – €3.000', 0), ('> €3.000', 0), ('geen prijs', 0)])
    for r in sub:
        if not r['prijs_max']: b['geen prijs'] += 1; continue
        p = float(r['prijs_max'])
        k = '< €50' if p < 50 else '€50 – €150' if p < 150 else '€150 – €500' if p < 500 else '€500 – €1.500' if p < 1500 else '€1.500 – €3.000' if p < 3000 else '> €3.000'
        b[k] += 1
    return table(['Prijsklasse (hoogste variantprijs)', 'Actief', 'Concept'], [[k, b[k], bd[k]] for k in b]) if False else b
ba = buckets(act); bd = buckets(dr)
L.append('\n## Prijsverdeling\n'); L.append(table(['Prijsklasse (hoogste variantprijs)', 'Actief', 'Concept'], [[k, ba[k], bd[k]] for k in ba]))
pa = [float(r['prijs_max']) for r in act if r['prijs_max']]
if pa: L.append(f"\nLive: laagste € {min(pa):.2f}, hoogste € {max(pa):.2f}, mediaan € {statistics.median(pa):.2f}.")

L.append('\n## Live producten · volledig overzicht\n')
L.append(table(['Titel', 'Merk', 'Type', 'Prijs', 'Woorden', 'Aanspreek', 'Meta', 'Afb.', 'Alt mist', 'Afmetingen', 'Collecties', 'Score'],
               [[r['titel'], r['merk'] or '-', r['producttype'] or '-', f"€ {r['prijs_max']}" if r['prijs_max'] else '-', r['beschrijving_woorden'], r['aanspreekvorm'],
                 ('T' if r['meta_titel'] == 'ja' else '-') + ('D' if r['meta_description'] == 'ja' else '-'), r['afbeeldingen'], r['alt_ontbreekt'],
                 r['afmetingen'], r['collecties'].replace('|', ', ') or '-', r['score']] for r in sorted(act, key=lambda r: -float(r['prijs_max'] or 0))]))

L.append('\n## Collecties\n')
L.append(table(['Collectie', 'Handle', 'Type', 'Regels', 'Producten', 'Woorden', 'Aanspreek', 'Meta T/D', 'Afb.'],
               [[c['titel'], c['handle'], c['type'], c['regels'], c['producten'], c['beschrijving_woorden'], c['aanspreekvorm'],
                 ('T' if c['meta_titel'] == 'ja' else '-') + ('D' if c['meta_description'] == 'ja' else '-'), c['afbeelding']] for c in crows]))

L.append('\n## Concepten · overzicht per merk en type\n')
cc = collections.Counter((r['merk'] or '(leeg)', r['producttype'] or '(leeg)') for r in dr)
L.append(table(['Merk', 'Type', 'Concepten'], [[a, b, n] for (a, b), n in cc.most_common()]))

L.append('\n## Concepten · toplijst op prijs (hoogste 25)\n')
L.append(table(['Titel', 'Merk', 'Prijs', 'Woorden', 'Afb.', 'Score'],
               [[r['titel'], r['merk'] or '-', f"€ {r['prijs_max']}" if r['prijs_max'] else '-', r['beschrijving_woorden'], r['afbeeldingen'], r['score']]
                for r in sorted(dr, key=lambda r: -float(r['prijs_max'] or 0))[:25]]))

open(OUT / 'samenvatting.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print(f"producten: {len(rows)} (actief {len(act)}, concept {len(dr)}, archief {len(ar)}); collecties: {len(crows)}")
