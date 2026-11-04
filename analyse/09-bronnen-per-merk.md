# 09 · Bronnen per merk en de lijst voor de netwerkbeperking

Datum: 2026-11-04. Vraag van de eigenaar: welke websites heeft de onderzoeker nodig voor de juiste productinformatie per merk, zodat de internettoegang van de cloudomgeving tot die sites beperkt kan worden.

## Merken in de export

Uit `data/raw/products-*.json`: Pole To Pole (157 producten), Jupiduu · Designed for Kids (14), MOOISA (2), Jesper Home (2), Kluster (1, eigen), InHuys (1, eigen dienst). Kluster en InHuys hebben geen externe bron.

## De lijst (kopiëren naar "Toegestane domeinen")

Hosts met én zonder `www`, omdat de sites doorsturen. Per merk eerst de fabrikant, dan dealers die maten publiceren.

| Merk | Host | Wat er staat | Gecontroleerd op |
|---|---|---|---|
| Pole To Pole | `poletopole.nl`, `www.poletopole.nl`, `b2b.poletopole.nl` | Fabrikant. Per SKU een specificatieblok (`extraFields`): breedte, diepte, hoogte, gewicht, armleuninghoogte, zithoogte, zitbreedte, materialen, brandvertragend, reinigingsinstructie, land van herkomst, doosinhoud. Product-sitemap met 322 producten. B2B-portal met login, alleen als de eigenaar die zelf wil gebruiken. | Cairo beige (871917285905) |
| Pole To Pole | `www.gigameubel.nl`, `gigameubel.nl` | Nederlandse dealer: zithoogte, gewicht, materialen, onderhoud. Nodig voor modellen die niet meer op poletopole.nl staan. | Wave barstoel, Fjord |
| Pole To Pole | `homka-living.de`, `www.homka-living.de` | Duitse dealer: maten in cm, zithoogte, materialen, onderhoud. | Cairo, Mars, Cloud barstoel |
| Pole To Pole | `huismerken.nl`, `www.huismerken.nl` | Nederlandse dealer: maten, zithoogte, zitdiepte, gewicht. | Sake |
| Pole To Pole | `www.stil-ambiente.de`, `stil-ambiente.de` | Duitse dealer: materiaal en prijs; reserve. | Cairo |
| Pole To Pole | `www.kunstplaza.de`, `kunstplaza.de` | Duitse dealer: maten; reserve, alleen om de Kathmandu-bron na te lezen. | Cloud barstoel, Mars bank |
| Pole To Pole | `mom.maison-objet.com` | Beursplatform met productbladen van oudere modellen; reserve. | Mars, Whale, Elephant, Wave, Fjord |
| Jupiduu | `jupiduu.com`, `www.jupiduu.com` | Fabrikant (Shopify, Duits; `/en/` Engels): maten, gewicht, materiaal, leeftijd, maximale belasting, onderhoud. Alle producten in de sitemap. | Glijbaan White Dolphin, Jumpspot |
| MOOISA | `www.mooisa.com`, `mooisa.com` | Fabrikant: maten in de titel, materiaal (travertin, marmer), onderhoudsblok. | Agano vaas, waxinelichthouders |
| Jesper Home | `www.jesperhome.com`, `jesperhome.com` | Fabrikant (Shopify): maattabel (hoogte, breedte, diepte, zithoogte, zitbreedte, zitdiepte, armleuning), gewicht, maximale belasting, materialen, reiniging. | Yanai dining chair |
| Werkwijze | `www.in-huys.nl`, `in-huys.nl` | Eigen winkel: live pagina's en sitemap controleren. | |
| Werkwijze | `cdn.shopify.com` | Beelden van de winkel en van de Shopify-sites van de merken. | |
| Werkwijze | `www.googleapis.com` | Search Console-meting (`tools/gsc_meting.py`). | |
| Werkwijze | `github.com`, `api.github.com` | Commit en push van de werkbranch. | |

**Minimale variant**: `poletopole.nl`, `www.gigameubel.nl`, `homka-living.de`, `huismerken.nl`, `jupiduu.com`, `www.mooisa.com`, `www.jesperhome.com` plus de vier werkwijze-hosts.

Buiten de beperking om (uitzonderingen van de proxy): de Shopify-MCP, de GitHub-MCP, de Anthropic-API, pip en npm.

## Niet op de lijst, met reden

