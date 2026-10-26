# InHuys · werkafspraken

Shopify-winkel www.in-huys.nl van InHuys (handelsnaam van Kluster). Werktaal Nederlands. Branch `claude/happy-noether-f2jyyd`.
De hoofdsessie doet regie en beoordeling en delegeert via de skills in `.claude/skills/` aan de agents in `.claude/agents/`.

## Harde regels (gelden voor elke sessie en elke agent)
1. Niets gaat live. Alleen DRAFT-producten, ongepubliceerde pagina's, collecties en artikelen en de thema-kopie `gid://shopify/OnlineStoreTheme/210233098579` mogen wijzigen.
2. Verboden zonder `INHUYS_GOLIVE=1` van de eigenaar: themePublish, elke publish of unpublish, urlRedirect*, elke delete of archivering, `status: ACTIVE`, prijzen, voorraad, kortingen, het live thema, de live menu's. `tools/guard_shopify.py` blokkeert dit; omzeil de hook nooit.
3. Raad nooit een ID. Alle concept-ID's staan in `data/ids.json`; nieuwe ID's registreer je met `python3 -I tools/status.py set <handle> gid=<gid>`.
4. Alt-tekst van een bestaand beeldbestand nooit wijzigen of weglaten: Shopify deelt bestanden tussen producten. Geef de huidige alt ongewijzigd mee (`md_naar_vars.py` doet dat).
5. Redirects blijven in `analyse/redirects.csv` tot de eigenaar go-live geeft.
6. Alle informatie van fabrikanten is alleen een bron voor feiten. Nooit een zin overnemen; `check_tekst.py` controleert op 7-woord-overlap.

## Schrijfregels
- Je-vorm, nooit u. Merknaam altijd `InHuys`. Tagline: `InHuys · ontwerp, advies en inrichting`.
- Eén gedachte per zin; effect in de ruimte eerst, dan product, dan specificaties; materiaal en maten concreet; geen superlatieven zonder reden.
- Alleen feiten uit `data/feiten/<model>.md` (met bron). Onvindbaar blijft `[AANVULLEN]` in de specificatietabel en gaat niet naar Shopify.
- Productteksten volgen `templates/productpagina-template.md` in de md-opbouw van `content/producten/eetkamerstoel-luna-set-van-2.md` (koppen en tabellen exact, anders werkt `md_naar_vars.py` niet).
- Details in `brand-guide.md`; alleen openen als je schrijft.

## Wie keurt wat goed
- Hoofdagent zelf: teksten binnen template en brand-guide, onderzoek, concepten aanmaken of bijwerken, controles, metingen, documenten, commits op de werkbranch, herstel van eigen fouten in concepten.
- Eigenaar, vooraf: alles wat live gaat, prijzen, voorraad, kortingen, bedrijfs- of juridische gegevens, de merknaam, verwijderen of archiveren, nieuwe of verruimde agents, hooks of skills met schrijfrechten, het faseplan, batches groter dan het faseplan, uitgaven buiten de raming. Twijfel = één alinea met de keuze aan de eigenaar.
- Elke fase begint met een goedgekeurd `plannen/fase-<n>.md` (skill `/faseplan`), met een toets of de agents nog passen.

## Zuinig werken
1. Grote resultaten naar bestand; in de sessie nooit meer dan 50 regels (jq, head, grep).
2. Agents krijgen paden, geen bestandsinhoud; ze lezen zelf met Grep eerst en Read met offset/limit.
3. Agentrapporten 5 tot 15 regels; details in bestanden.
4. `data/raw/` is de bron; geen nieuwe exports zonder reden.
5. Mutaties met aliassen batchen (max 5); producten één per aanroep.
6. Scripts in `tools/` hergebruiken (zie `tools/README.md`); teksten nooit in Python.
7. Opus alleen voor de eindtekst, batches van max 5 modellen, max één revisieronde.
8. `/clear` tussen batches; de stand staat in `data/status.csv` en `data/ids.json`.
9. Na twee mislukte toolaanroepen stoppen en rapporteren.
10. `analyse/0x-*.md` alleen openen als de taak erom vraagt.

## Vaste plekken
`content/` teksten · `templates/` template · `data/` bron en status · `tools/` scripts · `analyse/` naslag en metingen · `plannen/` faseplannen · `analyse/loop/` analyse-loop.
Commit per batch, in het Nederlands; push alleen op verzoek van de eigenaar.
