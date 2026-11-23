# Collecties controle vóór publicatie · 19 november 2026

Bron: `tools/collections.py`, `data/ids.json` (collecties), `data/orderchamp/voorraad-2026-11-19.csv`, producttypes en titels uit `data/out/productSet-<handle>.json` (voor de 6 live producten zonder bestand, o.a. Breeze en Safiya: `data/raw`). Peildatum: 27 actieve producten (26 via Orderchamp, plus Flitsadvies) en de 56 producten uit `analyse/12-voorstel-live-zetten.md`, samen 83. Regels voor titel en type zijn gelezen zoals ze na de go-live in Shopify staan (titel en type uit onze tekst).

## Overzicht

| Collectie | Soort | Live producten erin | Waarvan nu al actief |
|---|---|---|---|
| banken | automatisch type Banken | 7 | 0 |
| stoelen | automatisch type Stoelen | 35 | 17 |
| fauteuils | automatisch titel | 1 | 0 |
| barkrukken | automatisch type Barstoel of Keukenbarstoel | 5 | 4 |
| tafels | automatisch type Tafels | 4 | 0 |
| vazen | handmatig, 4 id | 3 | 0 |
| windlichten-en-kaarsenhouders | handmatig, 7 id | 2 | 0 |
| decoratie | handmatig, 11 id | 2 | 0 |
| maatwerk | handmatig, 0 id | 0 | 0 |
| kinderkamer | automatisch merk Jupiduu | 14 | 5 |

## Wijzigingen nodig vóór publicatie

Alle wijzigingen zijn `collectionUpdate` op de tien ongepubliceerde concept-collecties (ruleSet of productenlijst); ze raken geen product en geen live object. Publiceren zelf (`publishablePublish`) is een go-live-stap en vraagt `INHUYS_GOLIVE=1`.

1. **Vazen**: Agano (`9957680054611`) staat op concept sinds het besluit van 19 november en heeft geen vervanger; uit de lijst halen. Daarna 3 producten (Bubble, Meduse, Swoop).
2. **Windlichten en kaarsenhouders**: uit de lijst halen: `marmer-waxinelichthouder` (concept), Atlas en Soleil (concept, geen voorraad en tekst), `loterijen-lantaarn-m` (concept) en `lantaarn-raffles-s` (staat op kan-weg; `lantaarn-raffles` zit er al in). Daarna 2 producten (Raffles, Peninsula); een collectie van twee is dun, zie de beslissing hieronder.
3. **Decoratie**: uit de lijst halen: `krab-l` en `j72-shell-toren-parel-s` (kan-weg; `schelpentoren-pearl` zit er al in), `boekhouder`, `bowl-babi-m`, `mand-miso-set-van-3`, `messing-dodo-m`, `messing-dodo-s`, `juju-rasta`, `krab-messing` (allemaal concept). Daarna 2 producten (Babi, Pearl).
4. **Kettingen**: 9 producten die live gaan (7 schelpkettingen, 2 octo-kettingen, type Decoratie) vallen in geen enkele collectie, want `collections.py` laat ze bewust weg. Voorstel: toevoegen aan Decoratie (de collectie heeft dan 11 producten) en de inleiding één zin laten noemen dat er kettingen van schelp en hout zijn; of een elfde collectie Kettingen. Keuze voor de eigenaar (collectietekst is zijn goedgekeurde tekst).
5. **Fauteuils**: de titelregel (fauteuil, Loungestoel, Lounge Chair) vangt alleen Cairo. Omzetten naar `TYPE EQUALS Fauteuils` (Cairo heeft dat type al; de notitie in `collections.py` vraagt dit ook) maakt de collectie robuuster zodra Kathmandu, Mars en Panda voorraad hebben. Eén product bij publicatie.
6. **Maatwerk**: leeg. Niet publiceren (en niet in het menu) tot er projectfoto's en voorbeelden zijn, of de pagina tonen zonder productraster.
7. **Stoelen**: de regel `TYPE Stoelen` vangt 35 live producten, waaronder de 6 dubbelen die volgens `analyse/12-voorstel-live-zetten.md` naar concept gaan; die verdwijnen vanzelf uit de winkel zodra ze concept zijn. Geen wijziging nodig, wel de volgorde: eerst dubbelen naar concept, dan collecties publiceren.
8. **Flitsadvies** (dienst, type Accessoires) hoort in geen collectie; dat is zo bedoeld.
9. Banken, Tafels, Barkrukken en Kinderkamer: geen wijziging. Barkrukken bevat de 4 live Cloud-krukken en de Japandi-barkruk tan; de twee Japandi-keukenbarkrukken blijven concept (geen voorraad).

