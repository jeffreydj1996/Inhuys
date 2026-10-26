# Collectiestructuur · fase 2

Versie 1.0 · 26 oktober 2026 · bron van waarheid: `scripts/collections.py` in de scratchpad (teksten hieronder zijn identiek aan wat in Shopify als concept is aangemaakt).

Tien categoriecollecties vervangen de huidige modelcollecties als ingang voor bezoekers en Google. Ze zijn in Shopify aangemaakt als **ongepubliceerd** concept; ze verschijnen pas na akkoord. Producten zijn er niet voor gewijzigd: automatische collecties werken op het bestaande producttype of merk, handmatige collecties verwijzen naar product-ID's.

## Overzicht

| Collectie | Handle | Vulling | Aantal nu | Menu |
|---|---|---|---|---|
| Banken | `banken` | automatisch: TYPE EQUALS 'Banken' | 25 | Collectie |
| Stoelen | `stoelen` | automatisch: TYPE EQUALS 'Stoelen' | 78 | Collectie |
| Fauteuils en loungestoelen | `fauteuils` | automatisch: TITLE CONTAINS 'fauteuil' OF TITLE CONTAINS 'Loungestoel' OF TITLE CONTAINS 'Lounge Chair' | circa 12 | Collectie |
| Barkrukken | `barkrukken` | automatisch: TYPE EQUALS 'Barstoel' OF TYPE EQUALS 'Keukenbarstoel' | 3 | Collectie |
| Tafels | `tafels` | automatisch: TYPE EQUALS 'Tafels' | 6 | Collectie |
| Vazen | `vazen` | handmatig: 4 producten | 4 | Collectie |
| Windlichten en kaarsenhouders | `windlichten-en-kaarsenhouders` | handmatig: 7 producten | 7 | Collectie |
| Decoratie | `decoratie` | handmatig: 11 producten | 11 | Collectie |
| Maatwerk | `maatwerk` | handmatig: 0 producten | 0 | Collectie + Interieuradvies |
| Kinderkamer | `kinderkamer` | automatisch: VENDOR EQUALS 'Jupiduu - Designed for Kids' | 14 | alleen via Collectie-overzicht, niet in hoofdmenu |

**Verlichting** is bewust nog niet aangemaakt: er zijn geen lampen in het assortiment. Zodra die er zijn, komt de collectie erbij volgens hetzelfde patroon.

## Wat er met de bestaande 15 collecties gebeurt (voorstel, nog niet uitgevoerd)

- De twaalf modelcollecties (Amsterdam, Bow, Breeze, Cloud, EDO, Egg, Kathmandu, Luna, Panda, Rainbow, rocking, Whale) blijven bestaan als hulpmiddel voor 'Anderen bekeken ook', maar verdwijnen uit elk menu en krijgen in fase 3 een Nederlandse titel en een korte eigen tekst in je-vorm.
- 'Bestsellers' (prijsfilter € 490 tot € 3.000) wordt gedepubliceerd zodra de categoriecollecties live zijn; een echte bestsellerlijst komt terug zodra er verkoopdata is.
- 'Adviezen' en 'Homepage' zijn hulpcollecties van het thema; ongewijzigd laten tot het nieuwe thema live is, daarna opruimen.

## Menu-voorstel (nieuw hoofdmenu, alleen in de thema-kopie)

Interieuradvies · Projecten · Collectie (Banken, Stoelen, Fauteuils en loungestoelen, Barkrukken, Tafels, Vazen, Windlichten en kaarsenhouders, Decoratie, Maatwerk) · Inspiratie · Over InHuys

## Per collectie

### Banken

- Handle: `/collections/banken`
- Vulling: Automatisch op producttype Banken (25 producten, nu allemaal in concept).
- Meta-titel (53 tekens): Design banken en hoekbanken · boucle en stof · InHuys
- Meta-description (151 tekens): Banken, hoekbanken en loungebanken van 2,5 tot 6 zits, met of zonder ottoman. Gekozen op zitcomfort, maat en stof. Te zien in de showroom in Purmerend.
- Beeldadvies: Sfeerbeeld van een hoekbank in een lichte woonkamer, bij voorkeur uit een eigen project.

**Inleiding (boven het productraster):**

Een bank bepaalt hoe een woonkamer voelt. Niet alleen door de vorm, maar door de verhouding tot de ruimte, de zitdiepte en de stof. Wij kiezen banken die rust brengen: zachte lijnen, een lage rug, bekleding in boucle of een stevige weefstof, en kleuren die het licht in huis volgen.

In deze collectie vind je banken van 2,5 tot 6 zits, hoekbanken en loungebanken met ottoman. Elke serie is er in meerdere opstellingen, zodat de bank past bij de plattegrond in plaats van andersom. Bij elke bank staan de buitenmaten, de zithoogte en de zitdiepte, zodat je thuis kunt uitmeten of hij past.

