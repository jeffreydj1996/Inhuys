# Productoverzicht · fase 1

Versie 1.0 · compleet · 12 oktober 2026

**Bron.** Shopify Admin API, alleen-lezen, alle 177 producten en 15 collecties met beschrijving, SEO-velden, media en alt-teksten, varianten, metavelden en collectielidmaatschap. Per product staan alle velden in `producten.csv`; per collectie in `collecties.csv`; de teltabellen in `producten-samenvatting.md`. Dit document duidt de cijfers.

---

## 1. Kerncijfers

| Meting | Waarde |
|---|---|
| Producten totaal | 177 |
| Actief (live, gepubliceerd op het webshopkanaal) | 30 |
| Concept | 147 |
| Gearchiveerd | 0 |
| Collecties | 15, waarvan 0 categoriecollecties |
| Pagina's | 4 (Contact, Inspiratie, Collecties, Interieuradvies) |
| Blogs / artikelen | 4 / 2 |
| Orders tot nu toe | 0 |
| Klantaccounts | 12 |
| Verkoopkanalen | Webshop, Shop, Point of Sale, Facebook & Instagram, Pinterest |
| Redirects | 1 (`/products/vaas-1` → `/products/travertine-agano-vaas`) |
| Taal | Nederlands, één locale |

**Tijdlijn.** 5 producten aangemaakt in juni 2025, 13 in januari 2026, 157 in februari 2026 (bulkimport), daarna losse bewerkingen tot en met oktober 2026 (58 producten bijgewerkt in oktober).

---

## 2. Het assortiment

### Merken

| Merk | Totaal | Live | Wat |
|---|---|---|---|
| Pole To Pole | 157 | 21 | Stoelen, banken, tafels, decoratie. Groothandel met dropshipping; levertijd "kan per item verschillen". |
| Jupiduu · Designed for Kids | 14 | 5 | Ballenbak, glijbaan, jumpspots, zwembad, schommel. Kinderspeelgoed. |
| MOOISA | 2 | 2 | Travertin vaas Agano, marmeren waxinelichthouder |
| Jesper Home | 2 | 0 | Eetkamerstoel Yanai (zwart, goud), in concept |
| Kluster | 1 | 1 | Boekenhouder mangohout |
| InHuys | 1 | 1 | "Flitsadvies" als product van € 0 |

### Producttypes (alle 177)

Stoelen 78 · Accessoires 40 · Banken 25 · Decoratie 20 · Tafels 6 · Kids & Speel 4 · Keukenbarstoel 2 · Barstoel 1 · Vazen 1.

### Prijzen (hoogste variantprijs per product)

| Prijsklasse | Live | Concept |
|---|---|---|
| < € 50 | 2 | 20 |
| € 50 – € 150 | 1 | 20 |
| € 150 – € 500 | 22 | 63 |
| € 500 – € 1.500 | 5 | 14 |
| € 1.500 – € 3.000 | 0 | 12 |
| > € 3.000 | 0 | 18 |

Live loopt van € 31,95 (marmeren waxinelichthouder) tot € 599,80 (Breeze stoel, set van 2), mediaan € 399,80. Het Flitsadvies staat op € 0,00. De dure stukken (banken van € 2.000 tot € 7.000, de Londen- en Amsterdam-series) staan allemaal in concept.

### Wat er live staat (30)

- 21 stoelen van Pole To Pole, in zes modellen: Breeze (4 kleuren), Cloud (5 kleuren plus 4 barkrukvarianten), Whale (2), Luna (3), Boog (2), Scandi (1). Elke kleur is een apart product; de meeste zijn sets van twee.
- 5 kinderproducten van Jupiduu: ballenbak, glijbaan voor binnen, jumpspot binnen en buiten, zwembad.
- Travertin vaas Agano (MOOISA), marmeren waxinelichthouder (MOOISA), boekenhouder (Kluster).
- Flitsadvies (dienst als product).

### Observaties

