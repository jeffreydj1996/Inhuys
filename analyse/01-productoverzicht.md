# Productoverzicht · fase 1

Versie 0.1 · 12 oktober 2026

**Status: gedeeltelijk.** De Shopify-koppeling was in deze sessie verlopen en de winkel zelf was door het netwerkbeleid niet bereikbaar. Daardoor is het aantal concepten, het aantal live producten en de volledigheid per product (beschrijving, meta-titel, meta-description, alt-teksten, specificaties) nog niet vastgesteld. Wat hieronder staat, is afgeleid uit zoekmachine-snippets van www.in-huys.nl. Sectie 4 bevat de kant-en-klare query waarmee de volledige audit in één keer gedraaid wordt zodra de koppeling werkt.

**Legenda:** ✅ geverifieerd · ⚠️ aanname · ❌ niet beschikbaar in deze sessie

---

## 1. Wat zichtbaar is van het assortiment

### Aantallen

| Meting | Waarde |
|---|---|
| Producten in concept | ❌ onbekend (alleen uitleesbaar via Shopify Admin) |
| Producten live (actief en gepubliceerd) | ❌ onbekend |
| Producten gearchiveerd | ❌ onbekend |
| Productpagina's gevonden in de zoekindex | ✅ 0 |
| Collectiepagina's gevonden in de zoekindex | ✅ 1 (`/collections/all`) |

Dat er geen enkele productpagina en maar één collectiepagina in de index staat, is op zichzelf een belangrijke bevinding. Die komt terug in de SEO-scan.

### Productgroepen (✅ "Populaire categorieën" op de homepage)

| Naam op de site | Opmerking |
|---|---|
| Vazen | Kerncategorie, goed zoekvolume op materiaal (travertin, marmer, keramiek) |
| Kaarshouders | Schrijfwijze afwijkend; "kaarsenhouders" is de gangbare zoekterm |
| Windlichten | Kerncategorie |
| Banken | Onduidelijk of dit zitbanken of bankjes zijn; de naam moet dat verhelderen |
| Stoelen | Zichtbaar: eetkamerstoelen van Jesper Home |
| Accessoires | Verzamelcategorie, weinig onderscheidend |
| Maat Meubels | De categorie die het beste past bij het hogere segment; naam beter als "Maatwerk meubels" |
| Extra | Betekenisloze naam voor bezoeker en Google |

⚠️ Of dit alle collecties zijn, is niet vast te stellen. Shopify-winkels hebben vaak extra (verborgen of automatische) collecties, bijvoorbeeld "Bestsellers" of per merk.

### Merken in de collectie (✅ filter op `/collections/all`)

- Jesper Home (eetkamerstoelen)
- Kluster
- MOOISA (travertin en marmer, vermoedelijk vazen en kaarsenhouders)

### Voorbeeldproducten (✅ zichtbaar in snippets)

| Product | Merk | Prijs | Opmerking |
|---|---|---|---|
| Marmeren kaarsenhouder | ⚠️ MOOISA | € 16,95 | Instapprijs; past bij cadeaukoper, niet bij hoger segment |
| Boekenhouder, donker mangohout | ⚠️ | € 59,95 | |
| Vaas Agano, travertin | ⚠️ MOOISA | € 194,95 | Statement-stuk, sterke zoekterm "travertin vaas" |
| Eetkamerstoel Yanai, zwart en goud | Jesper Home | € 309,00 | Hoogste zichtbare prijspunt; wordt elders ook verkocht (Wehkamp, prijsvergelijkers), dus de productpagina moet iets toevoegen om te winnen |

### Eerste observaties over het assortiment

1. **Spreiding is groot.** Van € 16,95 tot € 309 binnen één overzicht. Het laagste segment trekt de aandacht van de dure stukken weg.
2. **Veel producten zijn niet exclusief.** Jesper Home-stoelen staan bij grote retailers. Zonder eigen tekst, eigen beeld en een adviescontext verliest Inhuys die vergelijking altijd op prijs.
3. **De onderscheidende categorie is maatwerk.** Dat is de enige groep waar Inhuys niet vergeleken kan worden en die direct aansluit bij verbouwingen. Die categorie is nu het minst zichtbaar.
4. **Categorienamen zijn niet consistent of niet duidelijk.** "Kaarshouders", "Maat Meubels", "Extra", "Banken".

---

## 2. Auditkader per product

Dit zijn de velden die per product worden gecontroleerd zodra de data beschikbaar is. Dit kader wordt ook de basis voor het productpagina-template in fase 2.