| Host | Reden |
|---|---|
| `www.polepole.nl` | Geparkeerd domein, geen merk (stond in een feitenbestand als fabrikant) |
| `mooisa.nl` | Te koop; de merk-site is `www.mooisa.com` |
| `jesperhome.nl`, `jesper-home.nl` | Bestaan niet |
| `www.poletopole.com` | Ander bedrijf |
| `www.faire.com`, `www.ankorstore.com` | Groothandelsmarktplaatsen; specificaties alleen na inloggen |
| `www.feriahabitatvalencia.com` | Persbericht, geen specificaties |
| `sneakids.com`, `kindermaxx.de`, `lespetits.fr`, `galaxus.ch`, `singular.shop`, `tabledusud.nl`, `kas20.nl` | Dealers die niets toevoegen aan de fabrikantsite |
| `bol.com`, `fonq.nl` | Geen producten van deze merken |

## Wat de controle opleverde

- **WebFetch werkt in deze omgeving niet**: zelfs `www.in-huys.nl` geeft `ENOTFOUND`, terwijl `curl` via de proxy dezelfde host bereikt. De "geblokkeerde hosts" uit de onderzoeksrondes van 26 oktober en 4 november waren dus grotendeels een gevolg van die tool. De onderzoeker gebruikt vanaf nu `tools/bron_ophalen.py` (curl) en heeft WebFetch niet meer.
- **Pole To Pole**: de product-URL bevat onze SKU (`/en/product/<sku>/<slug>/`), dus naam, kleur en specificaties zijn per SKU te verifiëren. Niet in de sitemap en niet onder `/en/products/discontinued/`: Mars (871917285522, 871917285726), Kathmandu (871917285910, 871917285911) en de Panda-eetkamerstoel (871917285791, 871917285792). Voor die modellen blijven dealers de bron. De "Kathmandu Amon" op kunstplaza.de is mogelijk geen Pole To Pole-product; het feitenbestand noemt die koppeling al als te verifiëren.
- **Giga Meubel heeft alle vijf modellen van fase 3** (Cairo in beide kleuren, Mars, Panda armstoel en eetkamerstoel, Kathmandu Amon in naturel en terra) met volledige specificatietabellen (maten, zithoogte, zitdiepte, zitbreedte, gewicht, materiaal onderstel, zitting en vulling, montage). WebSearch met `site:` vond die pagina's niet; de eigen zoekfunctie van de site wel. Daarom heeft `tools/bron_ophalen.py` een modus `dealer` die rechtstreeks in de zoekfunctie van gigameubel.nl, huismerken.nl en homka-living.de zoekt. De Kathmandu-pagina bij Giga Meubel bevestigt ook dat Kathmandu Amon een Pole To Pole-product is.
- Wel op poletopole.nl (telling in de sitemap): Amsterdam 10 URL's, Cloud 8, Whale 3, Luna 3, EDO 2, Egg 2, Rainbow 2, Bow 2, Breeze 1, Panda-fauteuil 1.
- Bereikbaarheid op 2026-11-04 met curl: alle hosts in de lijst geven 200, 301 of 302. `www.poletopole.nl` geeft een certificaatfout (de site zelf gebruikt het domein zonder www). Aan het eind van de sessie weigerde de proxy `www.jupiduu.com` (403 bij CONNECT) terwijl `jupiduu.com` bleef werken; de onderzoeker gebruikt daarom altijd de host zonder www.
- Test van het script: `sku 871917285905` geeft 20 feiten van de Cairo-pagina (onder meer zithoogte 42 cm, zitdiepte 69 cm, gewicht 38 kg, beukenhout en multiplex, schuim 38 kg/m³, stof 96% polyester / 4% acryl, herkomst China); `sku 871917285522` (Mars) meldt "niet op poletopole.nl"; de url-modus leest de maattabellen van jesperhome.com, mooisa.com (met gewicht 10,9 kg uit de Shopify-productjson) en gigameubel.nl.

## Gevolg voor de werkwijze

- `.claude/agents/onderzoeker.md`: fabrikant eerst (Pole To Pole per SKU; Jupiduu, MOOISA en Jesper Home rechtstreeks), dealers alleen als de SKU niet op poletopole.nl staat; WebSearch alleen om een productpagina op deze hosts te vinden.
- Zodra de beperking actief is: de vijf modellen van fase 3 (Panda-fauteuil, Kathmandu, Cairo, Mars, Panda-stoel) opnieuw laten onderzoeken en alleen de specificatietabellen en `inhuys.*`-metavelden bijwerken.