Dunne collecties na de wijzigingen: Fauteuils 1, Windlichten 2, Decoratie 2 (of 11 met de kettingen), Maatwerk 0. De eigenaar beslist of die bij de eerste publicatie meegaan.

## banken

| Product (geplande handle) | Type | Status na go-live | Voorraad |
|---|---|---|---|
| `bank-amsterdam` | Banken | nieuw live | 100 |
| `bank-londen-3-zits-ottoman-umber` | Banken | nieuw live | 100 |
| `bank-londen-6-zits-ottoman` | Banken | nieuw live | 200 |
| `bank-londen-6-zits-tan` | Banken | nieuw live | 200 |
| `bank-new-york` | Banken | nieuw live | 28 |
| `bank-new-york-4-zits-lounge-beige` | Banken | nieuw live | 11 |
| `bank-new-york-4-zits-lounge-coco` | Banken | nieuw live | 11 |

## stoelen

| Product (geplande handle) | Type | Status na go-live | Voorraad |
|---|---|---|---|
| `breeze-stoel-beige-set-van-2` | Stoelen | nu al live | 0 |
| `breeze-stoel-latte-set-van-2` | Stoelen | nu al live | 0 |
| `breeze-stoel-pastel-roze-set-van-2` | Stoelen | nu al live | 0 |
| `breeze-stoel-pistache-set-van-2` | Stoelen | nu al live | 0 |
| `cloud-stoel-safiya-naturel-set-van-2` | Stoelen | nu al live | 0 |
| `cloud-stoel-safiya-terracotta-set-van-2` | Stoelen | nu al live | 0 |
| `draaistoel-pebble` | Stoelen | nieuw live | 200 |
| `draaistoel-storm` | Stoelen | nieuw live | 186 |
| `eetkamerstoel-avena-set-van-2` | Stoelen | nieuw live | 331 |
| `eetkamerstoel-boog-creme-set-van-2` | Stoelen | nu al live | 55 |
| `eetkamerstoel-boog-karamel-set-van-2` | Stoelen | nu al live | 3 |
| `eetkamerstoel-cloud-beige-set-van-2` | Stoelen | nu al live | 86 |
| `eetkamerstoel-cloud-karamel-set-van-2` | Stoelen | nu al live | 0 |
| `eetkamerstoel-cloud-set-van-2` | Stoelen | nu al live | 0 |
| `eetkamerstoel-edo-reddish-set-van-2` | Stoelen | nieuw live | 200 |
| `eetkamerstoel-egg-set-van-2` | Stoelen | nieuw live | 200 |
| `eetkamerstoel-fjord-set-van-2` | Stoelen | nieuw live | 100 |
| `eetkamerstoel-fuji` | Stoelen | nieuw live | 343 |
| `eetkamerstoel-high-five-set-van-2` | Stoelen | nieuw live | 215 |
| `eetkamerstoel-japandi` | Stoelen | nieuw live | 1847 |
| `eetkamerstoel-luna-creme-set-van-2` | Stoelen | nu al live | 200 |
| `eetkamerstoel-luna-set-van-2` | Stoelen | nu al live | 0 |
| `eetkamerstoel-mera-karamel-set-van-2` | Stoelen | nieuw live | 334 |
| `eetkamerstoel-mera-set-van-2` | Stoelen | nieuw live | 121 |
| `eetkamerstoel-nox-umber-set-van-2` | Stoelen | nieuw live | 200 |
| `eetkamerstoel-osaka` | Stoelen | nieuw live | 488 |
| `eetkamerstoel-rainbow-coco-set-van-2` | Stoelen | nieuw live | 241 |
| `eetkamerstoel-rock-set-van-2` | Stoelen | nieuw live | 500 |
| `eetkamerstoel-sake` | Stoelen | nieuw live | 403 |
| `eetkamerstoel-scandi-set-van-2` | Stoelen | nu al live | 648 |
| `eetkamerstoel-wave-set-van-2` | Stoelen | nieuw live | 100 |
| `eetkamerstoel-whale-beige-set-van-2` | Stoelen | nu al live | 100 |
| `eetkamerstoel-whale-set-van-2` | Stoelen | nu al live | 200 |
| `eetkamerstoel-wing-set-van-2` | Stoelen | nieuw live | 100 |
| `luna-chair-mink-set-van-2` | Stoelen | nu al live | 0 |

