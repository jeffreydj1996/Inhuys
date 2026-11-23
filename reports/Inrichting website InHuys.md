# Herstel eerst vertrouwen, adverteer daarna pas

**Kort oordeel.** www.in-huys.nl is technisch vindbaar, maar commercieel en juridisch nog niet goed ingericht. Sitemap, robots.txt en canonicals zijn schoon en niets blokkeert de indexering. Toch doet de live site onware beloftes bij de koopknop: "100 Days Return", "Lifetime Warranty", gratis verzending "over $75", een automatische leverdatum "Nov 28 - Dec 02" en "100 in voorraad". Daarnaast geven de pagina's voor algemene voorwaarden, retour en verzending een 404 en ontbreekt de herroepingsknop, die sinds juni 2026 verplicht is. Daardoor kan een klant tot een jaar na de wettelijke bedenktijd nog herroepen, en dat bij banken van €2.700 tot €5.700. De voorbereide thema-werkversie lost het grootste deel van de demo-inhoud en de navigatie op. Vóór publicatie moet er nog wel iets gerepareerd worden: de structured data op product- en collectiepagina's is ongeldige JSON, en de leverdatum is vast op 14 dagen gezet zonder bevestiging van de leverancier. Op de markt is InHuys op identieke Pole To Pole-modellen 15 tot 25% duurder dan Giga Meubel. Je wint dus niet op prijs maar op advies. Het haalbare doel voor december 2026 tot en met februari 2027: **25 bestellingen en €6.500 omzet**, met in februari 1.300 sessies, een conversie van 0,9% en 80 geïndexeerde URL's. Dat gaat uit van €300 per maand aan Google Shopping, dat pas start als fase A hieronder klaar is. Zonder advertenties ligt de ondergrens op 4 tot 6 bestellingen. Met €1.000 per maand en meer content ligt het plafond op 90 bestellingen en €25.000. Of betaald verkeer winst oplevert, hangt af van je inkoopmarge. Die staat in Orderchamp en zit niet in dit onderzoek.

## De techniek staat; de meting misleidde

### Techniek en indexering: toets

