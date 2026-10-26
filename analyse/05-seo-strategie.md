# SEO-strategie · fase 2

Versie 1.0 · 26 oktober 2026

Deze strategie bouwt op de fase 1-scan (`02-seo-scan.md`), de Search Console-exports van 26 oktober 2026 (`gsc/`), de PageSpeed-meting (`pagespeed-2026-10-26.md`) en SERP-controles op de belangrijkste zoektermen. De zoektermen zelf staan in `zoekwoorden.csv`.

---

> Aanvulling 26 oktober 2026, via de API: geen sitemap aangemeld, 24 van de 30 productpagina's en alle 13 modelcollecties zijn onbekend bij Google. Zie `analyse/08-search-console-api-2026-10-26.md`.

## 1. Uitgangssituatie (Search Console, 26 oktober 2026)

### Indexatie

| Meting | Waarde |
|---|---|
| Geïndexeerd | 13 pagina's |
| Niet geïndexeerd | 18 pagina's |
| Waarvan "gecrawld, momenteel niet geïndexeerd" | 8 |
| Waarvan soft 404 | 2 |
| Waarvan uitgesloten door noindex | 1 |
| Waarvan pagina met omleiding | 3 |
| Waarvan geblokkeerd door robots.txt | 4 (Shopify-standaard: winkelwagen, zoeken, account; geen actie) |
| Sitemap | "Alle bekende pagina's" (geen sitemap aangemeld) |

De acht pagina's die Google wel crawlt maar niet opneemt, zijn de productpagina's: dezelfde sjabloontekst op elk product geeft Google geen reden om ze op te nemen. Dit is de harde bevestiging van de fase 1-conclusie. De twee soft 404's en de noindex-pagina worden in stap 7 nagelopen (waarschijnlijk de lege Collecties-pagina en een beleidspagina).

### Prestaties (afgelopen 3 maanden)

| Meting | Waarde |
|---|---|
| Klikken | 4 |
| Vertoningen | 106 |
| Gemiddelde positie | circa 35 |
| Klikken via merknaam ("in-huys", "in huys") | 1 van 4; de rest via de homepage op merkvarianten |
| Beste niet-merk-zoektermen | "online interieuradvies" (17 vertoningen, positie 71), "interieuradvies" (13 vertoningen, positie 80) |
| Productpagina met vertoningen | Luna Chair Mink (7 vertoningen, positie 4), Boogstoel karamel (2, positie 1), springplek binnen (2, positie 10) |
| Productfragmenten (rich results) | 3 vertoningen |
| Apparaten | mobiel 44 vertoningen, desktop 59, tablet 3 |

**Wat dit zegt.** De site is voor Google vrijwel onzichtbaar buiten de merknaam. Er is wél vraag naar "interieuradvies" en "online interieuradvies" waarop de Interieuradvies-pagina al vertoond wordt, op positie 70 tot 80. Die pagina heeft nu twee zinnen tekst. Met een volwaardige dienstpagina is dit de snelste weg naar zichtbaarheid. De enkele productpagina die vertoond wordt (Luna, positie 4) laat zien dat productpagina's kunnen scoren zodra Google ze opneemt.

### PageSpeed (homepage)

Mobiel 80, desktop 94. LCP mobiel 3,9 s. Toegankelijkheid 91 (zoomen geblokkeerd, contrast). SEO 100. Details en acties in `pagespeed-2026-10-26.md`.

---

## 2. Doelen

| Doel | Nu | Over 3 maanden | Over 6 maanden | Bron |
|---|---|---|---|---|
| Geïndexeerde pagina's | 13 | alle live pagina's (circa 25 na samenvoegen) | alle, inclusief nieuwe collecties en artikelen | Search Console, Pagina's |
| "interieuradvies" en "online interieuradvies" | positie 71 tot 80 | top 30 | top 10 | Search Console, Zoekopdrachten |
| "interieuradvies amsterdam", "interieurstylist amsterdam" | niet vertoond | vertoond, top 50 | top 10 | Search Console |
| Drie categorietermen (eetkamerstoel boucle, barkruk boucle, travertin vaas) | niet vertoond | top 30 | top 10 | Search Console |
| Vertoningen per dag | 3 tot 16 | 50 | 200 | Search Console, Diagram |
| Adviesaanvragen per maand | onbekend | 4 | 10 | Shopify Forms |
| PageSpeed mobiel | 80 | 85 | 90 | PageSpeed Insights |

Maandelijks dezelfde drie exports uit Search Console in `analyse/gsc/` zetten; eerste vergelijking eind november 2026.

---

## 3. Strategie in drie pijlers

### Pijler A · Dienst en lokaal (hoogste waarde per bezoeker)

