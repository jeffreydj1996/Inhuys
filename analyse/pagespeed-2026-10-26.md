# PageSpeed Insights · homepage www.in-huys.nl

Gemeten door de eigenaar op 26 oktober 2026, 11:55 CET, Lighthouse 13.5.0. Veldgegevens (echte gebruikers): geen, te weinig verkeer. Alle waarden zijn labmetingen.

## Scores

| Categorie | Mobiel | Desktop |
|---|---|---|
| Prestaties | 80 | 94 |
| Toegankelijkheid | 91 | 91 |
| Praktische tips | 96 | 96 |
| SEO | 100 | 100 |

## Kernmetingen

| Meting | Mobiel (Moto G Power, langzame 4G) | Desktop | Drempel "goed" |
|---|---|---|---|
| First Contentful Paint | 2,2 s | 0,6 s | ≤ 1,8 s |
| Largest Contentful Paint | 3,9 s | 0,8 s | ≤ 2,5 s |
| Total Blocking Time | 30 ms | 20 ms | ≤ 200 ms |
| Cumulative Layout Shift | 0,031 | 0,011 | ≤ 0,1 |
| Speed Index | 6,5 s | 2,2 s | ≤ 3,4 s |

## Wat de meting zegt

- **Mobiel is de zwakke plek.** LCP 3,9 s en Speed Index 6,5 s zitten boven de drempels; desktop is uitstekend. De oorzaak is niet JavaScript-blokkering (TBT is laag) maar laadvolgorde en gewicht: renderblokkerende verzoeken (300 ms), meer dan vier preconnects, 244 KiB ongebruikt JavaScript, 16 KiB ongebruikte CSS, 3,2 s werk op de hoofdthread, 7 lange taken, 10 niet-samengestelde animaties.
- **Beeldlevering** kost op desktop 95 KiB; op mobiel 5 KiB. Bij het vervangen van de 800 px-beelden door grotere beelden moet dit bewaakt worden (WebP, juiste srcset, lazy loading onder de vouw).
- **Toegankelijkheid 91.** Twee concrete fouten: de viewport-meta in `layout/theme.liquid` staat op `maximum-scale=1.0, user-scalable=0` (zoomen onmogelijk), en de contrastverhouding van enkele tekst-achtergrondcombinaties is te laag. Ook: identieke links met hetzelfde doel. Beide eerste punten worden in de thema-kopie opgelost (viewport-meta aanpassen; kleurschema met voldoende contrast).
- **Praktische tips 96.** Browserfouten in de console, en ontbrekende beveiligingskoppen (CSP, HSTS, COOP). De koppen beheert Shopify; de consolefouten komen uit thema- of app-scripts en worden in de thema-kopie nagelopen.
- **SEO 100** en "de gestructureerde gegevens zijn geldig" bevestigen de bevinding uit fase 1 dat de technische basis van het thema klopt. De score zegt niets over de inhoud van titels, teksten en collecties; dat is het werk van fase 2 en 3.
- **WebMCP: vier formulieren zonder annotaties.** Nieuw en nog in ontwikkeling; geen actie nu.

## Acties die in fase 2 in de thema-kopie worden voorbereid

1. Viewport-meta herstellen naar `width=device-width, initial-scale=1` (toegankelijkheid).
2. Contrast van de kleurschema's controleren bij de goedgekeurde kleuren (tekst `#222222` op `#faf8f5` en op `#dfd5c7`; knoptekst wit op `#695b4d`).
3. Ongebruikte thema-secties en app-snippets die scripts laden (Judge.me, SocialShopWave, countdown, flash sale) niet renderen als ze niet gebruikt worden; preconnects beperken tot Shopify CDN en fonts.
4. Beeldregels in het template: minimaal 2000 px maar aangeleverd als WebP en via de thema-eigen responsive-image snippet.

Opnieuw meten na publicatie van de thema-kopie, op dezelfde drie pagina's (homepage, een collectie, een product).