| Onderdeel | Oordeel | Bewijs |
|---|---|---|
| robots.txt en sitemap | goed | robots.txt is de Shopify-standaard met `Sitemap:`-regel ([robots.txt](https://www.in-huys.nl/robots.txt)); alle 104 sitemap-URL's geven 200 met een canonical naar zichzelf, zonder concepten ([sitemap.xml](https://www.in-huys.nl/sitemap.xml)) |
| Blokkades (noindex, wachtwoord, canonical) | goed | geen meta robots, geen X-Robots-Tag, geen wachtwoordpagina, `lang="nl"`; hreflang is bij één taal niet nodig ([homepage](https://www.in-huys.nl/)) |
| Werkelijke indexering | onvoldoende | URL-inspectie op 26 oktober: 48 van 66 URL's "unknown to Google", 11 geïndexeerd ([url-inspectie-2026-10-26.csv](/home/user/Inhuys/analyse/gsc/url-inspectie-2026-10-26.csv)); 25 pagina's kregen vertoningen in 28 dagen ([gsc-rapport-2026-11-19.md](/home/user/Inhuys/analyse/gsc-rapport-2026-11-19.md)) |
| Dubbele productversies | onvoldoende | oude `cloud-stoel-*`, `breeze-stoel-*` en `luna-stoelcreme-*` staan naast de nieuwe `eetkamerstoel-*`; daarnaast 13 speeltoestellen ([sitemap_products_1.xml](https://www.in-huys.nl/sitemap_products_1.xml)) |
| Structured data live | onvoldoende | Product/Offer is geldig, maar zonder GTIN, `shippingDetails` en `hasMerchantReturnPolicy`; Organization verwijst naar generieke social-URL's; geen BreadcrumbList ([product](https://www.in-huys.nl/products/bank-amsterdam), [homepage](https://www.in-huys.nl/)) |
| Structured data werkversie | onvoldoende, blokkeert publicatie | breadcrumb-JSON op product- en collectiepagina's is ongeldig, en WebSite staat er twee keer in ([preview product](https://www.in-huys.nl/products/eetkamerstoel-avena-set-van-2?preview_theme_id=210233098579)) |
| Interne links en 404's | onvoldoende | `/collections/mooisa` en `/collections/jesper-home` geven 404 vanuit een merkenslider op alle 15 collectiepagina's; 124 oude handles uit [redirects.csv](/home/user/Inhuys/analyse/redirects.csv) en 4 eerder geïndexeerde product-URL's geven 404 zonder redirect ([boogstoel-karamel](https://www.in-huys.nl/products/boogstoel-karamel-set-van-2), [travertine-agano-vaas](https://www.in-huys.nl/products/travertine-agano-vaas)) |
| On-page | onvoldoende | homepagetitel is alleen "InHuys"; `/pages/interieuradvies` (998 vertoningen) heeft geen H1 ([interieuradvies](https://www.in-huys.nl/pages/interieuradvies)); `/cart` is geïndexeerd |
| Snelheid | onvoldoende, geen blokkade | laatste meting 26 oktober: mobiel 80, LCP 3,9 s, desktop 94, geen velddata ([pagespeed-2026-10-26.md](/home/user/Inhuys/analyse/pagespeed-2026-10-26.md)); nieuwe meting lukte niet door het dagquotum ([PSI API](https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://www.in-huys.nl/&strategy=mobile)) |

Het getal dat tot nu toe de rapportage stuurde, "57 ingediend, 0 geïndexeerd", is geen meting. Google noemt het veld `contents[].indexed` in de Sitemaps-API **"Deprecated; do not use"** ([Search Console API, Sitemaps](https://developers.google.com/webmaster-tools/v1/sitemaps)). Uit de feiten blijkt dat er wel pagina's in de index staan. 25 pagina's kregen vertoningen, het indexeringsrapport telde op 23 oktober 13 geïndexeerde pagina's ([indexering-diagram](/home/user/Inhuys/analyse/gsc/indexering-diagram-2026-10-26.csv)), en de URL-inspectie gaf 11 keer "Submitted and indexed". Het echte knelpunt is dus niet een blokkade. Het is een combinatie van vier dingen. De sitemap werd pas eind oktober aangemeld en daarna twee keer flink gewijzigd. Oude en nieuwe versies van hetzelfde model staan naast elkaar. Het menu linkt bijna niet naar collecties. En eerder geïndexeerde URL's geven nu een 404. Google zegt zelf dat "Crawled - currently not indexed" vaak voorkomt, en raadt een nieuwe site aan te beginnen met het aanvragen van indexering voor de homepage ([Page indexing report](https://support.google.com/webmasters/answer/7440203?hl=en)). In de rapportage hoort voortaan het Pagina's-rapport of de URL-inspectie per URL.

Zoekverkeer is er nog nauwelijks: **1 klik en 1.007 vertoningen in 28 dagen**. Daarvan gingen er 998 naar `/pages/interieuradvies`, op een gemiddelde positie van 82,7. Voor producttermen zijn er 0 vertoningen ([gsc-rapport-2026-11-19.md](/home/user/Inhuys/analyse/gsc-rapport-2026-11-19.md)). Het enige zoekwoord met volume is een dienstwoord, "interieuradvies". Dat bepaalt ook waar de snelste organische winst zit.

## Vertrouwen en wettelijke eisen: hier zit het urgente werk

### Vertrouwen en wettelijke eisen: toets

| Onderdeel | Oordeel | Bewijs |
|---|---|---|
| Bedrijfsgegevens (Kluster, adres, KvK, btw) | onvoldoende | alleen op de ongelinkte pagina `/policies/contact-information`, zonder de naam Kluster ([contact-information](https://www.in-huys.nl/policies/contact-information)); de contactpagina heeft Engelse demotekst ([contact](https://www.in-huys.nl/pages/contact)) |
| Algemene voorwaarden | ontbreekt | 404 ([terms-of-service](https://www.in-huys.nl/policies/terms-of-service)) |
| Herroeping, modelformulier, retouradres, retourkosten | ontbreekt | 404 ([refund-policy](https://www.in-huys.nl/policies/refund-policy)); op de productpagina staat alleen één regel |
| Herroepingsknop | ontbreekt | verplicht sinds juni 2026 ([ACM herroepingsknop](https://www.acm.nl/nl/publicaties/acm-roept-online-retailers-op-zich-voor-te-bereiden-op-herroepingsknop)) |
| Verzendbeleid en verzendkosten vooraf | ontbreekt | 404 ([shipping-policy](https://www.in-huys.nl/policies/shipping-policy)); de enige vermelding is "over $75" |
| Levertijd | onjuist | automatisch "Estimated Delivery: Nov 28 - Dec 02", ook op uitverkochte producten ([bank-londen-6-zits-tan](https://www.in-huys.nl/products/bank-londen-6-zits-tan), [Breeze](https://www.in-huys.nl/products/breeze-stoel-beige-set-van-2)) |
| Garantie | onjuist | "Lifetime Warranty" uit het demothema; de wettelijke garantie staat er niet |
| Privacybeleid | onvoldoende | Shopify-sjabloon zonder Kluster, zonder verwerkers en zonder de AI-kamerpreview met foto-upload ([privacy-policy](https://www.in-huys.nl/policies/privacy-policy)) |
| Cookietoestemming | onvoldoende | Engelse themabanner naast de Shopify-banner, en een Pinterest-pixel met doel MARKETING ([homepage](https://www.in-huys.nl/)) |
| Prijzen inclusief btw | goed | "Inclusief belasting." ([bank-londen-6-zits-tan](https://www.in-huys.nl/products/bank-londen-6-zits-tan)) |
| Voorraad- en urgentiesignalen | onjuist | "100 in voorraad" is een standaardaantal van Orderchamp ([voorraad-2026-11-19b.csv](/home/user/Inhuys/data/orderchamp/voorraad-2026-11-19b.csv)) |
| Verzendlanden | te breed | 41 landen, onder meer de VS, Australië en Japan ([meta.json](https://www.in-huys.nl/meta.json)) |
| Keurmerk en reviews | ontbreekt | geen van beide op de site |
| Betaalmethoden | onzeker | Shopify Payments met Visa, Maestro en Mastercard staat aan; of iDEAL aanstaat, is niet gezien en er staan geen betaaliconen ([productbron](https://www.in-huys.nl/products/bank-londen-6-zits-tan)) |
| Demo-inhoud | schadelijk | leeftijdscheck "Are you 18 years old or older?", "Open Doors To A World Of Fashion", "10% off" en de u-vorm op de homepage ([homepage](https://www.in-huys.nl/)) |

De ernst zit in de combinatie. De ACM eist dat je vóór de koop vertelt dat de bedenktijd tot 14 dagen na levering loopt, wie de retour betaalt en wat die kost als het pakket niet door de brievenbus past. Een Nederlandse webwinkel moet daarbij een Nederlands retouradres vermelden. Ontbreekt die informatie, dan wordt **de bedenktijd met een jaar verlengd** en draag jij de retourkosten ([ACM bedenktijd](https://www.acm.nl/nl/verkoop-aan-consumenten/klantenservice/bedenktijd)). De herroepingsknop moet tijdens de hele bedenktijd vindbaar zijn, zonder verplicht account, en moet een bevestiging met datum en tijdstip geven (zelfde bron). Ook een levertijd moet kloppen: bij dropshipping moeten de reële levertijd en het land van verzending duidelijk zijn. De ACM trad daarop op tegen Grandado ([ACM Grandado](https://www.acm.nl/nl/publicaties/webwinkel-grandadocom-informeert-consumenten-beter-over-levertijd-na-optreden-acm)). Dat de boetes niet theoretisch zijn, laat de boete van €500.000 aan T.O.M. voor schending van de terugbetaalregels zien ([ACM boetebesluit](https://www.acm.nl/sites/default/files/old_publication/publicaties/16371_boetebesluit-webwinkel-tom-new.pdf)).

De demobeloftes zijn het grootste vertrouwensprobleem, groter dan het ontbreken van een keurmerk. Een klant kan zich beroepen op de ruimste belofte die je toont, zoals 100 dagen retour of levenslange garantie. Zo'n belofte kan ook gelden als misleidende handelspraktijk. Ze staan op elke productpagina naast je eigen regel "Retourneren kan binnen de wettelijke termijn" ([Rock](https://www.in-huys.nl/products/eetkamerstoel-rock-set-van-2)). Eén ding staat los van de inhoud: de dropshipping via Orderchamp verschuift de verantwoordelijkheid niet. Tegenover de consument blijft InHuys aanspreekpunt voor levertijd, schade, retour en garantie. Orderchamp hanteert voor de retailer een meldtermijn van 4 werkdagen voor schade ([Orderchamp help](https://orderchamp.zendesk.com/hc/en-150/articles/360019677797-How-do-I-report-damaged-or-missing-products), alleen via een zoekresultaat gezien). Dat is veel korter dan de rechten van de klant, en dat gat draag jij.

## Navigatie en productpagina's remmen de verkoop

### Structuur en conversie: toets

| Onderdeel | Oordeel | Bewijs |
|---|---|---|
| Categorienavigatie | ontbreekt | het menu heeft alleen Assortiment, Bestsellers, Inspiratie en Interieuradvies; 49 van de 77 producten zitten in geen enkele collectie; de homepage linkt naar 0 producten ([collections.json](https://www.in-huys.nl/collections.json?limit=250), [homepage](https://www.in-huys.nl/)) |
| Zoeken en filters | goed | `/search?q=stoel` geeft 45 resultaten, met filters op type, merk, prijs en voorraad ([zoeken](https://www.in-huys.nl/search?q=stoel), [collections/all](https://www.in-huys.nl/collections/all)) |
| Basis van de productpagina | goed | 3 tot 8 beelden, breadcrumb, sticky koopknop, eigen Nederlandse tekst en een AI-kamerpreview |
| Prijs per set of per stuk | onvoldoende | binnen één "set van 2" kost Rock Beige €479,80 en de andere kleuren €279,95; bij Avena is het €439,80 tegenover €249,95 ([Rock .js](https://www.in-huys.nl/products/eetkamerstoel-rock-set-van-2.js), [Avena .js](https://www.in-huys.nl/products/eetkamerstoel-avena-set-van-2.js)) |
| Variantnamen en variantbeelden | onvoldoende | machinevertalingen als "room", "Bruinen" en "Omber"; alleen Ballenbak koppelt een foto aan elke kleur ([Scandi .js](https://www.in-huys.nl/products/scandi-stoel-tan-set-van-2.js)) |
| Uitverkochte producten | onvoldoende | 9 actieve producten met voorraad 0 (export 19 november), met daarbij een leverdatum ([Cloud crème](https://www.in-huys.nl/products/cloud-stoel-creme-set-van-2)); het faseplan telt er 13 ([fase-4.md](/home/user/Inhuys/plannen/fase-4.md)) |
| Flitsadvies | onvoldoende | product van €0,00 met een accessoiretekst en de SEO-titel "Flitsadvies luxe accessoire"; geen productpagina linkt ernaar ([flitsadvies](https://www.in-huys.nl/products/flitsadvies)) |
| Winkelwagen | onvoldoende | geen verzendkosten of levertijd vooraf, en "Save" is vertaald als "Redden" |

Volgens Baymard **haakt 40% van de kopers af op te hoge extra kosten**. Daarna volgen trage levering (20%), wantrouwen bij het invullen van betaalgegevens (19%), een zwak retourbeleid (13%) en totale kosten die vooraf onzichtbaar zijn (12%) ([Baymard, cart abandonment](https://baymard.com/lists/cart-abandonment-rate)). Een bank van €2.740 zonder vermelde bezorgkosten, levertijd of retourvoorwaarden raakt alle vijf. Het prijsverschil binnen een set wijst waarschijnlijk op een verdubbelde stukprijs: de bedragen op ,80 zijn precies twee keer een bedrag op ,90. Dat is een afleiding en niet gecontroleerd in Orderchamp. Voor de bezoeker oogt een kleur die 70 tot 80% duurder is als een fout. Baymard stelt vast dat **81% van de winkels geen prijs per eenheid toont** bij producten die in wisselende hoeveelheden worden verkocht ([Baymard, product page UX](https://baymard.com/blog/current-state-ecommerce-product-page-ux)). "€279,95 per set van 2, €139,98 per stoel" lost dat op.

### Wat de werkversie oplost en wat nog open staat

De thema-kopie 210233098579 lost veel op ([07-thema-werkversie.md](/home/user/Inhuys/analyse/07-thema-werkversie.md), [theme_build.py](/home/user/Inhuys/tools/theme_build.py)):

- een nieuw hoofdmenu met een collectiemenu van negen categorieën en negen categorietegels op de homepage;
- Nederlandse labels;
- weg zijn "$75", "Open Doors To A World Of Fashion", "Why Minimog" en het nep-voorraadtal;
- een specificatietabel uit metavelden;
- het blok "Advies van InHuys" en een verwijzing naar Flitsadvies op elke productpagina;
- een footer met "InHuys is een handelsnaam van Kluster", KvK, btw en betaaliconen;
- een Nederlandse cookiebanner, een viewport zonder zoomblokkade en een nieuwsbrief zonder kortingsbelofte.

Wat nog open staat, valt in twee groepen. Een paar fouten moeten weg vóór publicatie, anders verslechtert de site:

- de ongeldige breadcrumb-JSON in `snippets/inhuys-schema.liquid`. Het filter `| json` escapet de hele opgebouwde string in plaats van alleen de titel. De oplossing is eerst `assign t = product.title | json` en daarna `| append: t` ([preview collectie](https://www.in-huys.nl/collections/cloud?preview_theme_id=210233098579));
- de dubbele WebSite-markup;
- de merkenslider met twee 404-links;
- de vaste leverdatum van 14 dagen, die het faseplan zelf tegenspreekt;
- demoresten die het bouwscript niet raakt: de zoeksuggesties "T-Shirt, Blue Jacket", de leeftijdscheck en "Redden";
- de projectenplaatshouders op de homepage;
- de FAQ-zin "in originele staat". Die mag geen voorwaarde voor herroeping zijn, want de klant mag het product beoordelen.

De andere groep zijn je eigen besluiten, en die lost geen thema op: beleidspagina's, prijzen per set, variantnamen, uitverkochte producten en redirects. Let op: de preview is technisch beoordeeld, maar niet visueel en niet op mobiel. Een anonieme bezoeker kreeg in één meting het live thema te zien.

## Op prijs verlies je van Giga Meubel; op advies niet

### Markt en positionering: toets

| Onderdeel | Oordeel | Bewijs |
|---|---|---|
| Prijs tegenover dezelfde modellen | onvoldoende | Luna Mink set van 2 kost €419,80 bij InHuys tegenover 2 × €169,90 = €339,80 bij Giga Meubel ([Giga Luna Mink](https://www.gigameubel.nl/pole-to-pole-eetkamerstoel-luna-mink)); Cloud-barkruk €299,90 tegenover €259,90 ([Giga Cloud barkruk](https://www.gigameubel.nl/pole-to-pole-barkruk-cloud-karamel)) |
| Jupiduu | onvoldoende | het merk verkoopt zelf in euro's aan Nederland; Jumpspot Indoor kost daar €239,90 en bij InHuys €269,90 ([Jupiduu products](https://jupiduu.com/products.json?limit=250), [InHuys products](https://www.in-huys.nl/products.json?limit=250)) |
| Basisbeloftes van de markt | ontbreekt | fonQ: gratis verzending vanaf €50 en achteraf betalen ([fonQ](https://www.fonq.nl/zoeken/?q=pole+to+pole)); Giga: 8,6/10 uit 2.653 reviews, betalen in 3 termijnen, showroom van 4.500 m² ([Giga Meubel](https://www.gigameubel.nl/catalogsearch/result/?q=pole+to+pole)) |
| Zichtbaarheid in Google | ontbreekt | buiten de merknaam vrijwel geen vertoningen; Luna Mink stond wel op positie 4 bij 7 vertoningen ([05-seo-strategie.md](/home/user/Inhuys/analyse/05-seo-strategie.md)) |
| Onderscheidend vermogen | goed in aanleg, onbenut | Flitsadvies, 3D-ontwerp en de showroom in Purmerend; Giga noemt interieuradvies alleen in de footer en biedt geen montage ([Giga Bezorging](https://www.gigameubel.nl/bezorging)) |

Giga Meubel voert vrijwel dezelfde Pole To Pole-modellen: Luna, Rock, Egg, Cloud, Edo, High Five, Breeze, Storm, Pebble en de banken Amsterdam en New York. Op identieke modellen zit InHuys in de normale periode **15 tot 25% hoger**, en tijdens acties 30 tot 40%. Giga belooft ook te leveren binnen twee weken ([Giga Levertijden](https://www.gigameubel.nl/levertijden)). Wie zoekt op "Pole to Pole Luna", vergelijkt prijs en kiest Giga. Daarom is verkeer op merk- en modelnaam weinig waard. De prijsvechters in de zoekresultaten op bouclé-stoelen (Sklum, Beliani, vidaXL) bieden sets van 2 voor €130 tot €270 ([Sklum](https://www.sklum.com/nl/kopen-pack-2-stoelen/133679-set-van-2-eetkamerstoelen-and.html)). In Home & Living kocht 17% van de Nederlanders in 2025 in het buitenland, tegenover 8% in 2021 ([Thuiswinkel Markt Monitor 2025](https://www.betaalvereniging.nl/en/news/more-online-product-purchases-less-spending-on-travel-and-events-in-2025/)). Daarmee neemt de prijsdruk eerder toe dan af.

De positie die je wel kunt verdedigen, is advies bij de aankoop. Elders kost online interieuradvies €100 tot €150 per ruimte ([Homedeal](https://www.homedeal.nl/architect/interieuradvies-kosten/)). Een gratis Flitsadvies onderscheidt je daarvan en sluit aan op het enige zoekwoord met volume. Table du Sud laat in Nederland zien dat een eigen collectie samen met stylisten en een gratis afspraak werkt ([Table du Sud](https://tabledusud.nl/stoelen/eetkamerstoelen/luna)). Concreet betekent dat drie dingen. Leg de nadruk op modellen die Giga niet of minder voert: de banken Londen en New York-lounge, Japandi, Osaka, Fuji, Avena en decoratie. Zet op elke productpagina een vraag als "Twijfel je over kleur of maat? Plan een gratis Flitsadvies". Gebruik Jupiduu alleen binnen advies voor de kinderkamer, niet als prijsaanbod. Over de kanalen: Google Shopping vangt koopintentie, en daar weegt de kwaliteit van de productfeed in 2026 zwaarder dan het bod ([Trendtrack](https://www.trendtrack.io/nl/blog-post/10-beste-marketingkanalen-voor-e-commerce-in-2026)). Pinterest is het natuurlijke kanaal voor interieurinspiratie, maar het gebruik in Nederland groeit niet duidelijk. Bronnen spreken elkaar daar tegen ([NL Times](https://nltimes.nl/node/78791), [Metricool](https://metricool.com/nl/meest-gebruikte-social-media-nederland/)).

## Het verbeterplan: drie fasen in deze volgorde

De volgorde volgt het risico. Fase A haalt eerst weg wat juridisch of voor vertrouwen schade doet, omdat elke bezoeker die je nu binnenhaalt die beloftes leest. Fase B maakt de werkversie publicatieklaar en voert fase 4 uit. Pas in fase C komt er geld en content voor groei. De inspanning is een inschatting: klein betekent minder dan een uur, middel een halve tot een hele dag, groot meerdere dagen. "Agent" betekent werk dat binnen de werkafspraken in [CLAUDE.md](/home/user/Inhuys/CLAUDE.md) zonder go-live kan, zoals de thema-kopie, concepten, teksten en metingen. "Eigenaar" betekent dat het live gaat of dat het om prijs, juridische of bedrijfsgegevens gaat.

### Fase A · nu, vóór elke advertentie-euro (week 48 en 49)

| # | Wat | Waarom | Wie | Inspanning |
|---|---|---|---|---|
| A1 | Demobeloftes van de live productpagina's en homepage halen: "100 Days Return", "Lifetime Warranty", "30-day guarantee", "$75", "Estimated Delivery", "100 in voorraad", de leeftijdscheck, "10% off" en "Fashion". Dat kan in de thema-editor van het live thema door blokken uit te zetten, als noodstap tot de werkversie live staat. | onware toezeggingen waar een klant zich op kan beroepen; ACM handhaaft op levertijdbeloftes | eigenaar (live thema); agent levert de lijst met blokken | klein |
| A2 | Beleid invullen in Shopify: herroeping en retour (14 dagen na levering, modelformulier, Nederlands retouradres, retourkosten per soort pakket en meubel, terugbetaling binnen 14 dagen), verzending (kosten, zones, levertijd per merk), algemene voorwaarden en wettelijke garantie | 404 nu; zonder deze informatie geldt een jaar extra bedenktijd ([ACM bedenktijd](https://www.acm.nl/nl/verkoop-aan-consumenten/klantenservice/bedenktijd)); Merchant Center vraagt erom | agent schrijft het concept; eigenaar beslist over bedragen en adres en zet het live | middel |
| A3 | Herroepingsknop: app of eigen pagina met formulier, gelinkt in de footer en in de orderbevestiging | wettelijk verplicht sinds juni 2026 | eigenaar kiest de app; agent bereidt pagina en tekst voor | middel |
| A4 | Bedrijfsgegevens zichtbaar maken: footerlink naar contactgegevens en de beleidspagina's, met "InHuys is een handelsnaam van Kluster" | wettelijk vereist vóór de koop; nu niet gelinkt | eigenaar (live menu); in de werkversie al opgelost | klein |
| A5 | Verzendlanden beperken tot Nederland (en België als de merken daar leveren) | 41 landen zijn onleverbaar en brengen btw- en consumentenrecht van andere landen mee | eigenaar | klein |
| A6 | Cookies en privacy: Engelse themabanner uit, alleen de Shopify-banner met toestemming voor de EU; privacybeleid aanvullen met Kluster, verwerkers, Pinterest, de foto-upload van de AI-preview, bewaartermijnen en het klachtrecht bij de AP | weigeren moet even makkelijk zijn als accepteren ([Consumentenbond](https://www.consumentenbond.nl/internet-privacy/bijna-4-op-de-10-cookiebanners-niet-in-de-haak)) | agent schrijft het concept; eigenaar zet het live | middel |
| A7 | Betaalmethoden controleren: iDEAL aan, Klarna overwegen | iDEAL heeft zo'n 70% van de Nederlandse online betalingen ([Betaalvereniging](https://www.betaalvereniging.nl/en/knowledge-base/online-payments/online-payment-methods/)) | eigenaar | klein |
| A8 | Flitsadvies-product: eigen diensttekst (wat je krijgt, duur, online of showroom, knop naar het formulier) of de URL doorsturen naar `/pages/interieuradvies` | nu een product van €0 met een accessoiretekst; bestellingen van €0 zonder afspraak zijn mogelijk | eigenaar opent `live_tekst` of besluit over de redirect; agent schrijft | klein |
| A9 | Nulmeting en meetfout herstellen: indexering via het Pagina's-rapport en de URL-inspectie, sessies, conversie en orders sinds 19 november uit Shopify Analytics | het doel heeft een echt startpunt nodig; "0 geïndexeerd" is een vervallen veld | agent (`/meting`) | klein |

### Fase B · de werkversie publicatieklaar maken en fase 4 uitvoeren (week 49 tot 51)

| # | Wat | Waarom | Wie | Inspanning |
|---|---|---|---|---|
| B1 | De breadcrumb-JSON in `inhuys-schema.liquid` repareren via `tools/theme_build.py`, en ook de templates `page` en `article` nakijken | ongeldige JSON-LD gooit LocalBusiness, WebSite en Breadcrumb op product- en collectiepagina's weg | agent (`/thema`) | klein |
| B2 | Eén WebSite- en Organization-blok overhouden; `sameAs` leeg laten tot er echte profielen zijn | dubbele markup en lege koppelingen | agent | klein |
| B3 | Merkenslider met mooisa en jesper-home verwijderen | 30 kapotte interne links | agent | klein |
| B4 | Leverdatumblok uit, of laten sturen door een metaveld `inhuys.levertijd` per merk | vaste 14 dagen is een onbevestigde belofte en botst met het faseplan | agent, na besluit B van de eigenaar | klein |
| B5 | Demoresten weg: zoeksuggesties, leeftijdscheck, "Redden", "Recently Viewed"; projectenplaatshouders verbergen | het bouwscript raakt ze niet ([theme_build.py](/home/user/Inhuys/tools/theme_build.py)) | agent | klein |
| B6 | FAQ- en retourtekst gelijktrekken met het beleid uit A2, zonder "in originele staat" | een tegenstrijdige of ongeldige voorwaarde | agent | klein |
| B7 | H1 op `/pages/interieuradvies`, nieuwe titel en omschrijving voor de homepage, `noindex` op cart en search | het enige zoekwoord met volume; de huidige titel is te dun | agent | klein |
| B8 | Collecties corrigeren: kettingen in Decoratie, Fauteuils op type, Maatwerk niet publiceren ([14-collecties-controle.md](/home/user/Inhuys/analyse/14-collecties-controle.md)) | 49 producten zonder collectie; dunne pagina's | agent (`collectionUpdate`) | klein |
| B9 | Preview op telefoon en desktop bekijken, `/controle thema` draaien, PageSpeed meten met een API-sleutel | de preview is niet visueel getoetst; het PSI-quotum was op | agent en eigenaar samen | middel |
| B10 | Fase 4, stap 1 tot 5: collecties, pagina's en artikelen publiceren; nieuwe handles met 301's, ook voor `boogstoel-karamel`, `marmer-waxinelichthouder`, `travertine-agano-vaas`, `wolkenbar-stoel-karamel` en `luna-stoel-caramel`; doelen die concept blijven verwijzen naar de collectie; daarna de thema-kopie publiceren ([fase-4.md](/home/user/Inhuys/plannen/fase-4.md)) | navigatie, vertrouwen en het behoud van eerder geïndexeerde URL's | eigenaar (`INHUYS_GOLIVE=1`); agent bereidt voor en maakt momentopnames | groot |
| B11 | Oude dubbele productversies weg uit de live catalogus (via de Orderchamp-app) en besluit over uitverkochte producten | dubbele pagina's remmen de indexering | eigenaar | middel |
| B12 | Na publicatie: sitemap opnieuw indienen, indexering aanvragen voor home, interieuradvies, inspiratie, de vijf belangrijkste collecties en de tien belangrijkste producten | Googles eigen advies voor nieuwe sites | eigenaar in Search Console | klein |

### Fase C · groei (vanaf half december, daarna doorlopend)

| # | Wat | Waarom | Wie | Inspanning |
|---|---|---|---|---|
| C1 | Google Bedrijfsprofiel voor de showroom in Purmerend, en reviews vragen na elk advies en elke bestelling | lokale diensttermen worden nu gedomineerd door Trustoo en Homedeal ([05-seo-strategie.md](/home/user/Inhuys/analyse/05-seo-strategie.md)) | eigenaar | middel |
| C2 | Reviewsysteem of goedkoop keurmerk (WebwinkelKeur of Kiyoh); Thuiswinkel Waarborg pas bij hogere omzet, het eerste jaar €75 + €390 + €518 ([Thuiswinkel.org](https://www.thuiswinkel.org/en/become-a-member/what-does-membership-of-thuiswinkel-org-cost/)) | Giga toont 2.653 reviews; een onbekende winkel heeft sociaal bewijs nodig | eigenaar | middel |
| C3 | Productmarkup uitbreiden: `gtin13` als de SKU's EAN's blijken te zijn, plus `shippingDetails` en `hasMerchantReturnPolicy` | voorwaarde voor merchant listings en Shopping | agent (thema-kopie) | klein tot middel |
| C4 | Merchant Center met gratis listings, daarna €300 per maand Shopping, alleen op producten waar InHuys niet duurder is dan Giga of die Giga niet voert | koopintentie; de feedkwaliteit telt meer dan het bod | eigenaar (budget, account); agent (feed, selectie) | middel |
| C5 | Twee artikelen per maand en dienstpagina's op "online interieuradvies", "gratis interieuradvies", Purmerend en long-tail productvragen | organische opbouw duurt 3 tot 6 maanden ([Shopify](https://shopify.com/blog/how-long-does-seo-take)), dus nu beginnen | agent (`/tekst`) | middel, doorlopend |
| C6 | Variantnamen opschonen ("Crème", "Bruin", optienaam "Kleur") en een foto per kleur koppelen | vertrouwen en minder verwarring; varianten en beelden zijn van Orderchamp (regel 7) | eigenaar in de Orderchamp-app | middel |
| C7 | Uitverkochte producten: melding bij nieuwe voorraad en een link naar een leverbaar alternatief | Breeze heeft de meeste vertoningen; een doodlopende pagina verspilt ze | agent (thema), eigenaar (app) | klein |
| C8 | Pinterest organisch met rich pins en sfeerbeelden, Instagram als portfolio, en een nieuwsbrief met een gratis Flitsadvies als welkomstvoordeel in plaats van korting | goedkoop zichtbaar worden zonder prijsstrijd | eigenaar, agent schrijft | middel |
| C9 | Analyse-loop inschakelen na vier weken data | sturen op de tussendoelen hieronder | agent, met akkoord van de eigenaar | klein |

## Het doel: 25 bestellingen en €6.500 omzet tot eind februari

Het hoofddoel voor 1 december 2026 tot en met 28 februari 2027 is **25 bestellingen en €6.500 omzet**. Daarbij gelden drie randvoorwaarden: in februari 80 geïndexeerde URL's, 1.300 sessies en een conversie van 0,9%. De advertentie-uitgaven blijven onder de €900. Dit is een ronde, iets voorzichtiger versie van het realistische scenario in de notities, dat op 28 bestellingen en €7.300 uitkwam. Alle getallen in de scenario's zijn eigen rekensommen op externe ankers, geen metingen. De scenario's verschillen vooral in advertentiebudget en in hoe snel fase A en B klaar zijn.

### Maandelijkse tussendoelen per scenario

| Maand | Scenario | Geïndexeerde URL's (eind maand) | Sessies (waarvan betaald) | Conversie | Bestellingen | Omzet |
|---|---|---|---|---|---|---|
| december | conservatief | 20 | 150 (0) | 0,5% | 1 | €250 |
| januari | conservatief | 35 | 250 (0) | 0,5% | 1 à 2 | €375 |
| februari | conservatief | 50 | 350 (0) | 0,5% | 2 | €475 |
| **3 maanden** | **conservatief** | | **750** | | **4 à 6** | **€1.000 à €1.500** |
| december | **hoofdscenario** | 35 | 800 (500) | 0,6% | 5 | €1.300 |
| januari | **hoofdscenario** | 60 | 1.000 (500) | 0,8% | 8 | €2.100 |
| februari | **hoofdscenario** | 80 | 1.300 (500) | 0,9% | 12 | €3.100 |
| **3 maanden** | **hoofdscenario** | | **3.100** | | **25** | **€6.500** |
| december | ambitieus | 50 | 2.400 (1.800) | 0,9% | 22 | €6.000 |
| januari | ambitieus | 75 | 2.800 (1.800) | 1,1% | 30 | €8.500 |
| februari | ambitieus | 90 | 3.400 (1.800) | 1,1% | 38 | €10.500 |
| **3 maanden** | **ambitieus** | | **8.600** | | **90** | **€25.000** |

### Aannames achter de getallen

**Conversie.** Home & furniture converteert op 1,2 tot 1,6% van de sessies. De Shopify-mediaan ligt rond 1,4% ([Shopify](https://www.shopify.com/blog/ecommerce-conversion-rate), [Flatline Agency](https://www.flatlineagency.com/blog/furniture-ecommerce-conversion-levers/)), de top 20% op 2,7 tot 3,2% ([Growthsuite](https://www.growthsuite.net/resources/shopify-conversion-rate/complete-guide/benchmarks-by-industry)). Een winkel van een paar maanden oud, zonder reviews en met een prijsnadeel op overlappende modellen, start daaronder. Daarom loopt het hoofdscenario op van 0,6 naar 0,9%. Ook het ambitieuze scenario blijft met 1,1% onder de branchemediaan.

**Orderwaarde.** De gemiddelde orderwaarde is €260. Die volgt uit het assortiment: de mediane instapprijs is €279,90 en 38 van de 77 producten kosten €200 tot €500. Banken van €2.700 en meer zijn uitschieters en tellen niet mee in het hoofdscenario ([varianten-2026-11-19b.json](/home/user/Inhuys/data/orderchamp/varianten-2026-11-19b.json)).

**Betaald verkeer.** €300 per maand aan Google Shopping bij een klikprijs van €0,60 geeft 500 betaalde sessies. De klikprijs is een aanname. De ankers zijn Meta NL met €0,58 ([Searchlab](https://searchlab.nl/statistieken/facebook-ads-statistieken-2026)) en een band van $0,70 tot $1,40 voor home/furniture ([CorePPC](https://coreppc-website.pages.dev/blog/ecommerce-advertising-benchmarks-2026/), toeschrijving onzeker). Googles zoekadvertenties voor furniture kosten in de VS $3,97 per klik ([WordStream 2026](https://www.wordstream.com/blog/2026-google-ads-benchmarks)). Om die reden is Shopping gekozen en niet Search.

**Organisch verkeer.** Een nieuwe site krijgt pas na 3 tot 6 maanden merkbaar organisch verkeer ([Neil Patel](https://neilpatel.com/marketing-stats/average-seo-traffic-growth-over-time/), [Search Engine Journal](https://www.searchenginejournal.com/case-study-long-take-see-organic-search-results/91241/)). Organisch is daarom tot februari vooral een opbouwdoel.

**Indexering.** Het startpunt is onbekend. De tussendoelen zijn een eigen inschatting op een basis van rond de 100 URL's. Ze bouwen voort op het praktijkverslag van 0 naar 72 geïndexeerde pagina's in twee maanden ([DEV Community](https://dev.to/serhii_kalyna_730b636889c/from-0-to-72-indexed-pages-in-2-months-what-google-actually-does-with-new-sites-3kca)) en gaan ervan uit dat de dubbelen uit de sitemap verdwijnen.

**Seizoen.** December draait om cadeaus. Decoratie en Jupiduu passen daarbij, meubels met een lange levertijd niet, tenzij die levertijd vóór kerst klopt. In januari gingen webwinkels in 2025 met 7,9% vooruit, maar meubelwinkels met 0,5% achteruit ([CBS](https://www.cbs.nl/nl-nl/nieuws/2025/10/detailhandel-zet-bijna-4-procent-meer-om-in-januari)). Februari is rustig.

**Voorwaarde.** Het hoofdscenario gaat ervan uit dat fase A uiterlijk 7 december klaar is, zodat de advertenties in december kunnen starten. Schuift dat naar half december, reken dan voor december op de helft.

### Wat het oplevert, en wanneer advertenties zich terugbetalen

Je inkoopmarge is onbekend, en die is doorslaggevend. Bij een brutomarge van 35%, €900 aan advertenties en €237 aan Orderchamp-abonnement (als de €948 per jaar uit een gebruikersreview klopt, [Shopify App Store](https://apps.shopify.com/orderchamp)) blijft er in het hoofdscenario €1.140 bijdrage over. Bij 25% marge is dat €490. Het break-evenpunt voor advertenties ligt bij een ROAS van 1 ÷ marge, dus 2,9 bij 35%. De benchmark voor home/furniture ligt op 2 tot 4 ([CorePPC](https://coreppc-website.pages.dev/blog/ecommerce-advertising-benchmarks-2026/)). Europese klikprijzen stegen in een jaar met 15% ([ChannelX](https://channelx.world/2026/07/cost-of-clicks-rises-15-year-over-year-and-roas-drops-46/)). Shopping betaalt zich dus alleen terug als de feed goed is en je niet adverteert op modellen waar Giga goedkoper is. Als stuurregel stel ik voor: zakt de ROAS eind januari onder de 2,9 bij minstens 800 betaalde klikken, pauzeer dan de advertenties en verbeter eerst de productpagina's. Die regel is een eigen voorstel, geen benchmark.

### Hoe het wordt gemeten

De keten loopt in deze volgorde:

1. geïndexeerde URL's (Search Console, Pagina's-rapport en URL-inspectie, niet het sitemapveld "indexed");
2. organische vertoningen en klikken (Search Console);
3. sessies per kanaal (Shopify Analytics);
4. toevoegingen aan de winkelwagen (als anker: furniture in België zit op 9,5 tot 10%, [ECDB](https://ecdb.com/resources/sample-data/market/be/furniture));
5. conversie;
6. bestellingen en gemiddelde orderwaarde;
7. omzet, advertentiekosten en ROAS (Merchant Center en Google Ads).

Als eigen leidende maat komt daar het aantal aangevraagde Flitsadviezen bij. Een benchmark daarvoor bestaat niet. Meet het vanaf de nulmeting en stel er na januari een doel op. De agent meet elke twee weken via `/meting`, met ijkmomenten op 31 december, 31 januari en 28 februari. De nulmeting (sessies, conversie en orders sinds 19 november) moet eerst bevestigen dat de startwaarden in de tabel kloppen. Ligt de omzet onder het conservatieve scenario, dan is er waarschijnlijk een technisch probleem met indexering, checkout of feed, en geen marktprobleem.

## De beslissingen die bij jou liggen

| Beslissing | Opties | Advies | Waarom het ertoe doet |
|---|---|---|---|
| Prijzen tegenover Giga Meubel | prijspariteit op overlappende modellen; meerwaarde tonen (gratis Flitsadvies, gratis bezorging boven een drempel); accepteren en inzetten op modellen die Giga niet voert | geen algemene prijsverlaging zolang de marge onbekend is; haal eerst de inkoopprijzen uit Orderchamp; adverteer alleen op modellen zonder prijsnadeel | 15 tot 25% duurder op identieke modellen ([Giga Rock](https://www.gigameubel.nl/pole-to-pole-eetkamerstoel-rock-karamel)) |
| Prijs per set of per stuk | setprijs met stukprijs ernaast; alles per stuk | toon "per set van 2" met de stukprijs erbij; zet de Fuji en andere losse stoelen expliciet op "per stuk"; controleer de prijzen op ,80 in Orderchamp | 16 producten hebben een variant die meer dan anderhalf keer zo duur is als de goedkoopste ([products.json](https://www.in-huys.nl/products.json?limit=250)) |
| Levertijd | vaste regel; leeg; levertijd per merk na schriftelijke bevestiging | vraag Pole To Pole en Jupiduu om een schriftelijke levertijd; toon tot dan geen datum maar "levertijd op aanvraag" | een onjuiste leverdatum is een handhavingspunt voor de ACM; Giga belooft 2 weken |
| Garantie | alleen wettelijk; extra commerciële garantie | noem de wettelijke garantie met InHuys als aanspreekpunt; geef geen extra garantie die de merken niet dekken | "Lifetime Warranty" staat nu live |
| Retourbeleid | wie betaalt; retouradres Purmerend of het merk; ophalen bij meubels | stel een vast bedrag per soort vast (pakket en meubel), vraag de klant schade binnen 48 uur met foto's te melden zonder zijn rechten te beperken, en leg de retourstroom vast met Orderchamp | de meldtermijn van Orderchamp is 4 werkdagen; de ACM eist dat de kosten vooraf bekend zijn |
| Verzendkosten en drempel | gratis vanaf een drempel; vaste tarieven | publiceer de tarieven; vergelijk met fonQ (gratis vanaf €50) en Giga (meubelbezorging €50, gratis vanaf €1.500, [Giga Bezorging](https://www.gigameubel.nl/bezorging)) | extra kosten zijn de nummer-1-reden om af te haken (40%) |
| Advertentiebudget | €0, €300 of €1.000 per maand | €300 per maand Shopping zodra fase A klaar is; opschalen pas bij een ROAS boven break-even | bepaalt het scenario |
| Uitverkochte live producten | actief laten met alternatief; naar concept | Breeze actief laten met een alternatief en een melding bij voorraad; de rest naar concept | vertoningen tegenover doodlopende pagina's |
| Dubbelen en redirects | nu; bij de go-live van fase 4 | bij de go-live, met `INHUYS_GOLIVE=1`, inclusief de 4 eerder geïndexeerde URL's die nu een 404 geven | zonder 301 verdwijnt het opgebouwde signaal |
| Flitsadvies-pagina | diensttekst op het product; doorsturen | doorsturen naar `/pages/interieuradvies` of het product opnemen in `live_tekst` | de belangrijkste conversiehefboom staat nu als accessoire van €0 online |
| Keurmerk | WebwinkelKeur of Kiyoh; Thuiswinkel Waarborg | eerst een goedkoop keurmerk met reviews, nadat de voorwaarden live staan | vertrouwen tegenover Giga en fonQ |
| Verzendlanden en betaalmethoden | 41 landen; alleen NL (en BE) | alleen NL, en BE na bevestiging; iDEAL aan, Klarna overwegen bij orders boven €200 | onleverbare orders en btw-plichten |
| Akkoord op fase 4 | per stap met `INHUYS_GOLIVE=1` of guard-openingen | per stap, met momentopnames, na B1 tot B9 | het faseplan wacht op jouw akkoord ([fase-4.md](/home/user/Inhuys/plannen/fase-4.md)) |

## Wat niet geverifieerd is

Een deel van het bewijs is zwakker dan de rest, en dat moet je weten voordat je erop beslist.

**Benchmarks uit zoeksamenvattingen.** Alle externe cijfers over conversie, klikprijzen, ROAS en orderwaarde komen uit samenvattingen van zoekresultaten. Het ophalen van de volledige pagina's werd geblokkeerd voor wordstream.com, shopify.com, cbs.nl en orderchamp.zendesk.com. Bij de CorePPC- en Foundry-cijfers is ook onduidelijk van wie ze zijn. De kolommen van Copyfy (marge 30 tot 50%, ROAS 3 tot 4) zijn een vermoeden.

**Orderchamp.** Het abonnement van €948 per jaar komt uit één gebruikersreview. De voorwaarden voor dropshipping (retour, schade, levertijd) gaven 403. De meldtermijn van 4 werkdagen is alleen via een zoekresultaat gezien.

**Regels voor cookies.** De eisen van de AP zijn via secundaire bronnen weergegeven, omdat de AP-pagina's 403 gaven.

**Herroepingsknop.** De ACM noemt op twee pagina's twee ingangsdata: 19 juni en 25 juni 2026. Beide liggen in het verleden.

**Concurrentie.** Dat Giga Meubel per stuk prijst, is afgeleid uit de producttitels. De prijzen van Huismerken en Vergelijk.nl komen uit zoekfragmenten. Home24, Lumz, Kwantum en Bol.com konden niet worden opgehaald.

**Marktcijfers.** Het cijfer van +24% voor Home & Living in het eerste kwartaal van 2026 komt uit een fragment en is daarom niet in dit rapport gebruikt. De tarieven van WebwinkelKeur en Kiyoh zijn niet geverifieerd. Absolute zoekvolumes ontbreken, omdat Keyword Planner niet beschikbaar was.

**Technische controles.** Googles Rich Results Test is niet gedraaid; de JSON is met een parser getoetst. Er is geen actuele PageSpeed-meting. De checkout is niet geopend, dus de betaalmethoden, verzendtarieven en het vuren van de Pinterest-pixel vóór toestemming zijn niet vastgesteld. De preview is niet visueel en niet op mobiel beoordeeld.

**Eigen gegevens.** Of de 12-cijferige SKU's EAN-nummers zijn, is onbekend. De voorraad komt uit de export van 19 november. Shopify Analytics is niet uitgelezen, dus sessies en conversie sinds de livegang ontbreken. Zonder deze nulmeting zijn de startwaarden van alle scenario's aannames.

## Conclusie

Het beeld kantelt op één punt. De vermeende indexeringscrisis van "0 van 57" bleek een vervallen API-veld. Het echte risico zit niet bij Google maar bij de klant en de ACM: wie vandaag een bank koopt, krijgt beloftes die je niet kunt nakomen, en heeft een jaar extra om te herroepen. Dat verandert de volgorde. Zet geen advertentie-euro in en publiceer geen werkversie voordat de beloftes kloppen, het beleid er staat en de structured data weer geldig is. Groei zonder die basis vergroot alleen de schade.

Het tweede inzicht gaat over het verdienmodel. Met dezelfde Pole To Pole-modellen als een grotere en goedkopere dealer is InHuys als webwinkel alleen niet onderscheidend. Het doel van 25 bestellingen is haalbaar, maar de interessantere maat voor februari is hoeveel Flitsadviezen er tot een aankoop leiden. Daar ligt de marge die Giga niet kan bieden. Je inkoopmarge bepaalt of betaald verkeer daarna kan opschalen of dat organisch werk en advies de motor blijven.