| Veld | Criterium voor "op orde" | Bron in Shopify |
|---|---|---|
| Titel | Bevat productsoort + kenmerk (materiaal of model) + eventueel merk; geen interne codes; 40 tot 70 tekens | `title` |
| Handle (URL) | Leesbaar, Nederlands, geen cijfers of codes, komt overeen met de titel | `handle` |
| Beschrijving | Eigen tekst, minimaal 150 woorden, beantwoordt: waar past het, waarom werkt het, waar is het van gemaakt, hoe onderhoud je het | `descriptionHtml` |
| Meta-titel | Ingevuld, 50 tot 60 tekens, zoekterm vooraan, merknaam achteraan | `seo.title` |
| Meta-description | Ingevuld, 120 tot 155 tekens, concrete belofte, geen herhaling van de titel | `seo.description` |
| Alt-teksten | Elke afbeelding heeft een beschrijvende alt-tekst in het Nederlands; geen bestandsnamen of lege waarden | `media.alt` |
| Specificaties | Afmetingen (h × b × d), materiaal, kleur, gewicht, afwerking, onderhoud, levertijd, herkomst | `metafields` of in de beschrijving |
| Productcategorie | Shopify-standaardcategorie ingevuld (nodig voor Google Shopping en de productfeed) | `category` |
| Producttype | Ingevuld en consistent (bijvoorbeeld "Vaas", niet "vaas" of "Vazen") | `productType` |
| Merk | Ingevuld in `vendor`, niet alleen in de titel | `vendor` |
| Tags | Alleen functionele tags (materiaal, kleur, stijl, ruimte); geen willekeur | `tags` |
| Afbeeldingen | Minimaal 3, waarvan 1 sfeerbeeld en 1 detail; consistente verhouding | `media` |
| Varianten | Opties heten logisch ("Kleur", "Maat") en hebben een eigen afbeelding | `variants`, `options` |
| Collecties | Zit in precies de juiste categoriecollectie(s), niet alleen in "Alle producten" | `collections` |
| Status | Draft of active bewust gekozen; geen half-afgemaakte live producten | `status` |

### Score per product

- **A** Alles ingevuld en eigen tekst. Klaar.
- **B** Basis aanwezig, maar meta-velden of alt-teksten ontbreken. Snelle winst.
- **C** Leveranciers- of lege beschrijving, geen specificaties. Herschrijven.
- **D** Concept zonder beeld of tekst. Beslissen: afmaken of verwijderen.

---

## 3. Op te leveren overzicht (zodra data beschikbaar is)

Eén tabel, één rij per product, als `analyse/producten.csv`:

```
id;titel;handle;status;merk;producttype;categorie;collecties;prijs_min;prijs_max;
beschrijving_woorden;eigen_tekst(ja/nee/onbekend);meta_titel(ja/nee);meta_description(ja/nee);
afbeeldingen;alt_ontbreekt;specificaties_aanwezig;score;opmerking
```

Plus een samenvatting met: totaal, per status, per collectie, verdeling van scores, en de top 20 producten om als eerste aan te pakken (hoogste prijs × hoogste zoekpotentie × laagste score).

---

## 4. Kant-en-klare query voor de volledige audit

Draaien via de Shopify-koppeling (`graphql_query`) zodra die weer werkt, in pagina's van 50 met de `after`-cursor. Eerst valideren met `validate_graphql_codeblocks`. Dit is alleen-lezen en wijzigt niets.

```graphql
query ProductAudit($first: Int!, $after: String) {
  products(first: $first, after: $after, sortKey: TITLE) {
    pageInfo { hasNextPage endCursor }
    edges {
      node {
        id
        title
        handle
        status
        vendor
        productType
        tags
        createdAt
        updatedAt
        publishedAt
        onlineStoreUrl
        category { name fullName }
        seo { title description }
        descriptionHtml
        featuredMedia { alt }
        media(first: 20) {
          edges {
            node {
              alt
              mediaContentType
              ... on MediaImage { image { url width height } }
            }
          }
        }
        options { name values }
        variants(first: 50) {
          edges {
            node {
              id
              title
              sku
              price
              compareAtPrice
              inventoryQuantity
              selectedOptions { name value }
            }
          }
        }
        collections(first: 20) { edges { node { title handle } } }
        metafields(first: 50) { edges { node { namespace key type value } } }
      }
    }
  }
}
```

Tellingen per status, los van de audit:

```graphql
query ProductCounts {
  actief: productsCount(query: "status:active") { count }
  concept: productsCount(query: "status:draft") { count }
  archief: productsCount(query: "status:archived") { count }
}
```

Collecties, inclusief regels van automatische collecties en de SEO-velden:

```graphql
query CollectionAudit($first: Int!, $after: String) {
  collections(first: $first, after: $after, sortKey: TITLE) {
    pageInfo { hasNextPage endCursor }
    edges {
      node {
        id
        title
        handle
        descriptionHtml
        productsCount { count }
        seo { title description }
        image { altText }
        ruleSet { appliedDisjunctively rules { column relation condition } }
      }
    }
  }
}
```

**Alternatief zonder Shopify-koppeling.** Als alleen het netwerkbeleid wordt opengezet, geven de openbare feeds `https://www.in-huys.nl/products.json?limit=250` en `https://www.in-huys.nl/collections.json?limit=250` de live producten en collecties, inclusief beschrijvingen, afbeeldingen en alt-teksten. Concepten, meta-titels en meta-descriptions zijn daar niet in te zien; daarvoor is de Admin-koppeling nodig.
