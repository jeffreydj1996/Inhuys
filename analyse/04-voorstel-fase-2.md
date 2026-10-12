# Voorstel fase 2 · SEO-strategie en vast template voor productpagina's

Versie 1.0 · 12 oktober 2026

Fase 2 levert twee dingen op: een SEO-strategie met een concreet plan voor de eerste 90 dagen, en een vast template voor productpagina's dat vanaf fase 3 op elk product wordt toegepast. Ook in fase 2 wordt niets live gezet; alles wordt als concept of in een thema-kopie voorbereid en pas na akkoord doorgevoerd.

---

## 0. Wat fase 1 heeft opgeleverd en wat nog open staat

Afgerond: volledige productaudit (177 producten, 15 collecties), uitlezen van thema, menu's, pagina's, blogs en verkoopkanalen, kleuren en typografie in de brand guide, SEO-scan op basis van de werkelijke thema-bestanden.

Nog open, alleen in de browser of in Google-tools (eerste werk van fase 2):
1. Google Search Console: werkelijke indexatie, sitemap, fouten.
2. PageSpeed Insights op drie pagina's.
3. Rich Results Test op één productpagina.
4. Controle of Google Analytics of het Google-kanaal al actief is (Shopify-instellingen).

De drie belangrijkste conclusies uit fase 1 bepalen de volgorde in fase 2:
- Er zijn geen categoriecollecties; die moeten er eerst komen.
- Alle 177 productteksten zijn sjabloonwerk met ingeplakte fabrikantzinnen; herschrijven gaat per model, niet per kleur.
- Het thema staat vol Engelse restanten; opruimen is de snelste zichtbare winst.

---

## Deel A · SEO-strategie

### A1. Doelen en meting

| Doel | Meting | Bron |
|---|---|---|
| Alle live producten en collecties geïndexeerd | Geïndexeerde pagina's ≈ aantal live pagina's | Search Console |
| Zichtbaar op de dienst-zoektermen | Top 10 op "interieuradvies [regio]" en "3D interieurontwerp" binnen 6 maanden | Search Console |
| Zichtbaar op productgroepen | Top 10 op drie categorietermen (bijvoorbeeld "design eetkamerstoel boucle", "hoekbank boucle", "travertin vaas") binnen 6 maanden | Search Console |
| Kwaliteit van verkeer | Adviesaanvragen per maand (Shopify Forms); eerste orders | Shopify |

Nulmeting in week 1, daarna maandelijks een kort rapport.

### A2. Sitestructuur

```
Home
├── Interieuradvies            (dienst: 3D-ontwerp compleet, Flitsadvies)
│   ├── Werkwijze
│   ├── Showroom               (adres, tijden, beeld; LocalBusiness-markup)
│   └── Gesprek aanvragen      (Shopify Forms, bestaat al)
├── Projecten                  (1 pagina per project)
├── Collectie
│   ├── Banken
│   ├── Stoelen
│   ├── Barkrukken
│   ├── Tafels
│   ├── Verlichting
│   ├── Vazen
│   ├── Windlichten en kaarsenhouders
│   ├── Decoratie
│   └── Maatwerk
├── Inspiratie                 (één blog, artikelen)
└── Over InHuys                (Sylvana, contact, bedrijfsgegevens)
```

Elke categoriecollectie krijgt een eigen inleiding, meta-velden, beeld en links naar twee artikelen. Elk artikel linkt naar één collectie en één of twee producten. Elk product linkt terug naar zijn collectie en naar één artikel. De twaalf modelcollecties blijven bestaan als interne hulpmiddelen (bijvoorbeeld voor "Anderen bekeken ook"), maar komen niet in het menu.

### A3. Zoekwoordonderzoek (week 1 tot 2)

1. Startlijst uit `02-seo-scan.md`, sectie 5.
2. Uitbreiden met Google Keyword Planner (of een tool naar keuze van de eigenaar) en met Search Console-data zodra beschikbaar.
3. Per zoekterm: volume, intentie (informatie, vergelijken, kopen, dienst), concurrentie, doelpagina.
4. Resultaat: `analyse/zoekwoorden.csv` en per pagina één hoofdterm en twee tot vier nevenvarianten.

### A4. Content per paginatype

| Paginatype | Minimale inhoud | Meta |
|---|---|---|
| Dienstpagina | 600 tot 1000 woorden: voor wie, wat je krijgt, stappen, doorlooptijd, prijs of "inbegrepen bij", veelgestelde vragen, aanvraagknop | Titel 50 tot 60 tekens, description 120 tot 155 |
| Projectpagina | 300 tot 500 woorden: opgave, keuzes, materialen, resultaat; 6 tot 10 foto's; links naar gebruikte producten | idem |
| Collectiepagina | 150 tot 300 woorden inleiding; subcategorieën; 2 artikel-links | idem |
| Productpagina | Volgens template (deel B) | idem |
| Artikel | 800 tot 1500 woorden; één onderwerp; eigen beeld; links naar collectie en producten | idem |

