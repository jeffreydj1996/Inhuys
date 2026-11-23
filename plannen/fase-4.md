# Faseplan 4 · go-live en nazorg

Status: **concept, wacht op akkoord van de eigenaar**. Opgesteld 19 november 2026 door de hoofdsessie na afronding van fase 3. Niets uit dit plan is uitgevoerd; elke stap hieronder vraagt zijn expliciete akkoord en `INHUYS_GOLIVE=1` of een nieuwe opening in `tools/guard_shopify.py`.

## 1. Doel

Alle voorbereide inhoud gaat in één gecontroleerde omschakeling naar de bezoeker: producten, collecties, pagina's, artikelen, nieuwe URL's met redirects, menu's en de thema-kopie `gid://shopify/OnlineStoreTheme/210233098579`. Elke stap staat los, heeft een momentopname vóór en na, en is terug te draaien. Daarna loopt de meting en de analyse-loop.

## 2. Wat al live staat of live mag

- 26 Orderchamp-producten zijn actief (21 Pole To Pole, 5 Jupiduu); 19 daarvan dragen onze tekst (`live_tekst`). Flitsadvies (dienst) is het zevenentwintigste actieve product.
- 56 concepten met onze tekst, voorraad en zonder dubbel mogen volgens `analyse/12-voorstel-live-zetten.md` actief (lijst `naar_live` in `data/ids.json`; de guard staat `productUpdate` met id en `status: ACTIVE` plus `publishablePublish` voor deze gids al toe).
- 6 actieve dubbelen gaan naar concept (`live_naar_concept` is leeg en wordt voor deze zes gevuld).
- Na deze stap: 76 actieve Orderchamp-producten plus Flitsadvies.
- Controles vooraf: `analyse/13-redirects-controle.md` (redirects), `analyse/14-collecties-controle.md` (collecties), `analyse/11-dubbele-producten.md` (dubbelen).

## 3. De omschakeling in volgorde

Volgorde met reden: eerst de inhoud die niemand tot nu toe ziet, dan de URL-wijziging, als laatste het thema. Een stap is pas klaar als de momentopname na gelijk is aan de verwachting en de volgende stap is goedgekeurd.

### Stap 0 · producten actief en dubbelen naar concept
- Bezoeker: 56 nieuwe productpagina's in zoekresultaten en collecties; 6 dubbele pagina's verdwijnen.
- Mutatie: `productUpdate {id, status}` per gid en `publishablePublish` naar de vijf kanalen van de bestaande producten; voor de dubbelen `productUpdate {id, status: DRAFT}`.
- Terug: `productUpdate {id, status: DRAFT}` (de guard staat dat alleen toe voor gids in `live_naar_concept`; daarom die lijst vullen).
- Guard: opening voor `naar_live` bestaat; voor `live_naar_concept` bestaat de opening. Geen wijziging.

### Stap 1 · collecties publiceren
- Bezoeker: tien categoriepagina's met inleiding en productraster op `/collections/<handle>`.
- Mutatie: eerst de wijzigingen uit `analyse/14` (`collectionUpdate`, mag nu), daarna `publishablePublish` per collectie op Online Store.
- Terug: `publishableUnpublish` per collectie.
- Guard: nieuwe opening `publishablePublish` en `publishableUnpublish` alleen voor gids onder `collecties` in `data/ids.json`, zonder andere velden. Nu geldt de opening alleen voor producten. Alternatief: `INHUYS_GOLIVE=1` per stap.
- Aanname: Maatwerk blijft ongepubliceerd tot er inhoud is.

