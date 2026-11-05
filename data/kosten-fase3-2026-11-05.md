# Kosten fase 3 tot en met 5 november 2026 · agents

Tokens van de agents (invoer plus uitvoer, uit de agentrapportage; de hoofdsessie niet meegeteld). Stand na batch 5 en 6; de regels voor batch 5 en 6 worden bijgewerkt zodra de laatste uitvoerders klaar zijn.

| Onderdeel | Agents | Tokens | Opmerking |
|---|---|---|---|
| Proefdraai en fase 2b (vóór fase 3) | 8 | 569.690 | Panda fauteuil, momentopnames, drie concepten bijwerken |
| Batch 1 fauteuils (Kathmandu, Cairo, Mars, Panda stoel) | 8 | 329.164 | zie data/kosten-batch1-2026-11-04.md |
| Bronnen per merk en herzoek van vijf modellen | 14 | 551.700 | zie data/kosten-herzoek-2026-11-04.md |
| Batch 2 tafels (feiten, teksten, controle) | 7 | 250.795 | Sycomore en Craft klein wachten op voorraad |
| Overzetting bestaande teksten op Orderchamp-concepten (stap 2 en 3) | 22 | 1.045.883 | uitlezing 91 producten, proef Cairo, Amsterdam, New York, Londen, Scandi, tafels, 10 korte varianten |
| Live hoofdteksten en korte varianten (stap 4) | 8 | 394.785 | teksten en controle klaar; overzetting wacht op INHUYS_LIVE_TEKST=1 |
| Batch 3 Japandi (12 producten) | 10 | 509.056 | inclusief herstelrun van twee producten |
| Batch 4 Avena, Mera, Nox, High Five, Wave (11 producten) | 9 | 386.449 | |
| Batch 5 Tusk, Rainbow, Rock, Storm, Pebble (16 producten) | 12 | 618.807 | voorlopig: twee uitvoerders lopen nog |
| Batch 6 EDO, Wing, Egg, Whale Retro, Fjord (7 producten) | 7 | 299.790 | voorlopig: controle en overzetting volgen |
| Batch 7 decoratie (alleen feiten en uitlezing) | 6 | 247.319 | teksten nog niet gestart |
| **Totaal** | **111** | **5.203.438** | |

## IJking tegen de raming in plannen/fase-3.md

- Raming overzetting bestaande teksten: 350.000. Werkelijk 1.045.883. Oorzaak: de uitlezing van alle 91 Orderchamp-producten, twee banken met samen negen korte varianten in plaats van de geraamde tien korte teksten voor alles, en vier uitvoerder-runs in plaats van dertien losse.
- Raming live producten: 150.000. Werkelijk 394.785, omdat de vijf live hoofdteksten na het herzoek opnieuw geschreven en gecontroleerd zijn (fabrikantfeiten in plaats van de fase-2-aannames).
- Raming nieuwe teksten: 95.000 per model. Werkelijk per batch van vijf modellen 390.000 tot 620.000, dus 78.000 tot 124.000 per model, inclusief de korte varianten per kleur (batch 5: 16 producten voor 5 modellen) en de uitlezing van de Orderchamp-concepten.
- Per product (hoofd of kort) kost een batch nu 36.000 tot 42.000 tokens, alles inbegrepen.

## Nog te verwachten

- Batch 7 decoratie: 5 families, naar verwachting 400.000 tot 500.000 tokens (teksten, controle, overzetting).
- Batch 8 Jupiduu: feiten moeten nog gezocht worden (jupiduu.com); schatting 500.000 tot 700.000.
- Stap 4 live producten: alleen nog uitvoerder en momentopnames, 150.000.
- Modellen zonder voorraad (Breeze, Boog, Panda, Mars, Kathmandu, Sycomore, Craft klein): pas bij voorraad, teksten liggen klaar.
