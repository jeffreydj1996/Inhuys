# Benchmarks voor een 3-maandendoel InHuys (december 2026 – februari 2027)

Werkwijze en beperking: onderzoek op 23 november 2026. WebFetch was in deze sessie geblokkeerd voor alle geprobeerde hosts (wordstream.com, shopify.com, cbs.nl, orderchamp.zendesk.com). Alle externe cijfers hieronder komen daarom uit zoekresultaat-samenvattingen en zijn niet tegen de volledige bronpagina gecontroleerd. Wie de cijfers hard wil maken, moet die hosts toestaan en de pagina's openen. Eigen data komt uit de repository (alleen gelezen).

## Uitgangssituatie InHuys (repository-data)

### Takeaway
InHuys start vrijwel vanaf nul: 0 van 57 sitemap-URL's geïndexeerd, 1 klik per 28 dagen, en de vertoningen komen bijna allemaal van één dienstpagina, niet van producten. Het assortiment heeft een mediane instapprijs rond €280, dus de orderwaarde ligt ruim boven het e-commercegemiddelde.

### Cited Findings
- GSC 19-11-2026 (periode 20-10 t/m 16-11): 1 klik, 1.007 vertoningen (was 60), 24 zoekopdrachten, 25 pagina's met vertoning; sitemap: web 57 ingediend / 0 geïndexeerd, image 32 / 0 — [analyse/gsc-rapport-2026-11-19.md](/home/user/Inhuys/analyse/gsc-rapport-2026-11-19.md)
- 998 van de 1.007 vertoningen gaan naar `/pages/interieuradvies` op gemiddelde positie 82,7; zoekterm "interieuradvies" 727 vertoningen op positie 93,4 (vorige meting 80,2). Producttermen (eetkamerstoel boucle, travertin vaas, bank met ottoman) hebben 0 vertoningen — [analyse/gsc-rapport-2026-11-19.md](/home/user/Inhuys/analyse/gsc-rapport-2026-11-19.md)
- Merkzoekterm "in-huys" positie 2,5; "in huys" zakte van 4,4 naar 11,6 — [analyse/gsc-rapport-2026-11-19.md](/home/user/Inhuys/analyse/gsc-rapport-2026-11-19.md)
- Meting 26-10-2026: 1 klik, 60 vertoningen, sitemap ook toen 0 geïndexeerd — [analyse/gsc-rapport-2026-10-26.md](/home/user/Inhuys/analyse/gsc-rapport-2026-10-26.md)
- Assortiment (eigen berekening uit varianten-2026-11-19b.json, laagste variantprijs per actief product): 77 actieve producten; Pole To Pole 62 (mediaan €279,95, bereik €23,95 – €5.740, 54 met voorraad), Jupiduu 14 (mediaan €274,90, bereik €69,90 – €799,90, alle 14 met voorraad), 1 InHuys-dienst (prijs €0, Flitsadvies). Over alles: mediaan €279,90, gemiddelde €687 (scheef door banken) — [data/orderchamp/varianten-2026-11-19b.json](/home/user/Inhuys/data/orderchamp/varianten-2026-11-19b.json), [data/orderchamp/voorraad-2026-11-19b.csv](/home/user/Inhuys/data/orderchamp/voorraad-2026-11-19b.csv)
- Prijsverdeling (instapprijs): <€50: 11 · €50–100: 8 · €100–200: 6 · €200–500: 38 · €500–1.000: 3 · €1.000–3.000: 5 · €3.000–10.000: 6 — zelfde bron.

### Inferences
- Zonder indexatie is organisch verkeer in december praktisch nul; de eerste mijlpaal is dus indexatie, niet omzet.
- De zwaartepunt-prijsklasse €200–500 (38 producten, vooral stoelsets) bepaalt de realistische orderwaarde; banken van €2.700–5.700 zijn uitschieters die een maand kunnen maken maar niet in een basisscenario horen.

### Gaps
- Geen Shopify Analytics-cijfers (sessies, conversie, orders) in deze notities opgevraagd; die zijn nodig om de nulmeting vast te leggen.

## Conversieratio en gemiddelde orderwaarde (home/furniture, Shopify, NL/EU)