1. **Het hogere segment staat niet live.** De banken en de grote series zitten in concept; wat live staat zijn stoelensets rond € 400 en kinderspeelgoed.
2. **De kinderlijn past niet bij de positionering.** Vijf van de dertig live producten zijn speeltoestellen. Op de homepage en in Google concurreren ze met het verhaal van interieurstyling.
3. **Kleurvarianten zijn aparte producten.** "Breeze Stoel Beige", "Breeze Stoel Latte", "Breeze Stoel Pastel Roze" en "Breeze Stoel Pistache" zijn vier producten met dezelfde tekst. Dat geeft dubbele content, versnippert de autoriteit van de productpagina en maakt de winkel onoverzichtelijk. Bovendien heeft "Breeze Stoel Beige" zelf nog een variant "Pastelroze" van € 349,95, wat tegenstrijdig is met het eigen product "Breeze Stoel Pastel Roze" van € 599,80.
4. **Voorraad.** 15 van de 48 live varianten staan op nul of lager.
5. **Een dienst als product.** Het Flitsadvies staat als product van € 0 in de categorie Accessoires, met een gegenereerde tekst die spreekt over "een modern en tijdloos item" dat "verzonden wordt via een zorgvuldig geselecteerde partner". Dat hoort een pagina te zijn, geen product.

---

## 3. Collecties

| Collectie | Type en regel | Producten | Tekst | Meta | Afbeelding |
|---|---|---|---|---|---|
| Bestsellers | Automatisch: prijs > 490 en < 3000 | 31 | 3 woorden | geen | geen |
| Amsterdam, Breeze, Cloud, EDO, Egg, Kathmandu, Luna, Panda, Rainbow, rocking, Whale, Bow | Automatisch op titel (één per model) | 2 tot 9 | 42 tot 131 woorden, vertaalde fabrikanttekst, 7 van 12 in u-vorm | geen | geen |
| Adviezen | Handmatig | 1 (Flitsadvies) | leeg | geen | geen |
| Homepage (frontpage) | Handmatig | 1 (Agano vaas) | leeg | geen | geen |

### Observaties

1. **Er bestaat geen enkele categoriecollectie.** Geen "Stoelen", "Banken", "Vazen", "Windlichten" of "Maatwerk". De acht categorietegels op de homepage ("Populaire Categorieën": Vazen, Kaarshouders, Windlichten, Banken, Stoelen, Accesiores, Maat Meubels, Extra) zijn niet aan een collectie gekoppeld; het veld is leeg. Ze leiden nergens heen. Voor het doel "hoog scoren op productgroepen" is dit de belangrijkste structurele bevinding: de pagina's waarop je wilt scoren, bestaan niet.
2. **"Bestsellers" is een prijsfilter**, geen verkoopranglijst. Alles tussen € 490 en € 3.000 komt erin, inclusief 19 concepten die niet zichtbaar zijn.
3. **Modelcollecties zijn te klein** voor een eigen pagina (2 tot 9 producten, vaak dezelfde stoel in kleuren) en hebben Engelse titels naast Nederlandse handles ("Bow" op `/collections/boog`, "Egg" op `/collections/eier`, "rocking" in kleine letters).
4. **Geen enkele collectie heeft een meta-titel, meta-description of afbeelding.**
5. **8 live producten zitten in geen enkele collectie** (de vijf Jupiduu-producten, Scandi stoel, boekenhouder, waxinelichthouder); 99 concepten evenmin.
6. Het thema heeft een "merk-collectie"-template met een "SALE UP TO 25% OFF"-banner; het wordt door geen collectie gebruikt. De uitgeschakelde merkenlijst op de homepage verwijst naar collecties `mooisa` en `jesper-home` die niet bestaan.

---

## 4. Wat ontbreekt per product

Op het eerste gezicht is alles ingevuld: 176 van 177 producten hebben een meta-titel en meta-description, alle producten hebben beeld met alt-tekst, categorie, producttype, merk en tags. Bij inhoudelijke toetsing blijkt dat vrijwel alle inhoud uit één generator komt.

### Live producten (30)

| Bevinding | Aantal | % |
|---|---|---|
| Beschrijving uit sjabloon (dezelfde standaardzinnen) | 30 | 100% |
| Fabrikantzin letterlijk ingeplakt in de beschrijving | 26 | 87% |
| Geen afmetingen in tekst of varianten | 23 | 77% |
| Beschrijving identiek aan een ander product | 16 | 53% |
| Alle alt-teksten van het product identiek ("Titel kleur InHuys") | 23 | 77% |
| Kleinste afbeelding smaller dan 1000 px | 17 | 57% |
| Minder dan 3 afbeeldingen | 2 | 7% |
| Meta-titel of meta-description ontbreekt | 1 | 3% |
| Alt-teksten ontbreken | 1 | 3% |
| Titel met vertaalfout of Engels | 2 | 7% |
| In geen enkele collectie | 8 | 27% |

