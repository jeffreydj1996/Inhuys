# Faseplan 3 · alle productgroepen als concept, klaar voor go-live

Status: **voorstel, wacht op akkoord van de eigenaar**. Opgesteld 26 oktober 2026 door de hoofdsessie na afronding van fase 2 en de werkinrichting (fase 2b). Fase 3 start pas na akkoord.

## 1. Afsluiting fase 2 en 2b

Opgeleverd (alles als concept, niets live):
- SEO-strategie, zoekwoorden, Search Console via de API (`analyse/05`, `analyse/08`, `analyse/gsc/`), sitemap aangemeld door de eigenaar op 26 oktober.
- Tien categoriecollecties, vijf conceptpagina's, drie menu's, thema-kopie met de goedgekeurde huisstijl (`210233098579`, preview `https://www.in-huys.nl/?preview_theme_id=210233098579`).
- Veertien conceptproducten met eigen tekst: Breeze, Cloud, Cloud barkruk, Whale, Luna, Boog, Scandi, Agano vaas, waxinelichthouder, boekensteun, Bank Amsterdam, New York, Londen en (proefdraai) Panda fauteuil (`gid://shopify/Product/11028600258899`). ID's in `data/ids.json`, stand in `data/status.csv`.
- Vier inspiratie-artikelen als concept; besluiten van de eigenaar verwerkt (prijs op aanvraag, op afspraak, InHuys als handelsnaam van Kluster).
- Werkinrichting: `CLAUDE.md`, zeven agents, acht skills, `tools/` met converter, tekstcontrole, hook, momentopname, status en meting; proefdraai geslaagd (`data/kosten-proefdraai-2026-10-26.md`).

Open gebleven: `.claude/settings.json` moet de eigenaar zelf plaatsen (kopie van `tools/claude-settings.voorbeeld.json`), anders draait de beveiligingshook niet; vanaf-prijs 3D-ontwerp; foto's; specificaties van Pole To Pole zijn online niet te vinden (zie 5).

Meting (26 oktober): 1 klik en 60 vertoningen in 28 dagen; 57 URL's ingediend via de sitemap, 0 geïndexeerd op de dag van aanmelding; 24 van de 30 live productpagina's waren tot vandaag onbekend bij Google.

## 2. Doel van fase 3

Elke productgroep krijgt één conceptproduct per model met eigen tekst, specificaties en meta's, zodat de hele winkel in één go-live kan omschakelen. De collectie- en dienstteksten staan al klaar. Aan het eind van fase 3 ligt er een complete go-live-checklist voor fase 4: thema-kopie publiceren, oude producten op concept, redirects, publicatie van collecties, pagina's en artikelen.

## 3. Stappen

Elke batch loopt via `/product` (onderzoeker → schrijver → controleur → beoordeling → shopify-uitvoerder), maximaal 5 modellen per schrijfbatch, momentopname vóór en na per sessie. Commit per batch; `/clear` tussen batches.

| Batch | Inhoud | Modellen (te bevestigen met `tools/varianten.py`) | Agents |
|---|---|---|---|
| 1 | Fauteuils en loungestoelen | Kathmandu loungestoel, Mars, Cairo, Panda stoel (eetkamer, set van 2) | onderzoeker, schrijver, controleur, uitvoerder |
| 2 | Tafels | De modellen in collectie Tafels (eettafels, salontafel Craft met travertijn) | idem |
| 3 | Resterende stoelen | Scandi (okura, umber) als varianten bij het bestaande concept; Rainbow/Regenboog samenvoegen met Boog na bevestiging; Edo, Eier, Rocking | idem; bij samenvoegen `productUpdate` op het bestaande concept |
| 4 | Resterende banken | Bank Kathmandu en overige bankseries in concept | idem |
| 5 | Kinderkamer (Jupiduu) en accessoires | Glijbaan, Jumpspot, Ballenbak, zwembad; vazen en windlichten van MOOISA en Jesper Home | idem; Jupiduu-producten zijn live: nieuwe concepten naast de bestaande, zoals bij de stoelen |
| 6 | Collecties en thema | Collectie-inleidingen controleren tegen de definitieve modellen; projectenblok en beelden in de thema-kopie zodra foto's er zijn (`/thema`) | controleur, uitvoerder |
| 7 | Metingen | `/meting` elke 14 dagen; eerste op 9 november 2026 | seo-meter |
| 8 | Afronding | Go-live-checklist voor fase 4, `analyse/redirects.csv` compleet, `/faseplan 4` | hoofdsessie |