## fauteuils

| Product (geplande handle) | Type | Status na go-live | Voorraad |
|---|---|---|---|
| `fauteuil-cairo` | Fauteuils | nieuw live | 100 |

## barkrukken

| Product (geplande handle) | Type | Status na go-live | Voorraad |
|---|---|---|---|
| `barkruk-cloud` | Barstoel | nu al live | 100 |
| `barkruk-cloud-barkruk-creme` | Barstoel | nu al live | 100 |
| `barkruk-cloud-barkruk-karamel` | Barstoel | nu al live | 0 |
| `barkruk-cloud-keukenbarkruk-karamel` | Barstoel | nu al live | 0 |
| `barkruk-japandi-tan-set-van-2` | Barstoel | nieuw live | 400 |

## tafels

| Product (geplande handle) | Type | Status na go-live | Voorraad |
|---|---|---|---|
| `eettafel-ellipse` | Tafels | nieuw live | 6 |
| `eettafel-urban-chique` | Tafels | nieuw live | 11 |
| `ronde-eettafel-urban-chique` | Tafels | nieuw live | 3 |
| `salontafel-craft` | Tafels | nieuw live | 100 |

## vazen

| Product (geplande handle) | Type | Status na go-live | Voorraad |
|---|---|---|---|
| `vaas-bubble` | Vazen | nieuw live | 17 |
| `vaas-meduse` | Vazen | nieuw live | 73 |
| `vaas-swoop-set-van-6` | Vazen | nieuw live | 12 |

Handmatige lijst:

| Product-id | Huidige handle | Status | Oordeel |
|---|---|---|---|
| 9957680054611 | `travertine-agano-vaas` | DRAFT | blijft concept: uit lijst halen of nog live zetten |
| 10447094219091 | `vaas-bubble` | DRAFT | gaat live |
| 10447094317395 | `vaas-meduse` | DRAFT | gaat live |
| 10447094284627 | `vaas-swoop-set-van-6` | DRAFT | gaat live |

## windlichten-en-kaarsenhouders

| Product (geplande handle) | Type | Status na go-live | Voorraad |
|---|---|---|---|
| `lantaarn-peninsula` | Decoratie | nieuw live | 47 |
| `lantaarn-raffles` | Decoratie | nieuw live | 37 |

Handmatige lijst:

| Product-id | Huidige handle | Status | Oordeel |
|---|---|---|---|
| 9966390739283 | `marmer-waxinelichthouder` | DRAFT | blijft concept: uit lijst halen of nog live zetten |
| 10447095628115 | `keramische-kaarsenhouder-atlas-set-van-2` | DRAFT | blijft concept: uit lijst halen of nog live zetten |
| 10447101067603 | `keramische-kaarsenhouder-soleil-set-van-2` | DRAFT | blijft concept: uit lijst halen of nog live zetten |
| 10447097463123 | `lantaarn-raffles` | DRAFT | gaat live |
| 10447097528659 | `lantaarn-raffles-s` | DRAFT | STAAT OP KAN WEG, blijft: `lantaarn-raffles` |
| 10447097233747 | `loterijen-lantaarn-m` | DRAFT | blijft concept: uit lijst halen of nog live zetten |
| 10447098184019 | `lantaarn-peninsula` | DRAFT | gaat live |

