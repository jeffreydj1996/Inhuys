# SEO-scan · fase 1

Versie 0.1 · 12 oktober 2026

**Reikwijdte.** Eerste scan op basis van wat zoekmachines van www.in-huys.nl laten zien. De winkel zelf en de Shopify Admin waren niet bereikbaar (zie README). Technische metingen (laadsnelheid, Core Web Vitals, gestructureerde data, canonicals, sitemap) staan daarom als *te verifiëren*. De bevindingen over indexatie, paginatitels en sitestructuur zijn wel hard.

**Legenda:** ✅ geverifieerd · ⚠️ aanname · ❌ te verifiëren zodra toegang beschikbaar is

---

## 1. Wat goed gaat

| Punt | Toelichting |
|---|---|
| ✅ Shopify als basis | Standaard goed: HTTPS, mobiel, automatische sitemap, canonical-tags, snelle hosting. De technische basis hoeft niet gebouwd te worden, alleen gecontroleerd. |
| ✅ Schone URL-structuur | `/collections/...`, `/products/...`, `/pages/...` zonder parameters of codes. |
| ✅ De juiste pijlers bestaan al | Interieuradvies en Inspiratie staan in het menu. Dat zijn precies de twee pijlers waarmee een bureau autoriteit opbouwt. Ze zijn nu alleen nog leeg. |
| ✅ Een gezicht achter het merk | "Ik ben Sylvana" is een echt vertrouwenssignaal. Google beloont aantoonbare expertise (ervaring, deskundigheid, autoriteit, betrouwbaarheid) steeds zwaarder. |
| ✅ Producten met materiaal-zoekintentie | Travertin, marmer, mangohout: mensen zoeken op materiaal, en die zoektermen zijn minder concurrerend dan "vaas". |
| ✅ Een categorie die niemand anders heeft | Maatwerk meubels is niet vergelijkbaar en sluit aan bij verbouwingen. |

---

## 2. Grootste kansen, op volgorde van impact

### Kans 1 · Indexatie: product- en collectiepagina's zijn onzichtbaar (✅)

In de geraadpleegde zoekindex staan precies drie pagina's van in-huys.nl: de homepage, `/pages/inspiratie` en `/collections/all`. Geen enkele productpagina, geen categoriecollectie (vazen, stoelen, windlichten), geen interieuradvies-pagina.

Mogelijke oorzaken, in volgorde van waarschijnlijkheid:
1. De winkel is jong of recent live, en Google heeft de diepere pagina's nog niet opgepikt.
2. De sitemap is niet aangemeld in Google Search Console.
3. Collecties en producten zijn wel aangemaakt maar niet gepubliceerd op het Online Store-kanaal.
4. Een `noindex` op productpagina's door een app of thema-instelling.

**Actie (fase 2, week 1):** Google Search Console openen of aanmaken, sitemap `https://www.in-huys.nl/sitemap.xml` indienen, rapport *Pagina's* controleren, en per producttype de publicatiestatus nalopen. Zonder indexatie heeft alle andere SEO-inspanning geen effect.

### Kans 2 · Paginatitels bevatten geen zoektermen (✅)

| Pagina | Huidige titel | Probleem |
|---|---|---|
| Homepage | "InHuys" | Zegt niets over interieurstyling of woonaccessoires. Google kan het merk niet onderscheiden van de drie naamgenoten. |
| `/collections/all` | "Producten" | Generiek. |
| `/pages/inspiratie` | "Inspiratie" | Generiek. |

**Richting:** een vast titelpatroon per paginatype.
- Homepage: `Inhuys · Interieurstyling en maatwerk voor verbouwingen`
- Collectie: `{Categorie} van {materiaal/stijl} · Inhuys` (bijvoorbeeld `Travertin en marmeren vazen · Inhuys`)
- Product: `{Productnaam} · {materiaal} {productsoort} · Inhuys`
- Dienst: `Interieuradvies bij verbouwing · werkwijze en tarieven · Inhuys`

### Kans 3 · Collectiepagina's zijn geen landingspagina's (⚠️)

Voor "hoog scoren op productgroepen" zijn de collectiepagina's het belangrijkste wapen. Ze moeten elk hebben: een eigen H1, een inleidende tekst van 150 tot 300 woorden die de categorie uitlegt (materialen, maten, waar het past), een meta-titel en meta-description, een subcategorie-navigatie en interne links naar adviesartikelen. Nu lijken het kale productrasters.

### Kans 4 · Productpagina's zonder eigen inhoud verliezen altijd (⚠️)

Producten van Jesper Home en MOOISA staan ook bij grotere winkels. Met dezelfde leverancierstekst kiest Google de grootste partij. Inhuys wint alleen met eigen tekst, eigen beeld, specificaties die anderen niet geven, en een adviescontext ("zo combineer je deze stoel met een eiken tafel"). Dit is de kern van het fase 2-template.

### Kans 5 · Merknaam is niet te onderscheiden (✅)

Drie andere bedrijven heten vrijwel hetzelfde, waarvan één (INHUYS stijl & wonen, Maasland) ook interieurstyling doet. Wie "inhuys" googelt, krijgt een gemengd beeld.

**Richting:** één schrijfwijze; organisatie-markup met `sameAs` naar de social kanalen; een Google Bedrijfsprofiel (ook zonder winkel kan dat als dienstverlener in een regio); de merknaam altijd combineren met de dienst in titels en social-bio's.

