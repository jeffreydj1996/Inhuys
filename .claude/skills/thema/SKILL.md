---
name: thema
description: Bouwt de thema-werkversie opnieuw uit tools/theme_build.py en laat de shopify-uitvoerder alleen de gewijzigde bestanden naar de kopie (210233098579) uploaden; publiceert nooit. Gebruik /thema [bestand ...].
argument-hint: "[bestandsnamen om te uploaden, standaard: alle gewijzigde]"
---
1. Wijzigingen aan het thema worden in `tools/theme_build.py` gemaakt (nooit rechtstreeks in Shopify), met een `log(...)`-regel per wijziging.
2. `python3 -I tools/theme_build.py data/theme-origineel data/out/theme-new`; vergelijk met de vorige uitvoer (`git stash`-vrije manier: bewaar de vorige map als `data/out/theme-vorig` en gebruik `diff -rq`) om te zien welke bestanden veranderd zijn.
3. Agent `shopify-uitvoerder`: `themeFilesUpsert` naar `gid://shopify/OnlineStoreTheme/210233098579` met alleen die bestanden (paden onder `data/out/theme-new/`), JSON vooraf gevalideerd, `userErrors` leeg.
4. Werk `analyse/07-thema-werkversie.md` bij (regel per bestand uit `data/out/theme-changelog.json`) en commit.
5. Meld de eigenaar de preview-link `https://www.in-huys.nl/?preview_theme_id=210233098579` en wat er veranderde. Publiceren is nooit onderdeel van deze skill.
