# Inspiratie-artikelen (fase 2, stap 6)

Vier eigen artikelen, geschreven voor het inspiratiecluster uit `analyse/zoekwoorden.csv`. Ze staan als **concept** (niet gepubliceerd) in blog Trends (`gid://shopify/Blog/119658316115`) en worden pas zichtbaar na akkoord van de eigenaar. Elk artikel linkt naar één collectie, één of twee producten en de dienstpagina; die links worden gezet bij publicatie, zodra de doelpagina's live zijn.

| Artikel | Handle | Shopify-ID | Zoekterm | Woorden |
|---|---|---|---|---|
| Boucle onderhouden: zo blijft je bank of stoel jaren mooi | `boucle-onderhouden-zo-blijft-je-bank-mooi` | `gid://shopify/Article/617286107475` | boucle onderhouden · boucle stof voordelen nadelen | 506 |
| Eetkamerstoelen bij een ronde tafel: hoeveel passen er en welke werken | `eetkamerstoelen-bij-een-ronde-tafel` | `gid://shopify/Article/617286140243` | eetkamerstoelen combineren met ronde tafel · hoeveel stoelen om een tafel | 460 |
| Je interieur inrichten na een verbouwing | `interieur-inrichten-na-een-verbouwing` | `gid://shopify/Article/617286173011` | interieur na verbouwing inrichten | 413 |
| Travertijn in huis: hoe je het onderhoudt en waar het mooi staat | `travertijn-in-huis-onderhoud-en-combineren` | `gid://shopify/Article/617286205779` | travertin onderhouden | 348 |

Auteur: "Sylvana, InHuys" (ik-vorm past bij de pagina's over het bureau; de artikelen gebruiken "we"). Meta-titel en meta-description staan in de metavelden `global.title_tag` en `global.description_tag`. Beeld: nog geen artikelbeeld gekoppeld; advies per artikel een eigen foto uit een project of de showroom (geen stockbeeld).

## Voorstel: één blog in plaats van vier

De winkel heeft vier blogs: `nieuws` (0 artikelen), `trends` (1 gepubliceerd artikel plus deze 4 concepten), `woontips` (0) en `woontips-1` (1 artikel, "Stijlvol wonen met kinderen"). Vier blogs versnipperen de URL's (`/blogs/trends/…`, `/blogs/woontips-1/…`) en tonen lege lijstpagina's.

Voorstel voor fase 3, in deze volgorde en zonder iets te verwijderen in fase 2:

1. Blog `trends` hernoemen naar **Inspiratie** met handle `inspiratie`, zodat alle artikelen op `/blogs/inspiratie/…` komen. Dat sluit aan op de pagina Inspiratie en op de menukeuze in de thema-kopie.
2. Het artikel "Stijlvol wonen met kinderen" opnieuw aanmaken onder `inspiratie` en een redirect zetten van `/blogs/woontips-1/…` naar de nieuwe URL (redirect pas bij de uitvoering, samen met `analyse/redirects.csv`).
3. Het artikel "Woontrends 2025" actualiseren naar 2027 of verwijderen; de URL met een redirect naar het nieuwe artikel. Een jaartal in de URL veroudert.
4. De lege blogs `nieuws` en `woontips` pas verwijderen als 1 tot 3 klaar zijn en de redirects staan.