Twijfel je over de maat of de opstelling? Kom zitten in de showroom in Purmerend, of plan een Flitsadvies. Dan tekenen we de bank in jouw plattegrond en kijken we meteen naar de rest van de ruimte: de looproute, de plek van de tafel en het licht van het raam.


### Stoelen

- Handle: `/collections/stoelen`
- Vulling: Automatisch op producttype Stoelen (78 producten, waarvan 21 live). Bevat nu ook fauteuils en loungestoelen; die krijgen daarnaast een eigen collectie.
- Meta-titel (57 tekens): Design eetkamerstoelen · boucle, velvet en staal · InHuys
- Meta-description (152 tekens): Eetkamerstoelen per set van twee, met of zonder armleuning, in boucle, velvet en weefstof. Met zithoogte, zitdiepte en combinatie-advies bij elke stoel.
- Beeldadvies: Set van twee stoelen aan een ovale tafel bij daglicht.

**Inleiding (boven het productraster):**

Een eetkamerstoel moet twee dingen kunnen: lang comfortabel zitten en mooi blijven bij de tafel die je al hebt. Daarom letten we bij elke stoel op zithoogte, zitdiepte, rugsteun en de verhouding tot tafelhoogtes van 75 tot 78 cm.

De collectie bestaat uit eetkamerstoelen per set van twee, in verschillende modellen: met een hoge, zachte rug, met een ronde kuip, met of zonder armleuning. De bekleding varieert van boucle en velvet tot een gladde weefstof; de poten zijn van gepoedercoat staal of hout. Kleuren lopen van crème en beige tot karamel, taupe en zwart, zodat je kunt afstemmen op vloer, tafel en wand.

Bij elke stoel staat met welke tafels hij goed combineert en hoeveel stoelen er om een tafel van 160, 180 of 220 cm passen. Wil je zeker weten dat het klopt? Vraag een Flitsadvies aan of kom proefzitten in de showroom in Purmerend. Neem een foto van je tafel mee; dan kiezen we ter plekke.


### Fauteuils en loungestoelen

- Handle: `/collections/fauteuils`
- Vulling: Automatisch op titel (fauteuil, Loungestoel, Lounge Chair). Bij het herschrijven van titels in fase 3 omzetten naar producttype Fauteuils.
- Meta-titel (56 tekens): Fauteuils en loungestoelen · boucle en weefstof · InHuys
- Meta-description (136 tekens): Fauteuils, loungestoelen en draaifauteuils voor de leeshoek, de erker of naast de bank. Geselecteerd op zitcomfort en rust in de ruimte.
- Beeldadvies: Eén fauteuil in een erker of leeshoek.

**Inleiding (boven het productraster):**

Een fauteuil is de plek waar je neerstrijkt met een boek of een kop koffie. Hij hoeft niet bij de bank te passen; hij moet erbij passen. Een andere stof, een andere kleur of een andere vorm geeft de zithoek diepte.

Hier vind je fauteuils met een omsluitende rug, loungestoelen met een lage, brede zit en draaifauteuils voor een hoek met uitzicht. De bekleding is boucle of een stevige weefstof; de onderstellen zijn van staal of hout. Bij elk model staan de buitenmaten en de zithoogte.

Weet je niet of een fauteuil in de hoek past zonder de loop te blokkeren? Stuur de maten van de ruimte mee met een Flitsadvies, dan tekenen we hem in. Een fauteuil heeft rondom minstens 60 cm vrije ruimte nodig om echt uit te nodigen; met een bijzettafel en een lamp ernaast wordt het een plek in plaats van een stoel.


### Barkrukken

- Handle: `/collections/barkrukken`
- Vulling: Automatisch op producttype Barstoel of Keukenbarstoel (3 producten, live). De Japandi-barkrukken in concept hebben nog producttype Stoelen; in fase 3 omzetten.
- Meta-titel (48 tekens): Barkrukken en keukenbarkrukken · boucle · InHuys
- Meta-description (131 tekens): Barkrukken met rugleuning voor keukeneilanden en bars, in twee zithoogtes. Boucle in crème en karamel, poten in gepoedercoat staal.
- Beeldadvies: Twee krukken aan een keukeneiland.

**Inleiding (boven het productraster):**

Een barkruk zit pas goed als de zithoogte klopt met het blad. Daarom maken we het verschil tussen keukenbarkrukken (voor bladen rond 90 cm) en barkrukken (voor bladen rond 105 cm) in elke productnaam zichtbaar.

