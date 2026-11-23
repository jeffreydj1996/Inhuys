# Structuur en conversie van www.in-huys.nl: live site tegenover de voorbereide versie (stand 23 november 2026)

Methode: live fetches op 23 november 2026 met `curl -A "Mozilla/5.0 …"` van de homepage, `/products.json`, `/collections.json`, `/collections/<handle>/products.json` (alle 15 gepubliceerde collecties), `/collections/all`, `/search?q=stoel`, `/pages/interieuradvies`, `/pages/inspiratie`, `/products/flitsadvies`, twee policy-URL's en tien productpagina's (HTML en `.js`). Ruwe bestanden staan in de scratchpad van deze sessie (niet in de repo). Live thema volgens de paginabron: `minimog-5-7-0 Met foto upload mogelijkheden`, id 200751743315, rol main. Niets gewijzigd in Shopify, geen bestelling geplaatst.

Belangrijke beperking: de preview `https://www.in-huys.nl/?preview_theme_id=210233098579` levert voor een anonieme bezoeker het live thema (de `Shopify.theme`-regel in de bron noemt id 200751743315, rol main). De nieuwe versie is daarom beoordeeld op de documenten en op de bouwscript-bron `tools/theme_build.py`, niet visueel.

## 1. Live site: homepage, hoofdmenu en collecties. Vindt een bezoeker alle 77 actieve producten?

