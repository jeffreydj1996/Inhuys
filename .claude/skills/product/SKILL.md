---
name: product
description: Maakt voor één of meer productmodellen de eigen productpagina als concept: feiten zoeken (onderzoeker), tekst schrijven (schrijver), controleren (controleur), omzetten en als DRAFT in Shopify zetten (shopify-uitvoerder). Gebruik /product <model of familie>.
argument-hint: <model of familie, bv. panda-fauteuil>
---
Werk de keten af voor de opgegeven modellen; batches van maximaal 5. Geef agents alleen paden en handles, nooit bestandsinhoud. Lees zelf alleen rapporten en de eindtekst.

1. Status: `python3 -I tools/status.py show` en `python3 -I tools/varianten.py <zoekwoord>`; sla modellen over die al `tekst=klaar` of `concept=DRAFT` hebben, tenzij de opdracht "opnieuw" zegt. Bepaal per model de bronhandles, het merk en de categoriecollectie (`data/ids.json`).
2. Onderzoek: agent `onderzoeker` per model (meerdere parallel). Opdracht: modelnaam, merk, bronhandles; uitvoer `data/feiten/<model>.md`. Daarna `python3 -I tools/status.py set <handle> feiten=klaar`.
3. Tekst: agent `schrijver`, per batch van maximaal 5 modellen. Opdracht: paden van feitenbestand, template, brand-guide, voorbeeld `content/producten/eetkamerstoel-luna-set-van-2.md`, zoekwoord, de doelhandle, taxonomie-gid en collectie-gid. Uitvoer `content/producten/<handle>.md`.
4. Controle: agent `controleur` met `check_tekst.py` en `md_naar_vars.py` op de nieuwe bestanden, plus de feitensteekproef. Bij AANPASSEN: één keer terug naar de schrijver met alleen de foutregels; daarna opnieuw controleren. Blijft het fout, stop en meld het aan de eigenaar.
5. Beoordeling: lees de md zelf (één keer, volledig). Past toon en inhoud bij CLAUDE.md en brand-guide, ga door; anders één gerichte aanwijzing aan de schrijver. Grote twijfel over feiten of positionering is een vraag aan de eigenaar.
6. Omzetten: `python3 -I tools/md_naar_vars.py content/producten/<handle>.md` → `data/out/productSet-<handle>.json`.
7. Shopify: agent `shopify-uitvoerder` met het pad van het variabelenbestand. Hij maakt het concept, verifieert en registreert gid en status.
8. Nacontrole: bij de eerste batch van een sessie de `lezer` een momentopname laten maken vóór stap 7 en erna, en de `controleur` ze laten vergelijken met `snapshot.py`. Bij een batch zonder incidenten volstaat de verificatiequery van de uitvoerder.
9. Afronden: `python3 -I tools/status.py set <handle> tekst=klaar controle=<GOED|...>`; redirectregels uit `data/out/redirects-<handle>.csv` toevoegen aan `analyse/redirects.csv` (niet aanmaken in Shopify); commit in het Nederlands. Meld de eigenaar in één alinea: modellen, gids, kosten uit `/cost`, afwijkingen, wat nog goedkeuring vraagt.