De krukken in deze collectie hebben allemaal een rugleuning en een zachte, ronde zitting in boucle, met een stalen onderstel. Ze zijn er in crème en karamel en passen bij een keukeneiland in hout, keramiek of steen.

Hoeveel krukken passen er aan jouw eiland? Reken op 60 cm per kruk en houd aan de kopse kant ruimte vrij om langs te lopen. Bij twijfel helpt een Flitsadvies: we kijken dan meteen naar de looproute rond het eiland, de hoogte van het blad en de plek van het licht erboven. Zo zit je straks goed, ook na een lang etentje aan de bar.


### Tafels

- Handle: `/collections/tafels`
- Vulling: Automatisch op producttype Tafels (6 producten, in concept).
- Meta-titel (58 tekens): Eettafels en salontafels · keramiek en travertijn · InHuys
- Meta-description (145 tekens): Eettafels en salontafels met bladen van keramiek met marmerlook of travertijn, rond en ovaal. Met bladmaten en het aantal stoelen dat erbij past.
- Beeldadvies: Ovale eettafel met stoelen, van boven of op ooghoogte.

**Inleiding (boven het productraster):**

Een tafel is het middelpunt van de ruimte: hij bepaalt de loop, het licht en hoeveel mensen er kunnen aanschuiven. Wij kiezen tafels met bladen die tegen het dagelijks leven kunnen: keramiek met marmerlook en travertijn zijn krasvast en makkelijk schoon te houden.

In deze collectie staan ronde en ovale eettafels en salontafels in twee maten. Bij elke tafel vind je de bladmaat, de hoogte en het aantal stoelen dat er comfortabel omheen past. De ronde tafels zijn geschikt voor zes personen; de ovale voor zes tot acht.

Een tafel op maat, in een andere afmeting of met een ander blad? Dat regelen we via Maatwerk. Vraag het na in een adviesgesprek. Houd bij het kiezen rekening met minstens 80 cm tussen de tafelrand en de muur of de kast erachter, zodat iedereen kan aanschuiven zonder te schuiven.


### Vazen

- Handle: `/collections/vazen`
- Vulling: Handmatig: Agano (live), Vase Bubble S, Vase Meduse, Vase Swoop L (concept). Producten worden hiervoor niet gewijzigd.
- Meta-titel (41 tekens): Vazen van travertijn en keramiek · InHuys
- Meta-description (118 tekens): Vazen in travertijn en keramiek, van klein tafelformaat tot vloermodel. Met gewicht, maat en of de vaas waterdicht is.
- Beeldadvies: Travertijn vaas met droge takken op een houten dressoir.

**Inleiding (boven het productraster):**

Een vaas is vaak het laatste wat je neerzet en het eerste wat opvalt. Een stenen vaas brengt gewicht en rust op een dressoir; een set kleine keramische vazen maakt een tafel levendig zonder druk.

Hier vind je vazen van travertijn, gedraaid uit één blok, en keramische vazen in sets. Bij elke vaas staat of hij waterdicht is en hoe je hem onderhoudt; travertijn is poreus en vraagt om droge takken of een glazen inzet.

Wil je weten welke vaas bij jouw dressoir of tafel past? Stuur een foto mee met je Flitsadvies, dan kiezen we samen. Een goede vuistregel: één groot stuk per oppervlak, of een groep van drie in verschillende hoogtes. Meer wordt snel onrustig, zeker op een dressoir dat al een lamp of een schaal draagt.


### Windlichten en kaarsenhouders

- Handle: `/collections/windlichten-en-kaarsenhouders`
- Vulling: Handmatig: marmeren waxinelichthouder (live), keramische kaarsenhouders Atlas en Soleil, lantaarns in drie maten en de Schiereiland-lantaarn (concept). De lantaarntitels bevatten vertaalfouten en worden in fase 3 hernoemd.
- Meta-titel (59 tekens): Windlichten en kaarsenhouders · marmer en keramiek · InHuys
- Meta-description (131 tekens): Windlichten, lantaarns en kaarsenhouders van marmer en keramiek, voor binnen en op het terras. Met maten en materiaal bij elk stuk.
- Beeldadvies: Lantaarn en kaarsenhouder op een terrastafel in avondlicht.

**Inleiding (boven het productraster):**

Licht maakt een ruimte 's avonds af. Een groot windlicht op de vloer, een lantaarn op het terras of een paar kaarsenhouders van marmer op tafel: kleine stukken met groot effect.

In deze collectie vind je lantaarns in drie maten, kaarsenhouders van marmer en keramische kaarsenhouders per set van twee. Bij elk stuk staan de maat en het materiaal, en of het buiten mag staan.

