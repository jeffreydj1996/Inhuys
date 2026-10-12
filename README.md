# Inhuys · merk, SEO en productcontent

Werkmap voor de doorontwikkeling van de Shopify-winkel van Inhuys (www.in-huys.nl). Inhuys is een interieurstylistenbureau met webshop. Doel: uitgroeien tot hét merk waar mensen in het hogere segment naartoe gaan voor hun verbouwing, en hoog scoren in Google op producten en productgroepen.

## Werkwijze in fases

| Fase | Doel | Status |
|---|---|---|
| 1 | Analyseren en vastleggen. Niets aanpassen in de winkel. | **Afgerond** (12 oktober 2026). Alleen de controles die een browser vereisen staan nog open, zie hieronder. |
| 2 | SEO-strategie en een vast template voor productpagina's | Voorstel staat klaar in `analyse/04-voorstel-fase-2.md`, wacht op akkoord |
| 3 en verder | Uitvoering per productgroep, altijd eerst als concept | Nog te plannen |

## Vaste regels

- Informatie van fabrikanten is alleen een bron. Alle tekst wordt zelf geschreven, nooit gekopieerd.
- Niets gaat live en het live thema wordt niet aangepast zonder akkoord van de eigenaar.
- In fase 1 is er niets in de winkel gewijzigd. Alle Shopify-data is alleen gelezen; er is geen enkele mutatie uitgevoerd.

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
| `templates/productpagina-template.md` | Het template zelf, klaar om per product in te vullen |

## Bronnen en wat nog open staat

De analyse is gebaseerd op de Shopify Admin API (producten, collecties, pagina's, blogs, menu's, verkoopkanalen en alle bestanden van het live thema) en op wat zoekmachines van www.in-huys.nl laten zien. De winkel zelf kon vanuit deze omgeving niet in een browser worden geopend (het netwerkbeleid van de cloud-omgeving blokkeert `www.in-huys.nl`). Daardoor staan drie controles nog open die alleen in een browser of in Google-tools kunnen:

1. **Google Search Console**: welke pagina's zijn echt geïndexeerd en is de sitemap aangemeld.
2. **PageSpeed Insights / Core Web Vitals** op de homepage, een collectie en een product.
3. **Rich Results Test** op een productpagina, om te bevestigen dat de productmarkup uit het thema foutloos wordt uitgelezen.

Deze drie staan als eerste werk in fase 2. Alles wat via de API te controleren was, is gecontroleerd.