### Concepten (147)

| Bevinding | Aantal | % |
|---|---|---|
| Beschrijving uit sjabloon | 147 | 100% |
| Fabrikantzin letterlijk ingeplakt | 147 | 100% |
| Geen afmetingen | 141 | 96% |
| Beschrijving identiek aan een ander product | 103 | 70% |
| Alle alt-teksten identiek | 141 | 96% |
| Materiaal niet benoemd | 34 | 23% |
| Titel met vertaalfout of Engels | 25 | 17% |
| Kleinste afbeelding smaller dan 1000 px | 65 | 44% |
| Geen specificatie-metavelden | 145 | 99% |
| In geen enkele collectie | 99 | 67% |

### Hoe de huidige teksten in elkaar zitten (✅ patroon in alle 177)

1. Openingszin: "Een [warm/modern/minimalistisch] en [ambachtelijk/tijdloos/rustig] [designstoel/bank/item] die …"
2. Sfeerzin met kleur en materiaal uit de tags.
3. "Fijn voor wie houdt van een interieur dat klopt in detail:" gevolgd door de eerste zin van de leverancierstekst, letterlijk, in kleine letters. Bijvoorbeeld de u-vorm uit de fabrikantzin midden in een je-tekst.
4. "Details": één vaste zin, "Tijdloos ontwerp dat gemakkelijk combineert met verschillende stijlen."
5. "Specificaties": alleen merk, een algemene leveringszin en een algemene retourzin. Geen maten, geen gewicht, geen materiaalopbouw, geen onderhoud.
6. "InHuys selectie": een variabele slotzin.

Dezelfde generator maakte de meta-titels ("{titel} design stoel | InHuys", "{titel} luxe accessoire | InHuys", "{titel} stijlvol voor thuis | InHuys"), de meta-descriptions ("Ontdek {titel}. …", allemaal exact 154 of 155 tekens en afgekapt met "…"), de alt-teksten ("{titel} {kleur} InHuys" op elke afbeelding) en de tags ("modern", "luxe" en "inhuys-selectie" op vrijwel alles).

**Gevolg.** De velden zijn technisch gevuld, maar: de ingeplakte fabrikantzinnen schenden de regel "nooit kopiëren"; de teksten geven de bezoeker geen enkel feit dat hij nodig heeft (maat, materiaal, levertijd); Google ziet 177 bijna identieke pagina's; en de dienst, het speelgoed en de banken krijgen dezelfde toon als een kaarsenhouder.

### Score

Elke productpagina is beoordeeld op inhoud, niet op het aantal gevulde velden.

| Score | Betekenis | Live | Concept |
|---|---|---|---|
| A | Eigen tekst, afmetingen en materiaal, meta-velden, beschrijvende alt-teksten, minimaal 3 beelden van 1000 px of meer | 0 | 0 |
| B | Eigen tekst met afmetingen, maar meta, alt of beeld onvolledig | 0 | 0 |
| C | Sjabloon- of fabrikanttekst, of geen afmetingen, of u-vorm, of vertaalfout in de titel | 30 | 147 |
| D | Geen beeld of vrijwel geen tekst | 0 | 0 |

Alle 177 producten moeten dus inhoudelijk opnieuw. Dat is geen ramp: de feiten (prijs, varianten, categorie, beeld) staan er al, en het werk is per model te doen, niet per kleur.

### Overige bevindingen

