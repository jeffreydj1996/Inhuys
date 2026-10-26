---
name: status
description: Toont de stand van het werk uit data/status.csv en data/ids.json zonder agents of API-aanroepen. Gebruik /status.
---
Voer `python3 -I tools/status.py show` uit en vat samen: aantal modellen per fase (feiten, tekst, controle, concept), modellen met controle C of een opmerking, en wat de eigenaar nog moet goedkeuren volgens het lopende faseplan in `plannen/`. Maximaal 15 regels. Geen Shopify-aanroepen.
