# SEO-scan · fase 1

Versie 1.0 · 12 oktober 2026

**Reikwijdte.** Gebaseerd op de Shopify Admin API (producten, collecties, pagina's, blogs, menu's, verkoopkanalen, alle thema-bestanden van het live thema Minimog 5.7.0) en op wat zoekmachines van www.in-huys.nl laten zien. Drie controles kunnen alleen in een browser of in Google-tools en staan in sectie 4.

**Legenda:** ✅ geverifieerd · ⚠️ voorstel · ❌ alleen in de browser te controleren

---

## 1. Wat goed gaat

| Punt | Toelichting |
|---|---|
| ✅ Shopify op een premium thema | Minimog 5.7.0 is een volwassen thema: canonical-tag, Open Graph- en Twitter-tags, breadcrumb, lazy loading en Product-markup (JSON-LD met naam, url, beeld, beschrijving, sku, merk en een Offer per variant met prijs en beschikbaarheid) zitten erin. |
| ✅ Titelpatroon in het thema | `<title>` = paginatitel, aangevuld met " – InHuys" als de merknaam er nog niet in staat. Meta-description wordt uit het SEO-veld gehaald. De basis klopt; alleen de inhoud van de velden moet beter. |
| ✅ Schone URL-structuur | `/collections/…`, `/products/…`, `/pages/…`, Nederlandse handles. Eén redirect al goed ingezet (`/products/vaas-1`). |
| ✅ Meta-velden overal gevuld | 176 van 177 producten hebben een meta-titel (31 tot 59 tekens, nooit te lang) en een meta-description (154 tot 155 tekens). Het invulwerk is gedaan; het herschrijfwerk niet. |
| ✅ Alt-teksten overal aanwezig | 969 van 970 productafbeeldingen hebben een alt-tekst. Ze zijn alleen per product identiek. |
| ✅ Shopify-productcategorie overal gevuld | Alle 177 producten hebben een taxonomiecategorie (nodig voor Google Shopping en de Facebook-feed). Een paar staan fout. |
| ✅ De juiste pijlers bestaan | Interieuradvies met twee concrete diensten, een Inspiratie-pagina, een blog met twee artikelen en een gezicht achter het merk. |
| ✅ Verkoopkanalen gekoppeld | Facebook & Instagram en Pinterest zijn als kanaal actief; de productfeed kan daar direct van profiteren zodra de content klopt. |

---

## 2. Grootste kansen, op volgorde van impact

### Kans 1 · Categoriecollecties bestaan niet (✅)

Doel van de eigenaar is scoren op producten én productgroepen. Er is geen enkele collectie per productgroep: geen Stoelen, Banken, Vazen, Windlichten, Tafels, Verlichting of Maatwerk. De acht categorietegels op de homepage zijn niet aan een collectie gekoppeld. De 15 bestaande collecties zijn twaalf modelcollecties (2 tot 9 producten), een prijsfilter dat "Bestsellers" heet, en twee hulpcollecties. Geen enkele collectie heeft meta-titel, meta-description of beeld.

**Richting.** Een categoriestructuur van circa tien collecties, elk met eigen inleiding (150 tot 300 woorden), meta-velden, beeld en interne links. Dit is de eerste stap van fase 3.

### Kans 2 · Productcontent is gegenereerd sjabloonwerk met ingeplakte fabrikantzinnen (✅)

Alle 177 beschrijvingen volgen één sjabloon, 173 bevatten een letterlijk ingeplakte leverancierszin, 164 hebben geen afmetingen, en bij 119 is de tekst identiek aan die van een ander product (kleurvarianten als losse producten). Meta-descriptions zijn allemaal "Ontdek {titel}. …" en afgekapt met "…". Alt-teksten zijn "{titel} {kleur} InHuys" op elke afbeelding.

**Gevolg.** Google heeft geen reden om een InHuys-pagina boven die van een grotere winkel met dezelfde Pole To Pole-stoel te zetten. Details in `01-productoverzicht.md`; aanpak in het template van fase 2.

### Kans 3 · Indexatie: product- en collectiepagina's zijn onzichtbaar in de zoekindex (✅ voor de geraadpleegde index, ❌ Google zelf)

In de zoekindex die beschikbaar was, staan drie pagina's van in-huys.nl: de homepage, `/pages/inspiratie` en `/collections/all`. Geen productpagina, geen Interieuradvies-pagina. De 30 live producten zijn wél gepubliceerd op het webshopkanaal en hebben een online-store-URL, dus de oorzaak zit niet in de publicatiestatus.

**Actie (fase 2, week 1):** Google Search Console openen of aanmaken, sitemap indienen, rapport *Pagina's* lezen. Pas dan is zeker wat Google wel en niet heeft.

### Kans 4 · Engels thema-restant en placeholders staan live (✅)

