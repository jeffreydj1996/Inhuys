# Search Console via de API · controle van 26 oktober 2026

Toegang: serviceaccount als beperkte gebruiker op de domeinproperty `sc-domain:in-huys.nl`, via de Search Console API (alleen lezen). Ruwe uitvoer in `analyse/gsc/api-*.csv` en `analyse/gsc/url-inspectie-2026-10-26.csv`.

## 1. Wat de API laat zien dat de exports niet lieten zien

| Onderdeel | Bevinding |
|---|---|
| Gegevensperiode | Alleen oktober 2026. De property is recent aangemaakt; er is geen geschiedenis van vóór oktober. Alle cijfers "laatste 3 maanden" en "laatste 16 maanden" zijn identiek: 4 klikken, 106 vertoningen. |
| Sitemap | **Geen sitemap aangemeld.** De API geeft een lege lijst. Shopify maakt `https://www.in-huys.nl/sitemap.xml` automatisch aan, maar Google verwerkt hem pas structureel na aanmelding in Search Console. |
| Onbekende URL's | Van de 66 gecontroleerde URL's zijn er **48 "onbekend bij Google"**: Google heeft ze nog nooit gezien, ook niet via een sitemap. Daaronder **24 van de 30 live productpagina's** en **alle 13 modelcollecties**. |
| Geïndexeerd | 11 URL's: homepage, `/collections/all`, Interieuradvies, Inspiratie, het artikel Woontrends 2025, `/cart` en zes productpagina's (`/products/boogstoel-karamel-set-van-2`, `/products/cloud-stoel-safiya-terracotta-set-van-2`, `/products/luna-chair-mink-set-van-2`, `/products/marmer-waxinelichthouder`, `/products/springplek-binnen`, `/products/travertine-agano-vaas`). |
| Gecrawld, niet geïndexeerd | `/blogs/nieuws`, `/collections/frontpage`, `/pages/contact`: een lege blog, de verborgen homepage-collectie en een dunne contactpagina. |
| Soft 404 | `/collections/bestsellers`: op 10 april 2026 gecrawld als lege collectie; sindsdien niet opnieuw bekeken. |
| Pagina met omleiding | `http://in-huys.nl/`, `http://www.in-huys.nl/`, `https://in-huys.nl/` leiden correct door naar `https://www.in-huys.nl/`. Geen actie nodig. |
| Canonicals | Bij alle gecrawlde URL's kiest Google dezelfde canonical als de site opgeeft. Geen duplicaatprobleem. |
| Crawl | Alles als mobiel gecrawld (Googlebot smartphone). Laatste crawl homepage: 26 oktober 2026. |

Alle 30 live producten staan gepubliceerd op het kanaal Webshop (gecontroleerd via de Shopify API), dus ze horen in de sitemap en zijn bereikbaar. Dat Google ze niet kent, komt door het ontbreken van een aangemelde sitemap in combinatie met zwakke interne links: de modelcollecties staan niet in het menu en de productpagina's zijn vanaf de homepage alleen via de "alle producten"-collectie bereikbaar.

## 2. Zoekopdrachten en pagina's (oktober 2026)

| Zoekopdracht | Klikken | Vertoningen | Positie |
|---|---|---|---|
| in-huys / in huys / inhys en andere merkvarianten | 1 | 25 | 3 tot 60 |
| online interieuradvies | 0 | 17 | 70,5 |
| interieuradvies | 0 | 13 | 80,2 |
| interieuradvies online, gratis interieuradvies, interieur advies gratis | 0 | 4 | 68 tot 90 |
| voorbeeld offerte interieuradvies | 0 | 1 | 16 |

Geen enkele vertoning op een productzoekterm (eetkamerstoel, barkruk, bank, vaas). De pagina's met vertoningen: homepage (53, positie 9,6), Interieuradvies (46, positie 60,5), Inspiratie (14), `/collections/all` (11), Luna Chair Mink (7). Apparaten: 59 vertoningen desktop, 44 mobiel. Land: 86 van de 106 vertoningen uit Nederland.

Dit bevestigt de baseline in `analyse/05-seo-strategie.md`: de site is alleen vindbaar op de eigen naam en scoort op "interieuradvies" op pagina 7 tot 9.

## 3. Acties

**Door de eigenaar, vandaag nog (5 minuten):**

1. In Search Console: **Sitemaps → nieuwe sitemap toevoegen → `sitemap.xml`** → Verzenden. Dit kan alleen een eigenaar of volledige gebruiker; het serviceaccount is beperkt.
2. Daarna in Search Console voor vijf URL's **"Indexering aanvragen"** via URL-inspectie: de homepage, `/collections/all`, `/pages/interieuradvies` en twee productpagina's die nu onbekend zijn, bijvoorbeeld `/products/breeze-stoel-beige-set-van-2` en `/products/cloud-stoel-beige-set-van-2`. Dat versnelt de eerste crawl; de rest volgt via de sitemap.