### Takeaway
Alle 77 producten zijn alleen vindbaar via "Assortiment" (`/collections/all`, drie pagina's van 32 met filters) en via zoeken. Er is geen categorienavigatie. De 15 gepubliceerde collecties zijn modelcollecties (Amsterdam, Cloud, Luna enz.) die niet in het menu staan. 49 van de 77 producten zitten in geen enkele collectie, en nog eens 7 alleen in Bestsellers. De homepage toont geen enkel product en bevat nog Engelse demotekst van het Minimog-thema.

### Cited Findings
- `/products.json` geeft 77 producten: 62 van Pole To Pole, 14 van Jupiduu en 1 van InHuys (Flitsadvies). Producttypes: Stoelen 31, Kinderkamer 14, Decoratie 13, Banken 7, Tafels 4, Vazen 3, Barstoel 3, Fauteuils 1, Accessoires 1. — [live products.json](https://www.in-huys.nl/products.json?limit=250)
- `/collections.json` toont 15 gepubliceerde collecties, allemaal model- of hulpcollecties: adviezen 1, amsterdam 9, bestsellers 36, boog ("Bow") 3, breeze 5, cloud 11, edo 2, eier ("Egg") 4, frontpage 1, kathmandu 5, luna 5, panda 8, rainbow 4, rocking ("rocking") 6, whale 5. Er is geen collectie voor Banken, Stoelen, Tafels, Kinderkamer of Decoratie. — [live collections.json](https://www.in-huys.nl/collections.json?limit=250)
- Kruising van alle collectie-productlijsten met de 77 producten: 56 producten zitten in geen modelcollectie. Daarvan staan er 7 alleen in Bestsellers (Nox umber, ronde eettafel Urban Chique, eettafel Ellipse, eettafel Urban Chique, Bank New York, Fauteuil Cairo, Klimkoepel Climb & Jump). De andere 49 staan in geen enkele collectie. Het gaat onder meer om alle 9 kettingen (7 schelpkettingen, 2 octo-kettingen), alle 3 vazen (Bubble, Meduse, Swoop), beide lantaarns, Babi, Pearl, 13 eetkamerstoelen (Fjord, Wing, Storm, Pebble, High Five, Wave, Mera ×2, Fuji, Osaka, Avena, Sake, Japandi, Scandi), 5 banken (Londen ×3, New York lounge ×2), salontafel Craft, barkruk Japandi en 12 van de 14 Jupiduu-kinderproducten. — [collectie-JSON per handle](https://www.in-huys.nl/collections/cloud/products.json), [products.json](https://www.in-huys.nl/products.json?limit=250)
- Het hoofdmenu bestaat uit vier punten: Assortiment (`/collections/all`), Bestsellers, Inspiratie en Interieuradvies. De homepage linkt naar 0 productpagina's. De enige collectielinks zijn `/collections/all` en `/collections/bestsellers`. — [homepage](https://www.in-huys.nl/)
- Engelse demotekst en plaatshouders op de live homepage: topbalk "Open Doors To A World Of Fashion | Discover More", blokken "Every Home Has Its Own Needs", "Design That Fits" en "Let's get in touch", nieuwsbrief "Sign up for our newsletter and receive 10% off your first order", footerkoppen "Quick link", "Company" en "Our store", zoeklade "populaire zoekopdrachten: T-Shirt Blue Jacket", "New Arrivals Shop Now", Engelse cookiebanner ("Allow cookies") en in de HTML de opmaak van een leeftijdscontrole "Confirm your age / Are you 18 years old or older?". — [homepage](https://www.in-huys.nl/)
- Het introductieblok spreekt de bezoeker met "u" aan ("Mijn doel is om het voor u zo makkelijk mogelijk te maken"), terwijl een ander blok "jou" gebruikt. — [homepage](https://www.in-huys.nl/)
- De winkelwagenlade vertaalt "Save" als "Redden". — [homepage](https://www.in-huys.nl/)
- `/collections/all` heeft filters op producttype, merk, prijs en beschikbaarheid ("Op voorraad (69)", "Niet op voorraad (23)") en sortering. Er zijn 3 pagina's met 32 producten per pagina. — [collections/all](https://www.in-huys.nl/collections/all)
- `/search?q=stoel` vindt 45 resultaten met filters op producttype, merk en prijs. Zoeken werkt dus. — [zoeken](https://www.in-huys.nl/search?q=stoel)
- `/pages/inspiratie` bevat geen links naar artikelen of producten. — [inspiratie](https://www.in-huys.nl/pages/inspiratie)
- Het interne collectieonderzoek bevestigt dat de 9 kettingen in geen concept-collectie vallen omdat `collections.py` ze bewust weglaat. Flitsadvies valt bedoeld in geen categoriecollectie. — [/home/user/Inhuys/analyse/14-collecties-controle.md](/home/user/Inhuys/analyse/14-collecties-controle.md)

### Inferences
- Wie wil bladeren per soort (bank, eettafel, kinderkamer) moet nu via "Assortiment" filteren op producttype. De homepage biedt geen instap per categorie. Voor een interieurwinkel met 77 producten is dat de grootste vindbaarheidsrem.
- De modelcollecties zijn wel geïndexeerd, maar onzichtbaar in de navigatie. Namen als "Bow", "Egg" en "rocking" ogen onaf.
- De Engelse demotekst ("Fashion", "T-Shirt Blue Jacket", "10% off", "Confirm your age") ondermijnt vertrouwen meer dan elk ontbrekend element. Hij staat op elke pagina, omdat de header, de zoeklade en de footer overal meekomen.

### Gaps
- Of de leeftijdscontrole echt verschijnt, hangt af van JavaScript of een instelling. De markup staat in de HTML (13 vermeldingen `age-verifier`), maar of hij actief is, kon ik zonder browser niet vaststellen.
- De volgorde van producten in `/collections/all` (staan uitverkochte producten achteraan?) is niet beoordeeld.

## 2. Productpagina's (10 live producten bekeken)

Bekeken: eetkamerstoel-rock-set-van-2, bank-new-york, eetkamerstoel-fuji, vaas-bubble, klimkoepel-climb-jump, scandi-stoel-tan-set-van-2, ballenbak, eetkamerstoel-avena-set-van-2, breeze-stoel-beige-set-van-2 en cloud-stoel-creme-set-van-2.

### Takeaway
De basis is in orde: alle tien laden met 3 tot 8 beelden, een breadcrumb, Product-JSON-LD, een sticky winkelwagenknop, een blok met aanbevelingen en een eigen Nederlandse tekst. Toch staan er bij de koopknop meerdere onjuiste of tegenstrijdige beloftes uit het Minimog-demothema: "$75", "100 Days Return", "Lifetime Warranty", "30-day satisfaction guarantee", een Engelse "Estimated Delivery" en "100 in voorraad". Daarnaast is bij sets onduidelijk wat de prijs dekt: binnen één "set van 2" kost de ene kleur bijna het dubbele van de andere. Varianten hebben machinevertaalde kleurnamen, en de foto wisselt niet mee met de kleurkeuze.

### Cited Findings
- **Demobeloftes bij de koopknop (live, op elke productpagina):** "Estimated Delivery: Nov 28 - Dec 02", "Free Shipping & Returns: On all orders over $75", een blok "Why Minimog? 100 Days Return … Lifetime Warranty …" en "backed by our 30-day satisfaction guarantee". Daarnaast staat de eigen tekst "Retourneren kan binnen de wettelijke termijn (uitgezonderd maatwerk)" en "Levertijd kan per variant verschillen". — [Rock](https://www.in-huys.nl/products/eetkamerstoel-rock-set-van-2), [Ballenbak](https://www.in-huys.nl/products/ballenbak), [Bank New York](https://www.in-huys.nl/products/bank-new-york)
- **Voorraadweergave:** Rock toont "100 in voorraad". In de Orderchamp-export van 19 november heeft Rock 500 stuks over 5 varianten, 100 per variant. — [Rock](https://www.in-huys.nl/products/eetkamerstoel-rock-set-van-2), [/home/user/Inhuys/data/orderchamp/voorraad-2026-11-19b.csv](/home/user/Inhuys/data/orderchamp/voorraad-2026-11-19b.csv)
- **Prijs per set tegenover per stuk (variantprijzen uit `/products/<handle>.js`):**
  - Rock, set van 2: Karamel, Bruin, Taupe en "room" €279,95; Beige €479,80. — [Rock .js](https://www.in-huys.nl/products/eetkamerstoel-rock-set-van-2.js)
  - Avena, set van 2: "room" €439,80; Karamel en "Nerts" €249,95. — [Avena .js](https://www.in-huys.nl/products/eetkamerstoel-avena-set-van-2.js)
  - Scandi, set van 2: Oatly, Omber en Okura €219,95; "Bruinen" €379,80. — [Scandi .js](https://www.in-huys.nl/products/scandi-stoel-tan-set-van-2.js)
  - Breeze, set van 2: Beige €599,80; Pastelroze €349,95. — [Breeze .js](https://www.in-huys.nl/products/breeze-stoel-beige-set-van-2.js)
  - Bank New York: Kokos €2.989,95; Beige €2.740,00. — [Bank New York .js](https://www.in-huys.nl/products/bank-new-york.js)
  - Fuji heeft geen "set" in de titel ("Fuji eetkamerstoel met armleuningen") en kost €249,95 per variant, zonder vermelding of dat per stuk of per set is. — [Fuji .js](https://www.in-huys.nl/products/eetkamerstoel-fuji.js)
  - Over alle 77 producten heeft 16 producten een variant die meer dan 1,5 keer zo duur is als de goedkoopste, onder meer EDO, Egg, Rainbow, Nox, Mera, Luna, Boog, Whale, Japandi-barkruk, Lantaarn Raffles en Zwembad. — [products.json](https://www.in-huys.nl/products.json?limit=250)
- **Variantnamen:** "room" (crème), "Bruinen" (werkwoord), "Kokos", "Nerts", "Omber", "Oatly", "Okura", hoofdletters door elkaar ("OLIJF", "BLAUW", "roos", "KAMEEL", "beige"). Rock heeft als optienaam het Engelse "color". — [Rock .js](https://www.in-huys.nl/products/eetkamerstoel-rock-set-van-2.js), [Ballenbak .js](https://www.in-huys.nl/products/ballenbak.js), [Fuji .js](https://www.in-huys.nl/products/eetkamerstoel-fuji.js)
- **Beelden:** het aantal beelden per product is 3 (Bubble, Cloud crème), 4 (Breeze, Klimkoepel), 5 (Bank New York, Avena, Fuji, Scandi), 6 (Rock) of 8 (Ballenbak). Alleen Ballenbak koppelt een beeld aan elke variant (5 van 5). Bij alle andere is `featured_image` per variant leeg, zodat de foto niet mee wisselt met de kleurkeuze. — de tien `.js`-bestanden, bijvoorbeeld [Bank New York .js](https://www.in-huys.nl/products/bank-new-york.js)
- **Koopknop en extra's:** de knop heet "Voeg toe aan winkelkar". Er is een AI-kamerpreview "Bekijk dit product in jouw kamer" met foto-upload en de waarschuwing dat het een AI-visualisatie is. De pagina laat ophaalbeschikbaarheid zien met de foutmelding "Kan de beschikbaarheid voor ophalen niet laden". — [Rock](https://www.in-huys.nl/products/eetkamerstoel-rock-set-van-2)
- **Cross-sell:** er is een sectie `product-recommendations` en een sectie "Recently Viewed Products" (Engels). De inhoud wordt met JavaScript geladen en is niet beoordeeld. — [Rock](https://www.in-huys.nl/products/eetkamerstoel-rock-set-van-2)
- **Doorverwijzing naar advies:** geen van de tien pagina's linkt in de inhoud naar Flitsadvies (0 links naar `/products/flitsadvies`). De 5 links naar `/pages/interieuradvies` per pagina zijn menulinks. — de tien productpagina's
- **Een paar productpagina's bevatten nog de oude Orderchamp-tekst.** Breeze heeft een blok "Specificaties Merk: Pole To Pole Levering: verzonden via een zorgvuldig geselecteerde partner … InHuys selectie :" naast de nieuwe sectie "Levering & retour". — [Breeze](https://www.in-huys.nl/products/breeze-stoel-beige-set-van-2)
- **Benchmarks:**
  - Baymard: 48% van de grote desktopwinkels en 38% van de mobiele hebben een productpagina die "decent" of beter scoort. — [Baymard, product page UX](https://baymard.com/blog/current-state-ecommerce-product-page-ux)
  - Baymard: 81% toont geen prijs per eenheid bij producten die in wisselende hoeveelheden worden verkocht. — [Baymard](https://baymard.com/blog/current-state-ecommerce-product-page-ux)
  - Baymard: 67% geeft bij de koopknop geen schatting van de totale kosten. — [Baymard](https://baymard.com/blog/current-state-ecommerce-product-page-ux)
  - Baymard: 44% linkt niet naar het retourbeleid vanuit de productinhoud. — [Baymard](https://baymard.com/blog/current-state-ecommerce-product-page-ux)
  - Baymard: 37% toont geen beelden "op schaal". — [Baymard](https://baymard.com/blog/current-state-ecommerce-product-page-ux)

### Inferences
- De prijzen die op ,80 eindigen (479,80, 439,80, 379,80, 599,80) zijn precies twee keer een prijs op ,90. Waarschijnlijk is daar de stukprijs van een andere Orderchamp-variant verdubbeld, terwijl de varianten op ,95 al setprijzen zijn. Hoe het ook zit: de bezoeker ziet binnen één "set van 2" een kleur die 70 tot 80% duurder is, zonder uitleg. Dat wekt wantrouwen of laat de goedkope kleur als foutprijs ogen. Per set en per stuk tonen ("€279,95 per set van 2 · €139,98 per stoel") volgt de Baymard-aanbeveling over prijs per eenheid. Volgens regel 2 van CLAUDE.md beslist de eigenaar over prijzen.
- "100 in voorraad" is een Orderchamp-standaardaantal en geen echte voorraad. Tonen is misleidend.
- Drie tegenstrijdige retourbeloftes (wettelijke termijn, 100 dagen, 30 dagen, plus "Lifetime Warranty") vormen een juridisch risico. Een consument kan zich op de ruimste belofte beroepen.
- De Engelse leverdatum van 5 tot 9 dagen staat ook op uitverkochte producten en is niet gebaseerd op de leverancier.

### Gaps
- Mobiele weergave niet gerenderd (geen browser of screenshot in deze sessie). Een eerdere meting staat in `/home/user/Inhuys/analyse/pagespeed-2026-10-26.md` (niet geopend).
- Welke producten Shopify werkelijk aanbeveelt in "product-recommendations" (JS-gestuurd) is niet beoordeeld.
- Of de prijzen op ,80 een fout zijn of een bewuste prijs: dat moet uit Orderchamp blijken, maar dat is niet gecontroleerd.

## 3. Live producten zonder voorraad

### Takeaway
Volgens de export van 19 november staan 9 actieve producten op voorraad 0: 3 keer Breeze, 4 keer Cloud, Luna mink en Flitsadvies. Ze tonen "Uitverkocht" en "Geen voorraad meer", maar tegelijk een Engelse leverdatum. In collecties en zoekresultaten staan ze gewoon tussen leverbare producten. Daarnaast zijn losse kleuren van leverbare producten uitverkocht (Fuji Okura en Omber, Scandi Omber).

### Cited Findings
- Actief met voorraad 0 (19 november): breeze-stoel-beige-, -latte- en -pistache-set-van-2, cloud-stoel-creme-, -karamel-, -safiya-naturel- en -safiya-terracotta-set-van-2, luna-chair-mink-set-van-2 en flitsadvies. — [/home/user/Inhuys/data/orderchamp/voorraad-2026-11-19b.csv](/home/user/Inhuys/data/orderchamp/voorraad-2026-11-19b.csv)
- Breeze beige en Cloud crème tonen "Geen voorraad meer", een knop "Uitverkocht" en tegelijk "Estimated Delivery: Nov 28 - Dec 02". In `.js` staat `available: false`. — [Breeze](https://www.in-huys.nl/products/breeze-stoel-beige-set-van-2), [Cloud crème](https://www.in-huys.nl/products/cloud-stoel-creme-set-van-2)
- In `/collections/all` en `/collections/cloud` krijgen uitverkochte producten een "Uitverkocht"-label tussen leverbare producten. De filter telt "Niet op voorraad (23)". — [collections/all](https://www.in-huys.nl/collections/all), [collections/cloud](https://www.in-huys.nl/collections/cloud)
- Gedeeltelijk uitverkocht: Fuji (Okura en Omber niet leverbaar), Scandi (Omber niet leverbaar). — [Fuji .js](https://www.in-huys.nl/products/eetkamerstoel-fuji.js), [Scandi .js](https://www.in-huys.nl/products/scandi-stoel-tan-set-van-2.js)
- Het faseplan legt de keuze "actief laten (zichtbaar als uitverkocht) of naar concept" open bij de eigenaar en noemt Breeze als het product met de meeste vertoningen. — [/home/user/Inhuys/plannen/fase-4.md](/home/user/Inhuys/plannen/fase-4.md)
- In de werkversie wordt uitverkocht "Tijdelijk niet leverbaar". De normale voorraadtekst is leeg, zodat "100 in voorraad" verdwijnt. — [/home/user/Inhuys/tools/theme_build.py](/home/user/Inhuys/tools/theme_build.py) (regel 128)

### Inferences
- Breeze en Cloud live laten als zoekingang heeft zin, maar dan zonder leverdatum, met een "mail me bij voorraad"-optie en een link naar een leverbaar alternatief (Cloud-barkruk, Luna of andere kleuren). Een doodlopende pagina kost een vertoning zonder vervolg.

### Gaps
- De export is van 19 november. De voorraad van 23 november is niet opnieuw opgehaald, conform de afspraak geen nieuwe exports zonder reden. Een "terug-op-voorraad"-app of melding is in de HTML niet gezien.

## 4. Zoeken, filters, winkelwagen, afrekenen, gratis verzending en cross-sell

### Takeaway
Zoeken en filters werken. Een echte drempel voor gratis verzending, een levertijdbelofte of een zichtbaar retourbeleid ontbreekt. De beleidspagina's voor verzending en retour geven 404. De winkelwagenlade biedt een opmerkingenveld, een verzendcalculator en een kortingscodeveld, maar geen voortgangsbalk of cross-sell.

### Cited Findings
- `/policies/shipping-policy` en `/policies/refund-policy` geven HTTP 404. — [shipping-policy](https://www.in-huys.nl/policies/shipping-policy), [refund-policy](https://www.in-huys.nl/policies/refund-policy)
- De winkelwagenlade bevat "Opmerking", "Schat de verzendkosten", "Coupon: Voeg een kortingscode toe", "Subtotaal", "Uitchecken" en "Bekijk winkelwagen". Er is geen drempel voor gratis verzending; de enige vermelding is de demotekst "over $75" op de productpagina. — [homepage, winkelwagenlade](https://www.in-huys.nl/), [Rock](https://www.in-huys.nl/products/eetkamerstoel-rock-set-van-2)
- Baymard over redenen om af te haken (zonder de groep "alleen kijken"): 40% vindt de extra kosten te hoog, 20% de levering te traag, 19% vertrouwt de site niet met betaalgegevens, 13% vindt het retourbeleid onvoldoende en 12% kan de totale kosten niet vooraf zien. Het gemiddelde afhaakpercentage is 70,22%. — [Baymard, cart abandonment](https://baymard.com/lists/cart-abandonment-rate)

### Inferences
- Een bank van €2.740 zonder vermelde bezorgkosten, levertijd of retourvoorwaarde raakt precies de top-vijf van afhaakredenen van Baymard. Bij meubels weegt "bezorging tot in huis, ja of nee" zwaar.
- De ontbrekende beleidspagina's zijn ook een nalevingsrisico: een webwinkel moet consumenten informeren over het herroepingsrecht. Shopify toont die pagina's pas als het beleid is ingevuld.

### Gaps
- De afrekenstappen zelf zijn niet bekeken (daarvoor moet een product in de winkelwagen; de opdracht verbood bestellen). Welke betaalmethoden actief zijn, is dus niet vastgesteld. De werkversie belooft "iDEAL, creditcard en meer".
- Privacybeleid en algemene voorwaarden (`/policies/privacy-policy`, `/policies/terms-of-service`) zijn niet gecontroleerd.

## 5. Voorbereide nieuwe versie: lost die de problemen op en wat ontbreekt nog?

### Takeaway
De werkversie (thema-kopie 210233098579 plus 10 conceptcollecties, pagina's en artikelen) lost het grootste deel op:
- categorienavigatie via een nieuw menu en negen categorietegels op de homepage;
- Nederlandse labels;
- weg met de "$75" en "Open Doors To A World Of Fashion";
- een "Waarom InHuys"-blok in plaats van "Why Minimog";
- geen nep-voorraadtal meer;
- een specificatietabel uit metavelden;
- "Advies van InHuys";
- Flitsadvies op elke productpagina;
- LocalBusiness- en BreadcrumbList-markup.

Nog open: dunne collecties, de kettingen, de ontbrekende beleidspagina's, de onduidelijke prijzen per set, de machinevertaalde variantnamen, een berekende leverdatum (14 dagen) zonder bevestiging van de leverancier, de productpagina van Flitsadvies zelf, de projectenplaatshouders op de homepage, en demoresten die het bouwscript niet noemt (populaire zoekopdrachten, leeftijdscontrole, "Redden").

### Cited Findings
- **Menu en homepage nieuw:**
  - Nieuw hoofdmenu: Interieuradvies, Projecten, Collectie met negen collecties, Inspiratie, Over InHuys. — [/home/user/Inhuys/plannen/fase-4.md](/home/user/Inhuys/plannen/fase-4.md)
  - Homepage: één slide, werkwijze in vier stappen, projectenblok "met plaatshouders tot er foto's zijn", negen categorietegels, showroomblok. — [/home/user/Inhuys/analyse/07-thema-werkversie.md](/home/user/Inhuys/analyse/07-thema-werkversie.md)
- **Collecties na correctie:**
  - banken 7, stoelen 35 (inclusief 6 dubbelen die naar concept gaan), fauteuils 1, barkrukken 5, tafels 4, vazen 3, windlichten 2, decoratie 2 (11 met kettingen), maatwerk 0, kinderkamer 14. — [/home/user/Inhuys/analyse/14-collecties-controle.md](/home/user/Inhuys/analyse/14-collecties-controle.md)
  - Voorstel: kettingen in Decoratie; Fauteuils omzetten naar `TYPE EQUALS Fauteuils`; Maatwerk niet publiceren. — [/home/user/Inhuys/analyse/14-collecties-controle.md](/home/user/Inhuys/analyse/14-collecties-controle.md)
- **Productpagina in de werkversie:**
  - Blokvolgorde: titel, korte omschrijving, "Andere uitvoeringen", prijs, varianten, AI-kamerpreview, voorraadstatus, koopknop, levering, betaalvertrouwen, omschrijving, specificaties, "Advies van InHuys". — [/home/user/Inhuys/tools/theme_build.py](/home/user/Inhuys/tools/theme_build.py) (regel 154)
  - Voorraad: normale tekst leeg, uitverkocht wordt "Tijdelijk niet leverbaar", "Op bestelling". — [theme_build.py](/home/user/Inhuys/tools/theme_build.py) (regel 128)
  - Levering: "Verwachte levering:" met `deliver_days: 14`, plus de tekst "Levering via onze merkpartner; de levertijd staat bij elk product. Vragen? Plan een gratis Flitsadvies." — [theme_build.py](/home/user/Inhuys/tools/theme_build.py) (regel 129)
  - Betaalvertrouwen: "Veilig afrekenen met iDEAL, creditcard en meer". — [theme_build.py](/home/user/Inhuys/tools/theme_build.py) (regel 130)
  - "Waarom InHuys" met "Advies inbegrepen" (link naar `/pages/interieuradvies`), "Levering via onze merkpartners" en "Showroom in Purmerend". FAQ met "Retourneren kan binnen veertien dagen; maatwerk is uitgezonderd". Aanbevelingen heten "Anderen bekeken ook", recent bekeken heet "Recent bekeken". — [theme_build.py](/home/user/Inhuys/tools/theme_build.py)
- **Overig in de werkversie:**
  - Footer met bedrijfsgegevens ("InHuys is een handelsnaam van Kluster", KvK, btw), betaaliconen, cookiebanner in het Nederlands, viewport zonder zoomblokkade. — [/home/user/Inhuys/analyse/07-thema-werkversie.md](/home/user/Inhuys/analyse/07-thema-werkversie.md)
  - De nieuwsbrief belooft geen korting meer. — [/home/user/Inhuys/analyse/07-thema-werkversie.md](/home/user/Inhuys/analyse/07-thema-werkversie.md)
- **Wat het faseplan open laat:** levertijd en garantie ("voorstel: leeg laten" per product), prijsverschillen per variant, 13 live producten zonder voorraad, dunne collecties, 21 redirect-doelen naar concepten, en de oude modelcollecties en Bestsellers die pas na twee weken opgeruimd worden. — [/home/user/Inhuys/plannen/fase-4.md](/home/user/Inhuys/plannen/fase-4.md)
- In `tools/theme_build.py` vond ik geen aanpassing voor de "populaire zoekopdrachten" (T-Shirt, Blue Jacket), de leeftijdscontrole, de vertaling "Redden" in de winkelwagen of de beleidspagina's (grep op deze termen leverde niets op). — [/home/user/Inhuys/tools/theme_build.py](/home/user/Inhuys/tools/theme_build.py)

### Inferences
- **Tegenstrijdigheid:** de werkversie rekent een leverdatum uit met vast 14 dagen, terwijl het faseplan voorstelt de levertijd leeg te laten tot de leverancier die bevestigt. Bij uitverkochte producten of langere Pole To Pole-levertijden wordt dat opnieuw een onjuiste belofte. Beter is dit blok uitzetten of laten sturen door een metaveld `inhuys.levertijd`.
- Het retourbeleid zegt in de FAQ "veertien dagen", maar zolang `/policies/refund-policy` 404 geeft, ontbreekt de juridische basis waarnaar die belofte verwijst.
- Het "Andere uitvoeringen"-blok werkt alleen als het hoofdproduct gepubliceerd en beschikbaar is, dus niet voor uitverkochte Breeze- en Cloud-kleuren.
- Een projectenblok met plaatshouders op de homepage is een nieuw onaf element. Beter verbergen tot er foto's zijn.

### Gaps
- De preview is niet visueel beoordeeld (anoniem krijg je het live thema). Er is geen mobiele controle van de werkversie gedaan.

## 6. Flitsadvies: presentatie en links vanuit producten

### Takeaway
Flitsadvies staat live als product van €0,00 met een algemene accessoiretekst ("Een modern en tijdloos item met een luxe, rustige uitstraling …") en een SEO-titel "Flitsadvies luxe accessoire". Er is geen boekingsstap of uitleg wat je krijgt. De pagina Interieuradvies prijst het aan als gratis, maar geen enkele productpagina linkt ernaar. De werkversie zet op elke productpagina een verwijzing naar een gratis Flitsadvies (naar `/pages/interieuradvies`), maar de productpagina `/products/flitsadvies` zelf blijft live zoals hij is.

### Cited Findings
- `/products/flitsadvies`:
  - `<title>`: "Flitsadvies luxe accessoire | InHuys"; prijs "Normale prijs €0,00 Verkoopprijs €0,00"; omschrijving "Een modern en tijdloos item met een luxe, rustige uitstraling ontworpen om je interieur net dat beetje ext[ra] …". — [Flitsadvies](https://www.in-huys.nl/products/flitsadvies)
  - Dezelfde pagina toont de AI-kamerpreview "Bekijk dit product in jouw kamer" en "Free Shipping & Returns: On all orders over $75". Breadcrumb: InHuys › Adviezen › Flitsadvies. — [Flitsadvies](https://www.in-huys.nl/products/flitsadvies)
- `/pages/interieuradvies`:
  - Diensten: "3D Interieurontwerp compleet gratis In onze Showroom", "Compleet Flitsadvies gratis Online of In onze Showroom", "Boek Direct een Call", "Kort online advies met direct resultaat". Ook staat er "Plan een welkomstgesprek en laat u inspireren" (u-vorm). — [Interieuradvies](https://www.in-huys.nl/pages/interieuradvies)
  - De pagina linkt niet naar `/products/flitsadvies` (0 links). — [Interieuradvies](https://www.in-huys.nl/pages/interieuradvies)
- Geen van de tien bekeken productpagina's linkt in de inhoud naar Flitsadvies. — de tien productpagina's onder punt 2
- In de werkversie:
  - Dienstkaarten herschreven ("Flitsadvies gratis"; 3D-ontwerp "Prijs op aanvraag; het bedrag verrekenen we bij aankoop van de inrichting via InHuys"); knoppen naar het aanvraagformulier op dezelfde pagina; "Shop now" wordt "Plan een Flitsadvies". — [/home/user/Inhuys/analyse/07-thema-werkversie.md](/home/user/Inhuys/analyse/07-thema-werkversie.md)
  - Elke productpagina verwijst naar een gratis Flitsadvies. — [/home/user/Inhuys/tools/theme_build.py](/home/user/Inhuys/tools/theme_build.py)
- Flitsadvies blijft volgens besluit actief en hoort in geen categoriecollectie. — [/home/user/Inhuys/plannen/fase-4.md](/home/user/Inhuys/plannen/fase-4.md), [/home/user/Inhuys/analyse/14-collecties-controle.md](/home/user/Inhuys/analyse/14-collecties-controle.md)

### Inferences
- Een gratis dienst als product van €0 met een "Voeg toe aan winkelkar"-stroom en accessoiretekst verwart de bezoeker. Ook kan iemand een bestelling van €0 doen zonder afspraak. Beter: de productpagina een eigen dienst-tekst geven, met wat je krijgt, hoe lang het duurt, online of in de showroom, en een knop naar het formulier. Of de URL doorsturen naar `/pages/interieuradvies` (vraagt akkoord van de eigenaar).
- Advies is het onderscheidende punt van InHuys tegenover andere Pole To Pole-dealers. Een gerichte vraag bij de koopknop ("Twijfel je over kleur of maat? Plan een gratis Flitsadvies") is daarom de belangrijkste conversiehefboom van de werkversie.

### Gaps
- Hoe een Flitsadvies daadwerkelijk wordt ingepland (formulier, agenda-app) is niet getest.

## Bijlage bij de vragen: prioriteitenlijst (wat werkt, wat de verkoop remt, wat te doen)

Deze lijst is afgeleid van de bevindingen hierboven; de onderbouwing en bronnen staan in de secties 1 tot 6.

**Wat werkt (live):** alle 77 producten zijn bereikbaar via Assortiment en zoeken (45 resultaten op "stoel"); de filters werken (type, merk, prijs, voorraad); 3 tot 8 beelden per product; breadcrumb, JSON-LD, sticky koopknop en een aanbevelingssectie; eigen Nederlandse producttekst met de sectie "Levering & retour"; een AI-kamerpreview als onderscheidend element.

**Prioriteit 1, remt nu de verkoop en kan zonder go-live van het hele thema niet weg (dus de go-live van de thema-kopie zelf):**
1. Demobeloftes weg: "$75", "100 Days Return", "Lifetime Warranty", "30-day", "Estimated Delivery", "100 in voorraad", "Open Doors To A World Of Fashion", "10% off" en "T-Shirt Blue Jacket". De werkversie lost alles op behalve de zoeksuggesties en de leeftijdscontrole; die twee apart controleren in de thema-kopie.
2. Beleidspagina's verzending en retour invullen in Shopify (nu 404). Dit is eigenaarsbesluit en juridisch.
3. Categorienavigatie: 10 categoriecollecties publiceren en het nieuwe menu activeren (fase 4, stap 1, 4 en 5). Nu zitten 49 van de 77 producten in geen collectie.

**Prioriteit 2, vertrouwen en duidelijkheid op de productpagina:**
4. Prijs per set tegenover per stuk: per variant controleren in Orderchamp (prijzen op ,80 tegenover ,95); "per set van 2" bij de prijs; Fuji en andere enkele stoelen expliciet "per stuk". Over prijzen beslist de eigenaar.
5. Variantnamen opschonen ("room" wordt "Crème", "Bruinen" wordt "Bruin", hoofdletters gelijk) en optienaam "Kleur". Variantnamen zijn van Orderchamp (regel 7), dus in de Orderchamp-app of na een besluit van de eigenaar.
6. Variantbeelden koppelen, zodat de foto meewisselt met de kleur. Beelden zijn van Orderchamp (regel 7).
7. Leverdatumblok in de werkversie niet op vaste 14 dagen, maar uit metaveld of uit.

**Prioriteit 3, conversie en cross-sell:**
8. Flitsadvies: eigen dienstpagina of doorsturen; de €0-accessoiretekst vervangen.
9. Uitverkochte producten (Breeze, Cloud): geen leverdatum, wel een melding bij voorraad en een link naar een leverbaar alternatief; of naar concept (eigenaarsbesluit 6 in fase 4).
10. Dunne collecties: kettingen in Decoratie (11); Fauteuils en Windlichten alleen publiceren met een tekst die naar Stoelen of Decoratie verwijst; Maatwerk niet publiceren; projectenplaatshouders op de homepage verbergen.
11. Winkelwagen: "Redden" vertalen. Overweeg een vermelding van bezorgkosten en levering tot in huis in de lade. Volgens Baymard is "extra kosten" de nummer-1-afhaakreden (40%).
12. Cross-sell: aanbevelingen controleren (bijvoorbeeld eettafel bij stoelen) zodra er categoriecollecties zijn; een "complete de eethoek"-blok is een kans, maar daar is nu niets van gemeten.
