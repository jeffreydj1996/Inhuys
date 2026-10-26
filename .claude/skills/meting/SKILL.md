---
name: meting
description: Tweewekelijkse Search Console-meting via de API (seo-meter) met kort advies van de hoofdsessie. Gebruik /meting [datum].
argument-hint: "[JJJJ-MM-DD]"
---
1. Agent `seo-meter`: `python3 -I tools/gsc_meting.py` (met `--datum` als opgegeven). Hij meldt de kerncijfers en het rapportpad `analyse/gsc-rapport-<datum>.md`.
2. Lees het rapport (maximaal 40 regels) en schrijf aan de eigenaar in maximaal 10 regels: wat veranderde ten opzichte van de vorige meting, welke doelzoekwoorden bewegen, de sitemapstatus (ingediend/geïndexeerd), en hoogstens drie concrete acties met wie ze goedkeurt.
3. Commit de nieuwe CSV's en het rapport ("Search Console-meting <datum>").
Zodra de analyse-loop aanstaat (`/analyse`), vervangt die stap 2.
