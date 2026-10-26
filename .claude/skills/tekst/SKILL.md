---
name: tekst
description: Schrijft en plaatst als concept een pagina, collectietekst of inspiratie-artikel (onderzoeker waar nodig, schrijver, controleur, shopify-uitvoerder). Gebruik /tekst <pagina|collectie|artikel> <naam>.
argument-hint: <pagina|collectie|artikel> <naam of onderwerp>
---
Zelfde keten als `/product`, met deze verschillen:

- **Template**: pagina's volgen de opbouw van `content/paginas/werkwijze.md`; collecties die van `analyse/06-collectiestructuur.md` (inleiding 150 tot 300 woorden, meta-titel ≤ 60, meta-description ≤ 155); artikelen die van `content/inspiratie/boucle-onderhouden-zo-blijft-je-bank-mooi.md` (400 tot 600 woorden, koppen als vragen of beloftes, één collectie en één of twee producten als interne link, auteur "Sylvana, InHuys").
- **Onderzoek** alleen als het onderwerp feiten vraagt (materiaalkennis, maten); de onderzoeker legt ze vast in `data/feiten/<onderwerp>.md`.
- **Controle**: `check_tekst.py` op het md-bestand (meta-lengtes, u-vorm, overlap).
- **Shopify**: de schrijver levert de md; de hoofdsessie maakt de HTML (koppen `h2`, alinea's `p`, lijsten `ul`/`ol`) en zet de mutatievariabelen in `data/out/<soort>-<handle>.json`; de `shopify-uitvoerder` gebruikt `pageCreate`/`pageUpdate`, `collectionCreate`/`collectionUpdate` of `articleCreate`/`articleUpdate`, altijd ongepubliceerd (`isPublished: false`; collecties daarna `resourcePublicationsCount` 0).
- **Registratie**: nieuwe gids in `data/ids.json` onder `paginas`, `collecties` of `artikelen`.
Meld de eigenaar in één alinea wat er klaarstaat en wat goedkeuring vraagt.
