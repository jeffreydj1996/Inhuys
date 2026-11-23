# Test werkversie op de echte winkel · 23 november 2026

Thema-kopie `210233098579` (`InHuys · fase 2 werkversie (niet publiceren)`, rol unpublished) bekeken via `?preview_theme_id=210233098579` met Playwright (Chromium), desktop 1366x900 en iPhone 13. Op elke pagina bevestigd dat `Shopify.theme.id` 210233098579 is. Niets gewijzigd in Shopify; het winkelwagentje bestond alleen in de testbrowser. Screenshots: `/tmp/claude-0/-home-user-Inhuys/260fa1f5-5941-5916-9ab1-87df4acf54d3/scratchpad/t/shots/` (en `home-desk.png`, `home-mob.png` ernaast).

Omvang: 32 URL's x 2 schermformaten, 7 productpagina's (kleur- en maatvarianten gekozen op desktop; 7 op mobiel), 96 unieke interne links opgevraagd, winkelwagen tot de checkout (desktop). Let op: in de voorvertoning zit een zwarte voorbeeldbalk onderin die op desktop de knoppen van de cookiebanner afdekt; dat is geen themafout.

## Wat werkt

- Voorvertoning pakt het juiste thema op elke pagina (theme.id 210233098579, role unpublished).
- Homepage `/`: 200, geen kapotte afbeeldingen, geen console-fouten van het thema. Topbalk (telefoon, e-mail, tagline, showroom), hero met projectbeeld en twee knoppen, vier stappen werkwijze, Voor/Na-vergelijker, "Ik ben Sylvana", showroom, inspiratie, startgesprek-formulier, footer met bedrijfsgegevens en betaaliconen. Alle tekst Nederlands, je-vorm.
- Hoofdmenu desktop: Interieuradvies, Projecten, Collectie (uitklap met negen collecties), Inspiratie, Over InHuys; werkt bij hover. Mobiel menu aanwezig (`m-menu-mobile`).
- `/collections/all` (200): 32 kaarten per pagina met beeld en prijs, `?page=2` werkt. Sorteren via `?sort_by=price-ascending` werkt; filter Producttype "Banken" geeft 7 producten, URL en raster passen zich aan. Filters: producttype, merk, prijs, beschikbaarheid.
- `/pages/interieuradvies`, `/pages/contact`, `/pages/inspiratie`, `/policies/privacy-policy`, `/policies/contact-information`: 200 met inhoud en titel "... – InHuys".
- Zoeken `/search?q=stoel`: 45 resultaten, kaarten met prijs; `q=zzzxx`: nette lege staat. 404-pagina geeft HTTP 404 met Nederlandse tekst ("Oeps! Pagina niet gevonden!", knop "Ga naar huis").
- Productpagina's (200, titel en meta description per product eigen en Nederlands, geen kapotte afbeeldingen, specificatietabel, "Advies van InHuys", Veelgestelde vragen, tab "Levering en retour", korte omschrijving): bank-londen-6-zits-tan, eetkamerstoel-sake, cloud-barstoel-creme, octo-ketting-black-tiger, ballenbak, lantaarn-raffles. Prijs per variant wisselt correct mee (Raffles S €129,95, L €119,95, XL €319,95; Cloud barkruk karamel €349,95).
- Hoofdfoto wisselt mee met de kleur bij sake (Okura, Oatly, Umber, Tan: vier verschillende foto's met eigen alt), Cloud barkruk (crème/karamel), Avena (crème/karamel/mink) en Ballenbak (beige, blauw, kameel). Desktop en mobiel gelijk.
- "Andere uitvoeringen" (`inhuys-uitv`): knoppen op bank-londen-6-zits-tan (3-zits met ottoman, 6-zits actief, 6-zits met ottoman), cloud-barstoel-creme (Keukenbarkruk, Barkruk) en octo-ketting-black-tiger (Maat S, Maat L); alle doelen geven 200. Op sake, ballenbak, lantaarn-raffles en flitsadvies staat het blok niet (hoort ook niet: geen modelgroep).
- Winkelwagen: toevoegen via de knop (POST /cart/add 200), zijpaneel met artikel, `/cart` met regel, aantal, Verwijderen, Opmerking, Verzenden, Coupon, subtotaal en knop Uitchecken. Checkout (`/checkouts/cn/...`, `nl-nl`) komt op: iDeal, Creditcard en Klarna, snelle checkout, kortingscode, factuuradres. Verzendkosten verschijnen pas na invullen van het adres ("Voer je bezorgadres in om de beschikbare verzendmethoden te zien"); niets ingevuld.
- Cookiebanner Nederlands; op mobiel verdwijnt hij na Accepteren en komt niet terug. Nieuwsbriefveld in de footer ("Je e-mailadres", knop Inschrijven, belofte "Geen aanbiedingen, wel inzicht"); niet verstuurd.
- Interne links: van 96 unieke interne links geven 79 een 200. De 17 overige staan hieronder.

## Wat niet werkt

1. **Menu- en footerdoelen geven 404 in de voorvertoning**: `/pages/projecten`, `/pages/over-inhuys`, `/pages/werkwijze`, `/pages/showroom`, `/pages/veelgestelde-vragen`, `/collections/banken`, `stoelen`, `fauteuils`, `barkrukken`, `tafels`, `vazen`, `windlichten-en-kaarsenhouders`, `decoratie`, `maatwerk`, `kinderkamer`. Dit zijn de nog ongepubliceerde pagina's en collecties (verwacht volgens `analyse/07`), maar het betekent dat het hoofdmenu, de homepage-tegels en alle productpagina's (broodkruimel, "Meer"-links, footer) bij publicatie van alleen het thema naar 404's wijzen. Publicatievolgorde uit `plannen/fase-4.md` (stap 1 en 2 vóór stap 5) is dus bindend. Opmerking: `/pages/over-inhuys` staat in het hoofdmenu én in de homepagina-knop "Lees meer over InHuys".
2. **Homepage, blok "Collectie"**: negen tegels tonen grijze plaatshouder-illustraties (tassen, schoenen, brillen, horloges) in plaats van collectiefoto's; de collecties zijn ongepubliceerd en hebben (waarschijnlijk) geen beeld. Zie `home-desk.png`.
3. **`/collections` is niet vertaald**: koptekst "All collection", tekst "Here is your chance to upgrade your wardrobe with a variation of styles and fits that are both feminine and relaxed.", en het raster toont de oude live collecties (Adviezen, Amsterdam, Bestsellers, Bow, ...) met h1 in het Engels. Meta description generiek. Screenshot `shots/_collections.png`.
4. **Retourbeleid bestaat niet**: `/policies/refund-policy` geeft 404, terwijl elke productpagina in de tab "Levering en retour" en in de FAQ ernaar linkt ("Alle voorwaarden staan in het retourbeleid"). Ook `/policies/terms-of-service` en `/policies/shipping-policy` zijn 404; in de footer staan alleen Privacybeleid en Contactgegevens.
5. **Variantfoto's wisselen niet bij een paar producten**:
   - bank-londen-6-zits-tan: Umber en Tan tonen dezelfde foto; bij de standaardkleur Umber staat de tan-foto ("Londen met 6 zitje tan InHuys") vooraan.
   - lantaarn-raffles: S, L en XL tonen dezelfde foto, met alt "Loterij Lantaarn L InHuys" (verkeerde naam en maat) terwijl maat S gekozen is.
   - bank-new-york: Coco en Beige tonen dezelfde foto (alt "... Beige").
   - ballenbak: de standaardkleur roos toont bij laden de beige foto (alt "Ballenbak beige"); OLIJF toont dezelfde beige foto; roos, blauw en kameel wisselen wel. Kleurnamen inconsistent: "roos, beige, BLAUW, OLIJF, KAMEEL".
6. **Flitsadvies** (live dienst): prijs €0,00 getoond, meta description en titel van een demo-product ("Flitsadvies luxe accessoire | InHuys", "Ontdek Flitsadvies. De neutrale basis en de hoogwaardige afwerking maken dit een rustige finishing touch ... Luxe, modern…"); geen specificaties of advies; wel de knop "Voeg toe". Moet een dienstpagina met eigen tekst worden, of zonder prijs naar de adviespagina verwijzen.
7. **Winkelwagenpagina**: onder de regel staat "Recently Viewed Products" in het Engels.
8. **Levering/FAQ-tekst verwijst naar iets wat er niet staat**: "De levertijd staat bij het product zodra die bekend is" terwijl geen enkel geteste product een regel "Levertijd:" toont (metaveld `inhuys.levertijd` leeg; beslissing eigenaar open in fase 4).
9. **Meta description op homepage, zoekpagina's en `/collections` is de oude standaardtekst** "Doe inspiratie op, vraag advies of shop direct de nieuwste trends voor in Huis" (Huis met hoofdletter, trendtaal). `/collections/all` ("Producten – InHuys"), `/pages/contact` en beleidspagina's hebben helemaal geen meta description. Homepage `<h1>` is leeg en `/pages/inspiratie` heeft geen h1.
10. **Producttype-filter op `/collections/all`** toont een lijst die niet bij het menu past: Accessoires, Banken, Barstoel (singular), Decoratie (13), Fauteuils, Kinderkamer, Stoelen (31), Tafels, Vazen; merkfilter "Jupiduu - Designed for Kids" en "Pole To Pole" (merkfilter toont leveranciersnaam, geen InHuys-merk).
11. **Cookiebanner**: neemt op mobiel meer dan de helft van het scherm in (3 knoppen onder elkaar); in de voorvertoning dekt de voorbeeldbalk de knoppen op desktop af, waardoor Accepteren niet te klikken was. Bij live bekijken opnieuw nagaan. De banner staat bovenop het winkelmandpaneel.
12. **Console**: alleen externe meldingen (Shopify monorail-request, shop.app frame CSP 403, hCaptcha logo, 429 bij snel achter elkaar opvragen); geen thema-JavaScript-fouten. Cloudflare gaf eenmalig 429 "Just a moment" bij veel parallelle verzoeken (testartefact).
13. Product- en kaartbeelden: geen `naturalWidth` 0 op de bezochte pagina's na scrollen. Demo-regex (Minimog, lorem, "Shop now", "Add to cart", "Sold out") geen treffers op de geteste pagina's behalve punt 3 en 7.
14. Mobiele checkout en mobiele winkelwagen zijn niet apart doorlopen (dezelfde Shopify-checkout); de mobiele homepage is wel geladen en toont dezelfde secties.

## Nog te doen

| Nr | Punt | Ernst | Waar | Wie |
|---|---|---|---|---|
| 1 | Pagina's Projecten, Over InHuys, Werkwijze, Showroom, Veelgestelde vragen publiceren vóór of samen met het thema (menu, homepage, productpagina's en footer verwijzen ernaartoe) | blokkeert publicatie | pagina's, menu | eigenaar (go-live stap 2), uitvoerder |
| 2 | Negen collecties (en Kinderkamer) publiceren vóór of samen met het thema; dunne collecties (Maatwerk 0 producten) beslissen | blokkeert publicatie | collecties | eigenaar, uitvoerder |
| 3 | Retourbeleid (en verzend- en algemene voorwaarden) aanmaken in Shopify; productpagina's linken ernaar | blokkeert publicatie | Shopify-instelling (beleid) | eigenaar |
| 4 | Collectietegels op de homepage: collectiefoto's instellen zodat de grijze plaatshouders verdwijnen | blokkeert publicatie | collecties (beeld), thema (sectie) | uitvoerder, thema-agent |
| 5 | `/collections` omzetten naar Nederlandse kop en tekst (h1 "Collectie", eigen intro), oude demo-collecties (Adviezen, Amsterdam, Bestsellers, Bow, ...) niet tonen | blokkeert publicatie | thema (`page.collecties`/collections-template), collecties | thema-agent |
| 6 | Flitsadvies: eigen titel, meta description en tekst, prijs €0,00 en winkelwagenknop herzien | blokkeert publicatie | product | schrijver, eigenaar (prijs) |
| 7 | "Recently Viewed Products" in Nederlands ("Onlangs bekeken") op de winkelwagenpagina | belangrijk | thema (locale of sectie) | thema-agent |
| 8 | Variantfoto's koppelen/aanvullen: bank Londen 6-zits (Umber vs Tan), Raffles S/L/XL (met correcte alt), bank New York (Coco vs Beige), Ballenbak roos en olijf | belangrijk | product (media, Orderchamp-beelden) | uitvoerder (regel 2e), eigenaar bij ontbrekende foto's |
| 9 | Kleurnamen Ballenbak gelijk trekken (Roos, Beige, Blauw, Olijf, Kameel) | klein | product (optiewaarden) | uitvoerder (`productOptionUpdate`, regel 2e) |
| 10 | Levertijdregel: of vullen per merk of de zin "De levertijd staat bij het product zodra die bekend is" uit FAQ en tab halen | belangrijk | product (metaveld, tekst) | eigenaar (beslissing), schrijver |
| 11 | Meta descriptions: homepage, `/collections`, zoekresultaten, contact, `/collections/all` eigen tekst; homepage en inspiratie krijgen een h1 | belangrijk | thema (settings, templates), pagina's | thema-agent, schrijver |
| 12 | Producttypen opschonen (Barstoel/Barkrukken, Kinderkamer, Accessoires) zodat filter en menu overeenkomen | klein | product (type) | schrijver, uitvoerder (regel 2a) |
| 13 | Cookiebanner op mobiel compacter (kleinere tekst of balk onderin) en na go-live nogmaals op desktop controleren | klein | Shopify-instelling (Customer privacy) en thema-CSS | thema-agent, eigenaar |
| 14 | Verzendinfo bij de checkout controleren met een testadres (verzendtarieven, levertijden) | belangrijk | Shopify-instelling (verzending) | eigenaar |
| 15 | Mobiele winkelwagen en checkout met Playwright herhalen na het oplossen van punt 1 tot 6 | klein | testwerk | uitvoerder |