- **Titels inconsistent.** "Luna Chair Mink" naast "Luna stoel Caramel" en "Luna stoel crème"; "Cloud Barstoel Crème" naast "Wolken barstoel karamel"; "Boogstoelcrème" zonder spatie; "zwembad" zonder hoofdletter; "Boekhouder" waar "boekenhouder" bedoeld is. In concept: "Scandi voorzitter Okura", "Nox voorzitter umber", "EDO WOUTEN AANGEVOERDER REDDISH", "Loterij Lantaarn", "London 6 SEATER + OTTOMAN TAN".
- **Categorieën deels fout.** "Bank Amsterdam 6 Zits Hoekbank" staat in "Meubelen > Poefs"; 18 schelpkettingen staan in "Kransen en slingers > Slingers".
- **Handles** volgen de titel, inclusief fouten (`edo-wouten-aangevoerder-reddish-set-van-2`). Bij herschrijven veranderen veel handles; elke wijziging vraagt een redirect.
- **Metavelden.** 26 producten hebben Shopify-standaardkenmerken (kleur, rugleuning, zittype, materiaal); 174 hebben een Facebook-productcategorie. Er is geen eigen set specificatievelden.
- **Varianten.** 159 van 177 producten hebben maar één variant; kleur zit in de titel in plaats van in een optie. Optienamen variëren: "Kleur", "kleur", "Maat", "Materiaal/farbe", "diameter".

---

## 5. Prioriteit en beslispunten

### Volgorde van aanpak (⚠️ voorstel, uitvoering in fase 3 na akkoord)

1. **Structuur eerst.** Categoriecollecties aanmaken (Stoelen, Barkrukken, Banken, Tafels, Verlichting, Vazen, Windlichten en kaarsenhouders, Decoratie, Maatwerk) en de homepage-tegels eraan koppelen. Zonder dit heeft het herschrijven van producten weinig effect op productgroepen.
2. **Per model, niet per kleur.** Eén moedertekst per model (Breeze, Cloud, Whale, Luna, Boog, Scandi, daarna de banken), met kleurvarianten als varianten of, zolang dat niet kan, met een korte eigen kleuralinea per product.
3. **Live producten eerst**: de 21 stoelen (6 modellen), de 3 accessoires. Daarna de banken in concept, want die dragen het hogere segment.
4. **Flitsadvies** van product naar pagina.
5. **Jupiduu en schelpkettingen**: pas na een keuze van de eigenaar.

### Beslispunten voor de eigenaar

- [ ] Blijft de Jupiduu-kinderlijn in de winkel, en zo ja, waar?
- [ ] Welke van de 147 concepten moeten live? Voorstel: de banken en tafels van Pole To Pole als eerste, de schelpkettingen niet.
- [ ] Kleurvarianten samenvoegen tot één product per model (aanbevolen) of apart laten?
- [ ] Mag het Flitsadvies als product verdwijnen zodra er een dienstpagina is?
- [ ] Zijn er specificatiebladen van Pole To Pole, MOOISA, Kluster en Jesper Home beschikbaar als bron voor maten en materialen?

---

## 6. Herhaalbaarheid

De audit is herhaalbaar met de queries hieronder (alleen-lezen) en het script dat de CSV's en de samenvatting maakt. Draai de audit opnieuw na elke batch herschreven producten om de score te volgen.

```graphql
query ProductCounts {
  actief: productsCount(query: "status:active") { count }
  concept: productsCount(query: "status:draft") { count }
  archief: productsCount(query: "status:archived") { count }
}
```

```graphql
query ProductAudit($first: Int!, $after: String) {
  products(first: $first, after: $after, sortKey: TITLE) {
    pageInfo { hasNextPage endCursor }
    edges { node {
      id title handle status vendor productType tags createdAt updatedAt publishedAt onlineStoreUrl templateSuffix
      category { name fullName }
      seo { title description }
      descriptionHtml
      media(first: 20) { edges { node { alt mediaContentType ... on MediaImage { image { url width height } } } } }
      options { name values }
      variants(first: 50) { edges { node { id title sku price compareAtPrice inventoryQuantity selectedOptions { name value } } } }
      collections(first: 20) { edges { node { title handle } } }
      metafields(first: 50) { edges { node { namespace key type value } } }
    } }
  }
}
```

```graphql
query CollectionAudit($first: Int!, $after: String) {
  collections(first: $first, after: $after, sortKey: TITLE) {
    pageInfo { hasNextPage endCursor }
    edges { node {
      id title handle descriptionHtml productsCount { count } seo { title description }
      image { altText url } ruleSet { appliedDisjunctively rules { column relation condition } } sortOrder templateSuffix updatedAt
    } }
  }
}
```
