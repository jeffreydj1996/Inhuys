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

## Opmerkingen

- **Lettertype koppen.** Het voorstel noemde Cormorant Garamond als eerste keus. Die familie is niet als Shopify-fonthandle te verifiëren vanuit deze omgeving; EB Garamond (`ebgaramond_n5`, gewicht 500) staat wel in de Shopify-bibliotheek en is in de kopie ingesteld. Wil je Cormorant Garamond, dan is dat in de thema-editor een keuze van één klik onder Thema-instellingen → Typografie.
- **Plaatshouders.** Vervallen op 26 oktober 2026: het 3D-ontwerp staat op "prijs op aanvraag" tot de eigenaar de vanaf-prijs doorgeeft, en de showroom is alleen op afspraak.
- **Productpagina.** Het blok met specificaties leest de metavelden `inhuys.*` (afmetingen, zithoogte, zitdiepte, gewicht, materiaal frame, materiaal bekleding, kleur en afwerking, set-inhoud, onderhoud, herkomst, levertijd, garantie) en toont alleen gevulde rijen; 'Advies van InHuys' en de product-FAQ komen uit `inhuys.advies` en `inhuys.faq`. De korte zin onder de titel komt uit `descriptor.short_description`.
- **Controle.** Alle `themeFilesUpsert`-aanroepen gaven geen `userErrors`; de kopie heeft rol UNPUBLISHED; het live thema heeft dezelfde `updatedAt` als in de momentopname vóór fase 2 (zie `analyse/04-voorstel-fase-2.md`, statusblok).