## decoratie

| Product (geplande handle) | Type | Status na go-live | Voorraad |
|---|---|---|---|
| `schaal-babi` | Decoratie | nieuw live | 27 |
| `schelpentoren-pearl` | Decoratie | nieuw live | 173 |

Handmatige lijst:

| Product-id | Huidige handle | Status | Oordeel |
|---|---|---|---|
| 9978474430803 | `boekhouder` | DRAFT | blijft concept: uit lijst halen of nog live zetten |
| 10447094186323 | `schaal-babi` | DRAFT | gaat live |
| 10447094251859 | `bowl-babi-m` | DRAFT | blijft concept: uit lijst halen of nog live zetten |
| 10447101264211 | `mand-miso-set-van-3` | DRAFT | blijft concept: uit lijst halen of nog live zetten |
| 10447095857491 | `messing-dodo-m` | DRAFT | blijft concept: uit lijst halen of nog live zetten |
| 10447100543315 | `messing-dodo-s` | DRAFT | blijft concept: uit lijst halen of nog live zetten |
| 10447096185171 | `juju-rasta` | DRAFT | blijft concept: uit lijst halen of nog live zetten |
| 10447102935379 | `krab-l` | DRAFT | STAAT OP KAN WEG, blijft: `krab-messing` |
| 10447102640467 | `krab-messing` | DRAFT | blijft concept: uit lijst halen of nog live zetten |
| 10447097692499 | `j72-shell-toren-parel-s` | DRAFT | STAAT OP KAN WEG, blijft: `schelpentoren-pearl` |
| 10447097725267 | `schelpentoren-pearl` | DRAFT | gaat live |

## maatwerk

Geen live producten.

Handmatige lijst:

| Product-id | Huidige handle | Status | Oordeel |
|---|---|---|---|

## kinderkamer

| Product (geplande handle) | Type | Status na go-live | Voorraad |
|---|---|---|---|
| `artboard` | Kinderkamer | nieuw live | 2 |
| `ballenbak` | Kinderkamer | nu al live | 400 |
| `flip-play-bank` | Kinderkamer | nieuw live | 100 |
| `glijbaan-white-dolphin` | Kinderkamer | nieuw live | 100 |
| `hoes-jumpspot-binnen` | Kinderkamer | nieuw live | 303 |
| `hoes-jumpspot-buiten` | Kinderkamer | nieuw live | 300 |
| `houten-glijbaan-binnen` | Kinderkamer | nu al live | 1776 |
| `jumpspot-binnen` | Kinderkamer | nu al live | 1442 |
| `jumpspot-buiten` | Kinderkamer | nu al live | 100 |
| `klimkoepel-climb-jump` | Kinderkamer | nieuw live | 100 |
| `schommel-play-chill` | Kinderkamer | nieuw live | 500 |
| `slide-surf-way` | Kinderkamer | nieuw live | 100 |
| `surfboard` | Kinderkamer | nieuw live | 28 |
| `zwembad` | Kinderkamer | nu al live | 300 |

## Live producten in geen enkele collectie