### A5. Technisch

- Search Console inrichten, sitemap indienen, indexatieproblemen oplossen.
- Thema-kopie maken van het live thema; daarin: placeholders en Engelse restanten corrigeren, BreadcrumbList-, Organization- en LocalBusiness-markup toevoegen, labels vertalen. Preview-link ter goedkeuring; pas dan publiceren.
- Oude thema-kopieën (vier stuks) opruimen na akkoord, zodat duidelijk is welke versie de waarheid is.
- Redirects voor elke handle die bij het herschrijven of samenvoegen verandert.
- Beeld: per product nagaan of de leverancier materiaal van 2000 px of meer heeft.

### A6. Autoriteit en merk

- Google Bedrijfsprofiel voor de showroom.
- Eén schrijfwijze van de naam (InHuys) overal; echte social links in het thema of geen.
- Vermeldingen aanvragen bij partners: Pole To Pole, MOOISA, Jesper Home en Kluster hebben vaak een dealerpagina; aannemers en keukenzaken kunnen linken naar projectpagina's.
- Reviews verzamelen na elk adviestraject.

### A7. Planning eerste 90 dagen

| Weken | Werk | Oplevering |
|---|---|---|
| 1 tot 2 | Search Console, nulmeting, zoekwoordonderzoek; thema-kopie met opruimwerk en markup; voorstel categoriestructuur | Zoekwoordenlijst, preview-link thema, collectievoorstel ter goedkeuring |
| 3 tot 4 | Dienstpagina's, werkwijze, showroom, Over; footergegevens; Flitsadvies van product naar pagina | Concepten ter goedkeuring |
| 5 tot 6 | Categoriecollecties aanmaken met inleidingen en meta; homepage-tegels koppelen; eerste project uitwerken | Collecties als concept (niet gepubliceerd), projectpagina als concept |
| 7 tot 10 | Productpagina's volgens template: eerst de zes live stoelmodellen en drie accessoires, daarna de banken in concept; kleurvarianten samenvoegen met redirects | Per model een concept in Shopify, ter goedkeuring; redirectlijst |
| 11 tot 12 | Eerste vier artikelen; blogs opschonen (één blog "Inspiratie"); maandrapport | Artikelen in concept, rapport |

Na akkoord per batch worden teksten gepubliceerd. Thema-aanpassingen gaan altijd via de thema-kopie met preview-link.

---

## Deel B · Vast template voor productpagina's

Het volledige template staat in `templates/productpagina-template.md`. Hieronder de opbouw en de regels, afgestemd op wat het thema nu al kan.

### B1. Opbouw van de pagina

1. **Titel (H1).** Modelnaam + productsoort + onderscheidend kenmerk. Bijvoorbeeld: "Breeze eetkamerstoel in boucle (set van 2)". Kleur niet in de titel maar als variant.
2. **Eén zin die de plek in het interieur beschrijft.** Direct onder de titel, boven de prijs. Het thema heeft hiervoor al een blok (`short_description`, uit het metaveld `descriptor.short_description`).
3. **Prijs, varianten (Kleur, Maat), levertijd, knop.** Levertijd concreet: "2 tot 3 weken, geleverd door onze partner" in plaats van "kan per item verschillen".
4. **Beschrijving in drie alinea's.**
   - *Zo werkt het in de ruimte:* waar past het, welke tafelmaat of ruimte, wat doet het met licht en rust.
   - *Materiaal en maakwijze:* bekleding, frame, afwerking, wat dat betekent voor gebruik en onderhoud.
   - *Combineren:* twee concrete combinaties met andere stukken uit de collectie of met veelvoorkomende interieurs.
5. **Specificaties.** Vaste tabel: afmetingen (h × b × d), zithoogte en zitdiepte bij zitmeubels, gewicht, materiaal frame, materiaal bekleding, kleur en afwerking, merk, onderhoud, herkomst, levertijd, garantie, set-inhoud.
6. **Advies van InHuys.** Twee tot vier zinnen van Sylvana over wanneer ze dit stuk wel en niet inzet. Dit is wat geen enkele andere winkel met dezelfde Pole To Pole-stoel heeft.
7. **Veelgestelde vragen.** Drie tot vijf vragen met korte antwoorden (onderhoud boucle, maatvoering, retour, combinaties). Het thema heeft hiervoor de "collapsible tabs"-sectie, nu uitgeschakeld met demotekst.
8. **Gerelateerd.** Categoriecollectie, één artikel, twee tot vier bijpassende stukken (het thema toont al "Anderen Bekeken Ook").

### B2. Meta en beeld

