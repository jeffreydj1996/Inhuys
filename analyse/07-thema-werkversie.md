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
| `templates/page.inspiratie.json` | Inspiratie-pagina: ontbrekend woord in de introzin hersteld, knop 'View More' → 'Meer artikelen', artikelen uit blog Trends. |
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