### Takeaway
Home & furniture converteert op 1,2–1,6% van de sessies; de Shopify-mediaan ligt rond 1,4% en de top 20% op 2,7–3,2%. Een nieuwe winkel zonder reviews en merkbekendheid zit daar in de eerste maanden meestal onder; reken met 0,5–1,0%.

### Cited Findings
- Shopify noemt voor Home and furniture een conversieratio van 1,41% (recente periode, niet gedateerd in snippet) — [Shopify blog](https://www.shopify.com/blog/ecommerce-conversion-rate)
- Nudgenow-tabel: Home and Furniture 1,22% (september 2025) — [Nudgenow](https://www.nudgenow.com/blogs/e-commerce-conversion-rates-benchmark)
- Meerdere 2025–2026 analyses zetten furniture & home op 1,2–1,6%, betaald verkeer hoger door koopintentie; ≥2% geldt als sterk — [Flatline Agency](https://www.flatlineagency.com/blog/furniture-ecommerce-conversion-levers/), [VividWorks](https://www.vividworks.com/blog/furniture-ecommerce-conversion-rate)
- Uitschieter: InMotion Hosting noemt 7,1% voor furniture zonder methode; onbetrouwbaar — [InMotion](https://inmotionhosting.com/blog/ecommerce-conversion-rates-by-industry)
- Littledata (2023, 2.800 Shopify-winkels): gemiddeld 1,4%; top 20% 3,2%, top 10% 4,7% — [Red Stag Fulfillment](https://redstagfulfillment.com/average-conversion-rate-for-shopify-stores/), [Growthsuite](https://www.growthsuite.net/resources/shopify-conversion-rate/complete-guide/benchmarks-by-industry)
- Nieuwere Littledata-benchmark (426 winkels, 90 dagen tot begin oktober 2026): mediaan 1,4%, top 20% 2,7%, top 10% >3,5%; een andere vermelding (juli–oktober 2026) mediaan 1,50%, top 10% 4,00%. Alleen via secundaire sites gezien — [Thunderbit](https://thunderbit.com/blog/shopify-conversion-rate-statistics), [Growthsuite](https://www.growthsuite.net/resources/shopify-conversion-rate/complete-guide/benchmarks-by-industry)
- ECDB 2025, furniture e-commerce België: add-to-cart 9,5–10,0%, winkelwagenverlating 82,5–83,0%; VK add-to-cart 10,5–11,0% — [ECDB België](https://ecdb.com/resources/sample-data/market/be/furniture)
- WordStream 2025 Google Ads-tabel: Furniture conversieratio 2,99% (op klikken uit Search-advertenties, niet op alle sessies) — [WordStream 2025](https://wordstream.com/blog/2025-google-ads-benchmarks)
- Orderwaarde: Triple Whale schat de wereldwijde AOV 2025 op $150–180; Shopify BFCM 2025 gemiddelde winkelwagen $114,70 — [Triple Whale](https://www.triplewhale.com/blog/ecommerce-benchmarks.md), [Red Stag/Thunderbit samenvatting](https://thunderbit.com/blog/shopify-conversion-rate-statistics)
- Specifieke furniture-AOV voor Europa/NL niet gevonden: ECDB-landpagina's noemen de metric maar tonen de waarde niet; Statista heeft een kwartaalreeks wereldwijd (Q1 2023 – Q1 2025) achter betaalmuur — [ECDB NL](https://ecdb.com/resources/sample-data/market/nl/furniture), [Statista](https://statista.com/topics/9979/furniture-e-commerce)

### Inferences
- Duurdere artikelen (banken €2.700+) converteren lager dan decoratie; benchmarks voor high-ticket meubels zijn niet hard gevonden, maar de lagere home & furniture-ratio (1,2–1,6% vs. hogere ratio's in voeding/beauty) wijst al op dat effect.
- Realistische AOV InHuys: €220–320 (stoelsets en kinderproducten domineren; decoratie trekt omlaag; af en toe een bank trekt fors omhoog). Dat is 1,5–2x het algemene e-commerce-AOV.
- Voor een nieuwe winkel: maand 1 conversie 0,3–0,6%, oplopend naar 0,8–1,2% als reviews, levertijden en vertrouwen (Thuiswinkel Waarborg, retourbeleid) op orde zijn. Dit is een inschatting, geen bron.

### Gaps
- Geen NL-specifieke conversiebenchmark voor woonwebshops gevonden (Thuiswinkel publiceert dat niet openbaar).
- Geen benchmark voor conversie van nieuwe (<6 maanden) Shopify-winkels specifiek.

## Indexatie en organische groei van een nieuwe Shopify-winkel

### Takeaway
Er is geen rigoureus onderzoek; praktijkdata wijst op 3–6 maanden voordat een nieuwe site merkbaar organisch verkeer krijgt. Voor InHuys betekent dat: organisch draagt in december–februari weinig bij en is vooral een opbouwdoel (indexatie, posities), geen omzetdoel.

### Cited Findings
- Neil Patel (42.391 SEO-actieve sites): +11,4% verkeersgroei in maand 0–6, +9,5% in maand 7–12 (relatieve groei, geen absolute aantallen voor een nieuw domein) — [Neil Patel](https://neilpatel.com/marketing-stats/average-seo-traffic-growth-over-time/)
- Casus: nieuw subdomein kreeg pas na 5 maanden zoekverkeer van betekenis — [Search Engine Journal](https://www.searchenginejournal.com/case-study-long-take-see-organic-search-results/91241/)
- Praktijkverslag "van 0 naar 72 geïndexeerde pagina's in 2 maanden" voor een nieuwe site — [DEV Community](https://dev.to/serhii_kalyna_730b636889c/from-0-to-72-indexed-pages-in-2-months-what-google-actually-does-with-new-sites-3kca)
- Forums en gidsen noemen 3–6 maanden (soms 6–9) voor consistent verkeer; het "sandbox"-begrip is nooit door Google bevestigd — [Wisp](https://www.wisp.blog/blog/the-google-sandbox-effect-why-your-search-traffic-drops-after-3-6-months), [Shopify: how long does SEO take](https://shopify.com/blog/how-long-does-seo-take)

### Inferences
- 0/57 geïndexeerd na ruim twee maanden in GSC terwijl pagina's wél vertoningen krijgen, wijst eerder op een rapportagevertraging of een technische kwestie (canonicals, sitemap van wachtwoord-/concepttijd, of URL's die in de sitemap staan maar niet in de index) dan op normale traagheid. De URL-inspectie in GSC per sleutelpagina geeft uitsluitsel. Dit is een hypothese.
- Redelijke indexatiemijlpalen: eind december ≥20 van 57 URL's, eind januari ≥40, eind februari ≥50 (eigen inschatting op basis van het DEV-verslag; geen benchmark).
- Organische sessies (alleen Google) als inschatting: december 20–80, januari 50–200, februari 100–400. Merkverkeer en direct verkeer komen daarbovenop.

### Gaps
- Geen NL-data over hoe snel nieuwe Shopify-winkels indexeren; geen Shopify-specifieke studie.

## Betaalde kanalen: CPC, CPM, ROAS en benodigd budget

### Takeaway
Furniture-klikken zijn in Google Search duur (VS: $3,97 CPC in 2026), Shopping en Meta zijn goedkoper (Meta NL: CPC €0,58, CPM €8,45). Benchmark-ROAS voor home/furniture ligt rond 2–4x; met een brutomarge van 30–40% is dat rond het break-evenpunt. Betaald verkeer is in deze periode vooral een leer- en vulbudget, geen winstmotor.

### Cited Findings
- WordStream 2026 Google Ads-benchmarks: Furniture CPC $3,97; Home & Home Improvement $8,33 (VS, LocaliQ-data) — [WordStream 2026](https://www.wordstream.com/blog/2026-google-ads-benchmarks)
- WordStream 2025: Furniture conversieratio 2,99%, kosten per lead $106,70 — [WordStream 2025](https://wordstream.com/blog/2025-google-ads-benchmarks)
- LocaliQ 2025 (16.446 campagnes): gemiddelde CPC $5,26 (+12,88% j-o-j), conversie 7,52% (alle branches, vooral leadgen) — [Search Engine Land](https://searchengineland.com/google-ads-costs-keep-rising-but-conversion-rates-improved-in-2025-451167)
- TwoMinuteReports: Home, Furniture & Interior Design CPC $1,38, mediane CPA $59,07 (hoogste CPA van alle branches) — [TwoMinuteReports](https://twominutereports.com/google-ads-benchmarks)
- E-commercegids (bron in snippet niet eenduidig; vermoedelijk een 2026-benchmarkartikel): Home/Furniture non-branded Google Ads CPC $0,70–1,40, CPA $45–90, ROAS 2x–4x — [CorePPC](https://coreppc-website.pages.dev/blog/ecommerce-advertising-benchmarks-2026/) / [Foundry CRO](https://foundrycro.com/blog/google-shopping-benchmarks-by-category-2026/) (toeschrijving onzeker)
- NL dropshippinggids noemt voor Meubels (hoge AOV) "30–50% | 3–4x" (kolommen vermoedelijk marge en ROAS; niet bevestigd) — [Copyfy](https://www.copyfy.io/nl/blog/wat-is-roas)
- Europese e-commerce: CPC in Google Ads +15% jaar-op-jaar, ROAS -46% (juli 2026) — [ChannelX](https://channelx.world/2026/07/cost-of-clicks-rises-15-year-over-year-and-roas-drops-46/)
- Meta Nederland: gemiddelde CPC €0,58, CPM €8,45, CPM +14% t.o.v. 2024 — [Searchlab](https://searchlab.nl/statistieken/facebook-ads-statistieken-2026)
- SuperAds: NL-CPM over alle branches 31% onder wereldwijd (14,2 vs 20,6); NL textiel-CPM 9,98 (okt 2024 – okt 2025) — [SuperAds NL CPM](https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/netherlands), [SuperAds textiel](https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/textiles/netherlands)
- Madgicx: Home Goods & Furnishings heeft de laagste mediane kosten per linkklik van alle branches (wereldwijd) — [Madgicx](https://madgicx.com/research/meta-ads-benchmarks)
- Channable en Smarter Ecommerce bieden EU-benchmarktools voor Shopping per categorie (cijfers niet uitgelezen) — [Channable](https://www.channable.com/google-ads-performance-benchmark), [smec Q4 2025](https://smarter-ecommerce.com/en/smec-market-observer/reports/Q4_2025/)

### Inferences
- Budgetformule: orders uit betaald = budget ÷ CPC × conversie. Voorbeeld Google Shopping: €300 ÷ €0,60 = 500 klikken × 1,0% = 5 orders × €275 = €1.375 omzet (ROAS 4,6). Bij 0,6% conversie: 3 orders, €825 (ROAS 2,75). De CPC van €0,60 voor NL-Shopping op "eetkamerstoelen" is een aanname (Meta NL €0,58 en de $0,70–1,40-band als ankers), niet gemeten.
- Break-even: maximale CPA = AOV × brutomarge. Bij AOV €275 en 35% marge: €96 per order; break-even ROAS = 1 ÷ 0,35 = 2,9. De benchmark-CPA $45–90 en ROAS 2–4x liggen daar net onder en boven: winstgevend alleen bij goede productfeed en conversie.
- Meta en Pinterest passen beter bij decoratie en kinderproducten (visueel, impulsiever, €25–120 en €70–800) dan bij banken; Google Shopping past bij stoelsets met concrete zoekvraag.
- Een nieuw account zonder conversiehistorie heeft 2–4 weken leerfase; reken in december met slechtere ROAS dan in februari.

### Gaps
- Geen NL-CPC voor "eetkamerstoelen" of Shopping-meubels gevonden; Google Keyword Planner in het eigen Ads-account geeft dat direct.
- Geen Pinterest-advertentiebenchmarks voor NL gevonden.

## Seizoen in NL: december – februari

### Takeaway
November (Black Friday/Cyber week) en de aanloop naar Sinterklaas/kerst zijn de online piek; januari is de maand van uitverkoop en kortingen, met online groei maar een zwakke maand voor meubelwinkels; februari is de laagste periode voor kortingsactiviteit. Er is geen harde NL-bron voor een januaripiek in online meubelverkoop.

### Cited Findings
- CBS januari 2025: omzet webwinkels +7,9% j-o-j; meubel- en woninginrichtingswinkels -0,5% — [CBS](https://www.cbs.nl/nl-nl/nieuws/2025/10/detailhandel-zet-bijna-4-procent-meer-om-in-januari)
- CBS januari 2026: online detailhandelsomzet +3,6% j-o-j; geen aparte meubelcijfer — [CBS](https://www.cbs.nl/en-gb/news/2026/10/retail-turnover-up-by-over-2-percent-in-january)
- Thuiswinkel Markt Monitor: NL online bestedingen 2025 €35,7 mld (-1% t.o.v. 2024), 347 mln aankopen (gelijk); productaankopen +2%, diensten krimpen — [Betaalvereniging](https://www.betaalvereniging.nl/en/news/more-online-product-purchases-less-spending-on-travel-and-events-in-2025/), [NielsenIQ NL](https://nielseniq.com/global/nl/news-center/2026/meer-online-productaankopen-minder-uitgaven-aan-reizen-en-evenementen-in-2025/)
- Thuiswinkel Markt Monitor Q1 2026: online bestedingen €9 mld in het kwartaal, geen uitsplitsing wonen in de snippet — [TMM Q1 2026 NL (pdf)](https://www.betaalvereniging.nl/wp-content/uploads/2026/06/TMM-Q1-2026-NL.pdf)
- INretail Branchevisie 2025 Wonen: 2024 "geen jubeljaar" voor de woonbranche — [INretail](https://inretail.nl/wp-content/uploads/2025/01/Branchevisie_2025_Wonen.pdf)
- Internationaal: clearance-prijzen pieken januari–februari en augustus–september; kortingscodes concentreren in november–december, dieptepunt februari–april (analyse 633 meubelretailers) — [SimplyCodes](https://simplycodes.com/blog/best-time-to-buy-furniture-2026)
- E-commercegidsen noemen een daling van de verkoop in januari na de Black Friday-piek — [Furniture News](https://furniturenews.net/resources/preparing-for-the-new-year-sale-online)

### Inferences
- December: cadeau-gedreven; decoratie (€25–120) en Jupiduu-kinderproducten (Sinterklaas is al 5 december voorbij, kerst telt) passen; meubels met lange levertijd verkopen slecht als ze niet vóór kerst leverbaar zijn. Levertijd duidelijk tonen.
- Januari: consumenten zoeken korting; InHuys mag prijzen niet zelf verlagen (CLAUDE.md regel 2), dus geen sale-strategie zonder besluit eigenaar. Verkeer kan wel stijgen (inrichtingsvoornemens), conversie lager.
- Februari: rustig, maar organisch verkeer is dan het verst opgebouwd; netto vergelijkbaar met januari.

### Gaps
- Geen maandreeks CBS online meubels/woninginrichting uitgelezen (cbs.nl niet bereikbaar). Google Trends voor "eetkamerstoelen"/"bank kopen" NL niet opgevraagd.

## Marges bij dropshipping via Orderchamp

### Takeaway
Er zijn geen openbare cijfers over de verhouding groothandelsprijs/adviesprijs bij Orderchamp, Pole To Pole of Jupiduu. Kosten aan de retailerkant bestaan uit een abonnement plus een verwerkingsfee. Voor de scenario's wordt met 25/35/45% brutomarge gerekend; de echte inkoopprijzen staan in het Orderchamp-dashboard van de eigenaar.

### Cited Findings
- Orderchamp: model met maandabonnement plus commissie op verzonden orders, commissie daalt met jaaromzet (GMV); alleen gerekend op orders die verzenden (beschrijft het marktplaatskanaal) — [Orderchamp helpcenter](https://orderchamp.zendesk.com/hc/en-150/articles/360016984018-Understanding-the-Commission-Model-on-Orderchamp)
- Gebruikersreview Shopify App Store (Duits): Starter-plan €948 per jaar plus 2,75% verwerkingsfee per order; reviews over dropshipping gemengd (sep. 2025 negatief) — [Shopify App Store Orderchamp](https://apps.shopify.com/orderchamp), [reviews](https://apps.shopify.com/reviews/1983149)
- Orderchamp betaalde in 2021 bij Black Friday mee aan kortingen om retailermarge te compenseren (oud, indicatief) — [Emerce](https://www.emerce.nl/wire/inkoopplatform-orderchamp-geeft-retailers-black-friday-marges-terug)
- ACM: leverancier mag een niet-bindende adviesprijs geven, retailer bepaalt de verkoopprijs — [ACM](https://www.acm.nl/nl/node/24306)
- Algemene dropshippingvuistregel: productkosten onder 40% van de verkoopprijs houden — [ShipStation](https://www.shipstation.com/blog/dropship-pricing-strategy/)
- Repository: geen inkoop- of margedata aanwezig; Pole To Pole beschreven als "groothandel met dropshipping; levertijd kan per item verschillen" — [analyse/01-productoverzicht.md](/home/user/Inhuys/analyse/01-productoverzicht.md)

### Inferences
- Vaste kosten Orderchamp (als €948/jaar klopt) zijn €79 per maand; over drie maanden €237. In het conservatieve scenario vreet dat een groot deel van de brutomarge op.
- Bij 2,75% fee, Shopify Payments-kosten en verzend-/dropshipfee blijft van een ruwe marge van 40–50% (bij retail ≈ 2x inkoop) netto 30–40% over. Dit is een rekenaanname, geen bron.

### Gaps
- Echte inkoopprijzen Pole To Pole / Jupiduu en de actuele Orderchamp-dropshipfee: eigenaar moet die uit het Orderchamp-account halen (zie ook analyse/10-orderchamp-koppeling.md).

## Drie scenario's (december 2026 – februari 2027)

### Takeaway
Conservatief (geen advertentiebudget): 4–6 orders, €1.000–1.500 omzet in drie maanden. Realistisch (€300/maand Google Shopping + organische opbouw): 25–28 orders, €6.500–7.400. Ambitieus (€1.000/maand advertenties + content + e-mail): 85–95 orders, €25.000 (rekenkundig plafond €31.600). Omzet onder conservatief betekent dat er een technisch probleem is (indexatie, checkout, feed).

### Cited Findings
- Conversie-ankers: home & furniture 1,2–1,6%; Shopify-mediaan 1,4%; top 20% 2,7–3,2% — zie sectie Conversieratio ([Shopify](https://www.shopify.com/blog/ecommerce-conversion-rate), [Growthsuite](https://www.growthsuite.net/resources/shopify-conversion-rate/complete-guide/benchmarks-by-industry))
- Kosten-ankers: Meta NL CPC €0,58 ([Searchlab](https://searchlab.nl/statistieken/facebook-ads-statistieken-2026)); home/furniture CPC $0,70–1,40, ROAS 2–4x ([CorePPC](https://coreppc-website.pages.dev/blog/ecommerce-advertising-benchmarks-2026/), toeschrijving onzeker); Furniture Search CPC $3,97 ([WordStream 2026](https://www.wordstream.com/blog/2026-google-ads-benchmarks))
- Organische ramp-up 3–6 maanden — [Neil Patel](https://neilpatel.com/marketing-stats/average-seo-traffic-growth-over-time/)

### Inferences

Aannames per scenario (alle getallen hieronder zijn eigen rekensommen op basis van de bovenstaande ankers):

| Aanname | Conservatief | Realistisch | Ambitieus |
|---|---|---|---|
| Advertentiebudget/maand | €0 | €300 (Google Shopping, stoelsets + kinderproducten) | €1.000 (€600 Shopping, €400 Meta/Pinterest) |
| CPC-aanname | – | €0,60 | €0,55 gemengd |
| Organisch + direct + merk + social, sessies dec/jan/feb | 150 / 250 / 350 | 300 / 500 / 800 | 600 / 1.000 / 1.600 |
| Conversie (alle sessies) | 0,5% | 0,8% (dec) → 1,0% (feb) | 1,0% (dec) → 1,4% (feb) |
| AOV | €250 | €260 | €300 (incl. af en toe een bank) |
| Geïndexeerde URL's eind dec/jan/feb | 10 / 25 / 40 | 20 / 40 / 50 | 40 / 55 / 57+ (plus nieuwe collectie-/artikelpagina's) |
| Overige inzet | alleen huidige SEO-werk | GSC-indexatie per URL, Merchant Center-feed, 2 artikelen/maand | idem + e-mailcapture, 4 artikelen/maand, Pinterest-pins, reviews-app |

Maandmijlpalen:

| Maand | Scenario | Sessies | Orders | Omzet |
|---|---|---|---|---|
| Dec | Conservatief | 150 | 1 | €250 |
| Jan | Conservatief | 250 | 1–2 | €375 |
| Feb | Conservatief | 350 | 2 | €440 – 500 |
| **3 mnd** | **Conservatief** | **750** | **4–6** | **€1.000 – 1.500** |
| Dec | Realistisch | 300 + 500 betaald = 800 | 6 | €1.650 |
| Jan | Realistisch | 500 + 500 = 1.000 | 9 | €2.350 |
| Feb | Realistisch | 800 + 500 = 1.300 | 13 | €3.400 |
| **3 mnd** | **Realistisch** | **3.100** | **28** | **€7.300** |
| Dec | Ambitieus | 600 + 1.800 = 2.400 | 24 | €7.200 |
| Jan | Ambitieus | 1.000 + 1.800 = 2.800 | 34 | €10.100 |
| Feb | Ambitieus | 1.600 + 1.800 = 3.400 | 48 | €14.300 |
| **3 mnd** | **Ambitieus** | **8.600** | **106** | **€31.600** |

Correctie op de ambitieuze rij: conversie 1,4% in februari ligt op de branchemediaan; voor een winkel van vier maanden oud is dat hoog. Met 1,0–1,2% vlak wordt het ambitieuze scenario 85–95 orders en €25.000–28.000. Advies: hanteer €25.000 als ambitieus plafond. Het conservatieve scenario is bij 0,5% conversie rekenkundig 4 orders (€940); met de Jupiduu-cadeauvraag in december is 4–6 orders (€1.000–1.500) de ondergrens.

Brutomarge (aanname 25/35/45%, zie sectie Marges) en advertentie-uitgaven:

| Scenario | Omzet 3 mnd | Brutomarge bij 35% | Advertenties 3 mnd | Orderchamp-abonnement 3 mnd (als €948/jaar klopt) | Contributie na ads en abonnement |
|---|---|---|---|---|---|
| Conservatief | €1.500 | €525 | €0 | €237 | €290 |
| Realistisch | €7.300 | €2.550 | €900 | €237 | €1.415 |
| Ambitieus | €25.000 | €8.750 | €3.000 | €237 | €5.500 |

- Bij 25% marge wordt het realistische scenario €1.825 bruto − €1.137 = €690 contributie; bij 45% €3.285 − €1.137 = €2.150. De margevraag is dus doorslaggevend voor of betaald verkeer de moeite loont.
- Betaalde ROAS in het realistische scenario: betaalde sessies 1.500 × 0,9% = 13–14 orders × €260 = €3.500 op €900 = ROAS 3,9; aan de bovenkant van de 2–4x-benchmark, dus kwetsbaar.
- Stuurgetallen per maand (in volgorde van de keten): geïndexeerde URL's (GSC) → organische klikken (GSC) → sessies (Shopify) → add-to-cart-ratio (ECDB-anker 9,5–11%) → conversie → orders → AOV → omzet → brutomarge.
- Doel dat ik zou voorstellen als "realistisch" kopdoel: eind februari 50 URL's geïndexeerd, 1.300 sessies in februari, 25 orders en €6.500 omzet over drie maanden, met maximaal €900 advertentie-uitgaven. Prijzen, budget en kortingen vallen onder besluit van de eigenaar (CLAUDE.md).

### Gaps
- Alle scenario-getallen zijn afgeleid, niet gemeten; nulmeting uit Shopify Analytics (sessies, add-to-cart, conversie sinds livegang 19-11-2026) moet de startwaarden bevestigen.
- NL-CPC's en echte inkoopmarges ontbreken; beide kunnen de scenario's met een factor 2 verschuiven.