- **Meta-titel:** `{Model} {productsoort} {kenmerk} | InHuys`, 50 tot 60 tekens. Geen generieke toevoegingen als "design stoel" of "luxe accessoire".
- **Meta-description:** 120 tot 155 tekens, eigen zin, begint met het effect in de ruimte, eindigt met levertijd of set-inhoud. Nooit afgekapt met "…".
- **Handle:** `{productsoort}-{model}-{kenmerk}`, bijvoorbeeld `eetkamerstoel-breeze-boucle-set-van-2`. Bij wijziging altijd een redirect.
- **Alt-tekst per beeld, verschillend per beeld:** `{Model} {productsoort}, {kleur/materiaal}, {wat het beeld toont}`. Bijvoorbeeld: "Breeze eetkamerstoel in beige boucle, zijaanzicht met stalen poten".
- **Beelden:** minimaal 3, minimaal 2000 px; volgorde: sfeer, vrijstaand, detail, leveranciersbeeld als laatste.

### B3. Schrijfregels voor het template

1. Alles zelf geschreven. Fabrikantinformatie wordt gebruikt voor feiten (maten, materiaal, herkomst) en wordt daarna gesloten; er wordt nooit uit geciteerd. De huidige ingeplakte fabrikantzinnen worden verwijderd.
2. 250 tot 400 woorden beschrijving plus specificaties en FAQ. Geen opvulling.
3. Hoofdzoekterm in H1, eerste zin, meta-titel en één alt-tekst. Niet vaker dan natuurlijk.
4. Geen "luxe", "hoogwaardig", "voortreffelijk" zonder onderbouwing.
5. Nederlandse spelling, samenstellingen aan elkaar, consequent "je", modelnamen in één taal.
6. Elke productpagina wordt eerst als concept opgeleverd. Pas na akkoord wordt de tekst in Shopify gezet, en ook dan eerst als draft of ongepubliceerde wijziging.

### B4. Opslag in Shopify (voorstel, nog niet ingericht)

Om het template herhaalbaar te maken zonder het thema te raken, worden de vaste onderdelen als productmetavelden opgeslagen. Twee bestaan al als Shopify-standaard (kleur, materiaal); de rest is nieuw.

| Metaveld | Type | Inhoud |
|---|---|---|
| `descriptor.short_description` | tekst | De zin onder de titel (thema toont dit al) |
| `inhuys.advies` | rich text | Het advies van Sylvana |
| `inhuys.faq` | lijst van tekst | Vragen en antwoorden |
| `inhuys.afmetingen` | afmeting | h, b, d |
| `inhuys.zithoogte`, `inhuys.zitdiepte` | afmeting | bij zitmeubels |
| `inhuys.gewicht` | gewicht | |
| `shopify.material`, `shopify.upholstery-material` | standaard | Materiaal frame en bekleding |
| `inhuys.afwerking` | tekst | |
| `inhuys.onderhoud` | tekst | |
| `inhuys.herkomst` | tekst | |
| `inhuys.levertijd` | tekst | |
| `inhuys.set_inhoud` | tekst | "2 stoelen" |
| `inhuys.artikel` | verwijzing naar blogartikel | |

Het tonen van de nieuwe velden vraagt een kleine aanpassing in de thema-kopie (een specificatietabel-blok in het producttemplate). Die wordt pas na akkoord gepubliceerd.

---

## Wat ik van de eigenaar nodig heb voor fase 2

1. Google Search Console: toegang, of de bevestiging dat ik een inrichtingsvoorstel mag doen.
2. Logo-bestanden en, als die bestaan, bestaande huisstijlafspraken.
3. Specificatiebladen van Pole To Pole, MOOISA, Jesper Home, Kluster en (als de lijn blijft) Jupiduu, als bron voor maten en materialen.
4. Adres en openingstijden van de showroom, en de regio waarin InHuys werkt.
5. Een beschrijving van de adviesdienst zoals die in de praktijk gaat: stappen, doorlooptijd, wat de klant ontvangt, en de keuze over "gratis".
6. Drie afgeronde projecten met foto's, of de planning voor een eerste shoot.
7. Beslissingen op de open keuzes hieronder.

## Beslispunten

- [ ] Akkoord op de aanpak van fase 2 zoals hierboven
- [ ] Akkoord op de opbouw van het productpagina-template
- [ ] Schrijfwijze merknaam: InHuys (aanbevolen)
- [ ] Tagline
- [ ] Kleur- en typografierichting (serif voor koppen, badges uit, kortingsrood uit)
- [ ] Jupiduu-kinderlijn en schelpkettingen: blijven of niet
- [ ] Kleurvarianten samenvoegen tot één product per model
- [ ] "Gratis" advies behouden of pakketten met vanaf-prijs
- [ ] Welke concepten als eerste live mogen (voorstel: banken en tafels Pole To Pole)
