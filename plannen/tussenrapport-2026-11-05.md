# Tussenrapport fase 3 · 5 november 2026

## Gedaan

- 66 Orderchamp-concepten dragen nu onze inhoud: titel, handle, tekst, SEO, metavelden (batch 2b 20, batch 3 12, batch 4 11, batch 5 16, batch 6 7). Status DRAFT, publicaties 0; varianten, prijzen, voorraad en beelden onveranderd van Orderchamp. Batch 5 en 6 zijn byte-voor-byte vergeleken met de bestanden (0 afwijkingen).
- Per model één hoofdproduct met volledige tekst en korte varianten per kleur of opstelling, gekoppeld via het metaveld `inhuys.hoofdproduct`.
- Teksten voor de tien live producten (Luna, Cloud, Whale, barkrukken Cloud, Scandi tan) zijn klaar en gecontroleerd; feiten en uitlezing voor de decoratie (batch 7) ook.
- Kosten agents fase 3 tot nu toe: 5,6 miljoen tokens, zie `data/kosten-fase3-2026-11-05.md`. Nog te verwachten: batch 7 400.000 tot 500.000, batch 8 Jupiduu 500.000 tot 700.000, live producten 150.000.

## Beslissingen voor de eigenaar

1. Live producten: `INHUYS_LIVE_TEKST=1` in de omgeving zetten; daarna krijg je de lijst van tien gids vooraf en gaat alleen titel, tekst, SEO en metavelden mee (handles blijven tot go-live).
2. Levertijd en garantie: de fabrikant noemt ze nergens. Eén vaste regel voor alle Pole To Pole-producten, of leeg laten? Nu staat overal [AANVULLEN] en gaat het veld niet mee.
3. Prijsverschillen binnen één Orderchamp-product: Egg goud € 319,80 tegen mink € 179,95; Pebble latte € 359,90 tegen pistache € 429,95; Luna mink en goud. Kloppen die in Orderchamp?
4. Naam "draaistoel" voor Storm en Pebble: de fabrikant zegt "rotating chair", maar beschrijft geen draaimechaniek voor Storm. Pebble wel (360 graden met terugkeer). Storm "draaistoel" houden?
5. "Discontinued" bij Pole To Pole: Wing parelwit, Egg goud en mink, Fjord taupe, Mera, Nox en meer. Ze hebben voorraad bij Orderchamp, dus de teksten staan erop; houd er rekening mee dat ze niet nabesteld worden.
6. Oude eigen concepten (`-eigen` in `data/ids.json`) kunnen weg; verwijderen doe jij.

## Volgende stap

Batch 7 decoratie (vazen aluminium bronze, lantaarns, schelpdecoratie, kettingen, octo): teksten, controle, overzetting. Daarna batch 8 Jupiduu (feiten via jupiduu.com) en de live producten zodra de omgevingsvariabele staat.
