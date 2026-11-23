# Feiten · verzending en levertijd (Pole To Pole, Jupiduu · Designed for Kids)
Datum: 2026-11-23

Doel: verzendkosten voor de consument in Nederland, gratis-drempel en levertijd per merk, met bron en opgever. Alleen wat op de geopende pagina's of in de Orderchamp-export staat.

## Eigen winkel (Shopify deliveryProfiles)
Niet uitgevoerd: de onderzoeker heeft geen graphql_query-tool. Verzendregels van de locatie "Orderchamp Dropshipping" zijn niet gelezen.

## Orderchamp-export (data/raw/products-*.json)
Alle 256 vermeldingen van "Levering" in de Orderchamp-importtekst (Pole To Pole en Jupiduu) zijn woordelijk gelijk: "Levering: verzonden via een zorgvuldig geselecteerde partner; levertijd kan per item verschillen." Geen termijn in dagen, geen verzendkosten, geen gratis-drempel.

## Feiten
| merk | feit | waarde | opgever | bron | datum |
|---|---|---|---|---|---|
| Pole To Pole | verzendkosten consument NL | niet gevonden (geen bedrag op de pagina's) | - | - | 2026-11-23 |
| Pole To Pole | gratis-drempel | niet gevonden | - | - | 2026-11-23 |
| Pole To Pole | toeslag per land (lijst) | Nederland 0%, België 5%, Luxemburg, Duitsland, Frankrijk, Oostenrijk 10%, overige landen 15% tot 40%. Op de pagina staat niet waarop het percentage slaat | Pole To Pole (fabrikant) | https://poletopole.nl/fr/supplements-par-pays/ (Franse pagina, geopend) | 2026-11-23 |
| Pole To Pole | levertijd Nederland | 1 tot 3 werkdagen ("1 à 3 jours ouvrés"); België en Duitsland 3 tot 5; Frankrijk 5 tot 7; rest van Europa 7 tot 14 werkdagen. Tabelkop: "Les délais de livraison dépendent du pays de livraison" | Pole To Pole (fabrikant) | https://poletopole.nl/fr/delai-de-livraison-prevu-par-pays/ (Franse pagina, geopend) | 2026-11-23 |
| Pole To Pole | levertijd, overig | "Op voorraad? snelle verzending. Verzending door heel Europa" (kopregel op de Nederlandse pagina, geen termijn) | Pole To Pole (fabrikant) | https://poletopole.nl/nl/over-ons/ | 2026-11-23 |
| Pole To Pole | levertijd per product | niet gevonden. Orderchamp-tekst: "levertijd kan per item verschillen" | Orderchamp | data/raw/products-1.json (export) | 2026-11-23 |
| Jupiduu | verzendkosten consument NL | niet gevonden als bedrag. Tekst: "Die genauen Versandkosten werden dir im Checkout angezeigt und richten sich nach Größe und Gewicht des Paketes." | Jupiduu (merk) | https://jupiduu.com/policies/shipping-policy | 2026-11-23 |
| Jupiduu | gratis-drempel | niet gevonden | - | https://jupiduu.com/policies/shipping-policy | 2026-11-23 |
| Jupiduu | levertijd buiten Duitsland (ook Nederland) | "Bestellungen außerhalb Deutschlands haben eine reguläre Laufzeit von 2 – 5 Tagen, je nach Lieferland etwas variierend." Express-optie aanwezig, zonder termijn in de tekst | Jupiduu (merk) | https://jupiduu.com/policies/shipping-policy | 2026-11-23 |
| Jupiduu | levertijd Duitsland (standaard) | "meist 2 - 4 Werktage im Standardversand" | Jupiduu (merk) | https://jupiduu.com/policies/shipping-policy | 2026-11-23 |
| Jupiduu | express | "Express-Bestellungen werden um 16 Uhr per Sonderkurier abgeholt und sind mit 95% Sicherheit am nächsten Morgen in Zustellung" (Duitsland) | Jupiduu (merk) | https://jupiduu.com/policies/shipping-policy | 2026-11-23 |
| Jupiduu | levertijd per product (Slide Surf Way) | "2–4 days Delivery" | Jupiduu (merk) | https://jupiduu.com/en/products/slide-surf-way | 2026-11-19 |
| Jupiduu | levertijd per product (Mantel, Surfboard, Flip Play Couch) | "Auf Lager. In 2-4 Tagen bei Dir"; "2–4 Tage Express optional". Algemene paginatekst, niet productspecifiek bevestigd | Jupiduu (merk) | https://jupiduu.com/products/artboard, https://jupiduu.com/products/surfboard, https://jupiduu.com/products/flip-play-couch | 2026-11-19 |
| Jupiduu | levertijd per product, overig | niet gevonden. Orderchamp-tekst: "levertijd kan per item verschillen" | Orderchamp | data/raw/products-2.json, products-3.json, products-4.json (export) | 2026-11-23 |
| Jupiduu | verzenddienst | DHL, FedEx en GLS, afhankelijk van pakettype, afmeting en gewicht | Jupiduu (merk) | https://jupiduu.com/policies/shipping-policy | 2026-11-23 |

## Opmerkingen
- Jupiduu-pagina's noemen Duitsland als basis; het Nederlandse tarief en de Nederlandse termijn staan niet apart. De "2 – 5 Tagen" geldt voor alle landen buiten Duitsland.
- De Jupiduu-verzendpagina en de Pole To Pole-pagina's gelden voor bestellingen op de merksites; de Orderchamp-importtekst noemt alleen "een zorgvuldig geselecteerde partner" als verzender. Of de consument via Orderchamp dezelfde termijnen krijgt, is niet vastgesteld.
- Orderchamp-helppagina's: help.orderchamp.com is ONBEREIKBAAR (proxy CONNECT 502). Niet opnieuw geprobeerd.
- Pole To Pole: de "Suppléments par pays"-pagina is in het Frans; de NL-waarde 0% is letterlijk overgenomen, de grondslag van het percentage staat niet op de pagina.
- Pole To Pole: geen dealerpagina met verzendinformatie gevonden; dealerzoekopdracht niet uitgevoerd (de opdracht vroeg om verzending, niet om een model).

## Bronnen
- https://jupiduu.com/policies/shipping-policy · "Versand" (Duits): kosten bij checkout, 2–4 werkdagen Duitsland, 2–5 dagen buiten Duitsland, Express, DHL/FedEx/GLS · geraadpleegd 2026-11-23
- https://jupiduu.com/en/products/slide-surf-way · "2–4 days Delivery" · geraadpleegd 2026-11-19
- https://jupiduu.com/products/artboard, https://jupiduu.com/products/surfboard, https://jupiduu.com/products/flip-play-couch · "2-4 Tagen" (algemene tekst) · geraadpleegd 2026-11-19
- https://poletopole.nl/fr/delai-de-livraison-prevu-par-pays/ · levertijd per land, Nederland 1–3 werkdagen · geraadpleegd 2026-11-23
- https://poletopole.nl/fr/supplements-par-pays/ · toeslag per land, Nederland 0% · geraadpleegd 2026-11-23
- https://poletopole.nl/nl/over-ons/ · "Op voorraad? snelle verzending / Verzending door heel Europa" · geraadpleegd 2026-11-23
- data/raw/products-1.json, products-2.json, products-3.json, products-4.json · Orderchamp-importtekst "Levering" · export
- Niet bereikbaar: help.orderchamp.com (proxy 502)
- Niet gevonden (404): jupiduu.com/pages/versand, poletopole.nl/pages/verzending, /pages/shipping, /en/pages/shipping, /pages/levering, /nl/levertijden-per-land/, /nl/faq/

## Huidige instelling in de winkel (Shopify, gelezen 2026-11-23)
Verzendprofiel "Algemeen profiel" (standaard), locatie "Netwerk 124": Nederland "Standaard" € 4,95; EU-zone (26 landen) € 12,95; "International" (14 landen buiten de EU) € 19,95. Geen gratis-drempel ingesteld. Orderchamp geeft zelf geen consumententarief op; dit is het tarief dat de klant nu bij het afrekenen betaalt.
