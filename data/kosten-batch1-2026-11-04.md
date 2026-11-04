# Kosten fase 3, batch 1 · fauteuils · 4 november 2026

Vier modellen in één batch: Kathmandu loungestoel, Cairo loungestoel, Mars loungestoel, Panda eetkamerstoel (set van 2). Tokens uit de agentrapportage (invoer plus uitvoer).

| Stap | Agent | Model | Tokens | Toolaanroepen | Duur |
|---|---|---|---|---|---|
| Feiten zoeken (4 parallel) | onderzoeker ×4 | haiku | 141.942 (37.480 · 30.427 · 35.492 · 38.543) | 66 | 1 tot 1,5 min per model |
| Momentopname vóór | lezer | haiku | 30.595 | 8 | 1,3 min |
| Tekst schrijven (4 in één batch) | schrijver | opus | 65.293 | 16 | 4,4 min |
| Tekstcontrole en steekproef (4) | controleur | haiku | 39.828 | 15 | 0,5 min |
| Concepten aanmaken en verifiëren (4) | shopify-uitvoerder | sonnet | 61.863 | 17 | 17 min (wachttijd op "Allow once" van de eigenaar) |
| Momentopname na | lezer | haiku | 29.471 | 8 | 3,5 min |
| **Totaal agents, 4 modellen** | | | **368.992** | | |

Per model dus circa 92.000 tokens, tegen 413.000 voor het ene model van de proefdraai. De winst zit in het batchen van de schrijver (Opus las template, brand-guide en voorbeelden één keer: 65.000 tokens voor vier teksten tegen 121.000 voor één) en in kortere onderzoekers (maximaal zes zoekopdrachten).

Kwaliteit: controleur GOED op alle vier; de hoofdsessie deed één ingreep (een maat minder in de Kathmandu-tekst). Geen hedge-woorden, geen maten als losse mededeling.

Beperking: de netwerkpolicy van de omgeving blokkeert dealerpagina's (gigameubel.nl, homka-living.de, stil-ambiente.de, poletopole.nl). Maten komen daardoor uit zoekresultaat-samenvattingen en staan in de feitenbestanden als "te verifiëren"; de Panda-eetkamerstoel heeft helemaal geen maten. Zodra de eigenaar de domeinen toestaat, draait de onderzoeker de vijf modellen opnieuw en worden de specificatietabellen en metavelden bijgewerkt zonder de teksten te herschrijven.

Vergelijking momentopname vóór en na: acht regels gewijzigd, geen daarvan door de agents. Vijf automatische collecties (bestsellers, kathmandu, panda, stoelen, fauteuils) kregen een nieuwe bewerkdatum omdat hun regels de nieuwe concepten matchen. Drie live producten (Ballenbak, Jumpspot voor Binnen, Luna stoel crème) zijn tussen 15:29 en 15:30 uur bijgewerkt door een koppeling buiten deze sessie; dezelfde producten veranderden eerder op de dag ook al zonder dat iemand hier iets deed. Inhoud, prijzen en beelden van live producten zijn niet aangeraakt.
