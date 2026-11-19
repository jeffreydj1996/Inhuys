# Stand van de batchloop · 19 november 2026

Lees dit eerst in een nieuwe sessie ("ga door met de batchloop"). Plan: `plannen/fase-3.md`; werkafspraken: `CLAUDE.md` (Orderchamp is de basis). De regie mag op een lichter model; Fable alleen voor de eindcontrole per batch.

## Klaar
- 92 Orderchamp-concepten dragen onze inhoud en zijn op 19 november byte-voor-byte gelijk bevonden (`data/orderchamp/verificatie/`).
- Jupiduu: 9 concepten overgezet; 5 live teksten klaar (ballenbak, houten-glijbaan-binnen, jumpspot-binnen, jumpspot-buiten, zwembad).
- Batch 9: 4 concepten overgezet; 4 live teksten klaar (Boog crème en karamel, Whale beige, Cloud barkruk crème).
- Beveiliging: tekst op de 19 live producten onder `live_tekst` mag nu (regel 2a); `python3 -I tools/guard_shopify.py --test` geeft 16 van 16.

## Te doen, in deze volgorde
1. **Variantenherziening afronden**: 21 teksten zijn herzien naar de actuele Orderchamp-varianten (lijst: `data/orderchamp/verificatie/varianten-afwijkingen-2026-11-19.txt`). Per bestand `check_tekst.py` en `md_naar_vars.py`, één controleur-run per 9 bestanden, dan uitvoerder (alleen id, title, descriptionHtml, seo, productType, tags, metafields; handle ongewijzigd) en byte-vergelijking.
2. **Live producten (19)**: eerst de actuele varianten van de live producten uitlezen en de teksten daarop nalopen (zoals stap 1). Momentopname vóór (`tools/snapshot.py`), dan per product `productUpdate` ZONDER handle (jq: `{id, title, descriptionHtml, seo, productType, tags, metafields}`), momentopname na, byte-vergelijking. Gids: `jq '.live_tekst' data/ids.json`. Links in teksten wijzen naar de huidige live handles.
3. **Afronden**: `status.py` voor de live producten, `analyse/redirects.csv` aanvullen met Jupiduu en batch 9 (uit `orderchamp_handles`), voortgang in `plannen/fase-3.md`, kosten in `data/kosten-fase3-2026-11-05.md`, commit en push.
4. **Aandachtspunten met de eigenaar** (pas daarna): teksten waar de fabrikant boven Orderchamp stond (krab H20 brons, Wing gewicht, Fjord zitdiepte, Peninsula herkomst), levertijd en garantie, 17 producten met onze inhoud zonder voorraad, dubbele SKU's tussen samengevoegde en losse kleurproducten, oude `-eigen`-concepten, go-live (handles, redirects, thema-blok "Andere uitvoeringen").

## Zuinig werken
- Uitvoerder en lezer: maximaal 5 producten per run; de lezer hoeft alleen te lezen, vergelijken doet `tools/nodes_uit_logboek.py` plus `tools/verifieer_overzetting.py`.
- Vertrouw nooit op `data/raw` voor varianten: Orderchamp verschuift kleuren. Lees het concept vóór het schrijven uit.
- Geen puntkomma's in `opmerking` van `status.py`.

## Live producten en Orderchamp (gecontroleerd 19 november 2026)
30 producten staan actief. 26 zijn gekoppeld aan Orderchamp (voorraadlocatie "Orderchamp Dropshipping"): 21 van Pole To Pole en 5 van Jupiduu. Niet gekoppeld (locatie "Netwerk 124", voorraad 0): `travertine-agano-vaas` en `marmer-waxinelichthouder` (MOOISA), `boekhouder` (Kluster), `flitsadvies` (InHuys, dienst). De eigenaar staat toe niet-gekoppelde producten op non-actief te zetten; wacht op zijn bevestiging per product (Flitsadvies is de eigen dienst) en op een aanpassing van de beveiliging, want statuswijzigingen zijn nu geblokkeerd.
13 gekoppelde live producten hebben voorraad 0: Cloud crème, karamel en beide Safiya, vier Breeze, Cloud barkruk karamel (2), Luna karamel en mink.
Stand variantenherziening: alle 21 teksten zijn herzien en mechanisch in orde; controleur, overzetting en byte-vergelijking moeten nog.

Uitgevoerd 19 november: `travertine-agano-vaas`, `marmer-waxinelichthouder` en `boekhouder` staan op concept (besluit eigenaar); Flitsadvies blijft actief. De lijst `live_naar_concept` is weer leeg. Hun oude URL's geven 404 tot de redirects bij go-live.

## Afgerond op 19 november 2026
Stap 1 tot en met 3 van "Te doen" zijn klaar: 21 herziene concepten en 19 live teksten staan op Shopify; eindvergelijking over 40 producten gaf 0 afwijkingen (`data/orderchamp/verificatie/verschillen-eindcontrole-2026-11-19.txt`). Links in live teksten wijzen naar de huidige live handles; links van live producten naar concepten zijn weggehaald en gaan bij go-live terug. Open blijft stap 4 (aandachtspunten met de eigenaar) en daarna de optimalisatie van de website.
