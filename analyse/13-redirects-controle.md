# Controle redirects · 19 november 2026

Uitgevoerd met `python3 -I tools/redirects_check.py` op `analyse/redirects.csv` (141 regels), `data/orderchamp/varianten-2026-11-19.json` (215 producten, 27 actief) en `data/ids.json` (`producten` en `live_tekst`). Er is niets in de CSV gewijzigd: `--fix` (ketens platslaan, exacte dubbelen weg) vond niets om te herstellen.

## Uitkomst

| Controle | Aantal |
|---|---|
| Dubbele oude handles (exact of met ander doel) | 0 |
| Zelfverwijzingen en kringen | 0 |
| Ketens (doel is zelf een oude handle) | 0 |
| Oude handle die tegelijk geplande handle van een ander product is | 0 |
| Doel dat geen geplande of bestaande handle is | 1 |
| Live product met afwijkende handle zonder regel | 1 (Flitsadvies, bedoeld) |

## Twijfelgevallen (niet aangepast)

1. **`eettafel-sycomore-l` naar `eettafel-sycomore`**: `eettafel-sycomore` staat wel in `data/status.csv` (tekst klaar) maar niet in `data/ids.json`: er is nog geen Orderchamp-concept geïmporteerd. Het oude product is concept (nooit publiek), dus de regel hoeft niet bij go-live. Voorstel: regel schrappen of pas laten gelden na import.
2. **`flitsadvies`**: staat actief en heeft geen geplande handle; de handle verandert niet, dus geen regel nodig.
3. **Doelen die na go-live concept blijven.** 21 van de 84 doelhandles horen bij producten die niet op de lijst van 56 staan en niet live zijn: Breeze (4 regels), Boog (2), Agano vaas, waxinelichthouder, boekensteun, bank-londen (2), Panda fauteuil (3), Kathmandu (2), Mars (2), Panda stoel (3), Sycomore, de twee Japandi keukenbarkrukken, vier Tusk, Rainbow taupe, Storm bruin, Wing zwart en Krab messing (2). Een redirect naar een concept geeft een 404. Vooral Breeze (4 actieve producten zonder voorraad), Boog en Agano zijn relevant, want daar komt verkeer. Per geval de keuze: product live zetten, redirect naar de collectie (`/collections/stoelen`, `/collections/vazen`) of oude pagina laten vervallen. Dit is een besluit voor de eigenaar.
4. **Actieve producten waarvan het doel een ander product is dan hun eigen geplande handle** (14):
   - Eigen plan bestaat: `cloud-barstoel-creme` naar `barkruk-cloud` (eigen plan `barkruk-cloud-barkruk-creme`), `wolkenkeukenbar-stoel-karamel` naar `barkruk-cloud`, `wolkenbar-stoel-karamel` naar `barkruk-cloud-barkruk-creme`, `whale-stoel-beige-set-van-2` naar `eetkamerstoel-whale-set-van-2`, `luna-stoel-caramel-set-van-2` naar `eetkamerstoel-luna-creme-set-van-2` (eigen plan `eetkamerstoel-luna-set-van-2`), `boogstoel-karamel-set-van-2` en `boogstoelcreme-set-van-2` naar `eetkamerstoel-boog-set-van-2`.
   - Geen eigen plan (oude dubbelen): vier Breeze, twee Safiya, `luna-chair-mink-set-van-2`.
   De eerste groep zijn live producten met een eigen tekst onder `live_tekst`. Krijgen ze hun geplande handle, dan stuurt de oude URL naar een ander product in plaats van naar zichzelf op de nieuwe handle. Moeten ze blijven bestaan (live), dan moet het doel de eigen geplande handle zijn; gaan ze naar concept (de 6 dubbelen in `analyse/12-voorstel-live-zetten.md`), dan klopt het doel. De hoofdsessie en de eigenaar bepalen welke van de twee per product geldt; pas daarna de CSV aanpassen.
5. **Kan-weg-lijst**: 30 van de 36 handles in `data/orderchamp/verificatie/kan-weg-2026-11-19.json` zijn concept en hebben geen regel nodig (nooit publiek). De zes die actief zijn hebben wel een regel (Boogstoel karamel, Breeze pastel roze, Wolkenbar karamel, Wolkenkeukenbar karamel, Luna caramel, Whale beige).

