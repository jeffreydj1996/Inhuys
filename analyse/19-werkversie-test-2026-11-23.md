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
