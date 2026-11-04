# 10 · Dropship-koppeling via Orderchamp

Datum: 2026-11-04. Vraag van de eigenaar: zijn de conceptproducten nog gekoppeld aan de dropship-omgeving, zodat bestellingen na go-live doorlinken? Onderzoek met alleen leesqueries op de Admin API.

## Hoe de koppeling werkt

- De shop gebruikt de app **Orderchamp** (dropshipping). Orderchamp heeft een eigen fulfilmentdienst "Orderchamp Dropshipping" met een eigen locatie (`gid://shopify/Location/110905327955`, `fulfillsOnlineOrders: true`). De enige andere locatie is de handmatige "Netwerk 124".
- Een product is gekoppeld als **Orderchamp het heeft aangemaakt** en de voorraad van elke variant op de Orderchamp-locatie staat (`inventoryItem.tracked: true`, voorraadregel op die locatie). Bestellingen van zo'n variant krijgen een fulfilmentorder op die locatie en gaan daarmee naar Orderchamp.
- Voorbeelden: live `cloud-stoel-creme-set-van-2` (SKU 871917285924, 39 stuks bij Orderchamp); oud concept `cairo-loungestoel-beige` (SKU 871917285905, bij Orderchamp); Jupiduu `holzrutsche-binnen` (vier SKU's bij Orderchamp).
- Orderchamp werkt alleen de voorraad bij (updatedAt van live producten op 4 november, 12:22); de teksten en tags die de eigenaar sinds februari op die producten zette, zijn blijven staan.

## Wat er mis was

Alle 18 door ons aangemaakte concepten (fase 2 en 3) hebben `tracked: false`, voorraad 0 op "Netwerk 124" en geen voorraadregel bij Orderchamp. Een bestelling zou na go-live niet naar Orderchamp gaan. De zelf aangemaakte concepten zijn daarom alleen nog drager van tekst en metavelden.

## Hoe Orderchamp importeert

Op 27 oktober 2026 heeft Orderchamp elf concepten aangemaakt, op verzoek van de eigenaar. Twee vormen:
- één product per model met de optie Color en één variant per kleur, elk met eigen SKU en voorraad (`japandi-stoel`, vier varianten);
- één product per kleur (`sake-stoel` en `sake-stoel-1`, elk één variant).
Welke vorm, bepaalt de leverancier op Orderchamp. De import-tekst bevat per kleur breedte, hoogte, lengte, gewicht (soms onzin, bijvoorbeeld "7g"), EAN en SKU; dat is een extra bron voor de onderzoeker, geen tekst om over te nemen.

## Werkwijze vanaf nu

1. De eigenaar importeert het model in de Orderchamp-app als concept (zijn gewone werkwijze).
2. De lezer leest het concept uit naar `data/orderchamp/<handle>.json` (gid, varianten, SKU's, kleurnamen, voorraadlocatie, beelden).
3. De uitvoerder zet titel, handle, tekst, seo, type, tags, categorie, metavelden en collecties uit `data/out/productSet-<handle>.json` op dat concept met `productUpdate`; varianten, voorraad, prijzen en beelden blijven van Orderchamp. Een eigen concept met dezelfde handle wordt eerst hernoemd naar `<handle>-eigen`.
4. De eigenaar zet het concept bij go-live online en verwijdert de overbodige eigen concepten.
5. `tools/guard_shopify.py` blokkeert `productSet` en `productCreate` voor de merken Pole To Pole en Jupiduu; CLAUDE.md heeft hiervoor harde regel 7.

Importeert Orderchamp een model per kleur, dan is één product met kleurvarianten niet mogelijk zonder de koppeling te verliezen; de keuze (per kleur een product met dezelfde tekst, of de leverancier vragen om een varianten-product) ligt bij de eigenaar.

## Stand van de 18 eigen concepten

| Handle | Merk | Vervolg |
|---|---|---|
| fauteuil-cairo | Pole To Pole | Proef: eerste model dat de eigenaar opnieuw importeert |
| fauteuil-panda, fauteuil-mars, fauteuil-kathmandu, eetkamerstoel-panda-set-van-2 | Pole To Pole | Batch na de proef |
| eetkamerstoel-luna-set-van-2, eetkamerstoel-cloud-set-van-2, eetkamerstoel-breeze-set-van-2, eetkamerstoel-whale-set-van-2, eetkamerstoel-boog-set-van-2, eetkamerstoel-scandi-set-van-2, barkruk-cloud, bank-amsterdam, bank-londen, bank-new-york | Pole To Pole | Batches van 5 na de proef |
| boekensteun-mangohout | Kluster | Blijft eigen concept (geen Orderchamp) |
| vaas-agano-travertijn, waxinelichthouder-marmer | MOOISA | Blijven eigen concept (geen Orderchamp); voorraad en afhandeling door de eigenaar |
