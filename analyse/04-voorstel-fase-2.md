# Voorstel fase 2 · SEO-strategie en vast template voor productpagina's

Versie 0.1 · 12 oktober 2026

Fase 2 levert twee dingen op: een SEO-strategie met een concreet plan voor de eerste 90 dagen, en een vast template voor productpagina's dat vanaf fase 3 op elk product wordt toegepast. Ook in fase 2 wordt niets live gezet; alles wordt als concept of in een thema-kopie voorbereid en pas na akkoord doorgevoerd.

---

## 0. Eerst afronden: de open punten uit fase 1

Dit kost een korte sessie zodra de toegang geregeld is (zie README):

1. Volledige productaudit draaien met de query uit `analyse/01-productoverzicht.md`; resultaat als `analyse/producten.csv` plus samenvatting.
2. Kleuren en lettertypen uitlezen en invullen in `brand-guide.md`.
3. Technische SEO-controles uit `analyse/02-seo-scan.md`, sectie 3.
4. Google Search Console: toegang krijgen of aanmaken, indexatierapport bekijken.

---

## Deel A · SEO-strategie

### A1. Doelen en meting

| Doel | Meting | Bron |
|---|---|---|
| Alle live producten en collecties geïndexeerd | Geïndexeerde pagina's ≈ aantal live pagina's | Search Console |
| Zichtbaar op de dienst-zoektermen | Top 10 op "interieuradvies verbouwing" en "interieurstylist [regio]" binnen 6 maanden | Search Console, handmatig |
| Zichtbaar op productgroepen | Top 10 op drie categorietermen (bijvoorbeeld "travertin vaas", "design eetkamerstoel", "groot windlicht") binnen 6 maanden | Search Console |
| Kwaliteit van verkeer | Aanvragen voor adviesgesprek per maand; orderwaarde per bezoek | Shopify, formulier |

Nulmeting in week 1, daarna maandelijks een kort rapport.

### A2. Sitestructuur

```
Home
├── Interieuradvies            (dienst, met werkwijze en tarieven)
│   ├── Werkwijze
│   ├── Tarieven en pakketten
│   └── Adviesgesprek aanvragen
├── Projecten                  (portfolio, 1 pagina per project)
├── Collectie
│   ├── Maatwerk meubels
│   ├── Stoelen
│   ├── Banken
│   ├── Tafels (indien aanwezig)
│   ├── Verlichting (indien aanwezig)
│   ├── Vazen
│   ├── Windlichten
│   ├── Kaarsenhouders
│   └── Accessoires
├── Inspiratie                 (artikelen)
└── Over Inhuys                (Sylvana, contact, bedrijfsgegevens)
```

Elke collectie krijgt een eigen inleiding, meta-velden en links naar twee relevante artikelen. Elk artikel linkt naar één collectie en één of twee producten. Elk product linkt terug naar zijn collectie en naar één artikel. Zo ontstaat een gesloten netwerk waarin autoriteit doorstroomt.

### A3. Zoekwoordonderzoek (week 1 tot 2)

1. Startlijst uit `analyse/02-seo-scan.md`, sectie 4.
2. Uitbreiden met een zoekwoordtool (Google Keyword Planner, of een tool naar keuze van de eigenaar) en met Search Console-data als die er is.
3. Per zoekterm vastleggen: volume, intentie (informatie, vergelijken, kopen, dienst), concurrentie, doelpagina.
4. Resultaat: `analyse/zoekwoorden.csv` en per pagina één hoofdterm en twee tot vier nevenvarianten.

### A4. Content per paginatype

| Paginatype | Minimale inhoud | Meta |
|---|---|---|
| Dienstpagina | 600 tot 1000 woorden: voor wie, wat je krijgt, stappen, doorlooptijd, vanaf-prijs, veelgestelde vragen, aanvraagknop | Titel 50 tot 60 tekens, description 120 tot 155 |
| Projectpagina | 300 tot 500 woorden: opgave, keuzes, materialen, resultaat; 6 tot 10 foto's; links naar gebruikte producten | idem |
| Collectiepagina | 150 tot 300 woorden inleiding boven of onder het raster; subcategorieën; 2 artikel-links | idem |
| Productpagina | Volgens template (deel B) | idem |
| Artikel | 800 tot 1500 woorden; één onderwerp; eigen beeld; links naar collectie en producten | idem |

