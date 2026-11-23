# Thema-werkversie · wijzigingslogboek (fase 2, stap 3)

Datum: 26 oktober 2026 · Status: **werkversie, niet gepubliceerd**. Het live thema (Minimog 5.7.0, ID 200751743315) is niet aangeraakt.

| Onderdeel | Waarde |
|---|---|
| Thema-kopie | `InHuys · fase 2 werkversie (niet publiceren)` · `gid://shopify/OnlineStoreTheme/210233098579` · rol UNPUBLISHED |
| Voorvertoning | `https://www.in-huys.nl/?preview_theme_id=210233098579` (alleen ingelogd als eigenaar; conceptpagina's en conceptproducten geven in de voorvertoning een 404 tot ze gepubliceerd zijn) |
| Gekoppeld menu | `hoofdmenu-fase-2` (345749160275), `footer-inhuys` (345749225811), `footer-service` (345749258579); het live hoofdmenu is ongewijzigd |
| Generator | scratchpad `scripts/theme_build.py`; elk bestand is als geheel opnieuw gegenereerd uit het live bestand plus de wijzigingen hieronder, JSON-gevalideerd vóór `themeFilesUpsert` |
| Publiceren | Pas na een aparte 'publiceer'-opdracht van de eigenaar (`themePublish` is in fase 2 niet gebruikt) |

## Doorgevoerde huisstijl (goedgekeurd 26 oktober 2026)

| Sectie huisstijlvoorstel | Waar in het thema | Status |
|---|---|---|
| 0 Opruimen | header-group, footer-group, product.json, page.contact/collecties/inspiratie, settings_data | Gedaan |
| 1 Positionering en homepage-volgorde | index.json, hoofdmenu-fase-2 | Gedaan; projectenblok met plaatshouders tot er foto's zijn |
| 2 Naam en tagline `InHuys · ontwerp, advies en inrichting` | topbalk, footer, homepage-titel, LocalBusiness-markup | Gedaan |
| 3 Kleur | settings_data (kleurschema's) | Gedaan |
| 4 Typografie | settings_data: koppen EB Garamond 500, lopende tekst Jost, regelafstand 1,6 | Gedaan; zie opmerking lettertype |
| 5 Beeld | logo 150 px desktop; AI-kamerpreview blijft, gelabeld | Gedaan |
| 6 Assortimentslagen | collectie-per-categorie op homepage en collecties-pagina | Gedaan, gekoppeld aan de tien conceptcollecties |
| 7 Vertrouwen | footer met bedrijfsgegevens; snippet inhuys-schema (LocalBusiness, WebSite, BreadcrumbList) | Gedaan |
| 8 Tone of voice | alle thematekst in je-vorm, Nederlands, zonder kortingstaal | Gedaan |

## Wijzigingen per bestand (voor → na)

| Bestand | Wijziging |
|---|---|
| `config/settings_data.json` | Kleurschema's: gebroken wit #faf8f5 als achtergrond, zand #dfd5c7 als tweede vlak en footer, knop #695b4d (hover #4f4338), geen kortingsrood (actieprijs = tekstkleur), badges in merkbruin. |
| `config/settings_data.json` | Koppen: EB Garamond 500 uit de Shopify-fontbibliotheek (ebgaramond_n5) in plaats van de eigen Jost-upload; basisgrootte koppen 40 px. Lopende tekst en knoppen blijven Jost. |
| `config/settings_data.json` | Placeholder-sociallinks en neplabels verwijderd (WhatsApp blijft); telefoonnummer en e-mail ingevuld; cookiebanner licht en in het Nederlands. |
| `sections/header-group.json` | Aankondigingsbalk uit (tekst alvast Nederlands); topbalk toont de tagline en de showroom in plaats van 'Open Doors To A World Of Fashion'; logo 150 px; nieuw hoofdmenu 'hoofdmenu-fase-2'. |
| `sections/footer-group.json` | Footer: Nederlandse koppen, nieuwsbrief zonder kortingsbelofte, menu's 'InHuys' en 'Service', showroomadres en bedrijfsgegevens, betaaliconen aan, copyright met tagline. |
| `templates/index.json` | Homepage in de goedgekeurde volgorde: één slide met projectbeeld en twee knoppen; werkwijze in vier stappen; projectenblok met plaatshouders; collectie in negen categorietegels gekoppeld aan de nieuwe collecties; 'Ontwerp dat past' vertaald; Sylvana in je-vorm met link naar Over InHuys; showroomblok; inspiratie (blog Trends) ingeschakeld; adviesformulier als afsluiter. Verwijderd: 'New Arrivals'-slides, 'The Coastal Edition', productbundels, merkenlijst. |
| `templates/product.json` | Productpagina: labels in het Nederlands ('Maat', 'Op bestelling', 'Verwachte levering', verzendtekst zonder dollars); korte omschrijving onder de titel (metaveld descriptor.short_description); specificatietabel en 'Advies van InHuys' uit de inhuys-metavelden; FAQ-sectie ingeschakeld met productvragen uit metaveld inhuys.faq; 'Why Minimog?' vervangen door drie echte beloftes; 'Recently Viewed Products' → 'Recent bekeken'. |
| `templates/page.contact.json` | Contactpagina: Nederlandse introductie, telefoonveld aan, blokken met showroomadres en contactgegevens. |
| `templates/page.collecties.json` | Collecties-pagina: vier 'Example collection title'-tegels vervangen door de tien categoriecollecties; blok met de plaatshoudertekst 'lijst met collecties' uitgeschakeld. |
| `templates/page.inspiratie.json` | Inspiratie-pagina: ontbrekend woord in de introzin hersteld, knop 'View More' → 'Meer artikelen', artikelen uit blog Trends. Paginasectie 'main' weer aan: de paginatitel is de enige h1 en `page.content` staat boven het artikeloverzicht; de hero (letterlijke tekst `{{ page.content }}`, titel leeg) en de losse breadcrumb (zit al in de paginasectie) staan uit. De tekst komt later uit `content/paginas/inspiratie.md` op de Shopify-pagina. Toets 23 november 2026 (Playwright, voorvertoning, `Shopify.theme.id` 210233098579): één h1 'Inspiratie', `.m-page-content` aanwezig, blog-artikelen zichtbaar, geen lege thema-sectie (alleen de bestaande mobile-sticky-bar), geen `{{` in de tekst; consolefouten alleen van shop.app (CSP-frame) en een 403, niet van het thema. |
| `templates/page.interieuradvies.json` | Interieuradvies: dienstkaarten herschreven (3D-ontwerp met vanaf-prijs, Flitsadvies gratis), knoppen linken naar het aanvraagformulier op dezelfde pagina in plaats van naar de pagina zelf; 'Shop now' → 'Plan een Flitsadvies'. De paginatekst zelf (live) is niet gewijzigd. |
| `layout/theme.liquid` | Viewport-meta zonder zoomblokkade (toegankelijkheidsfout uit PageSpeed); snippet 'inhuys-schema' gerenderd in de head. |
| `snippets/inhuys-schema.liquid` | Nieuw: LocalBusiness-markup (naam, tagline als alternateName, adres showroom, telefoon, werkgebied), WebSite met SearchAction en BreadcrumbList voor product-, collectie-, pagina- en artikelpagina's. |

## Aanvulling 26 oktober 2026 (besluiten eigenaar)

| Bestand | Wijziging |
|---|---|
| `templates/page.interieuradvies.json` | Kaart 3D-interieurontwerp: "Prijs op aanvraag; het bedrag verrekenen we bij aankoop van de inrichting via InHuys." in plaats van de plaatshouder voor de vanaf-prijs |
| `sections/footer-group.json` | Showroomblok: regel "InHuys is een handelsnaam van Kluster" boven KvK en btw |
| `snippets/inhuys-schema.liquid` | LocalBusiness: `legalName` Kluster, `vatID`, KvK als `identifier`; openingstijden "alleen op afspraak, ook 's avonds; zaterdag in overleg" |

## Aanvulling 19 november 2026

| Bestand | Wijziging |
|---|---|
| `templates/product.json` | Nieuw blok 'Andere uitvoeringen' onder de korte omschrijving: leest `inhuys.hoofdproduct` en toont "Onderdeel van <titel>" met link, alleen als het hoofdproduct gepubliceerd en beschikbaar is; canonical ongewijzigd |

## Aanvulling 23 november 2026 (fase B, B1 t/m B7; alleen gebouwd, nog niet geüpload)

| Bestand | Wijziging |
|---|---|
| `config/settings_data.json` | B5: zoeksuggesties 'T-Shirt, Blue, Jacket' vervangen door Nederlandse categorieen (Eetkamerstoel, Bank, Fauteuil, Eettafel, Vaas). |
| `sections/footer-group.json` | B5: leeftijdscheck (age-verifier-popup, Engelse tekst 'Confirm your age') uit de footer-groep verwijderd. |
| `templates/index.json` | B5: projectenblok met plaatshouders ('[Project 1 · plaats]') uitgeschakeld (disabled) tot er echte projecten en foto's zijn; sectie blijft staan zodat de eigenaar hem later aanzet. |
| `templates/product.json` | B4: leverdatumblok ('Verwachte levering' met vaste 14 dagen en berekende datum) vervangen door blok 'levertijd_inhuys': toont 'Levertijd: <tekst>' uit het productmetaveld inhuys.levertijd en niets als dat leeg is; geen berekende datum. De rij 'Levertijd' is uit de specificatietabel gehaald om dubbel tonen te voorkomen. |
| `templates/product.json` | B6: tab 'Levering en retour' en FAQ 'Levering, retour en advies' gelijkgetrokken: 14 dagen bedenktijd na ontvangst, retourkosten voor de klant (pakket € 6,95, meubel € 49), maatwerk uitgezonderd, link naar /policies/refund-policy; geen 'in originele staat'; geen 'wettelijke termijn' meer zonder getal. |
| `layout/theme.liquid` | B7: noindex voor winkelwagen en zoeken (meta robots noindex als template 'cart' of 'search' bevat); zoeken en cart blijven bereikbaar, maar komen niet in de index. |
| `sections/image-with-text-2.liquid` | B7: de titel van de hero is nu een <h1> in plaats van <h2> (zelfde klassen, dus zelfde opmaak). Dit geeft /pages/interieuradvies ('Interieuradvies') en /pages/inspiratie een H1; op beide pagina's is de 'main'-paginasectie uitgeschakeld en staat er maar één hero aan. Er is geen page.json of andere hero-gebruiker in de kopie. |
| `templates/collection.json` | B3: merkenslider (sectie brands-list met mooisa, jesper-home en 28 andere kapotte links) verwijderd; B5: 'Recently Viewed Products' wordt 'Recent bekeken'. |
| `templates/collection.merk-collectie.json` | B5: 'Recently Viewed Products' wordt 'Recent bekeken'. |
| `sections/header.liquid` | B2: Minimog-blokken Organization (met sameAs vol lege social-links) en WebSite uit de header verwijderd; alleen snippet inhuys-schema levert nog Organization/LocalBusiness en WebSite. |
| `locales/nl.json` | B5: winkelwagenlade-knop 'Redden' (letterlijke vertaling van 'Save') wordt 'Opslaan'. |
| `snippets/inhuys-schema.liquid` | B1: breadcrumb-JSON geldig gemaakt: de titels gaan eerst door de json-filter in een eigen variabele (t_product, t_collection, t_page, t_blog, t_article) en worden daarna aan de string toegevoegd; product-URL in de kruimel is altijd /products/<handle>. Geldt voor product, collectie, pagina en artikel. |
| `snippets/inhuys-schema.liquid` | B2: een Organization-blok (type Organization + LocalBusiness) en een WebSite-blok; geen sameAs, want er zijn nog geen echte profielen (toevoegen zodra die er zijn). |

Nog te doen buiten het thema, voor de eigenaar of de pagina-inhoud:

- **Homepage-titel en -omschrijving (B7).** Het thema neemt ze uit Online Store, Voorkeuren; ze staan niet in `templates/index.json` of de config. Voorstel titel (51 tekens): `InHuys · interieuradvies en inrichting in Amsterdam`; omschrijving (136 tekens): `Gratis Flitsadvies en 3D-interieurontwerp voor je verbouwing. Meubels en decoratie bekijk je in onze showroom in Purmerend, op afspraak.`
- **H1 op /pages/interieuradvies (B7).** Opgelost in het thema (hero-titel `Interieuradvies` is nu een H1); de pagina-inhoud hoeft niet te wijzigen.
- **Retourtekst op de pagina Veelgestelde vragen.** Aangepast op 23 november 2026 in `content/paginas/veelgestelde-vragen.md` (r. 41): veertien dagen bedenktijd, retourkosten voor de klant (pakket € 6,95, meubel € 49), geen eis "in originele staat", link naar `/policies/refund-policy`. Als `pageUpdate` (alleen body) op `gid://shopify/Page/185596477779` gezet; de pagina is niet gepubliceerd.
- **Breadcrumb op pagina en artikel (B1).** De kopie bevat geen `templates/page.json` en geen artikelsectie; de snippet bedient beide pagina-typen met de gerepareerde JSON, maar de eigen JSON-LD van de artikelsectie (`Article`) kon niet worden nagekeken.
- **sameAs (B2).** Weggelaten; toevoegen zodra er echte profielen zijn.
- **B4.** Het blok toont alleen iets als het metaveld `inhuys.levertijd` per product gevuld is; de eigenaar moet de waarden per merk bevestigen.
- **Upload.** Nieuwe of gewijzigde bestanden voor `themeFilesUpsert`: zie `data/out/theme-vars-4.json` (nieuw) en de bestaande batches 1 tot en met 3.

## Opmerkingen

- **Lettertype koppen.** Het voorstel noemde Cormorant Garamond als eerste keus. Die familie is niet als Shopify-fonthandle te verifiëren vanuit deze omgeving; EB Garamond (`ebgaramond_n5`, gewicht 500) staat wel in de Shopify-bibliotheek en is in de kopie ingesteld. Wil je Cormorant Garamond, dan is dat in de thema-editor een keuze van één klik onder Thema-instellingen → Typografie.
- **Plaatshouders.** Vervallen op 26 oktober 2026: het 3D-ontwerp staat op "prijs op aanvraag" tot de eigenaar de vanaf-prijs doorgeeft, en de showroom is alleen op afspraak.
- **Productpagina.** Het blok met specificaties leest de metavelden `inhuys.*` (afmetingen, zithoogte, zitdiepte, gewicht, materiaal frame, materiaal bekleding, kleur en afwerking, set-inhoud, onderhoud, herkomst, levertijd, garantie) en toont alleen gevulde rijen; 'Advies van InHuys' en de product-FAQ komen uit `inhuys.advies` en `inhuys.faq`. De korte zin onder de titel komt uit `descriptor.short_description`.
- **Controle.** Alle `themeFilesUpsert`-aanroepen gaven geen `userErrors`; de kopie heeft rol UNPUBLISHED; het live thema heeft dezelfde `updatedAt` als in de momentopname vóór fase 2 (zie `analyse/04-voorstel-fase-2.md`, statusblok).

- **Kaarten Interieuradvies en merkcollectie (23 november 2026).** `templates/page.interieuradvies.json`: het veld `button_link` staat niet in het schema van `text_card_with_image` (alleen `link`); beide kaarten (3D-ontwerp, Flitsadvies) gebruiken nu `link` naar `/pages/interieuradvies#shopify-section-17709804707992f0a4` (het formulier). `templates/collection.merk-collectie.json`: bannerblok "SALE UP TO 25% OFF" verwijderd. Beide bestanden met `themeFilesUpsert` naar de kopie (rol voor en na UNPUBLISHED, geen `userErrors`) en teruggelezen; de `link`-waarden staan erin.

- **Uitvoeringen per modelgroep (23 november 2026).** Nieuw snippet `snippets/inhuys-uitvoeringen.liquid` met een vaste lijst modelgroepen in Liquid (geen metavelden), gerenderd door het blok `uitvoeringen_inhuys` in `templates/product.json` (de oude regel 'Onderdeel van <hoofdproduct>' blijft eronder staan). Kleuren blijven varianten; andere opstellingen of maten zijn knoppen naar `/products/<handle>`. De knop van het huidige product is gevuld; andere knoppen verschijnen alleen als `all_products[handle]` bestaat en `available` is; de rij verschijnt bij minstens twee knoppen. Groepen (alleen ACTIEVE producten):
  - Bank Londen: `bank-londen-3-zits-ottoman-umber` (3-zits met ottoman), `bank-londen-6-zits-tan` (6-zits), `bank-londen-6-zits-ottoman` (6-zits met ottoman)
  - Bank New York: `bank-new-york` (2,5-zits lounge), `bank-new-york-4-zits-lounge-beige`, `bank-new-york-4-zits-lounge-coco`
  - Cloud: `cloud-kitchen-barstoel-creme` (Keukenbarkruk), `cloud-barstoel-creme` (Barkruk), `cloud-stoel-creme-set-van-2` (Eetkamerstoel)
  - Japandi: `eetkamerstoel-japandi` (Eetkamerstoel), `barkruk-japandi-tan-set-van-2` (Barkruk); Sake, Osaka en Fuji zijn eigen modellen en staan niet in een groep
  - Jumpspot: `springplek-binnen`, `jumpspot-buiten`, `hoes-jumpspot-binnen`, `hoes-jumpspot-buiten`
  - Glijbanen: `holzrutsche-binnen` (binnen), `glijbaan-white-dolphin` (buiten)
  - Octo-kettingen: `octo-ketting-zwart-wit-s` (Maat S), `octo-ketting-black-tiger` (Maat L)
  - Schelpenkettingen: `schelpenketting-j63`, `-j69`, `-j47`, `-j65`, `-j66`, `-j37`, `-h1` (label = code)
  Avena, Mera en Nox zijn aparte modellen en staan er niet in. Groep wijzigen: `UITV_GROEPEN` in `tools/theme_build.py`.

## Spoor A · werkplan werkversie (23 november 2026, uitgevoerd op de kopie 210233098579)

Alle wijzigingen staan in `tools/theme_build.py` (log-regel per wijziging in `data/out/theme-changelog.json`), zijn als bestand geüpload met `themeFilesUpsert` (userErrors leeg) en teruggelezen via `checksumMd5`. Rol van het thema bij elke stap: UNPUBLISHED. Niets gepubliceerd, geen producten, collecties of menu's gewijzigd. Voorheen bewaard in `data/out/theme-vorig`.

### 1 · Variantfoto's (T5, nr 8)

- **Oorzaak.** Het wisselen zelf werkt: bij het kiezen van een variant zet `product-media.js` (`setActiveMediaForSlider`) de slide op `variant.featured_media.position`. Het ging mis bij het laden: `show_featured_media` stond aan in `templates/product.json`, waardoor `product-info.js` bij het laden `updateMedia` overslaat en de galerij de eerste foto van het product toont in plaats van de foto van de gekozen standaardvariant. Dat verklaart bank Londen (Umber toont de tan-foto), bank New York (Coco toont de beige foto), Raffles S (toont de L-foto) en Ballenbak (roos toont beige). Voor de gekozen kleur zelf is geen alt-tekst nodig: de galerij leest `featured_media`. `enable_variant_group_images` (groeperen op het metaveld `foxecom-bs-kit.variant-images`) stond wel aan maar het metaveld bestaat niet, dus die route werd nooit gebruikt.
- **Wijziging.** `templates/product.json`, sectie `main`: `show_featured_media` uit en `enable_variant_group_images` uit.
- **Toets** (Playwright, voorvertoning, `Shopify.theme.id` 210233098579, desktop 1366 en mobiel iPhone 13). Bank Londen 6-zits, bank New York, lantaarn Raffles, Ballenbak en eetkamerstoel Sake: bij het laden en na het kiezen van elke variant (heen en terug) is het grote beeld het `featured_image` van die variant: bij vier producten kloppen alle varianten, bij Raffles S en L (XL: zie hieronder); mobiel Ballenbak (10 van 10) en bank New York (4 van 4) gelijk. Uitzondering: **Raffles XL heeft in Shopify geen `featured_image`** (`/products/lantaarn-raffles.js`); het thema laat dan de vorige foto staan. Dat is een gegevensgat in het product (beeld koppelen aan XL, regel 2e), niet te verhelpen in het thema.

### 2 · Homepage (T2/T4, T11, nr 20)

- `templates/index.json`: de negen tegels verwijzen naar `banken`, `stoelen`, `fauteuils`, `barkrukken`, `tafels`, `vazen`, `windlichten-en-kaarsenhouders`, `decoratie`, `kinderkamer` (was `maatwerk` in plaats van `kinderkamer`). `templates/page.collecties.json`: dezelfde negen.
- **Echte oorzaak plaatshouders.** De tegel nam alleen het tegelbeeld uit de sectie (`item_image`) en viel nooit terug op het collectiebeeld: ook na publicatie van de collecties bleef de grijze plaatshouder staan. `snippets/collection-card.liquid` valt nu terug op het collectiebeeld en anders op de hoofdfoto van het eerste product. In de voorvertoning tonen ze nog de plaatshouder, omdat de collecties ongepubliceerd zijn (`collections['banken']` is dan leeg); dit is dus pas na publicatie te zien.
- **Lege links.** Vier lege `button_link` (stappen werkwijze) en één lege `link`: de stappen hebben ook geen `button_label`, dus er wordt geen knop of link gerenderd; `image_link` en `footer_link` van de hero en `link`/`link_2` van Sylvana zijn leeg zonder dat er een element mee wordt gemaakt. Niets te verbergen of in te vullen.
- **h1.** `sections/slider.liquid`: de titel van de eerste slide op de homepage is een `<h1>`. `snippets/header-logo.liquid`: het logo was op de homepage de h1 (een afbeelding zonder tekst, vandaar "h1 leeg"); het is nu een `<div>`. De server-HTML heeft één h1: "Een verbouwing is pas af als de ruimte klopt". (In de browser staan door de kloon van de slider drie kopieën; dat is gedrag van de slider.)

### 3 · /collections (T3, nr 5)

`templates/list-collections.json`: kop "Collectie", intro "Van banken en stoelen tot vazen en kinderkamer. Kies een categorie en bekijk wat InHuys voor je heeft geselecteerd. Weet je niet waar je moet beginnen? Plan een adviesgesprek.", weergave "Geselecteerd" met de negen categoriecollecties, geen aantal producten. Getoetst: h1 "Collectie", negen kaarten, geen demotekst. De oude live collecties (Adviezen, Amsterdam, Bestsellers ...) staan er niet meer op. De kaarten tonen na publicatie het collectiebeeld (zie 2).

### 4 · Engelse en demotekst (T7, nr 21)

- `templates/cart.json`: "Recently Viewed Products" kwam uit de schema-standaardtekst; nu "Recent bekeken". Winkelwagen getoetst.
- `templates/blog.json`: "Blog posts" wordt "Inspiratie", "View More" wordt "Meer artikelen", zijbalk "Categories" en "Recent Post" worden "Categorieën" en "Recente artikelen".
- `locales/nl.json`: u-vorm naar je-vorm en foute vertalingen: "Register" (nu "Account aanmaken"), "Dashboard" ("Overzicht"), demotekst bij registreren over uitverkoop en nieuwkomers, "Links" ("beschikbaar"), "in kar", "In zoomen", "Product kwantiteit", "/ea", "Dichtbij" ("Sluiten"), "Toneelstuk" ("Afspelen"), "Rug" ("Terug"), Minimog in de blogtag, XR-knop, kortingsmeldingen. Nog u-vorm in schermen die InHuys niet gebruikt (account, adressen, cadeaubon, reactieformulier, contactformulier-melding); die staan niet in de winkelroute en zijn niet aangepast.
- Gescand: alle JSON-templates, `locales/nl.json` tegenover `en.default.json` en de gerenderde voorvertoning (home, collecties, product, blog, zoeken, contact, login, registreren, winkelwagen, 404, interieuradvies, inspiratie). Niet aangepast: harde aria-labels in snippets ("Previous", "Next", "Close", niet zichtbaar), "Shop Pay" (merknaam), sectienamen in de editor.
- **Demo-instellingen** (`config/settings_data.json`): `cart_estimate_shipping` en `show_delivery_days` uit (ze tonen tarieven en bezorgdagen die de eigenaar nog niet heeft bevestigd; de checkout toont de echte verzendkosten na het adres); `use_theme_currencies` uit en `theme_currencies` "EUR" (was "USD | EUR | GBP | VND"; de valutawisselaar werd niet getoond).

### 5 · Levertijdzin (T8, nr 10)

`templates/product.json`: de tab "Levering en retour" en de FAQ "Levering, retour en advies" zijn liquid-blokken geworden. De zin "De levertijd staat bij het product." staat er alleen als `inhuys.levertijd` gevuld is; anders ontbreekt hij. De toevoeging "zodra die bekend is" is vervallen, want als het metaveld gevuld is, is de tijd bekend. Getoetst op bank New York en Raffles (metaveld leeg): zin niet aanwezig, retourtekst wel.

### 6 · Cookiebanner mobiel (T13, nr 13)

De banner zit in het thema (`snippets/cookie-banner.liquid`, tekst in `config/settings_data.json`), niet in Customer privacy. `snippets/cookie-banner.liquid`: onder 768 px tekst 13 px, minder vulling, de knoppen naast elkaar over de volle breedte. Gemeten op iPhone 13: banner 122 px hoog van 664 px (18 procent van het scherm; eerder meer dan de helft). De zwarte voorbeeldbalk van de voorvertoning blijft op desktop de knoppen afdekken (geen themafout). Of de banner ook uit Shopify Customer privacy komt, is niet te zien vanuit het thema.

### Gewijzigde bestanden (spoor A)

`config/settings_data.json`, `locales/nl.json`, `templates/index.json`, `templates/page.collecties.json`, `templates/product.json`, `templates/list-collections.json`, `templates/cart.json`, `templates/blog.json`, `sections/slider.liquid`, `snippets/collection-card.liquid`, `snippets/header-logo.liquid`, `snippets/cookie-banner.liquid`. Bronkopieën van ongewijzigde Minimog-bestanden voor de bouw staan nu ook in `data/theme-origineel/` (`sections/slider.liquid` bestond al; nieuw: `templates/cart.json`, `snippets/collection-card.liquid`, `snippets/cookie-banner.liquid`).

### Broodkruimel op productpagina (23 november)

`snippets/breadcrumb.liquid` en `snippets/inhuys-schema.liquid`: de broodkruimel en de BreadcrumbList kiezen op een productpagina eerst de collectie uit de URL (klant komt via een collectie), anders de eerste collectie van het product met een handle uit `banken`, `stoelen`, `fauteuils`, `barkrukken`, `tafels`, `vazen`, `windlichten-en-kaarsenhouders`, `decoratie`, `kinderkamer`; staat het product in geen van die negen, dan alleen Home, (merk) en productnaam. Voorheen `product.collections.first`, vaak een modelcollectie (rocking, whale, cloud, luna). Geüpload naar de kopie (userErrors leeg, teruggelezen, rol UNPUBLISHED). Getoetst in de voorvertoning (Shopify.theme.id 210233098579) op schommel-play-chill, whale-stoel-coco-set-van-2 en bank-new-york: geen modelcollectie meer; omdat de categoriecollecties nog ongepubliceerd zijn staat er Home, merk, productnaam en in de JSON-LD Home, productnaam; geen Liquid-fouten. De merkschakel (vendor) in de zichtbare kruimel is niet gewijzigd. Na publicatie van de collecties verschijnt de categorie vanzelf.
