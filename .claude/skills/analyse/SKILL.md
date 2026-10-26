---
name: analyse
description: De analyse-loop (elke 14 dagen na go-live): meten, analyseren, voorstellen omzetten in werk, logboek. Skelet in fase 2b; inschakelen met akkoord van de eigenaar zodra er minstens vier weken data na go-live is. Gebruik /analyse [datum].
argument-hint: "[JJJJ-MM-DD]"
---
1. **Meten**: agent `seo-meter` (`tools/gsc_meting.py`); kopieer de CSV's van die datum naar `analyse/loop/<datum>/data-gsc-*.csv`. Zodra producten live zijn: ook Shopify-cijfers via `mcp__Shopify__run-analytics-query` (bezoeken, conversie, omzet per product en collectie, 28 dagen) naar `data-shopify-*.csv`, en PageSpeed via de API naar `data-pagespeed.csv`.
2. **Analyseren**: agent `analist` met de map `analyse/loop/<datum>/`, het vorige `conclusies.md` en de doelen; uitvoer `analyse/loop/<datum>/conclusies.md` (≤ 60 regels) en een regel in `analyse/loop/logboek.md`.
3. **Voorstellen omzetten**: wat binnen "hoofdagent keurt zelf goed" valt, komt als regel in `data/status.csv` (kolom opmerking: "loop <datum>: ...") en gaat mee in de volgende `/product`- of `/tekst`-batch. Grote ingrepen gaan als voorstel naar de eigenaar, één alinea per punt met cijfers en verwachte impact.
4. **Melden**: één alinea aan de eigenaar met de drie belangrijkste conclusies, wat automatisch is ingepland en wat goedkeuring vraagt. Commit.

Inschakelen als geplande taak (elke 14 dagen, verse sessie, prompt `/analyse`) gebeurt pas na expliciet akkoord van de eigenaar; het is een terugkerende uitgave.