### Stap 2 · dienstpagina's en artikelen
- Bezoeker: Werkwijze, Showroom, Over InHuys, Projecten, Veelgestelde vragen en vier inspiratie-artikelen in de blog.
- Mutatie: `pageUpdate` en `articleUpdate` met `isPublished: true` (5 pagina's, 4 artikelen); de guard blokkeert `isPublished: true` nu in elk object.
- Terug: dezelfde mutatie met `isPublished: false`.
- Guard: opening voor `isPublished` alleen op gids onder `paginas` en `artikelen`, anders `INHUYS_GOLIVE=1`.

### Stap 3 · nieuwe handles voor de live producten, met redirects
- Bezoeker: de 19 live producten met tekst krijgen de nieuwe URL (`eetkamerstoel-...`); oude URL's sturen door met 301. Dit is de gevoeligste stap: Google heeft de oude URL's geïndexeerd (zie meting 26 oktober).
- Mutatie: per product `productUpdate {id, handle, redirectNewHandle: true}`; voor oude handles van producten die zelf blijven bestaan en voor alle samengevoegde dubbelen `urlRedirectCreate {path, target}` volgens `analyse/redirects.csv` (141 regels; vooraf `python3 -I tools/redirects_check.py` zonder fouten).
- Terug: `urlRedirectDelete` en handle terugzetten (`productUpdate` met de oude handle); de oude handles staan in `data/orderchamp/varianten-2026-11-19.json`.
- Guard: nu verboden (regel 2a sluit handle uit; `urlredirect` staat in `VERBODEN_RE`). Voorstel: opening `live_handle` in `data/ids.json` voor `productUpdate {id, handle, redirectNewHandle}` en opening voor `urlRedirectCreate` waarvan het paar in `analyse/redirects.csv` staat. Zonder deze opening: `INHUYS_GOLIVE=1`.
- Open: 21 doelhandles horen bij producten die niet live gaan (zie `analyse/13`); die regels pas activeren als het doel bestaat of omleiden naar de collectie.
- Aanname: `redirectNewHandle` volstaat voor de hernoemde producten; de CSV dekt de overige regels.

### Stap 4 · menu's
- Bezoeker: nieuw hoofdmenu (Interieuradvies, Projecten, Collectie met negen collecties, Inspiratie, Over InHuys) en twee footermenu's.
- Mutatie: geen. De thema-kopie verwijst naar `hoofdmenu-fase-2`, `footer-inhuys` en `footer-service`; de live menu's (`menu_hoofd`, `menu_footer`) blijven ongewijzigd en vallen weg zodra het thema live is.
- Terug: oud thema opnieuw publiceren (stap 5).
- Guard: geen opening nodig. Controle vooraf: elk menulink-doel bestaat (collecties en pagina's gepubliceerd in stap 1 en 2).
- Aanname: de live menu's blijven bestaan zonder gebruik.

### Stap 5 · thema-kopie publiceren
- Bezoeker: nieuwe huisstijl, homepage, header en footer, blok "Andere uitvoeringen" op productpagina's.
- Mutatie: `themePublish(id: 210233098579)` (of via de Shopify-app: Online winkel, Thema's, Publiceren).
- Terug: het huidige thema `200751743315` opnieuw publiceren (blijft staan, nooit verwijderen).
- Guard: nu verboden (`themepublish`); opening alleen voor de gid in `thema_kopie`, anders `INHUYS_GOLIVE=1`.
- Controle vooraf: preview `https://www.in-huys.nl/?preview_theme_id=210233098579` op telefoon en desktop, `/controle thema`, pagespeed-meting tegen `analyse/pagespeed-2026-10-26.md`.

### Na elke stap
`tools/snapshot.py` vóór en na, byte-vergelijking van de objecten die niet mochten veranderen, `python3 -I tools/status.py` bijwerken, commit in het Nederlands.

## 4. Open beslissingen voor de eigenaar

1. **Levertijd en garantie**: vaste regel in elke productpagina, of leeg laten tot Orderchamp en de merken dit bevestigen. Voorstel: leeg laten en per merk toevoegen zodra de leverancier het schriftelijk bevestigt.
2. **Dubbelen verwijderen** (36, zie `analyse/11-dubbele-producten.md`): in de Orderchamp-app, zodat de koppeling niet opnieuw importeert. Daarna draait de controle opnieuw; tot die tijd gaan alleen de 6 actieve dubbelen naar concept.
3. **Krab met gedeelde SKU** (`krab-messing` en `krab-l`): eerst in Orderchamp nakijken; het product blijft tot die tijd concept en de twee regels in `redirects.csv` wijzen naar een concept.
4. **Prijsverschillen per variant** tussen Orderchamp en de oude winkelprijzen: de concepten houden de Orderchamp-prijs (regel 2); bevestig dat die prijzen bij go-live gelden.
5. **Tien concepten met tekst zonder voorraad** (bank-londen, beide Japandi keukenbarkrukken, vier Tusk, Rainbow taupe, Storm bruin, Wing zwart): blijven concept; de redirects ernaartoe wachten of wijzen naar de collectie.
6. **13 live producten zonder voorraad** (Cloud crème, karamel en beide Safiya, vier Breeze, Cloud barkruk karamel twee keer, Luna karamel en mink): actief laten (zichtbaar met de status uitverkocht) of naar concept. Breeze heeft de meeste vertoningen.
7. **Oude eigen concepten** uit fase 2 (18, zie `analyse/11`): blijven concept of worden verwijderd; verwijderen vraagt zijn akkoord per product.
8. **Dunne collecties**: Fauteuils (1), Windlichten (2), Decoratie (2, of 11 met de kettingen) en Maatwerk (0), zie `analyse/14`. Publiceren of wachten.
9. **Flitsadvies** blijft actief; **marmer waxinelichthouder, Agano vaas en boekhouder** staan op concept; hun redirects wijzen naar concepten.
10. De guard-openingen uit sectie 3, of `INHUYS_GOLIVE=1` per stap.

## 5. Nazorg

- Dag 0 tot 7: dagelijks in Search Console de dekking en 404's lezen (`/meting`), de sitemap opnieuw aanmelden na stap 5, elke 404 op een oude URL als nieuwe regel in `urlRedirectCreate`.
- Week 2 en 4: `/meting` (elke 14 dagen, eerste meting op 7 dagen na go-live), vergelijking met de nulmeting van 26 oktober (1 klik, 60 vertoningen).
- Vanaf vier weken data: analyse-loop inschakelen met `/analyse`; de eigenaar geeft apart akkoord.
- Voorraadlocatie en Orderchamp-koppeling controleren op de nieuwe producten (voorraad uit Orderchamp, geen eigen voorraadmutaties).
- Opruimen na twee weken stabiel: modelcollecties verwijderen uit menu's, `Bestsellers` depubliceren, live menu's en oud thema laten staan tot de eigenaar anders beslist.

## 6. Agents en kosten

De bestaande zeven agents volstaan. Nieuw voorgesteld: `redirect-uitvoerder` (alleen schrijfrechten voor de stappen 2 en 3, alleen met `INHUYS_GOLIVE=1` of de guard-opening); akkoord van de eigenaar vooraf. Raming: momentopnames per stap 160.000 tokens (haiku), uitvoering per stap 30.000 tokens (sonnet), meting per twee weken 25.000 tokens.

## 7. Runbook (toegevoegd 23 november 2026)

Geldt per stap uit sectie 3; de besluiten daar blijven staan. Uitvoering door de shopify-uitvoerder; de eigenaar geeft per stap het akkoord en zet `INHUYS_GOLIVE=1` in de omgeving van die ene aanroep (de guard kent geen openingen voor deze stappen; een opening vraagt apart akkoord). Na de stap zet de eigenaar de variabele weer uit.

**Vooraf, elke stap**
1. `git status` schoon; `python3 -I tools/redirects_check.py` (24 regels met `/collections/...` als `onbekend_doel` zijn verwacht, zie `analyse/13`) en `/controle alles` zonder fouten.
2. Momentopname vóór: lezer-agent draait `tools/gql/snapshot.graphql` en schrijft `data/snapshots/snapshot-<datum>-voor-stap<n>.txt`.
3. Stop bij elke afwijking; na twee mislukte aanroepen rapporteren, niet doorgaan.

**Na elke stap**
1. Momentopname na naar `data/snapshots/snapshot-<datum>-na-stap<n>.txt`; `python3 tools/snapshot.py voor na` (exit 1 = live object dat niet in de stap hoort is gewijzigd of verdwenen: terugdraaien).
2. Controle van de stap (hieronder), `python3 -I tools/status.py` bijwerken, commit in het Nederlands. Daarna pas de volgende stap.

### Stap 0 · producten actief, dubbelen naar concept
- Volgorde: eerst de 6 dubbelen (`live_naar_concept` vullen met hun gids uit `analyse/11-dubbele-producten.md`, `productUpdate {id, status: DRAFT}` één per aanroep), dan de 56 gids uit `naar_live`: `productUpdate {id, status: ACTIVE}` één per aanroep, daarna `publishablePublish` naar de vijf kanalen, aliassen max 5.
- Guard: bestaande openingen (regel 2b en 2c); geen `INHUYS_GOLIVE`. Lijsten leeg zetten na afloop.
- Controle: `status` en `publishedOnCurrentPublication` per gid via `verifieer-product.graphql`; telling actief = 76 plus Flitsadvies; `live_actief` in `data/ids.json` bijwerken.
- Terug: `productUpdate {id, status: DRAFT}` voor de gids onder `live_naar_concept`; de dubbelen weer ACTIVE vraagt `INHUYS_GOLIVE=1`.

### Stap 1 · collecties
- Ids: tien gids onder `collecties` in `data/ids.json`; Maatwerk blijft ongepubliceerd.
- Volgorde: `collectionUpdate` voor de wijzigingen uit `analyse/14-collecties-controle.md` (mag nu), dan `publishablePublish` op Online Store, één collectie per aanroep, eerst de collecties die redirect-doel zijn (stoelen, fauteuils, tafels, vazen, windlichten-en-kaarsenhouders, decoratie).
- Guard: `INHUYS_GOLIVE=1`.
- Controle: `https://www.in-huys.nl/collections/<handle>` geeft 200 voor negen collecties, `/collections/maatwerk` 404; productaantallen gelijk aan `analyse/14`.
- Terug: `publishableUnpublish` per collectie (`INHUYS_GOLIVE=1`).

### Stap 2 · pagina's en artikelen
- Ids: vijf gids onder `paginas`, vier onder `artikelen` in `data/ids.json`.
- Volgorde: pagina's (werkwijze, showroom, over-inhuys, projecten, veelgestelde-vragen), dan de artikelen; `pageUpdate` en `articleUpdate {isPublished: true}`, één per aanroep.
- Guard: `INHUYS_GOLIVE=1`.
- Controle: URL's `/pages/<handle>` en `/blogs/.../<handle>` geven 200; geen `[AANVULLEN]` in de HTML; interne links werken (`tools/links_live.py`).
- Terug: zelfde mutatie met `isPublished: false`.

### Stap 3 · handles en redirects
- Vooraf: `python3 -I tools/redirects_check.py` zonder andere melding dan de verwachte collectiedoelen; besluit 6 en 3 uit sectie 4 genomen (Breeze, Safiya, Luna mink eerst naar concept, anders hun regel schrappen); `data/tmp/redirects-voor-2026-11-23.csv` is de oude stand.
- Bestanden en ids: `analyse/redirects.csv` (141 regels, doel `/collections/<handle>` of een handle), geplande handles uit `producten` en `live_tekst`, oude handles uit `data/orderchamp/varianten-2026-11-19.json`.
- Volgorde: (a) per live product met plan `productUpdate {id, handle, redirectNewHandle: true}`, één per aanroep; (b) per CSV-regel waarvan de oude handle niet bij (a) is aangemaakt `urlRedirectCreate {path: /products/<oud>, target: /products/<nieuw>}` (collectiedoel: `/collections/<handle>`), aliassen max 5; (c) niet zichtbaar uitvoeren zolang een doel nog concept is.
- Guard: `INHUYS_GOLIVE=1`.
- Controle: `curl -sI` op alle oude URL's: 301 naar het doel, doel 200, geen keten; `urlRedirects`-lijst heeft evenveel regels als de CSV plus de door `redirectNewHandle` gemaakte; Search Console 404's de eerste week.
- Terug: `urlRedirectDelete` per aangemaakte id; `productUpdate {id, handle: <oud>}` met oude handle uit het varianten-bestand (`redirectNewHandle: false`).

### Stap 4 · menu's
- Ids: `hoofdmenu-fase-2`, `footer-inhuys`, `footer-service` (bestaan al, geen mutatie); live `menu_hoofd` en `menu_footer` onder `live_niet_aanraken` blijven ongewijzigd.
- Controle vooraf: elk menulink-doel uit stap 1 en 2 geeft 200 (`tools/links_live.py` op de thema-preview).
- Guard: geen. Terug: stap 5 terugdraaien.

### Stap 5 · thema
- Id: `thema_kopie` `gid://shopify/OnlineStoreTheme/210233098579`; huidig thema `200751743315`.
- Vooraf: `/controle thema`, preview `?preview_theme_id=210233098579` op telefoon en desktop, `analyse/pagespeed-2026-10-26.md` als maatstaf, momentopname menu's en thema-id's.
- Mutatie: `themePublish(id: 210233098579)` (`INHUYS_GOLIVE=1`) of in de beheeromgeving Thema's, Publiceren.
- Controle: homepage, een categoriepagina, een productpagina met "Andere uitvoeringen", header en footer met de nieuwe menu's; sitemap opnieuw aanmelden.
- Terug: `themePublish(id: 200751743315)`; het kopie-thema blijft staan.

### Na de laatste stap
`INHUYS_GOLIVE` uit; `data/ids.json` lijsten (`naar_live`, `live_naar_concept`, `fase_ab`) leeg; `live_actief` bijgewerkt; nazorg uit sectie 5 start.