- Eén volwaardige dienstpagina (Interieuradvies) met twee diensten: Flitsadvies (gratis, online of in de showroom, circa een uur) en 3D-interieurontwerp compleet (vanaf-prijs, verrekend bij aankoop).
- Ondersteunende pagina's: Werkwijze (met tarievenblok), Showroom Purmerend, Over InHuys, Projecten, Veelgestelde vragen.
- Lokale signalen: Amsterdam als werkgebied in tekst en meta, Purmerend als showroom; LocalBusiness-markup; Google Bedrijfsprofiel voor de showroom (actie eigenaar); vermelding op Trustoo en vergelijkbare directories die de SERP domineren.
- Reviews: na elk adviestraject één review op het Google Bedrijfsprofiel.

### Pijler B · Collectie (productgroepen en producten)

- Tien categoriecollecties met eigen inleiding en meta (`06-collectiestructuur.md`).
- Eén product per model met kleurvarianten; eigen tekst volgens het template; afmetingen en materiaal in metavelden.
- Positionering in de SERP: de prijsvechters (Sklum, Beliani, House Nordic) winnen op prijs; InHuys wint op advies, maatvoering, combinatie-advies en de showroom. Elke productpagina krijgt daarom het "Advies van InHuys"-blok en concrete maten.
- Volgorde: live stoelen (6 modellen), accessoires (3), daarna banken en tafels in concept.

### Pijler C · Autoriteit

- Inspiratie: twee artikelen per maand, elk gekoppeld aan één collectie en één of twee producten.
- Projecten: minimaal drie projectpagina's met eigen fotografie.
- Vermeldingen: dealerpagina's van Pole To Pole, MOOISA, Jesper Home en Kluster; partners in Amsterdam en Purmerend.
- Merknaam: InHuys met Organization-markup, `alternateName` "In-Huys" en "In Huys" (de schrijfwijzen waarop nu gezocht wordt).

---

## 4. Zoekwoordclusters

| Cluster | Aantal termen | Doelpagina's | Prioriteit |
|---|---|---|---|
| Dienst | 18 | Interieuradvies, Werkwijze, Showroom, Over | 1 |
| Showroom | 3 | Showroom | 2 |
| Merk | 4 | Homepage | 1 |
| Collectie | 34 | Tien categoriecollecties en de modelproducten | 1 tot 3 |
| Kinderkamer | 2 | Kinderkamer | 3 (bewust laag) |
| Inspiratie | 8 | Artikelen | 1 tot 3 |

Volledige lijst met intentie, doelpagina, prioriteit en bron in `zoekwoorden.csv`. Volumes zijn "te valideren": zonder Google Ads-account zijn er geen betrouwbare cijfers; de Search Console-vertoningen zijn de eerste echte meetpunten. Validatie met Keyword Planner is een actie voor de eigenaar in week 2.

### SERP-observaties (26 oktober 2026)

| Zoekterm | Wie staat er | Gevolg voor InHuys |
|---|---|---|
| interieuradvies amsterdam, interieurstylist amsterdam | Directories (Trustoo met 2.308 reviews, Homedeal met kostenrange), studio's (VINK, Studio Frieda May met 9,9) | Eigen pagina met werkwijze en tarieven, plus vermelding op Trustoo en een Google Bedrijfsprofiel met reviews |
| 3D interieurontwerp laten maken | Werkspot-freelancers, softwareleveranciers, blogs | Weinig bureaus met een eigen 3D-pagina; kans om met één goede pagina te scoren |
| eetkamerstoel boucle set van 2 | Sklum, Beliani via Brico, House Nordic; prijzen € 130 tot € 270 per set | Niet op prijs concurreren; wel op maten, advies en set-logica; collectiepagina met eigen inleiding |
| hoekbank boucle met ottoman | Nauwelijks echte bouclé-hoekbanken in de SERP | Kans voor de Londen- en Amsterdam-series zodra ze live zijn |
| barkruk boucle | Vrijwel geen relevante resultaten | Kans voor de Cloud-barkrukken |
| travertin vaas | Byflou (Wabi Sabi Siv, circa € 388), 1stdibs, Chairish; veel nadruk op "waterdicht" en onderhoud | Agano-pagina moet waterdichtheid en onderhoud expliciet beantwoorden |
| meubelshowroom purmerend | Geen directe concurrent | Showroompagina kan snel scoren |

---

## 5. Vaste patronen per paginatype