## Opnieuw draaien

`python3 -I tools/redirects_check.py` toont de tellingen; met `--fix` worden ketens platgeslagen en exacte dubbelen verwijderd (de CSV wordt herschreven, controleer de diff). Draai het na elke aanvulling en vlak vóór de import.

## Aanpassing 23 november 2026 (punten 38, 39, 40)

Kopie van de oude stand: `data/tmp/redirects-voor-2026-11-23.csv`. Rekengrond: `data/ids.json` `live_actief` (77 gids) met de geplande handles uit `producten` en `live_tekst`. Volgorde van de keuze: live product van hetzelfde model, anders de categoriecollectie, anders `/collections/all` (niet nodig geweest). Collecties moeten in fase 4 stap 1 live zijn vóór stap 3.

Aantal gewijzigd: 34 van 141 regels. 10 naar een live product, 24 naar een collectie. Per punt: 38 = 1, 39 = 31, 40 = 2.

| Oude handle | Oud doel | Nieuw doel | Reden |
|---|---|---|---|
| `breeze-stoel-beige-set-van-2` | `eetkamerstoel-breeze-set-van-2` | `/collections/stoelen` | doel concept; collectie, geen live product van dit model |
| `breeze-stoel-latte-set-van-2` | `eetkamerstoel-breeze-set-van-2` | `/collections/stoelen` | doel blijft concept; collectie, geen live product van dit model |
| `breeze-stoel-pastel-roze-set-van-2` | `eetkamerstoel-breeze-set-van-2` | `/collections/stoelen` | doel blijft concept; collectie, geen live product van dit model |
| `breeze-stoel-pistache-set-van-2` | `eetkamerstoel-breeze-set-van-2` | `/collections/stoelen` | doel blijft concept; collectie, geen live product van dit model |
| `cloud-barstoel-creme` | `barkruk-cloud` | `barkruk-cloud-barkruk-creme` | doel was ander product dan eigen geplande handle; live product van hetzelfde model |
| `boogstoel-karamel-set-van-2` | `eetkamerstoel-boog-set-van-2` | `eetkamerstoel-boog-creme-set-van-2` | doel blijft concept; live product van hetzelfde model |
| `boogstoelcreme-set-van-2` | `eetkamerstoel-boog-set-van-2` | `eetkamerstoel-boog-creme-set-van-2` | doel concept en niet de eigen geplande handle; live product van hetzelfde model |
| `travertine-agano-vaas` | `vaas-agano-travertijn` | `/collections/vazen` | doel blijft concept; collectie, geen live product van dit model |
| `marmer-waxinelichthouder` | `waxinelichthouder-marmer` | `/collections/windlichten-en-kaarsenhouders` | doel blijft concept; collectie, geen live product van dit model |
| `boekhouder` | `boekensteun-mangohout` | `/collections/decoratie` | doel blijft concept; collectie, geen live product van dit model |
| `londen-3-zits-umber` | `bank-londen` | `bank-londen-3-zits-ottoman-umber` | doel blijft concept; live product van hetzelfde model |
| `londen-6-zitter-ottoman-umber` | `bank-londen` | `bank-londen-6-zits-ottoman` | doel blijft concept; live product van hetzelfde model |
| `panda-fauteuil-beige` | `fauteuil-panda` | `/collections/fauteuils` | doel blijft concept; collectie, geen live product van dit model |
| `panda-fauteuil-coco` | `fauteuil-panda` | `/collections/fauteuils` | doel blijft concept; collectie, geen live product van dit model |
| `panda-fauteuil-witte-parel` | `fauteuil-panda` | `/collections/fauteuils` | doel blijft concept; collectie, geen live product van dit model |
| `kathmandu-loungestoel-amon-naturel` | `fauteuil-kathmandu` | `/collections/fauteuils` | doel blijft concept; collectie, geen live product van dit model |
| `kathmandu-loungestoel-amon-terracotta` | `fauteuil-kathmandu` | `/collections/fauteuils` | doel blijft concept; collectie, geen live product van dit model |
| `mars-lounge-chair-beige` | `fauteuil-mars` | `/collections/fauteuils` | doel blijft concept; collectie, geen live product van dit model |
| `mars-loungestoel-coco` | `fauteuil-mars` | `/collections/fauteuils` | doel blijft concept; collectie, geen live product van dit model |
| `panda-stoel-beige-set-van-2` | `eetkamerstoel-panda-set-van-2` | `/collections/stoelen` | doel blijft concept; collectie, geen live product van dit model |
| `panda-stoel-coco-set-van-2` | `eetkamerstoel-panda-set-van-2` | `/collections/stoelen` | doel blijft concept; collectie, geen live product van dit model |
| `panda-stoel-witte-parel-set-van-2` | `eetkamerstoel-panda-set-van-2` | `/collections/stoelen` | doel blijft concept; collectie, geen live product van dit model |
| `eettafel-sycomore-l` | `eettafel-sycomore` | `/collections/tafels` | doel onbekend (Sycomore niet geïmporteerd); collectie, geen live product van dit model |
| `japandi-keukenbar-stoel-okura-set-van-2` | `keukenbarkruk-japandi-set-van-2` | `barkruk-japandi-tan-set-van-2` | doel blijft concept; live product van hetzelfde model |
| `japandi-keukenbar-stoel-umber-set-van-2` | `keukenbarkruk-japandi-umber-set-van-2` | `barkruk-japandi-tan-set-van-2` | doel blijft concept; live product van hetzelfde model |
| `tusk-stoel-beige-brandvertragend-set-van-2` | `eetkamerstoel-tusk-set-van-2` | `/collections/stoelen` | doel blijft concept; collectie, geen live product van dit model |
| `tusk-stoel-zandwit-brandvertragend-set-van-2` | `eetkamerstoel-tusk-zandwit-set-van-2` | `/collections/stoelen` | doel blijft concept; collectie, geen live product van dit model |
| `tusk-stoel-bruin-brandvertragend-set-van-2` | `eetkamerstoel-tusk-bruin-set-van-2` | `/collections/stoelen` | doel blijft concept; collectie, geen live product van dit model |
| `tusk-stoel-coco-brandvertragend-set-van-2` | `eetkamerstoel-tusk-coco-set-van-2` | `/collections/stoelen` | doel blijft concept; collectie, geen live product van dit model |
| `rainbow-stoel-taupe-set-van-2` | `eetkamerstoel-rainbow-taupe-set-van-2` | `eetkamerstoel-rainbow-coco-set-van-2` | doel blijft concept; live product van hetzelfde model |
| `storm-draaistoel-bruin` | `draaistoel-storm-bruin` | `draaistoel-storm` | doel blijft concept; live product van hetzelfde model |
| `vleugelstoel-zwart-set-van-2` | `eetkamerstoel-wing-zwart-set-van-2` | `eetkamerstoel-wing-set-van-2` | doel blijft concept; live product van hetzelfde model |
| `h20-krab-s` | `krab-messing` | `/collections/decoratie` | doel blijft concept; collectie, geen live product van dit model |
| `h19-krab-l` | `krab-messing` | `/collections/decoratie` | doel blijft concept; collectie, geen live product van dit model |

Niet gewijzigd (doel is wel live): Cloud (Safiya, wolkenbar, wolkenkeukenbar), Whale beige, Luna caramel en Luna mink wijzen naar een live product van hetzelfde model. Wolkenkeukenbar karamel, wolkenbar karamel, Whale beige, Luna caramel en Boogstoel karamel zijn volgens `live_actief` inmiddels geen actief product meer.

Let op:
- `redirects_check.py` kent alleen handles als doel en meldt de 24 collectiedoelen als `onbekend_doel`. Dat is verwacht; het script (buiten dit werk) hoort `/collections/<handle>` te herkennen vóór de import. Alle 24 collecties staan in `data/ids.json` `collecties`.
- Breeze beige, latte en pistache, de twee Safiya en Luna mink staan nu live zonder geplande handle. Hun redirect werkt pas als het product naar concept gaat (stap 0, besluit 6 in `fase-4.md`). Blijft zo'n product actief, schrap dan zijn regel.
- Krab messing en Krab L delen een SKU (besluit 3); de collectie is tijdelijk, tot de eigenaar de Krab-vraag beantwoordt.
- Geen ketens, geen zelfverwijzing; geen enkel doel is zelf een bron.