| Plek | Tekst |
|---|---|
| Aankondigingsbalk | "Free shipping for all orders from $60+" (twee keer) |
| Topbalk | "Open Doors To A World Of Fashion \| Discover More" (link naar "#") |
| Homepage-slider | "New Arrivals · Geïnspireerd door de laatste trends · Shop Now", "Creative Together · Interieur Advies", "Op Maat Interieur · Shop Now". Geen van de knoppen heeft een link. |
| Homepage-tegels | "Accesiores" (typefout), "Extra", niet gekoppeld |
| Productpagina | "Estimated Delivery", "Free Shipping & Returns: On all orders over $75", "Guarantee safe & secure checkout", variantlabel "Size", "Backordered", "Why Minimog?" met "100 Days Return", "Lifetime Warranty", "Customers Services" (tekst over activewear), "Recently Viewed Products" |
| Footer | "Let's get in touch", "Sign up for our newsletter and receive 10% off your first order", "Quick link" en "Company" (beide het hoofdmenu), "Our store" |
| Collecties-pagina (gepubliceerd) | Vier tegels "Example collection title" |
| Contactpagina | "We would love to hear from you. If you've got great products your making…" |
| Social links | Placeholders naar facebook.com/, instagram.com/, twitter.com/ met labels "300k Followers" en "100k Followers"; de Twitter-placeholder zorgt voor een lege `twitter:site`-tag |
| Inspiratie-pagina | "Elke vind je hier nieuwe tips" (woord ontbreekt), knop "View More" |

Dit kost geen rankings op zich, maar het ondermijnt elk vertrouwenssignaal dat Google en bezoekers meewegen, en het conflicteert met de euro-prijzen en de Nederlandse doelgroep. Alles hiervan zit in thema-instellingen en is zonder code te corrigeren, in een thema-kopie, na akkoord.

### Kans 5 · Dienstpagina's zijn dun en verwijzen naar zichzelf (✅)

De Interieuradvies-pagina heeft twee dienstkaarten (3D Interieurontwerp compleet, Flitsadvies), beide "gratis", met knoppen die naar dezelfde pagina linken. Er is geen werkwijze, geen portfolio, geen Over-pagina, geen showroompagina, geen tarievenpagina. Voor de doelgroep "verbouwing, hoger segment" zijn dit de pagina's waarop gezocht en beslist wordt, en commercieel de hoogste waarde per bezoeker.

### Kans 6 · Dubbele content door kleurvarianten (✅)

Elke kleur is een apart product met dezelfde tekst. Samenvoegen tot één product per model met kleurvarianten halveert het aantal pagina's, bundelt de autoriteit en maakt de collectiepagina's leesbaar. Redirects van de oude handles zijn dan verplicht.

### Kans 7 · Merknaam is niet te onderscheiden (✅)

Drie andere bedrijven heten vrijwel hetzelfde, waarvan één ook interieurstyling doet. Het thema heeft geen Organization-markup en de social links zijn placeholders.

**Richting.** Eén schrijfwijze (InHuys), Organization-markup met `sameAs` naar echte social kanalen, Google Bedrijfsprofiel voor de showroom, en de merknaam altijd gecombineerd met de dienst.

### Kans 8 · Blog en inspiratie zijn vrijwel leeg (✅)

Vier blogs, twee artikelen (juni 2025, april 2026), twee blogs heten "woontips". De Inspiratie-pagina toont de blogposts maar heeft geen eigen inhoud. Tien goede artikelen per kwartaal bouwen de autoriteit op waarmee ook product- en collectiepagina's stijgen.

### Kans 9 · Beeldkwaliteit (✅)

299 van 970 productafbeeldingen zijn smaller dan 1000 px (meestal 800 × 800), 1 is 2000 px of breder. Voor Google Afbeeldingen en voor de uitstraling op grote schermen is dat te weinig. Alt-teksten zijn aanwezig maar niet beschrijvend.

### Kans 10 · Gestructureerde data: goed begin, drie gaten (✅)

Aanwezig: Product met Offers. Afwezig: BreadcrumbList (de breadcrumb staat wel op de pagina), Organization/LocalBusiness (showroom), en reviews (er is geen reviews-app actief, dus ook geen aggregateRating). Toevoegen kan in een thema-kopie.

---

## 3. Technische bevindingen uit het thema (✅)

