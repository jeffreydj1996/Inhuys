# tools/ · scripts van InHuys

Alle scripts draaien vanuit de repo-root met `python3 -I tools/<script>.py`. Teksten staan in `content/`, nooit in Python. Grote uitvoer gaat naar `data/out/` (niet in git).

| Script | Doet | Gebruik |
|---|---|---|
| `md_naar_vars.py` | Productbestand (`content/producten/<handle>.md`) → `data/out/productSet-<handle>.json` + `redirects-<handle>.csv`. Beelden en huidige alt-teksten uit `data/raw` en `data/alt-origineel.json`; `[AANVULLEN]`-waarden gaan niet mee; optievolgorde = volgorde in de variantentabel; rij `hoofdproduct` (handle) wordt metaveld `inhuys.hoofdproduct` (product_reference). | `python3 -I tools/md_naar_vars.py content/producten/x.md` |
| `nodes_uit_logboek.py` | Haalt de ruwe productknopen uit het logboek van een lezer (`/tmp/claude-0/.../tasks/<agentId>.output`) naar JSON, zonder overtypen door een agent. Gebruik: `python3 -I tools/nodes_uit_logboek.py <agent.output> data/orderchamp/verificatie/<batch>-nodes.json`. |
| `verifieer_overzetting.py` | Vergelijkt die knopen byte-voor-byte met `data/out/productSet-<handle>.json` (titel, type, tags, categorie, seo, descriptionHtml, alle metavelden). Gebruik: `python3 -I tools/verifieer_overzetting.py <nodes.json> data/orderchamp/verificatie/verschillen-<batch>.txt`. Na elke overzetting draaien: de uitvoerder geeft de tekst als toolargument door en kan daarbij overtypen. |
| `check_tekst.py` | Controle op u-vorm, Engels, sjabloonzinnen, plaatshouders, meta-lengtes, verplichte koppen, 7-woord-overlap met oude product- en fabrikantteksten. Exit 1 bij fouten. | `python3 -I tools/check_tekst.py content/producten/*.md` |
| `guard_shopify.py` | PreToolUse-hook: blokkeert elke Shopify-mutatie buiten concepten en de thema-kopie (zie `.claude/settings.json`); blokkeert `productSet`/`productCreate` voor Orderchamp-merken en alles op `live_niet_aanraken`; met `INHUYS_LIVE_TEKST=1` mag `productUpdate` (alleen titel, tekst, seo, type, tags, categorie, metavelden, collecties) op gids uit `live_tekst` in `data/ids.json`. | `python3 -I tools/guard_shopify.py --test` |
| `snapshot.py` | Vergelijkt twee momentopnames van live objecten (gemaakt door de lezer met `gql/snapshot.graphql`). Exit 1 bij wijzigingen. | `python3 -I tools/snapshot.py data/snapshots/a.txt data/snapshots/b.txt` |
| `status.py` | Statusregister `data/status.csv`; `set handle gid=...` werkt ook `data/ids.json` bij. | `python3 -I tools/status.py show` |
| `gsc_meting.py` | Search Console-meting (28 dagen) → `analyse/gsc/<datum>-*.csv` en `analyse/gsc-rapport-<datum>.md` met delta's. | `python3 -I tools/gsc_meting.py` |
| `bron_ophalen.py` | Haalt bronpagina's op via de proxy (curl) en print alleen feitregels; `sku` leest de specificaties per SKU van poletopole.nl, `url` een fabrikant- of dealerpagina (Shopify: ook `/products/<handle>.json`), `zoek` andere uitvoeringen in de sitemap van poletopole.nl, `dealer` product-URL's uit de eigen zoekfunctie van de dealers. Met `<model>` gaat de brontekst naar `data/bron-teksten/<model>.txt` voor de overlapcontrole. Exit 2 bij een onbereikbare host. Hosts: `analyse/09-bronnen-per-merk.md`. | `python3 -I tools/bron_ophalen.py sku 871917285905 cairo-loungestoel` |
| `audit.py` | Productaudit uit de ruwe export (fase 1). | `python3 -I tools/audit.py data/raw data/out/audit` |
| `theme_build.py` | Bouwt de thema-werkversie uit `data/theme-origineel/` naar `data/out/theme-new/` + `theme-vars-*.json` + `theme-changelog.json`. Upload via de shopify-uitvoerder (`themeFilesUpsert`, alleen kopie 210233098579). | `python3 -I tools/theme_build.py data/theme-origineel data/out/theme-new` |
| `pages.py`, `collections.py` | Fase 2-generatoren voor pagina's en collecties (teksten nog in het script; bij een volgende wijziging omzetten naar md + converter zoals bij producten). | `python3 -I tools/pages.py content/paginas data/out/pages-vars.json` |
| `products_build.py`, `articles_build.py` | Fase 2-generatoren, vervangen door `md_naar_vars.py`; alleen bewaard als regressiebron. | – |
| `gql/*.graphql` | Vaste query- en mutatieteksten voor de agents. | – |

Regressie `md_naar_vars.py` (26 oktober 2026): 12 van 13 producten byte-gelijk aan de fase 2-uitvoer; Bank Londen verschilt alleen in de volgorde van de kleurwaarden (Umber vóór Tan, volgens de tabel).
