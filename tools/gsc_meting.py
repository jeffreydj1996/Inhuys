#!/usr/bin/env python3
"""Search Console-meting via de API (serviceaccount via de omgevingsproxy, alleen lezen).
Schrijft analyse/gsc/<datum>-zoekopdrachten.csv, -paginas.csv, -apparaten.csv, -sitemaps.csv (laatste 28 dagen tot drie dagen geleden)
en analyse/gsc-rapport-<datum>.md met de verschillen ten opzichte van de vorige meting. Gebruik: python3 tools/gsc_meting.py [--datum JJJJ-MM-DD]"""
import json, subprocess, sys, os, csv, datetime, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GSC = os.path.join(ROOT, "analyse", "gsc"); SITE = "sc-domain%3Ain-huys.nl"
API = f"https://www.googleapis.com/webmasters/v3/sites/{SITE}"
def api(path, body=None):
    cmd = ["curl", "-sS", "--max-time", "40", API + path]
    if body is not None: cmd += ["-H", "Content-Type: application/json", "-X", "POST", "-d", json.dumps(body)]
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    try: return json.loads(out)
    except Exception: return {"error": out[:300]}
def rows(dim, start, end, limit=250):
    d = api("/searchAnalytics/query", {"startDate": start, "endDate": end, "dimensions": [dim], "rowLimit": limit})
    if "error" in d: raise SystemExit(f"API-fout: {d['error']}")
    return [(r["keys"][0], r["clicks"], r["impressions"], round(r["ctr"] * 100, 1), round(r["position"], 1)) for r in d.get("rows", [])]
def schrijf(path, kop, data):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";"); w.writerow([kop, "klikken", "vertoningen", "ctr", "positie"]); w.writerows(data)
def lees(path):
    if not os.path.exists(path): return {}
    r = list(csv.reader(open(path, encoding="utf-8"), delimiter=";"))[1:]
    return {x[0]: (int(x[1]), int(x[2]), float(x[4])) for x in r if len(x) >= 5}
def main():
    datum = sys.argv[sys.argv.index("--datum") + 1] if "--datum" in sys.argv else datetime.date.today().isoformat()
    end = (datetime.date.fromisoformat(datum) - datetime.timedelta(days=3)).isoformat()
    start = (datetime.date.fromisoformat(end) - datetime.timedelta(days=27)).isoformat()
    os.makedirs(GSC, exist_ok=True)
    q, p, dev = rows("query", start, end), rows("page", start, end), rows("device", start, end)
    schrijf(f"{GSC}/{datum}-zoekopdrachten.csv", "zoekopdracht", q); schrijf(f"{GSC}/{datum}-paginas.csv", "pagina", p); schrijf(f"{GSC}/{datum}-apparaten.csv", "apparaat", dev)
    sm = api("/sitemaps").get("sitemap", [])
    with open(f"{GSC}/{datum}-sitemaps.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";"); w.writerow(["pad", "laatst_gelezen", "fouten", "waarschuwingen", "type", "ingediend", "geindexeerd"])
        for s in sm:
            for c in s.get("contents", []) or [{}]: w.writerow([s.get("path"), s.get("lastDownloaded"), s.get("errors"), s.get("warnings"), c.get("type"), c.get("submitted"), c.get("indexed")])
    vorige = sorted(x for x in glob.glob(f"{GSC}/*-zoekopdrachten.csv") if not x.endswith(f"{datum}-zoekopdrachten.csv"))
    vq = lees(vorige[-1]) if vorige else {}; vp = lees(vorige[-1].replace("zoekopdrachten", "paginas")) if vorige else {}
    vdatum = os.path.basename(vorige[-1])[:10] if vorige else "geen"
    tk, ti = sum(x[1] for x in q), sum(x[2] for x in q); vk, vi = sum(v[0] for v in vq.values()), sum(v[1] for v in vq.values())
    doel = []
    zw = os.path.join(ROOT, "analyse", "zoekwoorden.csv")
    if os.path.exists(zw):
        for r in csv.DictReader(open(zw, encoding="utf-8"), delimiter=";"):
            if r.get("prioriteit") == "1": doel.append(r["zoekterm"].lower())
    qd = {x[0]: x for x in q}
    L = [f"# Search Console-meting {datum}", "", f"Periode {start} tot {end} (28 dagen), vergeleken met de meting van {vdatum}.", "",
         "| | Nu | Vorige | Verschil |", "|---|---|---|---|", f"| Klikken | {tk} | {vk} | {tk - vk:+d} |", f"| Vertoningen | {ti} | {vi} | {ti - vi:+d} |",
         f"| Zoekopdrachten met vertoning | {len(q)} | {len(vq)} | {len(q) - len(vq):+d} |", f"| Pagina's met vertoning | {len(p)} | {len(vp)} | {len(p) - len(vp):+d} |", "",
         "## Sitemap", ""]
    for s in sm:
        for c in s.get("contents", []): L.append(f"- {s.get('path')}: {c.get('type')} ingediend {c.get('submitted')}, geïndexeerd {c.get('indexed')}; laatst gelezen {str(s.get('lastDownloaded'))[:16]}; fouten {s.get('errors')}")
    if not sm: L.append("- geen sitemap aangemeld")
    L += ["", "## Doelzoekwoorden (prioriteit 1)", "", "| Zoekterm | Vertoningen | Positie | Vorige positie |", "|---|---|---|---|"]
    for t in doel:
        x = qd.get(t); v = vq.get(t)
        L.append(f"| {t} | {x[2] if x else 0} | {x[4] if x else '-'} | {v[2] if v else '-'} |")
    L += ["", "## Top 10 zoekopdrachten", "", "| Zoekopdracht | Klikken | Vertoningen | Positie | Vorige positie |", "|---|---|---|---|---|"]
    for x in sorted(q, key=lambda r: (-r[1], -r[2]))[:10]:
        v = vq.get(x[0]); L.append(f"| {x[0]} | {x[1]} | {x[2]} | {x[4]} | {v[2] if v else '-'} |")
    L += ["", "## Top 10 pagina's", "", "| Pagina | Klikken | Vertoningen | Positie | Vorige vertoningen |", "|---|---|---|---|---|"]
    for x in sorted(p, key=lambda r: (-r[1], -r[2]))[:10]:
        v = vp.get(x[0]); L.append(f"| {x[0].replace('https://www.in-huys.nl', '')} | {x[1]} | {x[2]} | {x[4]} | {v[1] if v else '-'} |")
    L += ["", "## Apparaten", "", "| Apparaat | Klikken | Vertoningen | Positie |", "|---|---|---|---|"] + [f"| {x[0]} | {x[1]} | {x[2]} | {x[4]} |" for x in dev]
    L += ["", "Bron: Search Console API, alleen lezen. Ruwe cijfers in analyse/gsc/" + datum + "-*.csv."]
    out = os.path.join(ROOT, "analyse", f"gsc-rapport-{datum}.md"); open(out, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"klikken {tk} ({tk - vk:+d}) · vertoningen {ti} ({ti - vi:+d}) · zoekopdrachten {len(q)} · pagina's {len(p)} · sitemaps {len(sm)} · rapport {os.path.relpath(out, ROOT)}")
if __name__ == "__main__": main()