| Onderdeel | Bevinding |
|---|---|
| Thema | Minimog 5.7.0 (FoxEcom), live versie "minimog-5-7-0 Met foto upload mogelijkheden" met code-aanpassingen (AI-kamerpreview-knop). Vier ongepubliceerde kopieën: 5.5.0, "met aanpassingen in code", "Kopie van", "Kopie van … Backup". |
| Title-tag | `page_title` + " – InHuys" tenzij de naam er al in staat. Productmeta-titels eindigen al op "\| InHuys", dus geen dubbele merknaam. |
| Meta-description | Uit het SEO-veld; valt terug op de paginabeschrijving. |
| Canonical | Aanwezig (`canonical_url`). |
| Open Graph / Twitter | Aanwezig; `twitter:site` is leeg door de placeholder-link. |
| Product-markup | JSON-LD Product + Offer per variant. Geen BreadcrumbList, geen Organization, geen reviews. |
| Breadcrumb | Visueel aanwezig op product-, collectie- en pagina-templates. |
| Robots | Geen eigen `robots.txt.liquid`; Shopify-standaard (goed). |
| Custom code | De snippets voor eigen code in head en body zijn leeg: geen Google Analytics-, Search Console- of tagmanager-code in het thema. (Kan via Shopify-instellingen of het Google-kanaal lopen; ❌ niet via de API te zien.) |
| Apps / snippets | Shopify Forms (adviesaanvraag), eigen AI-kamerpreview, Facebook- en Pinterest-kanaal, Judge.me- en SocialShopWave-snippets (thema-standaard, niet actief). |
| Taal | Alleen `nl`; geen hreflang nodig. |
| Templates | Productpagina: breadcrumb, hoofdblok, tabs (beschrijving + "Levering & retour"), aanbevelingen "Anderen Bekeken Ook", uitgeschakelde FAQ met Engelse demotekst, iconenrij "Why Minimog?" (live), recent bekeken. Collectiepagina: header met beschrijving, merkenlijst, raster met filters en productteller, recent bekeken. |
| Collecties-pagina | Gepubliceerd met vier placeholder-tegels. |
| Over-pagina | Template met Engelse modeteksten en fictief team bestaat; niet gekoppeld aan een pagina. |
| Redirects | 1. |

---

## 4. Alleen in de browser of in Google-tools te controleren (❌)

| Controle | Hoe |
|---|---|
| Werkelijke indexatie en sitemap | Google Search Console, rapport *Pagina's* en *Sitemaps* |
| Core Web Vitals en laadtijd | PageSpeed Insights op homepage, een collectie en een product, mobiel |
| Product-markup foutloos | Rich Results Test op `/products/travertine-agano-vaas` |
| Analytics en tracking | Shopify-instellingen → Google-kanaal / Meta-kanaal |

---

## 5. Eerste zoekwoordrichting (⚠️ volumes te valideren in fase 2)

| Cluster | Voorbeelden | Paginatype | Waarom |
|---|---|---|---|
| Dienst | interieuradvies verbouwing, 3D interieurontwerp, interieurstylist [regio], kleuradvies interieur | Dienstpagina's | Hoogste waarde per bezoeker, minste concurrentie van grote retailers |
| Maatwerk | eettafel op maat, kast op maat, maatwerk meubels | Collectie + dienst | Uniek voor InHuys |
| Stoelen | design eetkamerstoel, eetkamerstoel boucle, eetkamerstoel set van 2, barkruk boucle | Collectie + product | Grootste live categorie |
| Banken | hoekbank boucle, design bank 3 zits, bank met ottoman | Collectie + product | Hoogste orderwaarde, nu in concept |
| Vazen en kaarsenhouders | travertin vaas, marmeren kaarsenhouder | Collectie + product | Materiaal-intentie, kooprijp |
| Inspiratie | boucle onderhouden, eetkamerstoelen combineren met ronde tafel, verbouwing stylen | Artikelen | Autoriteit en interne links |

---

## 6. Prioriteit (impact × inspanning)

| # | Actie | Impact | Inspanning |
|---|---|---|---|
| 1 | Search Console inrichten, sitemap indienen, indexatie vaststellen | Zeer hoog | Laag |
| 2 | Thema-placeholders en Engelse restanten corrigeren (thema-kopie, akkoord, publiceren) | Hoog | Laag |
| 3 | Categoriecollecties bouwen en tegels koppelen | Zeer hoog | Middel |
| 4 | Dienstpagina's: interieuradvies, werkwijze, showroom, projecten, over | Zeer hoog | Middel |
| 5 | Productpagina's herschrijven volgens template, per model, live eerst | Hoog | Hoog |
| 6 | Kleurvarianten samenvoegen + redirects | Hoog | Middel |
| 7 | Organization-, LocalBusiness- en BreadcrumbList-markup | Middel | Laag |
| 8 | Reviews verzamelen en tonen | Middel | Laag |
| 9 | Artikelen op Inspiratie, twee per maand; blogs opschonen | Hoog op termijn | Middel |
| 10 | Beeld: eigen fotografie, minimaal 2000 px | Middel | Hoog |

Alles in deze lijst is een voorstel. Niets wordt uitgevoerd zonder akkoord.