**In fase 3, met de thema-kopie en de nieuwe structuur:**

3. De tien categoriecollecties in het hoofdmenu en op de homepage (staat klaar in de thema-kopie) geven elke productpagina een pad van twee klikken vanaf de homepage. Dat is de structurele oplossing voor "onbekend bij Google".
4. `/collections/bestsellers` (soft 404) en `/collections/frontpage` niet in de sitemap laten staan of vullen; `/blogs/nieuws` en `/blogs/woontips` samenvoegen volgens `content/inspiratie/README.md`.
5. `/cart` hoort niet in de index; de thema-kopie kan daar een `noindex` op zetten (Shopify blokkeert `/cart` wel in robots.txt, maar Google heeft hem al geïndexeerd).
6. De contactpagina krijgt de nieuwe tekst uit `content/paginas/contact.md`, zodat hij niet langer te dun is voor indexering.

## 4. Meting voortaan

Met de API-toegang kan elke controle zonder export: prestaties per zoekterm en pagina over een vrije periode, de indexeringsstatus van elke URL en de sitemapstatus. Voorstel: één vaste meting per twee weken, vastgelegd in `analyse/gsc/`, met de 15 kerntermen uit `analyse/zoekwoorden.csv` en de dekkingscijfers.

## Bijlage: alle 66 gecontroleerde URL's per status

**Submitted and indexed** (11): `/blogs/trends/woontrends-2025-van-greige-tot-bold-seventies`, `/cart`, `/collections/all`, `/pages/inspiratie`, `/pages/interieuradvies`, `/products/boogstoel-karamel-set-van-2`, `/products/cloud-stoel-safiya-terracotta-set-van-2`, `/products/luna-chair-mink-set-van-2`, `/products/marmer-waxinelichthouder`, `/products/springplek-binnen`, `/products/travertine-agano-vaas`

**Crawled - currently not indexed** (3): `/blogs/nieuws`, `/collections/frontpage`, `/pages/contact`

**Soft 404** (1): `/collections/bestsellers`

**Page with redirect** (3): `http://in-huys.nl/`, `http://www.in-huys.nl/`, `https://in-huys.nl/`

**URL is unknown to Google** (48): `/account/login`, `/blogs/trends`, `/blogs/woontips`, `/blogs/woontips-1`, `/collections`, `/collections/adviezen`, `/collections/amsterdam`, `/collections/boog`, `/collections/breeze`, `/collections/cloud`, `/collections/edo`, `/collections/eier`, `/collections/kathmandu`, `/collections/luna`, `/collections/panda`, `/collections/rainbow`, `/collections/rocking`, `/collections/whale`, `/pages/collecties`, `/policies/contact-information`, `/policies/privacy-policy`, `/policies/refund-policy`, `/policies/shipping-policy`, `/policies/terms-of-service`, `/products/ballenbak`, `/products/boekhouder`, `/products/boogstoelcreme-set-van-2`, `/products/breeze-stoel-beige-set-van-2`, `/products/breeze-stoel-latte-set-van-2`, `/products/breeze-stoel-pastel-roze-set-van-2`, `/products/breeze-stoel-pistache-set-van-2`, `/products/cloud-barstoel-creme`, `/products/cloud-kitchen-barstoel-creme`, `/products/cloud-stoel-beige-set-van-2`, `/products/cloud-stoel-creme-set-van-2`, `/products/cloud-stoel-karamel-set-van-2`, `/products/cloud-stoel-safiya-naturel-set-van-2`, `/products/flitsadvies`, `/products/holzrutsche-binnen`, `/products/jumpspot-buiten`, `/products/luna-stoel-caramel-set-van-2`, `/products/luna-stoelcreme-set-van-2`, `/products/scandi-stoel-tan-set-van-2`, `/products/whale-stoel-beige-set-van-2`, `/products/whale-stoel-coco-set-van-2`, `/products/wolkenbar-stoel-karamel`, `/products/wolkenkeukenbar-stoel-karamel`, `/products/zwembad`

## Nacontrole sitemap, 26 oktober 2026 om 15:54 uur (UTC)

De eigenaar heeft de sitemap om 14:21 uur aangemeld en voor vijf URL's indexering aangevraagd. Stand via de API:

- `https://www.in-huys.nl/sitemap.xml`: laatst gelezen 2026-10-26T14:21Z, in behandeling False, fouten 0, waarschuwingen 0
  - web: ingediend 57, geïndexeerd 0
  - image: ingediend 32, geïndexeerd 0

De API toont alleen de aangemelde index-sitemap; de deel-sitemaps (producten, pagina's, collecties, blogs) worden daaronder samengeteld. Alle 57 pagina-URL's zijn bekend bij Google; de teller "geïndexeerd" loopt pas op als Google de pagina's heeft gecrawld en opgenomen, meestal binnen één tot vier weken. Volgende controle bij de eerstvolgende `/meting`.