| Product | Type | Titel | Reden |
|---|---|---|---|
| `flitsadvies` | Accessoires | Flitsadvies | nu al live, type Accessoires valt in geen regel |
| `octo-ketting-black-tiger` | Decoratie | Octo-ketting Black Tiger L | nieuw live, type Decoratie valt in geen regel |
| `octo-ketting-zwart-wit-s` | Decoratie | Octo-ketting zwart-wit S | nieuw live, type Decoratie valt in geen regel |
| `schelpenketting-h1` | Decoratie | H1 kleine schelpenketting · maat M | nieuw live, type Decoratie valt in geen regel |
| `schelpenketting-j37` | Decoratie | J37 kleine schelpenketting in wit | nieuw live, type Decoratie valt in geen regel |
| `schelpenketting-j47` | Decoratie | J47 schelpenketting op standaard | nieuw live, type Decoratie valt in geen regel |
| `schelpenketting-j63` | Decoratie | J63 schelpenketting | nieuw live, type Decoratie valt in geen regel |
| `schelpenketting-j65` | Decoratie | J65 kleine schelpenketting | nieuw live, type Decoratie valt in geen regel |
| `schelpenketting-j66` | Decoratie | J66 kleine schelpenketting in grijs | nieuw live, type Decoratie valt in geen regel |
| `schelpenketting-j69` | Decoratie | J69 schelpenketting | nieuw live, type Decoratie valt in geen regel |

## Uitgevoerd 23 november

**Status: uitgevoerd 23 november** via `collectionUpdate` met `sourcesToUpdate` (bron-id's uit `collectie_bronnen` in `data/ids.json`). Fauteuils: de titelregel is ook echt verwijderd. Verificatie: productsCount (telt concepten mee) vóór en na: banken 32/32, stoelen 94/94, fauteuils 15/7, barkrukken 9/9, tafels 6/6, vazen 5/3, windlichten 8/2, decoratie 14/11, maatwerk 0/0, kinderkamer 14/14; alle tien `resourcePublicationsCount` 0.

Stand vóór: de collecties bleken ruimer gevuld dan op 19 november (de aantallen tellen ook concepten mee) en de Admin API (2026-10) kent geen `ruleSet`, `collectionAddProducts` of `collectionRemoveProducts` meer; wijzigen gaat via `collectionUpdate` met `sourcesToUpdate` (condities en handmatige selecties). Alle tien collecties staan op `resourcePublicationsCount` 0 en blijven zo.

Wijzigingen (alleen op de ongepubliceerde concept-collecties, geen product en geen publicatie geraakt):

1. **Fauteuils**: de titelregel (fauteuil, Loungestoel, Lounge Chair) vervangen door `TYPE EQUALS Fauteuils`; de vier handmatig toegevoegde concepten (Panda, Kathmandu, Cairo-eigen, Mars) uit de selectie, want Kathmandu, Mars en Panda vallen nu op type. Cairo (live) valt op type. Toegevoegd als selectie: `draaistoel-pebble` en `draaistoel-storm` (live, type Stoelen, draaistoelen per stuk); ze blijven ook in Stoelen. Beslispunt voor de eigenaar: niet als fauteuil benoemd in titel of type, dus terugdraaien kan door de twee selecties te verwijderen.
2. **Decoratie**: kettingen toegevoegd (schelpenketting h1, j37, j47, j65, j66, j69 en octo-ketting zwart-wit S; j63 en Black Tiger zaten er al). Eruit als concept: boekhouder, boekensteun-mangohout, bowl-babi-m, mand-miso-set-van-3, messing-dodo-m en -s, juju-rasta, krab-messing, krab-l (kan weg), j72-shell-toren-parel-s (kan weg). Over: schaal-babi, schelpentoren-pearl en negen kettingen, 11 live.
3. **Vazen**: eruit `travertine-agano-vaas` en `vaas-agano-travertijn` (concept). Over: Bubble, Swoop, Meduse.
4. **Windlichten en kaarsenhouders**: eruit marmer-waxinelichthouder, waxinelichthouder-marmer, Atlas, Soleil, loterijen-lantaarn-m (concept) en lantaarn-raffles-s (kan weg). Over: Raffles en Peninsula.
5. **Maatwerk**: ongewijzigd, leeg en ongepubliceerd; niet publiceren tot er projectfoto's zijn.
6. Banken, Stoelen, Barkrukken, Tafels, Kinderkamer: ongewijzigd (regels op type of merk).