| Paginatype | Titel (50 tot 60 tekens) | Meta-description (120 tot 155) | H1 | URL |
|---|---|---|---|---|
| Homepage | InHuys · ontwerp, advies en inrichting | Interieurstyling en 3D-ontwerp voor verbouwingen in Amsterdam en omgeving. Showroom in Purmerend. | Tagline in beeld | / |
| Dienst | Interieuradvies Amsterdam · Flitsadvies en 3D-ontwerp · InHuys | Wat je krijgt, voor wie, vanaf-prijs, eerste stap | Dienstnaam | /pages/interieuradvies |
| Showroom | Showroom Purmerend · InHuys bij Kluster | Adres, wat je er ziet, afspraak | Showroom InHuys in Purmerend | /pages/showroom |
| Collectie | {Categorie} {materiaal of kenmerk} · InHuys | Wat de categorie biedt, maten, waar het past, showroom | Categorienaam | /collections/{categorie} |
| Product | {Model} {productsoort} {kenmerk} · InHuys | Effect in de ruimte, materiaal, set-inhoud, levertijd | Modelnaam + productsoort | /products/{productsoort}-{model}-{kenmerk} |
| Artikel | {Onderwerp als vraag of belofte} · InHuys | Wat de lezer leert, in één zin | Titel | /blogs/inspiratie/{onderwerp} |
| Project | {Projectnaam} · {plaats} · InHuys | Opgave en resultaat in één zin | Projectnaam | /pages/project-{naam} |

Het thema voegt " – InHuys" toe als de merknaam ontbreekt; daarom eindigen alle titels zelf op "· InHuys" en wordt de automatische toevoeging niet geactiveerd.

---

## 6. Interne links

1. Homepage → de tien categoriecollecties, Interieuradvies, Showroom, drie projecten, twee artikelen.
2. Collectie → eigen producten, twee artikelen, Interieuradvies ("laat je adviseren").
3. Product → eigen collectie (breadcrumb), één artikel, twee tot vier bijpassende stukken, Showroom.
4. Artikel → één collectie, één of twee producten, Interieuradvies.
5. Dienstpagina's → onderling (Interieuradvies ↔ Werkwijze ↔ Showroom ↔ Projecten) en naar Maatwerk.
6. Footer: InHuys-menu (dienst, projecten, showroom, over, contact) en Service-menu (verzending, retour, voorwaarden, privacy).
7. Modelcollecties (Breeze, Cloud, enzovoort) blijven bestaan voor "Anderen bekeken ook", maar krijgen geen menuplek en geen interne tekstlinks.

---

## 7. Technisch

| Actie | Wanneer | Door wie |
|---|---|---|
| Sitemap `https://www.in-huys.nl/sitemap.xml` aanmelden in Search Console | nu | eigenaar (één klik) |
| Soft 404's en noindex-pagina opzoeken in het rapport Pagina's en beoordelen | stap 7 | Claude op basis van export met URL's (eigenaar exporteert de detailtabel) |
| Viewport-meta zonder zoomblokkade | thema-kopie | Claude |
| Organization/LocalBusiness- en BreadcrumbList-markup | thema-kopie | Claude |
| Contrast van kleurschema's | thema-kopie | Claude |
| Ongebruikte scripts en preconnects beperken | thema-kopie, na functionele controle | Claude |
| Redirects van oude producthandles | fase 3, bij livegang | Claude na akkoord |
| Beeld: WebP, 2000 px, lazy loading | fase 3, per product | eigenaar levert beeld |

---

## 8. Planning (start 27 oktober 2026)

| Periode | Werk | Oplevering |
|---|---|---|
| 27 okt – 9 nov | Fase 2 in deze sessie: strategie, collectiestructuur, thema-kopie, dienstpagina's, template, eerste conceptproducten, vier artikelen | Alles als concept, ter beoordeling |
| 10 – 23 nov | Eigenaar beoordeelt preview en concepten; levert specificatiebladen, showroomgegevens, foto's; valideert zoekvolumes; meldt sitemap aan; maakt Google Bedrijfsprofiel aan | Akkoordlijst |
| 24 nov – 7 dec | Fase 3 start: publiceren van thema-kopie en dienstpagina's na akkoord; collecties publiceren; eerste modelproducten live met redirects | Live, eerste meting |
| 8 dec – 4 jan | Banken en tafels herschrijven en live; projectpagina's; artikelen 5 tot 8 | Live |
| 5 – 25 jan | Maandrapport, bijsturen op Search Console-data; tweede PageSpeed-meting | Rapport |

---

## 9. Afhankelijkheden en risico's

- **Zonder sitemap en zonder herschreven producten blijft indexatie het knelpunt.** De sitemap kost één klik; de producten kosten fase 3.
- **De directories winnen op "interieuradvies amsterdam".** Een eigen pagina alleen is niet genoeg; reviews en een Google Bedrijfsprofiel zijn voorwaarden.
- **Dropshipping-levertijden.** "Levertijd kan per item verschillen" is geen tekst voor het hogere segment. Per model een echte levertijd van de leverancier is nodig voor het template.
- **Beeld.** Zonder eigen fotografie blijft de site op leveranciersbeeld van 800 px draaien; dat beperkt zowel Google Afbeeldingen als de perceptie van segment.
