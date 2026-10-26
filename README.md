# Inhuys · merk, SEO en productcontent

Werkmap voor de doorontwikkeling van de Shopify-winkel van Inhuys (www.in-huys.nl). Inhuys is een interieurstylistenbureau met webshop. Doel: uitgroeien tot hét merk waar mensen in het hogere segment naartoe gaan voor hun verbouwing, en hoog scoren in Google op producten en productgroepen.

## Werkwijze in fases

| Fase | Doel | Status |
|---|---|---|
| 1 | Analyseren en vastleggen. Niets aanpassen in de winkel. | **Afgerond** (12 oktober 2026). Alleen de controles die een browser vereisen staan nog open, zie hieronder. |
| 2 | SEO-strategie en een vast template voor productpagina's | **Uitgevoerd als concept** (26 oktober 2026). Alles staat in de repository en als ongepubliceerd concept in Shopify; statusblok en goedkeuringslijst in `analyse/04-voorstel-fase-2.md` |
| 3 en verder | Uitvoering per productgroep, altijd eerst als concept; go-live van de thema-kopie, redirects, resterende producten | Nog te plannen, start na akkoord op fase 2 |

## Vaste regels

- Informatie van fabrikanten is alleen een bron. Alle tekst wordt zelf geschreven, nooit gekopieerd.
- Niets gaat live en het live thema wordt niet aangepast zonder akkoord van de eigenaar.
- In fase 1 is er niets in de winkel gewijzigd. Alle Shopify-data is alleen gelezen; er is geen enkele mutatie uitgevoerd.
- In fase 2 zijn alleen nieuwe, ongepubliceerde objecten aangemaakt: een thema-kopie, collecties, pagina's, conceptproducten, artikelen, menu's en metaveld-definities. Live thema, live pagina's, live menu en live collecties zijn niet aangepast. Eén onbedoelde wijziging aan alt-teksten van live productbeelden is binnen enkele minuten hersteld; zie `content/producten/overzicht.md`.

## Bestanden

| Bestand | Inhoud |
|---|---|
| `brand-guide.md` | Merkkern, doelgroep, tone of voice, kleuren, typografie, beeldtaal, schrijfregels. Kleuren en lettertypen zijn uit het live thema uitgelezen. |
| `analyse/01-productoverzicht.md` | Volledig productoverzicht: aantallen, merken, prijzen, collecties, wat er per product ontbreekt, prioriteiten en beslispunten |
| `analyse/producten.csv` | Eén rij per product (177), alle auditvelden, puntkomma-gescheiden |
| `analyse/collecties.csv` | Eén rij per collectie (15) |
| `analyse/producten-samenvatting.md` | Automatisch gegenereerde teltabellen uit de twee CSV's |
| `analyse/02-seo-scan.md` | SEO-scan: wat goed gaat, grootste kansen, technische bevindingen uit het thema, prioriteiten |
| `analyse/03-huisstijl-voorstellen.md` | Voorstellen om de huisstijl te laten aansluiten bij het hogere segment, afgezet tegen de huidige thema-instellingen |
| `analyse/04-voorstel-fase-2.md` | Voorstel voor fase 2: SEO-strategie en vast template voor productpagina's |
| `templates/productpagina-template.md` | Het template zelf (v1.1, goedgekeurd 26 oktober 2026) |
| `analyse/05-seo-strategie.md` | SEO-strategie fase 2: baseline uit Search Console, doelen, drie pijlers, SERP-observaties, patronen voor titels en meta's, interne links, techniek, planning vanaf 27 oktober 2026 |
| `analyse/zoekwoorden.csv` | 69 zoektermen met cluster, intentie, doelpagina en prioriteit |
| `analyse/gsc/` | Exports uit Google Search Console van 26 oktober 2026 (dekking, HTTPS, prestaties) |
| `analyse/pagespeed-2026-10-26.md` | PageSpeed Insights homepage, mobiel en desktop, met acties |
| `analyse/08-search-console-api-2026-10-26.md` | Controle via de Search Console API: sitemapstatus, indexeringsstatus van alle 66 URL's, zoekopdrachten, acties |
| `analyse/06-collectiestructuur.md` | De tien categoriecollecties: regels, inleidingen, meta's, Shopify-ID's |
| `analyse/07-thema-werkversie.md` | Wijzigingslogboek van de thema-kopie (voor → na per bestand), preview-link |
| `analyse/redirects.csv` | Oude producthandle → nieuwe handle (47 regels), klaar voor fase 3; nog niet aangemaakt |
| `content/paginas/` | Eigen teksten voor Interieuradvies, Werkwijze, Showroom, Over InHuys, Projecten, Veelgestelde vragen en Contact |
| `content/producten/` | Dertien productteksten volgens het template, plus `overzicht.md` met Shopify-ID's en openstaande punten |
| `content/inspiratie/` | Vier inspiratie-artikelen, plus README met het voorstel om de vier blogs samen te voegen |

## Bronnen en wat nog open staat

De analyse is gebaseerd op de Shopify Admin API (producten, collecties, pagina's, blogs, menu's, verkoopkanalen en alle bestanden van het live thema) en op wat zoekmachines van www.in-huys.nl laten zien. De winkel zelf kon vanuit deze omgeving niet in een browser worden geopend (het netwerkbeleid van de cloud-omgeving blokkeert `www.in-huys.nl`). Daardoor staan drie controles nog open die alleen in een browser of in Google-tools kunnen:

1. **Google Search Console**: welke pagina's zijn echt geïndexeerd en is de sitemap aangemeld.
2. **PageSpeed Insights / Core Web Vitals** op de homepage, een collectie en een product.
3. **Rich Results Test** op een productpagina, om te bevestigen dat de productmarkup uit het thema foutloos wordt uitgelezen.

Stand na fase 2: Search Console is via de API gekoppeld (serviceaccount, alleen lezen) en samen met PageSpeed (rapport van de eigenaar) verwerkt; de Rich Results Test staat nog open voor de eigenaar zodra de thema-kopie live is. Alles wat via de API te controleren was, is gecontroleerd.
