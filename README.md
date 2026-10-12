# Inhuys · merk, SEO en productcontent

Werkmap voor de doorontwikkeling van de Shopify-winkel van Inhuys (www.in-huys.nl). Inhuys is een interieurstylistenbureau met webshop. Doel: uitgroeien tot hét merk waar mensen in het hogere segment naartoe gaan voor hun verbouwing, en hoog scoren in Google op producten en productgroepen.

## Werkwijze in fases

| Fase | Doel | Status |
|---|---|---|
| 1 | Analyseren en vastleggen. Niets aanpassen in de winkel. | Afgerond, met twee voorbehouden (zie *Blokkades*) |
| 2 | SEO-strategie en een vast template voor productpagina's | Voorstel staat klaar in `analyse/04-voorstel-fase-2.md` |
| 3 en verder | Uitvoering per productgroep, altijd eerst als concept | Nog te plannen |

## Vaste regels

- Informatie van fabrikanten is alleen een bron. Alle tekst wordt zelf geschreven, nooit gekopieerd.
- Niets gaat live en het live thema wordt niet aangepast zonder akkoord van de eigenaar.
- In fase 1 is er niets in de winkel gewijzigd. Alles in deze map is een alleen-lezen analyse.

## Bestanden

| Bestand | Inhoud |
|---|---|
| `brand-guide.md` | Merkkern, doelgroep, tone of voice, kleuren, typografie, beeldtaal, schrijfregels |
| `analyse/01-productoverzicht.md` | Wat er zichtbaar is van het assortiment, het auditkader per product en de kant-en-klare query om de volledige audit te draaien |
| `analyse/02-seo-scan.md` | Eerste SEO-scan: wat goed gaat, grootste kansen, prioriteiten |
| `analyse/03-huisstijl-voorstellen.md` | Voorstellen om de huisstijl te laten aansluiten bij het hogere segment |
| `analyse/04-voorstel-fase-2.md` | Voorstel voor fase 2: SEO-strategie en vast template voor productpagina's |
| `templates/productpagina-template.md` | Het template zelf, klaar om per product in te vullen |

## Blokkades in fase 1 en hoe je ze opheft

Twee bronnen waren in deze sessie niet bereikbaar. Daardoor zijn sommige onderdelen van fase 1 gebaseerd op zoekmachine-snippets in plaats van op de volledige winkel. Elk document markeert per onderdeel wat geverifieerd is en wat nog gecontroleerd moet worden.

1. **Shopify-koppeling verlopen.** De Shopify-connector vraagt om een nieuwe autorisatie. Zonder die koppeling zijn conceptproducten, meta-titels, meta-descriptions, alt-teksten en metavelden niet uitleesbaar. Oplossing: de Shopify-connector opnieuw autoriseren via de connector-instellingen in claude.ai.
2. **Netwerkbeleid blokkeert www.in-huys.nl.** De cloud-omgeving staat geen verbinding toe met de winkel zelf. Daardoor zijn kleuren, lettertypen, de volledige catalogus en de technische SEO-signalen niet direct uitgelezen. Oplossing: in de instellingen van de cloud-omgeving (titelbalk van de sessie, dan *Edit*) bij *Network access* het domein `www.in-huys.nl` toevoegen onder *Allowed domains*, of een ruimer toegangsniveau kiezen. Stappen: https://code.claude.com/docs/en/cloud-environments#network-access

Zodra één van beide is opgelost, kan de rest van fase 1 in een korte vervolgsessie worden afgerond. In `analyse/01-productoverzicht.md` staat precies welke query daarvoor klaarstaat.