Combineer een groot windlicht met een lage kaarsenhouder op dezelfde tafel voor hoogteverschil; dat geeft meer rust dan drie dezelfde stukken naast elkaar. Buiten werkt een lantaarn het mooist op de grond naast de deur of aan het eind van het terras, zodat het licht de ruimte afbakent. Binnen kies je liever één groot windlicht dan drie kleine; het oog heeft een rustpunt nodig.


### Decoratie

- Handle: `/collections/decoratie`
- Vulling: Handmatig: boekenhouder (live), Bowl Babi L en M, mand Miso, Messing Dodo M en S, Juju Rasta, Krab L en S, Shell Toren Parel S en Schelptoren Parel L (concept). De 19 schelpkettingen zijn bewust niet opgenomen.
- Meta-titel (52 tekens): Woondecoratie · schalen, manden en objecten · InHuys
- Meta-description (115 tekens): Schalen, manden, boekensteunen en objecten van hout, messing en keramiek. De afwerking van een ruimte die al klopt.
- Beeldadvies: Stilleven van schaal, object en boek op een dressoir.

**Inleiding (boven het productraster):**

Decoratie is het laatste half procent: de schaal op tafel, de mand naast de bank, de boekensteun op de plank. Het zijn de stukken die een ruimte bewoond laten voelen zonder druk te maken.

Hier vind je schalen in twee maten, manden per set, objecten van messing en een boekensteun van mangohout. We kiezen op materiaal en vorm, niet op trend; alles in deze collectie combineert met de banken, stoelen en tafels uit onze projecten.

Een goede regel: per oppervlak maximaal drie objecten, in verschillende hoogtes. Meer nodig? Laat ons de laatste laag van je interieur verzorgen als onderdeel van een inrichting. We komen dan langs met een selectie, zetten alles op zijn plek en nemen mee wat niet past. Zo blijft het rustig, ook als er meer in huis staat dan je dacht.


### Maatwerk

- Handle: `/collections/maatwerk`
- Vulling: Handmatig, nog leeg. Wordt gevuld met projectfoto's en maatwerkvoorbeelden in fase 3.
- Meta-titel (50 tekens): Maatwerk meubels · ontwerp en productie via InHuys
- Meta-description (142 tekens): Tafels, kasten en zitmeubels op maat, ontworpen door InHuys en gemaakt door onze partners. Van schets tot plaatsing, in Amsterdam en omgeving.
- Beeldadvies: Maatwerk kast of tafel uit een eigen project.

**Inleiding (boven het productraster):**

Soms past geen enkel standaardmeubel. Een kast die precies tussen twee muren moet, een tafel voor een nis, een bank voor een erker met een schuine hoek. Dan ontwerpen we het zelf en laten we het maken.

Maatwerk begint bij een gesprek en een opmeting. Daarna maken we een ontwerp in 3D, kiezen we materiaal en afwerking, en begeleiden we de productie en de plaatsing. Je ziet vooraf precies wat je krijgt.

Deze pagina toont voorbeelden uit onze projecten zodra die zijn gefotografeerd. Wil je weten wat er kan? Vraag een adviesgesprek aan; maatwerk is altijd onderdeel van een inrichting via InHuys. We werken met meubelmakers in de regio, in eiken, noten, gelakt mdf en staal. De levertijd ligt doorgaans tussen zes en tien weken na akkoord op het ontwerp, afhankelijk van materiaal en drukte in de werkplaats.


### Kinderkamer

- Handle: `/collections/kinderkamer`
- Vulling: Automatisch op merk Jupiduu (14 producten, 5 live). Geen plek op de homepage of in het hoofdmenu, conform besluit eigenaar.
- Meta-titel (47 tekens): Kinderkamer · speelmeubels van Jupiduu · InHuys
- Meta-description (137 tekens): Speelmeubels voor de kinderkamer: ballenbak, glijbaan en speelplek van Jupiduu, in rustige kleuren die passen in een ontworpen interieur.
- Beeldadvies: Ballenbak in een rustige kinderkamer.

**Inleiding (boven het productraster):**

Een kinderkamer hoort bij het huis, niet erbuiten. Daarom kiezen we speelmeubels in rustige kleuren en zachte materialen, die mooi blijven staan als de kamer verder is ingericht.

In deze collectie vind je de speelmeubels van Jupiduu: een ballenbak, een glijbaan voor binnen en buiten, en speelplekken met verwisselbare hoezen. Bij elk stuk staan de maten en de leeftijd waarvoor het geschikt is.

Deze collectie staat bewust los van de rest van het assortiment. Wil je een complete kinderkamer laten ontwerpen? Dat kan als onderdeel van een inrichting. We kijken dan naar opbergruimte, een rustige kleurbasis en een speelplek die meegroeit, zodat de kamer over een paar jaar nog steeds klopt. Ook als de ballenbak al lang is vervangen door een bureau.