## Ronde 2 (23 november 2026)

Zelfde werkwijze als ronde 1 (Playwright, `?preview_theme_id=210233098579`, `Shopify.theme.id` op elke pagina 210233098579, desktop 1366x900 en iPhone 13, pauzes tussen pagina's). Niets in Shopify gewijzigd. Scripts en uitvoer: `/tmp/claude-0/-home-user-Inhuys/260fa1f5-5941-5916-9ab1-87df4acf54d3/scratchpad/t/r2/` (`v-<handle>-desk|mob.txt`, `ld.out`, `shots/`). De winkelwagen bestond alleen in de testbrowser en is daarna geleegd.

### Uitkomst per punt uit ronde 1

| Nr | Punt | Uitkomst |
|---|---|---|
| 1 | Pagina's 404 | Nog open, verwacht: pagina's zijn ongepubliceerd. Footer heeft nu ook `/pages/herroepen` (404, zelfde reden; `content/paginas/herroepen.md` bestaat). Menu verwijst nog naar `/collections/maatwerk`, dat in de nieuwe lijst van negen niet meer voorkomt (alleen het menu, geen thema). |
| 2 | Collecties 404 | Nog open (ongepubliceerd). |
| 3 | `/collections` | Opgelost: h1 "Collectie", Nederlandse intro, geen demotekst. Meta description is nog de oude standaardtekst (zie 9). |
| 4 | Retourbeleid | Nog open: `/policies/refund-policy`, `terms-of-service` en `shipping-policy` geven 404; productteksten en FAQ linken ernaar. Shopify-instelling van de eigenaar. |
| 5 | Collectietegels homepage | Nog open, pas na publicatie te toetsen. De tegels hebben in de voorvertoning `href="#"` en geen beeld omdat de collecties ongepubliceerd zijn. De terugval op collectiebeeld of eerste productfoto is dus niet te verifiëren. |
| 6 | Variantfoto's (nr 5 hierboven) | Grotendeels opgelost, zie het blok hieronder. |
| 7 | Flitsadvies | Nog open: titel en meta description van het demo-product, prijs 0, JSON-LD `price` 0 (ongeldig voor Google). |
| 8 | "Recently Viewed" in winkelwagen | Opgelost: "Recent bekeken" (desktop en mobiel). |
| 9 | Levertijd | Opgelost wat de zin betreft: "De levertijd staat bij het product" komt niet meer voor; op bank Londen alleen "Levering via onze merkpartners". Het veld `inhuys.levertijd` is nog leeg, dus geen levertijdregel op producten (beslissing eigenaar open). |
| 10 | Meta descriptions en h1 | Gedeeltelijk. Homepage heeft nu één echte h1 ("Een verbouwing is pas af als de ruimte klopt"; de twee lege h1's in de DOM zijn slider-klonen). Interieuradvies heeft h1. **`/pages/inspiratie` heeft nog geen h1 en geen h2** (in de gerenderde pagina). Meta description nog de oude tekst op `/`, `/collections`, zoeken; ontbreekt op `/collections/all`, contact, beleidspagina's (homepage-titel en omschrijving moeten in Voorkeuren; open). |
| 11 | Producttypen | Niet getoetst in de filters; breadcrumb op Play & Chill toont wel het type "rocking" (Engels), zie nieuw 4. |
| 12 | Cookiebanner | **Niet opgelost op mobiel.** De banner komt uit Shopify Customer privacy (`shopify-pc__banner__dialog`), niet uit het thema; hij is 450 van 664 px hoog (68 procent) met kopje, lange tekst, Accepteren en Afwijzen. De thema-CSS in `snippets/cookie-banner.liquid` raakt hem niet. Na Accepteren verdwijnt hij en blijft weg. Alleen te verkleinen in Shopify (Instellingen, Klantprivacy, tekst inkorten). |
| 13 | Console | Geen thema-JavaScript-fouten. Alleen 404's van de ongepubliceerde collectie-links in het menu, `shop.app` frame-CSP, 403 en monorail (extern), en 401/403 op de checkout (normaal). |
| 14 | Mobiele winkelwagen | Zie hieronder: werkt. |

### Variantfoto's (bij laden en na elke keuze, heen en terug)

Eigen toets: het grote beeld moet het `featured_image` van de gekozen variant zijn. Desktop en iPhone 13 gelijk.

| Product | Resultaat |
|---|---|
| bank-londen-6-zits-tan | Opgelost: Umber en Tan hebben elk een eigen beeld (alt "Bank Londen 6-zits in Umber"), laden toont Umber. |
| bank-new-york | Opgelost: Coco en Beige verschillend, laden toont Coco. |
| lantaarn-raffles | S en L goed, laden toont S. **XL heeft nog geen `featured_image`**: bij XL blijft het vorige beeld staan. Gegevensgat, geen themafout (koppelen via regel 2e). De L-foto heeft nog de alt "Loterij Lantaarn L InHuys" (bestaande alt, regel 4). |
| ballenbak | Alle vijf varianten (OLIJF, beige, roos, BLAUW, KAMEEL) tonen een eigen foto, ook bij laden. Olijf is nu echt een olijfgroene bak. De alt van het olijfbeeld is nog "Ballenbak beige InHuys" (gedeeld bestand, regel 4). Kleurnamen nog inconsistent (OLIJF, beige, roos, BLAUW, KAMEEL). |
| eetkamerstoel-sake | Opgelost voor vier kleuren; laden toont Oatly. |
| eetkamerstoel-japandi | Goed: vier kleuren, eigen foto en alt. Optienaam is nog Engels ("color"). |
| cloud-barstoel-creme | Goed (Crème en Karamel). |
| schommel-play-chill | Goed, vijf kleuren, eigen foto's. Optienaam "kleur" met kleine letter, waarden "beige", "lichtblauw" klein tegen "Kameel", "Olijf", "Roos". Roos-foto heeft alt "in Roze". |

### Mobiel: winkelwagen en checkout (iPhone 13, Octo-ketting Black Tiger L)

- Toevoegen: knop "Voeg toe aan winkelkar", lade met artikel, subtotaal, Uitchecken en Bekijk winkelwagen. Winkelwagen telt 1 (badge in header).
- `/cart`: plus brengt aantal 1 naar 2 (totaal 119,80), min terug naar 1, "Verwijderen" leegt de wagen ("Je winkelwagen is momenteel leeg", Recent bekeken blijft staan). Alles zonder fouten.
- Uitchecken leidt naar `/checkouts/cn/...` (InHuys Checkout, snelle checkout, contact, bezorging, verzendwijze zegt "Voer je bezorgadres in"); niets ingevuld. Console alleen 401/403 van Shopify zelf.
- Cookiebanner (Shopify) dekt op mobiel eerst twee derde van de pagina; na Accepteren werkt alles.

### Overig (punt 4 van de opdracht)

- Homepage: eerst h1 in server-HTML klopt (zie 10). `/collections`: h1 "Collectie". Winkelwagen: "Recent bekeken".
- Footer: Interieuradvies, Werkwijze, Showroom Purmerend, Projecten, Over InHuys, Contact, Veelgestelde vragen, Kinderkamer, Privacybeleid, Contactgegevens, Herroepen, telefoon, e-mail. Werkend: Interieuradvies, Contact, Privacybeleid, Contactgegevens (200). 404 in voorvertoning: Werkwijze, Showroom, Projecten, Over InHuys, Veelgestelde vragen, Kinderkamer, Herroepen (ongepubliceerd). Footer toont geen Retourbeleid of Voorwaarden.
- Levertijdzin: zie 9.

### JSON-LD (homepage, bank Londen, Raffles, Play & Chill, Flitsadvies, `/collections/all`, interieuradvies)

Alle blokken zijn geldige JSON. Homepage: Organization/LocalBusiness en WebSite, geen dubbelen meer. Producten: BreadcrumbList en Product met name, image, description, offers, `priceCurrency` EUR, `availability` InStock en prijs per variant (Londen 2 offers vanaf 4739,95; Raffles 3 vanaf 129,95; Play & Chill 5 vanaf 199,90). Fouten: **Flitsadvies `price` 0**; Product heeft telkens één `image`; broodkruimel Raffles en Play & Chill toont productnaam in de kruimel zonder collectie, Flitsadvies "Adviezen" (oude collectie), Play & Chill "rocking" (Engels producttype); Raffles-titel "maat S en L" terwijl er ook XL is.

### Nieuwe problemen door de aanpassingen

Geen verslechtering gevonden. Wel nieuw zichtbaar: (a) footerlink naar `/pages/herroepen` (404 tot publicatie); (b) hoofdmenu bevat nog `/collections/maatwerk` terwijl de homepage nu `kinderkamer` gebruikt; (c) `/pages/inspiratie` zonder h1; (d) Engelse producttype "rocking" in de broodkruimel en JSON-LD van Play & Chill. In de volledige-paginascreenshot van de winkelwagen (mobiel) lijkt de nieuwsbriefkop in de footer leeg: waarschijnlijk een scrollanimatie, niet bevestigd.

### Nog te doen (bijgewerkt)

| Nr | Punt | Ernst | Waar | Wie |
|---|---|---|---|---|
| 1 | Pagina's Projecten, Over InHuys, Werkwijze, Showroom, Veelgestelde vragen, Herroepen publiceren vóór of met het thema | blokkeert publicatie | pagina's | eigenaar (go-live), uitvoerder |
| 2 | Negen collecties publiceren; menu `/collections/maatwerk` vervangen of uit het menu; daarna tegels en beelden op de homepage toetsen | blokkeert publicatie | collecties, menu | eigenaar, uitvoerder |
| 3 | Retourbeleid, verzend- en algemene voorwaarden in Shopify (`/policies/refund-policy` 404) | blokkeert publicatie | Shopify-instelling | eigenaar |
| 4 | Flitsadvies: eigen titel, meta description, tekst; prijs 0 (ook JSON-LD) en winkelwagenknop herzien | blokkeert publicatie | product | schrijver, eigenaar (prijs) |
| 5 | Raffles XL: beeld aan variant koppelen; titel "maat S en L" nalopen | belangrijk | product (media, titel) | uitvoerder (regel 2e) |
| 6 | Cookiebanner mobiel: tekst Customer privacy inkorten (nu 68 procent van het scherm) | belangrijk | Shopify-instelling | eigenaar |
| 7 | Homepage-titel en -omschrijving (Voorkeuren), meta descriptions van `/collections`, `/collections/all`, contact en beleid; h1 op `/pages/inspiratie` | belangrijk | Shopify-instelling, thema/pagina | eigenaar, thema-agent |
| 8 | Levertijd: waarden `inhuys.levertijd` per merk bevestigen en vullen | belangrijk | product (metaveld) | eigenaar, uitvoerder |
| 9 | Verzendinfo in de checkout toetsen met een testadres | belangrijk | Shopify-instelling | eigenaar |
| 10 | Kleurnamen gelijktrekken: Ballenbak (Olijf, Beige, Roos, Blauw, Kameel), Play & Chill (Beige, Lichtblauw), optienaam Japandi "Kleur" | klein | product (optiewaarden) | uitvoerder (`productOptionUpdate`, regel 2e) |
| 11 | Producttypen opschonen ("rocking", Barstoel, Accessoires, Kinderkamer) zodat kruimel, JSON-LD en filter kloppen | klein | product (type) | schrijver, uitvoerder (regel 2a) |
| 12 | Alt-teksten "Loterij Lantaarn L" en "Ballenbak beige" (olijfbeeld) corrigeren | klein | bestandsalt | eigenaar beslist (regel 4: gedeelde bestanden) |
| 13 | Na publicatie opnieuw: collectietegels, footerlinks, menu, kruimels, cookiebanner op desktop | klein | testwerk | uitvoerder |