### Kans 6 · De dienst heeft geen eigen vindbare pagina's (✅)

"Interieuradvies" staat in het menu, maar er is geen pagina over de werkwijze, geen portfolio en geen tarievenpagina in de index. Voor de doelgroep "verbouwing, hoger segment" zijn dit de pagina's waarop gezocht wordt: interieuradvies verbouwing, interieurontwerp op maat, interieurstylist [regio]. Dit is ook commercieel de hoogste waarde per bezoeker.

### Kans 7 · Inspiratie is een lege belofte (✅)

De Inspiratie-pagina kondigt woontrends en stylingtips aan, maar er zijn geen artikelen in de index. Een blog met tien goede artikelen per kwartaal bouwt de autoriteit op waarmee ook productpagina's gaan stijgen. Onderwerpen liggen voor het oprapen: travertin onderhouden, eetkamerstoelen kiezen bij een ronde tafel, windlichten als lichtplan, een verbouwing stylen in drie stappen.

### Kans 8 · Hygiëne en vertrouwen (✅)

- Voorbeeldzoekterm "T-Shirt Blue Jacket" in het zoekveld is een thema-restant.
- Categorie "Extra" betekent niets.
- Geen reviews gevonden op Trustpilot, Kiyoh of Klantenvertellen.
- Geen adres, telefoon of KvK zichtbaar; alleen een e-mailadres. Voor Google en voor een klant die tienduizenden euro's uitgeeft, is dat te weinig.

### Kans 9 · Beeld-SEO (⚠️)

Alt-teksten, bestandsnamen en beeldformaat zijn niet gecontroleerd. In Shopify-winkels met leveranciersbeelden ontbreken alt-teksten bijna altijd of staan ze op de bestandsnaam. Google Afbeeldingen is voor interieur een relevante verkeersbron.

---

## 3. Te verifiëren zodra de winkel bereikbaar is (❌)

| Controle | Hoe |
|---|---|
| Sitemap aanwezig en volledig | `/sitemap.xml` openen, aantal producten vergelijken met Shopify |
| Robots.txt | `/robots.txt`; geen onbedoelde `Disallow` |
| Noindex op producten of collecties | Bron van een productpagina bekijken |
| Canonical van `/collections/x/products/y` naar `/products/y` | Bron bekijken |
| Gestructureerde data (Product, Offer, BreadcrumbList, Organization) | Google Rich Results Test |
| Core Web Vitals en laadtijd | PageSpeed Insights, mobiel |
| Apps die scripts injecteren | Thema en app-lijst nalopen |
| Hreflang en taal | Is de winkel alleen Nederlands? Dan geen hreflang nodig, wel `lang="nl"` |
| 404's en redirects | Search Console, rapport *Pagina's* |
| Dubbele titels en descriptions | Export uit Shopify of crawl met Screaming Frog |

---

## 4. Eerste zoekwoordrichting (⚠️ volumes nog te valideren met een zoekwoordtool)

| Cluster | Voorbeelden | Paginatype | Waarom |
|---|---|---|---|
| Dienst | interieuradvies verbouwing, interieurstylist [regio], interieurontwerp woonkamer, kleuradvies interieur | Dienstpagina's | Hoogste waarde per bezoeker, minste concurrentie van grote retailers |
| Maatwerk | eettafel op maat, kast op maat, maatwerk meubels | Collectie + dienst | Uniek voor Inhuys |
| Vazen | travertin vaas, marmeren vaas, grote vaas vloer | Collectie + product | Materiaal-intentie, kooprijp |
| Stoelen | design eetkamerstoel, eetkamerstoel velvet, eetkamerstoel zwart goud | Collectie + product | Hoge orderwaarde |
| Windlichten | groot windlicht, windlicht glas metaal | Collectie + product | Kerncategorie |
| Kaarsenhouders | marmeren kaarsenhouder, kandelaar travertin | Collectie | Instap, maar ondersteunend |
| Inspiratie | travertin onderhouden, eetkamerstoelen combineren, verbouwing stylen | Artikelen | Autoriteit en interne links |

---

## 5. Prioriteit (impact × inspanning)

| # | Actie | Impact | Inspanning |
|---|---|---|---|
| 1 | Search Console inrichten, sitemap indienen, indexatie oplossen | Zeer hoog | Laag |
| 2 | Titelpatronen en meta-descriptions voor alle pagina's | Hoog | Laag |
| 3 | Dienstpagina's: interieuradvies, werkwijze, projecten, tarieven | Zeer hoog | Middel |
| 4 | Collectiepagina's ombouwen tot landingspagina's | Hoog | Middel |
| 5 | Productpagina's volgens vast template, te beginnen bij de 20 duurste | Hoog | Hoog |
| 6 | Merkconsistentie, organisatie-markup, Google Bedrijfsprofiel | Middel | Laag |
| 7 | Reviews verzamelen en tonen | Middel | Laag |
| 8 | Artikelen op Inspiratie, twee per maand | Hoog op termijn | Middel |
| 9 | Hygiëne: zoekveld, categorie "Extra", schrijfwijzen | Laag | Zeer laag |

Alles in deze lijst is een voorstel. Niets wordt uitgevoerd zonder akkoord.
