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