Orde van grootte: 147 conceptproducten en 30 live producten vallen in 92 naamgroepen (eerste woord van de titel) en worden naar verwachting 50 tot 60 modellen; de precieze lijst per batch stelt de hoofdsessie op met `tools/varianten.py` en legt hij vast in `data/status.csv` vóór de batch start.

## 4. Kostenraming

Uit de proefdraai (één model, drie kleuren):

| Stap | Model | Tokens |
|---|---|---|
| Feiten zoeken | haiku | ~100.000 |
| Tekst schrijven | opus | ~120.000 (in een batch van 5 daalt dit per model, omdat template en brand-guide eenmaal worden gelezen) |
| Controle | haiku | ~25.000 |
| Concept aanmaken en verifiëren | sonnet | ~30.000 |
| Momentopname vóór en na, per sessie | haiku | ~160.000 |

Per model dus ruwweg 300.000 tokens, waarvan circa een derde op Opus; per batch van 5 komt daar eenmaal de momentopname bij. Voor 55 modellen: in de orde van 17 miljoen tokens over de agents, plus de regie van de hoofdsessie. De hoofdsessie leest per model één keer de eindtekst (circa 2.000 tokens) en de rapporten. Raming in geld volgt uit `/cost` na batch 1; batch 1 is daarmee ook de ijking voor de rest van de fase.

## 5. Grote ingrepen die de eigenaar vooraf goedkeurt

1. Dit faseplan en de batchvolgorde.
2. Samenvoegen van modellen waarvan de identiteit onzeker is (Rainbow/Regenboog met Boog; Scandi-kleuren): per geval één alinea met voorstel.
3. Elke prijs- of assortimentswijziging die uit het onderzoek naar voren komt (bijvoorbeeld een variant die niet meer bestaat): de hoofdsessie meldt, de eigenaar beslist; concepten houden de huidige prijzen.
4. Specificaties van Pole To Pole: online niet vindbaar. Voorstel: de eigenaar vraagt de leverancier om de maatbladen of de link naar de dealerportal; tot die tijd blijven maten die niet in de oude teksten staan op `[AANVULLEN]`.
5. Nieuwe agents of rechten: in fase 3 niet nodig. Voor fase 4 worden voorgesteld: `redirect-uitvoerder` (alleen met `INHUYS_GOLIVE=1`) en `beeld-agent` (zodra er foto's zijn).
6. Inschakelen van de analyse-loop als geplande taak: pas na go-live, aparte vraag.
7. Alles wat live gaat blijft fase 4: themePublish, oude producten op concept, redirects, publiceren van collecties, pagina's en artikelen, samenvoegen van de blogs.

## 6. Agents

| Agent | Taak in fase 3 | Past nog | Wijziging |
|---|---|---|---|
| onderzoeker (haiku) | Feiten per model | Ja, met kanttekening | Krijgt als startpunt de bronteksten uit de export en, zodra bekend, de officiële Pole To Pole-site of maatbladen van de eigenaar; bij nul resultaten na zes zoekopdrachten stoppen (nu negen) |
| schrijver (opus) | Productteksten, later collectiecorrecties | Ja | Batches van 5; voorbeeldbestand blijft Luna; voor fauteuils en banken het Panda- en Amsterdam-bestand als tweede voorbeeld |
| controleur (haiku) | Tekst- en feitencontrole, momentopname-vergelijking | Ja | Steekproefregel is na de proefdraai aangescherpt (alleen productfeiten) |
| shopify-uitvoerder (sonnet) | Concepten aanmaken en bijwerken, thema-upserts | Ja | Gebruikt `productByIdentifier` (productByHandle is verouderd); bij samenvoegen `productUpdate` op bestaand concept-id uit `data/ids.json` |
| seo-meter (haiku) | Tweewekelijkse meting | Ja | – |
| lezer (haiku) | Momentopnames, lookups | Ja, duur | Momentopname alleen vóór en na een sessie, niet per batch; onderzoeken of de query via een script naar bestand kan zonder agentcontext |
| analist (sonnet) | – | Uit | Pas in fase 4 na go-live |

## 7. Verificatie van fase 3

- `python3 -I tools/status.py show`: elk model van de batchlijst heeft `tekst=klaar`, `controle=GOED` (of B met reden) en `concept=DRAFT` met gid.
- `python3 -I tools/check_tekst.py content/producten/*.md` zonder FOUT.
- Momentopname vóór en na elke sessie identiek voor live objecten (`tools/snapshot.py`).
- Alle concepten `resourcePublicationsCount` 0; geen redirect, geen publicatie, geen prijswijziging op live producten.
- `analyse/redirects.csv` dekt elk oud product dat in een model is opgegaan.
- Twee metingen (9 en 23 november) vastgelegd in `analyse/gsc/`.