### A5. Technisch (na de controles uit fase 1)

- Sitemap indienen, indexatieproblemen oplossen.
- Gestructureerde data controleren: Product en Offer (standaard in de meeste Shopify-thema's), Organization met `sameAs`, BreadcrumbList. Aanvullen alleen in een thema-kopie.
- Alt-teksten en bestandsnamen bij het herschrijven van elk product meenemen.
- Laadtijd: ongebruikte apps verwijderen, beelden in WebP, geen video's automatisch afspelen boven de vouw.
- Redirects voor elke handle die bij het herschrijven verandert.

### A6. Autoriteit en merk

- Google Bedrijfsprofiel aanmaken als dienstverlener, met regio.
- Eén schrijfwijze van de naam overal.
- Vermeldingen aanvragen bij partners: leveranciers (MOOISA, Jesper Home, Kluster) hebben vaak een dealerpagina; aannemers en keukenzaken waarmee wordt samengewerkt kunnen linken naar projectpagina's.
- Reviews verzamelen na elk project.

### A7. Planning eerste 90 dagen

| Weken | Werk | Oplevering |
|---|---|---|
| 1 tot 2 | Open punten fase 1; Search Console; zoekwoordonderzoek; titelpatronen | Audit-CSV, zoekwoordenlijst, titel- en descriptionvoorstel voor alle bestaande pagina's |
| 3 tot 4 | Dienstpagina's en Over-pagina schrijven; footergegevens | Concepten ter goedkeuring |
| 5 tot 6 | Eerste project uitwerken; collectie-inleidingen schrijven | Concepten ter goedkeuring |
| 7 tot 10 | Productpagina's volgens template, te beginnen bij de 20 producten met hoogste prijs × zoekpotentie | Per product een concept in Shopify (status draft of als niet-gepubliceerde tekst), ter goedkeuring |
| 11 tot 12 | Eerste vier artikelen; nulmeting vergelijken; rapport | Artikelen in concept, maandrapport |

Na akkoord per batch worden teksten gepubliceerd. Thema-aanpassingen (titelpatronen, structuur, kleur, typografie) gaan altijd via een thema-kopie met preview-link.

---

## Deel B · Vast template voor productpagina's

Het volledige template staat in `templates/productpagina-template.md`. Hieronder de opbouw en de regels.

### B1. Opbouw van de pagina

1. **Titel (H1).** Productnaam + materiaal + productsoort. Bijvoorbeeld: "Agano · travertin vaas".
2. **Eén zin die de plek in het interieur beschrijft.** Direct onder de titel, boven de prijs.
3. **Prijs, varianten, levertijd, knop.** Levertijd altijd concreet ("3 tot 5 werkdagen" of "levertijd 6 weken, op bestelling").
4. **Beschrijving in drie alinea's.**
   - *Zo werkt het in de ruimte:* waar past het, welke verhoudingen, wat doet het met licht en rust.
   - *Materiaal en maakwijze:* waar het van gemaakt is, hoe het gemaakt is, wat dat betekent voor uitstraling en gebruik.
   - *Combineren:* twee concrete combinaties met andere stukken uit de collectie of met veelvoorkomende interieurs.
5. **Specificaties.** Vaste tabel: afmetingen (h × b × d), gewicht, materiaal, kleur en afwerking, merk, onderhoud, herkomst, levertijd, garantie.
6. **Advies van Inhuys.** Twee tot vier zinnen van Sylvana over wanneer ze dit stuk wel en niet inzet. Dit is wat geen enkele andere winkel heeft.
7. **Veelgestelde vragen.** Drie tot vijf vragen met korte antwoorden (onderhoud, maatvoering, retour, combinaties).
8. **Gerelateerd.** Collectie waar het in zit, één artikel, twee tot vier bijpassende stukken.

### B2. Meta en beeld

- **Meta-titel:** `{Productnaam} · {materiaal} {productsoort} · Inhuys`, 50 tot 60 tekens.
- **Meta-description:** 120 tot 155 tekens, begint met het effect in de ruimte, eindigt met levertijd of maatvoering.
- **Handle:** `{productsoort}-{materiaal}-{naam}`, bijvoorbeeld `vaas-travertin-agano`. Bij wijziging altijd een redirect.
- **Alt-tekst per beeld:** `{Productnaam}, {materiaal} {productsoort}, {wat het beeld toont}`. Bijvoorbeeld: "Agano travertin vaas op eiken dressoir in woonkamer met daglicht".
- **Beelden:** minimaal 3; volgorde: sfeer, vrijstaand, detail, eventueel leveranciersbeeld als laatste.

### B3. Schrijfregels voor het template

1. Alles zelf geschreven. Fabrikantinformatie wordt gebruikt voor feiten (maten, materiaal, herkomst) en wordt daarna gesloten; er wordt nooit uit geciteerd.
2. 250 tot 400 woorden beschrijving plus specificaties en FAQ. Geen opvulling.
3. Hoofdzoekterm in H1, eerste zin, meta-titel en één alt-tekst. Niet vaker dan natuurlijk.
4. Geen "wij zijn trots", "prachtig", "uniek" zonder onderbouwing.
5. Nederlandse spelling, samenstellingen aan elkaar, consequent "je".
6. Elke productpagina wordt eerst als concept opgeleverd. Pas na akkoord wordt de tekst in Shopify gezet, en ook dan eerst als draft of ongepubliceerde wijziging.

### B4. Opslag in Shopify (voorstel, nog niet ingericht)

Om het template herhaalbaar te maken zonder het thema te raken, worden de vaste onderdelen als productmetavelden opgeslagen:

| Metaveld | Type | Inhoud |
|---|---|---|
| `inhuys.ruimte_zin` | tekst | De zin onder de titel |
| `inhuys.advies` | rich text | Het advies van Sylvana |
| `inhuys.faq` | lijst van tekst | Vragen en antwoorden |
| `inhuys.afmetingen` | afmeting | h, b, d |
| `inhuys.gewicht` | gewicht | |
| `inhuys.materiaal` | tekst | |
| `inhuys.afwerking` | tekst | |
| `inhuys.onderhoud` | tekst | |
| `inhuys.herkomst` | tekst | |
| `inhuys.levertijd` | tekst | |
| `inhuys.artikel` | verwijzing naar blogartikel | |

Het tonen van deze velden vraagt een kleine thema-aanpassing. Die wordt in een thema-kopie gebouwd en pas na akkoord gepubliceerd.

---

## Wat ik van de eigenaar nodig heb voor fase 2

1. Toegang: Shopify-connector opnieuw autoriseren en `www.in-huys.nl` toestaan in de netwerkinstellingen (zie README).
2. Google Search Console: toegang of de bevestiging dat ik een voorstel voor inrichting mag doen.
3. Logo-bestanden en, als die bestaan, bestaande huisstijlafspraken.
4. Fabrikantinformatie per merk (als bron, niet als tekst): specificatiebladen van MOOISA, Jesper Home en Kluster.
5. De regio waarin Inhuys werkt, voor lokale zoektermen en het Google Bedrijfsprofiel.
6. Een beschrijving van de adviesdienst: pakketten, stappen, doorlooptijd, vanaf-prijzen.
7. Drie afgeronde projecten met foto's, of de planning voor een eerste shoot.
8. Beslissingen op de open keuzes: schrijfwijze van de naam, tagline, accentkleur, en of de kleine accessoires in de collectie blijven.

## Beslispunten

- [ ] Akkoord op de aanpak van fase 2 zoals hierboven
- [ ] Akkoord op de opbouw van het productpagina-template
- [ ] Keuze schrijfwijze merknaam
- [ ] Keuze tagline
- [ ] Keuze accentkleur en typografie-richting
- [ ] Keuze over de positie van kleine accessoires in de collectie
