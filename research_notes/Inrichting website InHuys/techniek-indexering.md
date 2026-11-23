# Technische SEO en indexering www.in-huys.nl (stand 23 november 2026)

Methode: live fetches met curl op 23-11-2026 (alle 104 sitemap-URL's, 183 bekende/oude URL's uit GSC en `analyse/redirects.csv`, 217 interne links), plus de repo-bestanden onder `analyse/`. Ruwe output staat in de scratchpad (`.../scratchpad/fetch/status.tsv`, `known_status.tsv`, `link_status.tsv`). Live thema: `minimog-5-7-0 Met foto upload mogelijkheden` (id 200751743315); preview: `InHuys · fase 2 werkversie (niet publiceren)` (id 210233098579).

## 1. robots.txt en sitemap.xml: wat staat erin, en leeft het?

### Takeaway
robots.txt en sitemap zijn schoon: geen blokkade van product-, collectie-, pagina- of blog-URL's, en alle 104 URL's in de sitemaps geven HTTP 200 met een canonical naar zichzelf. Er staan geen concepten of verwijderde producten in de sitemap. Wel staan oude dubbele productversies en de speeltoestellen (holzrutsche, springplek ...) er gewoon in.

### Cited Findings
- robots.txt is Shopify-standaard (nieuwe versie met agent/UCP-commentaar): `Allow: /`; Disallow alleen op /admin, /cart/, /checkout, /orders, /account, /search-achtige sorteer- en filtervallen (`/collections/*sort_by*`, `/collections/*+*`, `filter*&*filter`), `/*?*preview_theme_id=*`, `/services`, `/sf_*`; regel `Sitemap: https://www.in-huys.nl/sitemap.xml` — [robots.txt](https://www.in-huys.nl/robots.txt)
- Let op: `/cart` (zonder slash) en `/search` worden níet door robots.txt geblokkeerd en hebben geen `meta robots noindex`; beide hebben een canonical naar zichzelf — [cart](https://www.in-huys.nl/cart), [search](https://www.in-huys.nl/search). GSC URL-inspectie van 26-10 meldt `/cart` als "Submitted and indexed" (`analyse/gsc/url-inspectie-2026-10-26.csv`) en `/cart` haalde 11 vertoningen (`analyse/gsc-rapport-2026-11-19.md`).
- Sitemap-index met 6 kinderen: `sitemap_agentic_discovery.xml` (1 URL: /agents.md), `sitemap_products_1.xml` (78 URL's, 77 met `<image:image>`), `sitemap_pages_1.xml` (4), `sitemap_collections_1.xml` (15), `sitemap_blogs_1.xml` (4), `sitemap_articles_1.xml` (2). Lastmod van alle producten 2026-11-23T11:00 — [sitemap.xml](https://www.in-huys.nl/sitemap.xml)
- Alle 104 URL's: HTTP 200, geen redirect, `<link rel="canonical">` = eigen URL, geen `<meta name="robots">` (eigen meting 23-11, `status.tsv`).
- Geen concepten in de sitemap: o.a. `luna-stoel-caramel-set-van-2`, `travertine-agano-vaas`, `marmer-waxinelichthouder`, `boekhouder`, `boogstoel-karamel-set-van-2`, `wolkenbar-stoel-karamel` geven 404 en staan niet in de sitemap (eigen meting).
- In de sitemap staan wel tegelijk oude en nieuwe versies van hetzelfde model, bv. `cloud-stoel-beige-set-van-2`, `cloud-stoel-creme-set-van-2`, `cloud-stoel-karamel-set-van-2` naast nieuwe `eetkamerstoel-*`; `luna-stoelcreme-set-van-2` + `luna-chair-mink-set-van-2`; `breeze-stoel-beige/latte/pistache-set-van-2`; en 13 kinderspeeltoestellen (`holzrutsche-binnen`, `springplek-binnen`, `ballenbak`, `jumpspot-buiten`, `glijbaan-white-dolphin`, …) — [sitemap_products_1.xml](https://www.in-huys.nl/sitemap_products_1.xml)
- Domeinvarianten: `https://in-huys.nl/` en `http://www.in-huys.nl/` stuurden met 1 redirect naar `https://www.in-huys.nl/` (200). HSTS-header aanwezig (`max-age=7889238`), `content-language: nl-NL` (eigen meting).
- GSC las de sitemap op 16-11 met 57 web-URL's en 32 afbeeldingen (`analyse/gsc/2026-11-19-sitemaps.csv`); nu zijn het 104 URL's: de 19-11 "naar live"-ronde (`analyse/12-live-gezet-2026-11-19.md`) kwam erna.

### Inferences
- Technisch blokkeert niets op sitemapniveau de indexering. Het probleem zit in inhoud en signalen (zie 6).
- Oude en nieuwe productversies van hetzelfde model naast elkaar in de sitemap geven dubbele of bijna-dubbele pagina's. Dat is een bekende oorzaak van "gecrawld, niet geïndexeerd". Ook de speeltoestellen vertroebelen het onderwerp van de site (interieur).
- `/cart` geïndexeerd is onschuldig maar slordig. Een `noindex` op cart en search in `theme.liquid` (`{% if template contains 'cart' or template contains 'search' %}`) is een kleine fix in de thema-kopie.

### Gaps
- Of Shopify het aantal "ingediend 57" inmiddels heeft bijgewerkt naar 104 kan alleen in GSC gezien worden (na 16-11 niet gemeten).

## 2. Canonical, noindex, hreflang, wachtwoord: iets dat indexering blokkeert?

### Takeaway
Nee. Er is geen wachtwoordpagina, geen noindex, geen X-Robots-Tag, en de canonicals zijn correct (self-referencing, www, https). Hreflang ontbreekt, maar dat is juist voor een site in één taal (`lang="nl"`).

### Cited Findings
- Homepage, collecties, producten en pagina's: `<html lang="nl">`, canonical naar zichzelf, geen meta robots, geen `x-robots-tag` header; geen `<link rel="alternate" hreflang>` (het enige "hreflang" in de bron is een JS-string) — eigen meting [homepage](https://www.in-huys.nl/)
- Geen wachtwoordbeveiliging: alle pagina's geven direct 200 met inhoud (eigen meting).
- Viewport live nog `maximum-scale=1.0, user-scalable=0` (toegankelijkheid, geen indexblokkade); in de preview hersteld naar `width=device-width, initial-scale=1` — [homepage](https://www.in-huys.nl/), [preview](https://www.in-huys.nl/?preview_theme_id=210233098579)
- `og:image` op productpagina's gebruikt `http://www.in-huys.nl/cdn/...` in plaats van https (eigen meting, `products/eetkamerstoel-avena-set-van-2`).
- Shopify zet een `rel=canonical` naar de eigen URL; product-URL's via een collectie (`/collections/x/products/y`) canonicaliseren naar `/products/y` (standaard thema-gedrag; in de linkcrawl kwamen geen `/collections/*/products/*`-links voor die afwijken).

### Inferences
- Indexering wordt niet technisch tegengehouden. Hreflang is niet nodig zolang er alleen een Nederlandse markt en taal is.

### Gaps
- Shopify Markets-instellingen (andere landen/talen) niet gecontroleerd. Zonder extra talen geldt het bovenstaande.

## 3. Structured data (home, collectie, 3 producten)

### Takeaway
Live: Product/Offer op productpagina's is geldig met prijs in EUR en `InStock`, maar mist GTIN, `shippingDetails` en `hasMerchantReturnPolicy`. BreadcrumbList ontbreekt overal. Organization heeft lege placeholder-`sameAs`. In de preview-thema is de nieuwe `inhuys-schema`-snippet op product- en collectiepagina's **ongeldige JSON**: de hele LocalBusiness-, WebSite- en Breadcrumb-graph gaat daar verloren. Dat moet vóór publicatie gerepareerd worden.

### Cited Findings (live, 23-11)
- Home: `Organization` (name InHuys, logo ja) met `sameAs` = `https://twitter.com/`, `https://facebook.com/`, `https://www.pinterest.com/`, `https://instagram.com/`, `https://www.snapchat.com/`, `https://www.youtube.com/` plus twee lege. Dat zijn placeholders zonder account. `WebSite` met SearchAction. Geen BreadcrumbList — [homepage](https://www.in-huys.nl/)
- Collectie `/collections/cloud`: alleen Organization, geen ItemList/CollectionPage/BreadcrumbList — [cloud](https://www.in-huys.nl/collections/cloud)
- Product `cloud-stoel-beige-set-van-2`: Product, brand Pole To Pole, offer 439.80 EUR InStock, sku 871917285928, geen gtin — [product](https://www.in-huys.nl/products/cloud-stoel-beige-set-van-2)
- Product `eetkamerstoel-avena-set-van-2`: offers 439.80 / 249.95 / 249.95 EUR InStock. De .js-feed toont varianten `room` 439.80, `Karamel` 249.95, `Nerts` 249.95. De variantnaam "room" (vertaling van crème) en het prijsverschil tussen kleuren van dezelfde set vallen op — [product](https://www.in-huys.nl/products/eetkamerstoel-avena-set-van-2), [.js](https://www.in-huys.nl/products/eetkamerstoel-avena-set-van-2.js)
- Product `bank-amsterdam`: offer 3989.95 EUR InStock, sku 871974353040, geen gtin — [product](https://www.in-huys.nl/products/bank-amsterdam)
- `flitsadvies`: Product met prijs 0.0 EUR InStock — [product](https://www.in-huys.nl/products/flitsadvies)
- Geen `priceValidUntil`, geen `shippingDetails`, geen `hasMerchantReturnPolicy` op de gemeten productpagina's (eigen parse).
- De sku's zijn 12-cijferig en beginnen met 87 (871917…, 871974…). Dat lijkt op EAN-nummers, maar ze staan niet als `gtin13` in de markup (eigen parse).
- `/pages/interieuradvies` (de pagina met 998 vertoningen) heeft live geen `<h1>`; title "Interieuradvies – InHuys" — eigen meting, [pagina](https://www.in-huys.nl/pages/interieuradvies); vertoningen uit `analyse/gsc-rapport-2026-11-19.md`
- Homepage-title is alleen "InHuys"; meta description "Doe inspiratie op, vraag advies of shop direct de nieuwste trends voor in Huis" — [homepage](https://www.in-huys.nl/)
- PageSpeed (26-10) meldde "gestructureerde gegevens zijn geldig" en SEO 100 (`analyse/pagespeed-2026-10-26.md`). Dat klopt voor de live versie, maar zegt niets over volledigheid.

### Cited Findings (preview-thema 210233098579)
- Home: nieuw `LocalBusiness` (met PostalAddress, City, AdministrativeArea, OpeningHoursSpecification) + `WebSite`. De oude Organization- en WebSite-blokken van Minimog staan er ook nog, dus WebSite komt dubbel voor. `sameAs` nu 8 lege strings — [preview home](https://www.in-huys.nl/?preview_theme_id=210233098579)
- Product- en collectiepagina: het JSON-LD-blok uit `snippets/inhuys-schema.liquid` is ongeldig ("Expecting ',' delimiter", regel 37). Het gerenderde ListItem ziet er zo uit: `"{\"@type\":\"ListItem\",\"position\":2,\"name\":Avena eetkamerstoel, set van 2","item":"..."}` — [preview product](https://www.in-huys.nl/products/eetkamerstoel-avena-set-van-2?preview_theme_id=210233098579), [preview collectie](https://www.in-huys.nl/collections/cloud?preview_theme_id=210233098579)
- Oorzaak in de bron (`data/out/theme-new/snippets/inhuys-schema.liquid`, r. 12-24): `assign crumbs = crumbs | append: '{"@type":"ListItem",...,"name":' | append: c.title | json | append: ...`. Liquid-filters werken van links naar rechts, dus `| json` escapet de hele opgebouwde string en niet alleen de titel. De bron is `tools/theme_build.py`. Fix: eerst `assign t = product.title | json`, dan `| append: t`.

### Inferences
- Product rich results (prijs en voorraad in Google) zijn mogelijk met de huidige markup. Voor merchant listings en Shopping-ervaringen zijn GTIN, verzend- en retourgegevens de grootste winst. Retour en verzending kunnen ook via Merchant Center of de Shopify Google & YouTube-app.
- De placeholder-`sameAs` live (generieke social-URL's) koppelen InHuys aan niets. Leeg laten of echte profielen invullen; in de preview is dat leeg, wat beter is.
- Publicatie van de preview met deze snippet zou de structured data op product- en collectiepagina's verslechteren. Dit is fix nummer 1 vóór go-live.

### Gaps
- Google Rich Results Test en Schema Validator niet gedraaid: geen netwerktoegang tot search.google.com vanuit deze sessie. De geldigheid is met een JSON-parser getoetst, niet met Googles validator.
- Of de 12-cijferige sku's echte EAN's zijn, is niet vastgesteld (EAN-13 heeft 13 cijfers).

## 4. Interne links en 404's

### Takeaway
Header en footer verwijzen alleen naar levende pagina's. Er zijn twee kapotte links: een merken-slider op alle 15 collectiepagina's linkt naar `/collections/mooisa` en `/collections/jesper-home` (404, ook in de preview). Daarnaast geven 124 oude product-handles uit `redirects.csv` en vier eerder geïndexeerde product-URL's 404 zonder redirect. Drie verplichte beleidspagina's geven 404.

### Cited Findings
- 217 unieke interne links uit alle 104 sitemap-pagina's: 214 × 200, 3 × 404 (zonder querystring). `/collections/vendors?q=Pole%20To%20Pole` (op 77 productpagina's) geeft met query wel 200, dus vals alarm. Echte 404's: `/collections/mooisa` en `/collections/jesper-home`, elk op 15 collectiepagina's, in een swiper-slider met merklogo's (eigen meting; `link_status.tsv`).
- Header-menu: `/`, `/collections/all`, `/collections/bestsellers`, `/pages/inspiratie`, `/pages/interieuradvies`, `/cart`, account. Footer: dezelfde vier plus WhatsApp en placeholder-socials (`https://facebook.com/` enz.) en `cookiesandyou.com`. Geen link naar contact, beleid of over-ons in de footer (eigen parse homepage).
- Er zijn geen links naar modelcollecties of `/collections/stoelen` e.d. in header of footer. Collecties zijn alleen via de sitemap en interne productlinks te vinden (eigen parse).
- Beleidspagina's: `/policies/privacy-policy` en `/policies/contact-information` geven 200; `/policies/refund-policy`, `/policies/shipping-policy` en `/policies/terms-of-service` geven **404** — [refund](https://www.in-huys.nl/policies/refund-policy), [shipping](https://www.in-huys.nl/policies/shipping-policy), [terms](https://www.in-huys.nl/policies/terms-of-service)
- Eerder geïndexeerde of vertoonde URL's die nu 404 geven: `/products/boogstoel-karamel-set-van-2`, `/products/marmer-waxinelichthouder`, `/products/travertine-agano-vaas` (alle drie "Submitted and indexed" op 26-10) en `/products/wolkenbar-stoel-karamel` (had vertoningen) — eigen meting; `analyse/gsc/url-inspectie-2026-10-26.csv`, `analyse/gsc/2026-11-19-paginas.csv`
- `/products/luna-stoel-caramel-set-van-2` geeft 404 (concept). Volgens `analyse/redirects.csv` hoort die naar `eetkamerstoel-luna-creme-set-van-2` te gaan, maar die regel bestaat nog niet in Shopify (regel 5 CLAUDE.md: redirects pas bij go-live).
- Van de 141 regels in `analyse/redirects.csv` geven de oude handles nu: 124 × 404, 17 × 200 (die 17 zijn nog live oude versies) — eigen meting.
- `analyse/13-redirects-controle.md` wijst erop dat 21 van de 84 doel-handles concept blijven. Een redirect daarheen eindigt dus ook in 404 (Breeze, Boog, Agano, waxinelichthouder e.a.).
- `/collections/frontpage` heeft 0 productlinks en stond op 26-10 als "Crawled - currently not indexed"; `/collections/bestsellers` was toen "Soft 404" en heeft nu 13 producten (eigen meting; `url-inspectie-2026-10-26.csv`).

### Inferences
- De 404's op eerder geïndexeerde URL's zijn het directe gevolg van het naar concept zetten (regel 2b) zonder redirect. Google verwijdert die URL's na herhaalde 404's uit de index en het opgebouwde signaal gaat verloren. Een 301 naar het vervangende product of de collectie houdt dat vast. Daarvoor is een besluit van de eigenaar nodig (urlRedirectCreate is verboden zonder `INHUYS_GOLIVE=1`).
- De slider met merken is een overblijfsel van een demo of oude merken. Weghalen of de links leeg maken in de thema-kopie lost 30 kapotte links op.
- Ontbrekende retour-, verzend- en voorwaardenbeleidspagina's zijn een vertrouwens- en compliancepunt. Google Merchant Center vraagt ook om retour- en verzendbeleid. Dit is werk voor de eigenaar (juridische gegevens).

### Gaps
- Links in JS-gerenderde onderdelen (mega-menu via JS, zoekresultaten) zijn niet gecrawld; alleen server-HTML.
- Afbeeldingen- en CDN-links niet op 404 getoetst.

## 5. Page speed en Core Web Vitals

### Takeaway
De PageSpeed Insights API gaf vandaag geen resultaat (dagquotum op, anoniem). De laatste meting blijft die van 26-10: mobiel prestaties 80, LCP 3,9 s, Speed Index 6,5 s; desktop 94; geen velddata door te weinig verkeer. Snelheid is niet de oorzaak van het indexeringsprobleem.

### Cited Findings
- PSI-API-aanroep 23-11 (4×, home/product/collectie mobiel, home desktop): "Quota exceeded for quota metric 'Queries' and limit 'Queries per day' of service 'pagespeedonline.googleapis.com'" — [PSI API](https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://www.in-huys.nl/&strategy=mobile)
- 26-10 (Lighthouse 13.5.0): mobiel Prestaties 80, Toegankelijkheid 91, Praktisch 96, SEO 100. FCP 2,2 s, LCP 3,9 s, TBT 30 ms, CLS 0,031, SI 6,5 s. Desktop 94 / LCP 0,8 s. Geen veldgegevens. Oorzaken: renderblokkering 300 ms, 244 KiB ongebruikte JS, meer dan 4 preconnects, app-scripts (Judge.me, SocialShopWave, countdown, flash sale) — `analyse/pagespeed-2026-10-26.md`
- Server-timing live: processing 201 ms (db 164 ms, render 38 ms), via edge IAD bij een request vanuit de VS (eigen meting headers).
- Preview: viewport hersteld. Of de app-scripts in de preview weg zijn, is niet gemeten.

### Inferences
- LCP 3,9 s mobiel (lab) valt in "verbetering nodig". Zonder velddata (CrUX) gebruikt Google geen CWV-signaal voor deze site, dus snelheid is nu geen rankingfactor van betekenis. Wel van belang voor conversie.

### Gaps
- Geen actuele PSI-meting (quotum). Opnieuw meten met een API-sleutel of via pagespeed.web.dev door de eigenaar, op home, `/collections/cloud` en `/products/eetkamerstoel-avena-set-van-2`, live én preview.

## 6. Search Console: wat zeggen de data, en waarom "57 ingediend, 0 geïndexeerd"?

### Takeaway
"0 geïndexeerd" in het sitemaprapport via de API is geen echte meting. Het veld `contents[].indexed` van de Search Console Sitemaps-API is door Google **deprecated ("do not use")** en geeft geen betrouwbaar getal. Het bewijs dat pagina's wél geïndexeerd zijn: 25 pagina's kregen vertoningen in 28 dagen (alleen geïndexeerde pagina's krijgen vertoningen), het indexeringsrapport toonde op 23-10 13 geïndexeerde pagina's, en URL-inspectie gaf 11 × "Submitted and indexed". Het echte knelpunt is dat het meeste nieuwe nog "URL is unknown to Google" is en dat de site weinig autoriteit heeft.

### Cited Findings
- Sitemaps-API documentatie: "contents[].indexed — N/A — Deprecated; do not use." en "contents[].submitted — The number of URLs in the sitemap" — [Google Search Console API, Sitemaps](https://developers.google.com/webmaster-tools/v1/sitemaps)
- GSC-meting 19-11 (API): sitemap web ingediend 57, geïndexeerd 0; image 32/0; laatst gelezen 16-11; 0 fouten. 28 dagen: 1 klik (zoekopdracht), 1007 vertoningen (was 60), 24 zoekopdrachten, 25 pagina's met vertoning — `analyse/gsc-rapport-2026-11-19.md`
- Pagina's met vertoningen (19-11): `/` 4 klikken/119 vert./pos 8,8; `/pages/interieuradvies` 998 vert./pos 82,7; `/pages/inspiratie` 28/pos 5,4; `/collections/breeze`, `/collections/rocking`, `/collections/amsterdam` met posities 6-7; `/products/cloud-stoel-beige-set-van-2` 12/pos 26 — `analyse/gsc-rapport-2026-11-19.md`
- Zoekopdrachten: "interieuradvies" 727 vert. op pos 93,4 (was 80,2), "meubeladvies" 91 op pos 49, merknaam "in-huys" pos 2,5, "in huys" pos 11,6 (was 4,4). Voor alle productzoekwoorden (eetkamerstoel boucle, travertin vaas …) 0 vertoningen — `analyse/gsc-rapport-2026-11-19.md`
- Indexeringsdiagram tot 23-10: 13 geïndexeerd, 18 niet geïndexeerd — `analyse/gsc/indexering-diagram-2026-10-26.csv`
- Redenen niet geïndexeerd (26-10): Gecrawld - momenteel niet geïndexeerd 8; Geblokkeerd door robots.txt 4; Pagina met omleiding 3; Soft 404 2; Uitgesloten door noindex 1 — `analyse/gsc/indexering-niet-kritieke-problemen-2026-10-26.csv`
- URL-inspectie 26-10 (66 URL's): 48 "URL is unknown to Google", 11 "Submitted and indexed", 3 "Page with redirect" (domeinvarianten), 3 "Crawled - currently not indexed" (`/blogs/nieuws`, `/collections/frontpage`, `/pages/contact`), 1 "Soft 404" (`/collections/bestsellers`) — `analyse/gsc/url-inspectie-2026-10-26.csv`
- Vóór 26-10 was er geen sitemap aangemeld — `analyse/05-seo-strategie.md` r. 9, 24
- Google over "Crawled - currently not indexed": "Google doesn't index all pages across the web, so this is a common message for many sites and doesn't necessarily indicate an issue". Over "Discovered - currently not indexed": Google heeft de URL gevonden maar de crawl uitgesteld. Over ontbrekende pagina's: een pagina moet "linked from a known page, or from a sitemap" zijn. Voor een nieuwe site is de beste eerste stap "request indexing of your homepage" — [Page indexing report, Search Console Help](https://support.google.com/webmasters/answer/7440203?hl=en)

### Inferences
- De boodschap "0 van 57 geïndexeerd" moet uit de rapportage. Gebruik in `/meting` het indexeringsrapport (Pagina's) of URL-inspectie per URL. Of tel pagina's met vertoningen als ondergrens van "geïndexeerd".
- Typische oorzaken bij een jonge Shopify-winkel, hier van toepassing: (a) sitemap pas eind oktober aangemeld en in november twee keer flink gewijzigd (handles en concepten), zodat veel URL's nieuw en onbekend zijn; (b) dubbele of bijna-dubbele productpagina's (oude en nieuwe versies, Orderchamp-importteksten die ook bij andere dealers staan); (c) weinig interne links naar modelcollecties en producten vanuit het menu; (d) weinig externe links of merkautoriteit; (e) eerder geïndexeerde URL's die nu 404 geven zonder redirect.
- Fixes die werken: dubbelen weg uit de live catalogus of canonical en redirect naar één versie; collecties in het hoofdmenu; per hoofdpagina indexering aanvragen via URL-inspectie (home, interieuradvies, belangrijkste collecties, top-10 producten); sitemap opnieuw indienen na de handle-wissel; Google Bedrijfsprofiel en een paar echte externe vermeldingen (Orderchamp-merkenpagina's, social).
- "Interieuradvies" (727 vertoningen, pos 93) is het enige zoekwoord met volume. De pagina heeft geen H1. H1 en interne links naar die pagina zijn snelle winst.

### Gaps
- Geen actuele indexeringsrapport-export na 26-10. Hoeveel van de 104 URL's nu geïndexeerd zijn, is alleen met GSC (Pagina's-rapport of URL-inspectie-API) vast te stellen.
- Backlinkprofiel niet onderzocht.

## 7. Verschil preview-thema (210233098579) op deze punten

### Takeaway
De preview verbetert de viewport, maakt `sameAs` leeg en voegt LocalBusiness toe. Daar staat tegenover dat de JSON-LD op product- en collectiepagina's kapot is, dat WebSite dubbel voorkomt en dat de kapotte merklinks (mooisa, jesper-home) blijven. Canonicals en robots zijn gelijk aan live.

### Cited Findings
- Preview home, product en collectie: canonical gelijk aan live, geen meta robots; viewport `width=device-width, initial-scale=1` — [preview](https://www.in-huys.nl/?preview_theme_id=210233098579)
- Preview product/collectie: ongeldige JSON-LD door de `| json`-volgorde in `snippets/inhuys-schema.liquid` (zie 3) — [preview product](https://www.in-huys.nl/products/eetkamerstoel-avena-set-van-2?preview_theme_id=210233098579)
- Preview collectie bevat nog `/collections/mooisa` en `/collections/jesper-home` (eigen meting `prev_coll.html`).
- Preview-URL's met `?preview_theme_id=` staan in robots.txt op Disallow. Ze lekken dus niet in de index — [robots.txt](https://www.in-huys.nl/robots.txt)

### Inferences
- Vóór publicatie van de thema-kopie: (1) breadcrumb-Liquid repareren en opnieuw parsen; (2) Minimog's eigen Organization/WebSite uitschakelen of de nieuwe snippet alleen LocalBusiness + Breadcrumb laten leveren (geen dubbele WebSite); (3) merken-slider verwijderen; (4) `noindex` voor cart/search toevoegen; (5) H1 op `/pages/interieuradvies`.

### Gaps
- Preview niet gecontroleerd op artikelpagina's en `page`-templates (zelfde bug te verwachten: dezelfde code-opbouw in `when 'page'` en `when 'article'`).

---

## Prioriteitenlijst (voor de rapportschrijver)

1. **Meetfout eruit:** "0 geïndexeerd" komt uit een deprecated API-veld. Rapporteer indexering via het Pagina's-rapport of URL-inspectie. (Geen risico, direct.)
2. **Preview-schema repareren vóór thema-publicatie:** breadcrumb-JSON ongeldig op product- en collectiepagina's; dubbele WebSite. (Thema-kopie, mag nu.)
3. **404's op eerder geïndexeerde URL's:** 301's voor `boogstoel-karamel-set-van-2`, `marmer-waxinelichthouder`, `travertine-agano-vaas`, `wolkenbar-stoel-karamel`, `luna-stoel-caramel-set-van-2` en de rest van `redirects.csv`; doelen die concept blijven naar een collectie laten wijzen. (Besluit eigenaar, `INHUYS_GOLIVE=1`.)
4. **Beleidspagina's** refund, shipping en terms aanmaken (nu 404). (Eigenaar, juridisch.)
5. **Dubbele productversies** (oud cloud/breeze/luna naast nieuwe `eetkamerstoel-*`) uit de live catalogus of samenvoegen. Speeltoestellen eventueel apart of eruit. (Eigenaar.)
6. **Interne links:** modelcollecties in het menu; merken-slider met mooisa en jesper-home weg; contact en beleid in de footer. (Thema-kopie en menu's: menu live = eigenaar.)
7. **On-page:** H1 op `/pages/interieuradvies`; homepage-title en description herschrijven ("InHuys" en "voor in Huis" zijn te dun). Placeholder-socials live weghalen.
8. **Product-markup:** GTIN (als de sku's EAN's zijn), verzend- en retourgegevens (snippet of Merchant Center).
9. **Na de wijzigingen:** sitemap opnieuw indienen, indexering aanvragen voor home, interieuradvies, inspiratie, de 5 belangrijkste collecties en de top-10 producten; PSI opnieuw meten met een sleutel.
