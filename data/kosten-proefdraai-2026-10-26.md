# Kosten proefdraai werkinrichting · Panda fauteuil · 26 oktober 2026

Tokens per agent (uit de agentrapportage van de sessie; invoer plus uitvoer, inclusief het lezen van CLAUDE.md en de agentdefinitie).

| Stap | Agent | Model | Tokens | Toolaanroepen | Duur |
|---|---|---|---|---|---|
| Feiten zoeken | onderzoeker | haiku | 102.475 | 26 | 3,2 min |
| Momentopname vóór | lezer | haiku | 80.078 | 8 | 6,8 min |
| Tekst schrijven | schrijver | opus | 121.098 | 18 | 5,6 min |
| Tekstcontrole en steekproef | controleur | haiku | 23.511 | 7 | 0,7 min |
| Concept aanmaken en verifiëren | shopify-uitvoerder | sonnet | 29.777 | 9 | 2,6 min |
| Search Console-meting | seo-meter | haiku | 11.264 | 3 | 0,2 min |
| Momentopname na (vergelijking door hoofdsessie met snapshot.py) | lezer | haiku | 45.002 | 7 | 2,1 min |
| **Totaal agents** | | | **413.205** | | |

Lessen uit de proefdraai:
- De onderzoeker vond online geen fabrikant- of dealerpagina voor Pole To Pole (negen zoekopdrachten); de feiten kwamen uit de eigen export. Voor Pole To Pole-modellen is de verwachting dus: maten alleen als ze in de oude producttekst staan. Volgende stap: de eigenaar vraagt de leverancier om de maatbladen, of de onderzoeker krijgt de officiële Pole To Pole-site als startpunt zodra die bekend is.
- De schrijver (Opus) levert in één keer een tekst die alle mechanische controles haalt; één redactionele ingreep van de hoofdsessie (kleurbeschrijving coco).
- De controleur meldde drie onterechte "feiten" (materialen van de ruimte, afgeleide oppervlakte); de steekproefregel is daarop aangescherpt.
- De lezer is traag en relatief duur voor een momentopname (80.000 tokens, 7 minuten) omdat hij het ruwe JSON in zijn context krijgt; verbetering: de query in één keer naar bestand laten schrijven via een script zodra de proxy of MCP dat toelaat, of de momentopname alleen bij de eerste batch van een sessie maken (zoals de skill al zegt).
- Opus zag circa 20.000 invoertokens aan bronmateriaal; de rest van zijn verbruik zit in het lezen van template, brand-guide en voorbeeld. Bij batches van 5 modellen wordt dat eenmaal gelezen.

Vergelijking momentopname vóór en na de proefdraai: drie regels gewijzigd, geen daarvan door de agents. "Jumpspot voor Binnen" wordt sinds vanmorgen elke paar uur bijgewerkt door een koppeling buiten deze sessie (11:09, 13:03, 15:27, 16:13 uur); de automatische collecties `panda` en `fauteuils` kregen een nieuwe bewerkdatum omdat hun regels het nieuwe conceptproduct matchen. Inhoud, prijzen en beelden van live producten zijn niet aangeraakt.
