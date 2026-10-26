# Conceptproducten per model (fase 2, stap 5)

Dertien nieuwe producten, één per model, allemaal met status **DRAFT** en nergens gepubliceerd (`resourcePublicationsCount` = 0). De bestaande kleurproducten zijn niet aangepast en blijven live tot de redirects in fase 3 worden gezet (`analyse/redirects.csv`, 47 regels). Teksten volgen `templates/productpagina-template.md`; feiten komen uit de huidige productdata, maten die niet uit eigen bron te halen waren staan als `[AANVULLEN]` in het bestand en zijn in Shopify leeg gelaten (de productpagina toont die rij dan niet).

| Model | Handle | Shopify-ID | Opties | Varianten | Beelden | Bron (oude producten) |
|---|---|---|---|---|---|---|
| Breeze eetkamerstoel met armleuning (set van 2) | `eetkamerstoel-breeze-set-van-2` | `gid://shopify/Product/11027132940627` | Kleur | 4 | 19 | 4 |
| Cloud eetkamerstoel (set van 2) | `eetkamerstoel-cloud-set-van-2` | `gid://shopify/Product/11027133038931` | Kleur | 5 | 15 | 5 |
| Cloud barkruk met rugleuning | `barkruk-cloud` | `gid://shopify/Product/11027133202771` | Hoogte · Kleur | 4 | 32 | 4 |
| Whale eetkamerstoel (set van 2) | `eetkamerstoel-whale-set-van-2` | `gid://shopify/Product/11027175571795` | Kleur | 2 | 16 | 2 |
| Luna eetkamerstoel (set van 2) | `eetkamerstoel-luna-set-van-2` | `gid://shopify/Product/11027175702867` | Kleur | 3 | 24 | 3 |
| Boog eetkamerstoel (set van 2) | `eetkamerstoel-boog-set-van-2` | `gid://shopify/Product/11027175833939` | Kleur | 2 | 16 | 2 |
| Scandi eetkamerstoel (set van 2) | `eetkamerstoel-scandi-set-van-2` | `gid://shopify/Product/11027175932243` | Kleur | 1 | 5 | 1 |
| Agano vaas van travertijn | `vaas-agano-travertijn` | `gid://shopify/Product/11027182879059` | Maat | 2 | 5 | 1 |
| Marmeren waxinelichthouder | `waxinelichthouder-marmer` | `gid://shopify/Product/11027182977363` | Maat | 3 | 5 | 1 |
| Boekensteun van mangohout | `boekensteun-mangohout` | `gid://shopify/Product/11027158434131` | Uitvoering | 1 | 2 | 1 |
| Bank Amsterdam | `bank-amsterdam` | `gid://shopify/Product/11027197755731` | Opstelling | 4 | 26 | 4 (concept) |
| Bank New York | `bank-new-york` | `gid://shopify/Product/11027220595027` | Opstelling · Kleur | 12 | 58 | 12 (concept) |
| Bank Londen | `bank-londen` | `gid://shopify/Product/11027197886803` | Opstelling · Kleur | 7 | 24 | 7 (concept) |

Per product gezet: titel, handle, merk, producttype, Shopify-categorie (taxonomie), tags, beschrijving in drie blokken, meta-titel en meta-description, `descriptor.short_description`, de metavelden `inhuys.*` (specificaties, advies, FAQ), varianten met de huidige prijzen en SKU's, en voor vazen, windlichten en decoratie de handmatige collectie. Stoelen, barkrukken en banken vallen automatisch in hun categoriecollectie via het producttype.

## Beelden en alt-teksten: wat er is gebeurd en wat er nog moet

Bij het aanmaken van de eerste drie producten (Breeze, Cloud, Cloud barkruk) bleek dat Shopify een beeld met een bestaande CDN-URL niet kopieert maar **hetzelfde bestand** koppelt dat het live product gebruikt. De alt-tekst is een eigenschap van dat bestand. De nieuwe alt-teksten die ik meegaf, kwamen daardoor ook op de 66 beelden van de dertien live kleurproducten terecht. Dat is binnen enkele minuten hersteld met `fileUpdate` naar de oorspronkelijke alt-teksten uit de export van vóór fase 2 (gecontroleerd per bestand); de teksten, prijzen en instellingen van die producten zijn niet aangeraakt. Bij een test met de boekensteun (alt weggelaten) wiste Shopify de alt; ook die twee bestanden zijn hersteld. Zichtbaar gevolg: de `updatedAt` van veertien live producten staat op 26 oktober 2026, 12:34 tot 12:39 uur. Inhoudelijk is er niets veranderd.

Voor de overige tien producten is de bestaande alt-tekst ongewijzigd meegegeven; daar is niets aan de live producten veranderd (gecontroleerd op `updatedAt`).

Gevolg voor de concepten: alle dertien producten delen hun beeldbestanden met de oude producten en tonen dus nog de oude alt-teksten. De beoogde alt-teksten per beeld staan in elk productbestand onder "Beelden". Toepassen in fase 3, zodra de oude producten op concept gaan en de redirects staan: dan kunnen de bestanden veilig een nieuwe alt krijgen (één `fileUpdate` per model).

## Opmerkingen uit de brondata

- "Breeze Stoel Beige" bevat een afwijkende variant "Pastelroze" van € 349,95 en "Luna stoel crème" een variant "Goud" van € 239,95; beide zijn niet overgenomen. Controleren of dit fouten zijn.
- SKU `71917285932` (New York 4-zits lounge rechts, zand boucle) mist vermoedelijk een cijfer; SKU `8719743533011` (Londen 6-zits met ottoman, umber) heeft er een te veel. SKU `7FCA77ABFB3DBD7B` (Cloud Safiya naturel) wijkt af van de EAN-reeks.
- De combinatie Londen 3-zits in tan zonder ottoman bestaat niet in de brondata en is niet aangemaakt.
- De beelden zijn 800 tot 1200 px; het template vraagt minimaal 2000 px. Nieuwe fotografie of originele leveranciersbeelden nodig.
- Productspecificaties van Pole To Pole (afmetingen, zithoogte, zitdiepte, gewicht, stofsamenstelling) zijn niet openbaar; aan te leveren door de eigenaar.

## Auditscore (zelfde script als fase 1)

| Product | Score | Reden dat het geen A is |
|---|---|---|
| Luna, Agano vaas | A | – |
| Breeze, Cloud, Cloud barkruk, Whale, Boog, Scandi, waxinelichthouder, boekensteun | B | Beelden kleiner dan 1000 px (gedeeld met de oude producten); bij de barkruk ontbreken 8 oude alt-teksten, bij Scandi en boekensteun zijn de oude alt-teksten per beeld gelijk. Allemaal beeldpunten die in fase 3 met nieuwe beelden en de beoogde alt-teksten verdwijnen. |
| Bank Amsterdam, New York, Londen | C | Geen afmetingen in de tekst: de maten per opstelling zijn niet uit eigen bron te halen en staan als `[AANVULLEN]`. Zodra de specificatiebladen er zijn, worden de metavelden gevuld en springt de score naar B of A. |

Geen enkel concept bevat sjabloontekst, een fabrikantzin, de u-vorm of Engels in de titel; alle dertien hebben meta-titel, meta-description, materiaal en specificatie-metavelden.
