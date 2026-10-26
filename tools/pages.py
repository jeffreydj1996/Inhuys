# Bron van waarheid voor de nieuwe pagina's (fase 2). Genereert markdown in de repo en de pageCreate-variabelen.
import json, sys, re, html
OUT_DIR, OUT_JSON = sys.argv[1], sys.argv[2]
PAGES = []
def page(handle, title, seo_title, seo_desc, blocks, published_note=""):
    PAGES.append(dict(handle=handle, title=title, seo_title=seo_title, seo_desc=seo_desc, blocks=blocks, note=published_note))

# blocks: list of (tag, text) with tags h2, p, ul (list of items), note (invisible in html, visible in md)
page("werkwijze", "Werkwijze", "Werkwijze interieuradvies · gesprek tot inrichting · InHuys",
  "Zo werkt een interieurtraject bij InHuys: gesprek, 3D-ontwerp, materiaal- en kleuradvies, inrichting en begeleiding. Met doorlooptijd en tarieven.",
  [("p","Een interieur dat klopt, ontstaat niet in één keer. Het ontstaat in vier stappen, in een vaste volgorde, met jou aan tafel. Zo weet je op elk moment waar je staat en wat er nog komt."),
   ("h2","1. Gesprek"),
   ("p","We beginnen met een gesprek, online of in de showroom in Purmerend. Je vertelt over het huis, de verbouwing en hoe je wilt wonen. Wij luisteren, stellen vragen en kijken mee naar plattegronden en foto's. Aan het eind van het gesprek weet je of een Flitsadvies genoeg is, of dat je huis om een compleet 3D-ontwerp vraagt."),
   ("h2","2. Ontwerp in 3D"),
   ("p","Bij een compleet traject meten we de ruimte op en tekenen we een plattegrond met de indeling, de looproutes en de plek van elk meubel. Daarna bouwen we het ontwerp in 3D, zodat je precies ziet hoe de ruimte wordt: de verhouding van de bank tot het raam, de hoogte van de tafel, het licht in de avond. Je krijgt het ontwerp als beeld en als plattegrond, met een meubelvoorstel dat bij je wensen en je budget past."),
   ("h2","3. Materiaal en kleur"),
   ("p","Een ontwerp wordt pas echt met stof in de hand. We stellen een moodboard samen met stalen van bekleding, hout, steen en verf, en adviseren over kleur voor wanden, vloer en gordijnen. Alles wat we voorstellen, is in de showroom te zien en te voelen."),
   ("h2","4. Inrichting en begeleiding"),
   ("p","Na akkoord bestellen we de meubels bij onze merkpartners, bewaken we de levertijden en stemmen we af met je aannemer of schilder waar dat nodig is. Op de dag van levering zijn we erbij: we zetten alles op zijn plek en maken het af met de laatste laag, van vaas tot plaid. Maatwerk, zoals een kast of een tafel op maat, ontwerpen we zelf en laten we maken door meubelmakers in de regio."),
   ("h2","Wat je krijgt"),
   ("ul",["Een plattegrond met indeling en maatvoering","Een 3D-ontwerp van de ruimte, als beeld en als wandel-door-de-ruimte-weergave in de showroom","Een meubelvoorstel met prijzen en levertijden","Een moodboard met materiaal- en kleuradvies","Begeleiding bij bestelling, levering en plaatsing"]),
   ("h2","Doorlooptijd"),
   ("p","Een Flitsadvies is binnen een week gepland en duurt ongeveer een uur. Een compleet 3D-ontwerp vraagt twee tot vier weken, afhankelijk van de omvang van het huis en hoe snel we samen keuzes kunnen maken. Levertijden van meubels liggen meestal tussen de twee en acht weken; maatwerk tussen zes en tien weken na akkoord op het ontwerp."),
   ("h2","Tarieven"),
   ("ul",["Flitsadvies: gratis. Online of in de showroom, ongeveer een uur, inclusief een basis 2D-vloerplan als dat helpt.","3D-interieurontwerp compleet: prijs op aanvraag; het bedrag verrekenen we bij aankoop van de inrichting via InHuys.","Maatwerk: op offerte, na het ontwerp."]),
   ("p","Zo weet je vooraf waar je aan toe bent, en betaal je voor het ontwerp alleen als je de inrichting ergens anders koopt."),
   ("h2","Begin met een gesprek"),
   ("p","Plan een Flitsadvies of vraag direct het complete 3D-ontwerp aan via de pagina Interieuradvies. Liever eerst even kijken? Je bent welkom in de showroom in Purmerend, op afspraak.")],
  "Nieuwe pagina, aangemaakt als concept (niet gepubliceerd). Vanaf-prijs van het 3D-ontwerp moet de eigenaar invullen.")

page("showroom", "Showroom Purmerend", "Showroom Purmerend · InHuys bij Kluster · op afspraak",
  "Bezoek de showroom van InHuys in Purmerend (Netwerk 124, bij Kluster). Stoelen, banken, stalen en materialen uit onze projecten. Op afspraak, ook 's avonds.",
  [("p","Een stoel kies je met je rug, niet met je ogen. Daarom hebben we een showroom in Purmerend, in het pand van Kluster aan de Netwerk 124. Hier zie je de stoelen, barkrukken en banken uit onze collectie in het echt, en voel je de stalen van boucle, velvet en weefstof naast elkaar."),
   ("h2","Wat je er vindt"),
   ("ul",["De eetkamerstoelen en barkrukken uit de collectie, om te proefzitten","Banken en fauteuils uit de series die we in projecten gebruiken","Stalenboeken van bekleding, hout, keramiek en travertijn","Vazen, windlichten en decoratie","Een werkplek met het 3D-ontwerp van jouw huis, als je een traject bij ons doet"]),
   ("h2","Adres en bereikbaarheid"),
   ("p","InHuys bij Kluster<br>Netwerk 124<br>1446 WR Purmerend"),
   ("p","De showroom ligt op bedrijventerrein Baanstee, met parkeren voor de deur. Vanuit Amsterdam ben je er in ongeveer een half uur via de A7 of de N235."),
   ("h2","Openingstijden"),
   ("p","We werken op afspraak, zodat we de tijd voor je hebben en de showroom niet deelt met een andere klant. Afspraken zijn mogelijk op werkdagen, overdag en 's avonds, en in overleg op zaterdag. Bel, app of mail om een moment te kiezen."),
   ("ul",["Telefoon en WhatsApp: +31 6 12932148","E-mail: info@in-huys.nl"]),
   ("h2","Neem je plattegrond mee"),
   ("p","Een bezoek wordt het nuttigst als je de maten van de ruimte, een paar foto's en eventueel de plattegrond van de verbouwing meeneemt. Dan tekenen we ter plekke hoe een bank of tafel in jouw huis past.")],
  "Nieuwe pagina, aangemaakt als concept. Openingstijden en het wijkdeel (Baanstee) moet de eigenaar bevestigen.")

page("over-inhuys", "Over InHuys", "Over InHuys · interieurstylist Sylvana · Amsterdam",
  "InHuys is het interieurbureau van Sylvana: ontwerp, advies en inrichting voor verbouwingen in Amsterdam en omgeving, met een showroom in Purmerend.",
  [("p","InHuys is het interieurbureau van Sylvana. Ontwerp, advies en inrichting: dat is wat we doen, voor mensen die verbouwen of opnieuw beginnen in een huis dat ze al kennen. We werken in Amsterdam en omgeving en hebben een showroom in Purmerend."),
   ("h2","Ik ben Sylvana"),
   ("p","Elke dag help ik mensen hun huis samen te stellen: de indeling, de meubels, de materialen en de laatste laag die een ruimte afmaakt. Ik hou van interieurs die rust geven en kloppen in de details, zonder dat je ziet hoeveel werk erin zit. Ik woon zelf met kinderen, dus ik weet dat mooi en praktisch samen moeten gaan."),
   ("p","Wat ik het liefst doe, is met iemand aan tafel zitten, een plattegrond uitvouwen en samen uitzoeken waar het licht valt, waar de bank moet staan en welke stof dat mooi draagt. Daarna zorg ik dat het ook gebeurt, tot en met de dag dat alles op zijn plek staat."),
   ("h2","Hoe we kiezen"),
   ("p","De collectie op deze site is geen webshop met alles erop en eraan. Het is een selectie van stukken die we in projecten gebruiken en in de showroom hebben staan. We werken met een paar merken waarvan we de kwaliteit kennen: Pole To Pole voor stoelen, barkrukken en banken, MOOISA voor steen, Jesper Home en Kluster voor accessoires. Bij elk product staan de maten, het materiaal en de levertijd, en een advies over waar het wel en niet past."),
   ("h2","Wat je van ons mag verwachten"),
   ("ul",["Een eerlijk advies, ook als dat betekent dat je minder hoeft te kopen","Concrete maten en materialen, geen mooie woorden","Eén aanspreekpunt van gesprek tot plaatsing","Een showroom waar je alles kunt zien en voelen"]),
   ("h2","Bedrijfsgegevens"),
   ("p","InHuys<br>Netwerk 124, 1446 WR Purmerend<br>InHuys is een handelsnaam van Kluster · KvK 88545857 · btw NL8680053B01<br>+31 6 12932148 · info@in-huys.nl")],
  "Nieuwe pagina, aangemaakt als concept. De persoonlijke alinea's zijn een voorzet in Sylvana's stem; zij past ze aan.")

page("projecten", "Projecten", "Projecten · interieurontwerp en inrichting · InHuys",
  "Bekijk projecten van InHuys: verbouwingen en inrichtingen in Amsterdam en omgeving, van plattegrond tot de laatste vaas, met de keuzes erbij.",
  [("p","Elk project begint met een vraag en eindigt met een huis dat klopt. Hieronder laten we zien wat daartussen gebeurt: de opgave, de keuzes en het resultaat."),
   ("h2","[PROJECT 1 · naam of straat, plaats]"),
   ("p","[Opgave: wat vroeg de bewoner? Bijvoorbeeld een uitbouw met open keuken, waar de zithoek en de eettafel elkaar in de weg zaten.]"),
   ("p","[Keuzes: indeling, materialen, kleuren, meubels. Welke stukken uit de collectie, welk maatwerk.]"),
   ("p","[Resultaat: wat is er veranderd in hoe het huis voelt en werkt. Eén zin van de bewoner als die er is.]"),
   ("p","[Foto's: 6 tot 10 beelden, minimaal 2000 px breed, in daglicht.]"),
   ("h2","[PROJECT 2 · naam of straat, plaats]"),
   ("p","[Zelfde opbouw.]"),
   ("h2","[PROJECT 3 · naam of straat, plaats]"),
   ("p","[Zelfde opbouw.]"),
   ("h2","Jouw project"),
   ("p","Wil je weten wat we voor jouw huis kunnen doen? Plan een gesprek via de pagina Interieuradvies, of kom langs in de showroom in Purmerend.")],
  "Nieuwe pagina, aangemaakt als concept met plaatshouders. Wordt gevuld zodra de eigenaar drie projecten met foto's aanlevert.")

page("veelgestelde-vragen", "Veelgestelde vragen", "Veelgestelde vragen · advies, levering en retour · InHuys",
  "Antwoorden op vragen over interieuradvies, het 3D-ontwerp, de showroom, levertijden, retourneren en maatwerk bij InHuys.",
  [("h2","Over het advies"),
   ("p","<strong>Wat is het verschil tussen een Flitsadvies en een 3D-ontwerp?</strong><br>Een Flitsadvies is een gesprek van ongeveer een uur, online of in de showroom, over één concrete vraag: een kleur, een indeling, een meubel. Een 3D-ontwerp is een compleet traject voor een ruimte of een huis, met opmeting, plattegrond, 3D-beelden, meubelvoorstel en moodboard."),
   ("p","<strong>Wat kost het?</strong><br>Het Flitsadvies is gratis. Het 3D-ontwerp heeft een vanaf-prijs die je terugkrijgt als je de inrichting via InHuys koopt. De actuele bedragen staan op de pagina Werkwijze."),
   ("p","<strong>Werken jullie ook buiten Amsterdam?</strong><br>Ons werkgebied is Amsterdam en omgeving, inclusief Purmerend en de regio Waterland. Voor een online Flitsadvies maakt de plaats niet uit."),
   ("p","<strong>Moet ik de meubels bij InHuys kopen?</strong><br>Nee. Het advies staat op zichzelf. Koop je de inrichting bij ons, dan verrekenen we de kosten van het 3D-ontwerp."),
   ("h2","Over de showroom"),
   ("p","<strong>Kan ik zomaar binnenlopen?</strong><br>We werken op afspraak, zodat we tijd voor je hebben. Bel, app of mail en we plannen een moment, ook buiten kantoortijden."),
   ("p","<strong>Staat alles uit de collectie in de showroom?</strong><br>De stoelen, barkrukken en een selectie banken en accessoires staan er. Van de overige stukken hebben we stalen en afbeeldingen."),
   ("h2","Over bestellen en levering"),
   ("p","<strong>Hoe lang is de levertijd?</strong><br>Die staat bij elk product. Stoelen en accessoires zijn meestal binnen twee tot drie weken te leveren; banken en tafels binnen vier tot acht weken; maatwerk binnen zes tot tien weken na akkoord op het ontwerp."),
   ("p","<strong>Wie levert?</strong><br>Meubels worden geleverd door de merkpartner of een transporteur die wij inschakelen. Bij een inrichting via InHuys zijn we bij de levering aanwezig en zetten we alles op zijn plek."),
   ("p","<strong>Kan ik retourneren?</strong><br>Ja, binnen de wettelijke termijn van veertien dagen na ontvangst, in originele staat. Maatwerk en producten die speciaal voor jou zijn gemaakt, zijn uitgesloten. De volledige voorwaarden staan in het retourbeleid."),
   ("p","<strong>Hoe kan ik betalen?</strong><br>Via iDEAL, creditcard en de andere betaalmethoden in de webshop. Bij een inrichting via InHuys ontvang je een offerte en factuur."),
   ("h2","Over maatwerk"),
   ("p","<strong>Wat kan er op maat?</strong><br>Tafels, kasten, wandmeubels en zitmeubels voor een specifieke plek. We ontwerpen het en laten het maken door meubelmakers in de regio, in eiken, noten, gelakt mdf en staal."),
   ("p","<strong>Krijg ik eerst een tekening?</strong><br>Ja. Je ziet het ontwerp in 3D en krijgt een werktekening met maten voordat de productie start.")],
  "Nieuwe pagina, aangemaakt als concept. Levertijden zijn richtwaarden en moeten per merk worden bevestigd.")

# Teksten voor bestaande live pagina's: alleen in de repo en in de thema-kopie, niet via de API gewijzigd.
EXTRA = {
 "interieuradvies": ("Interieuradvies (bestaande pagina · nieuwe tekst voor na akkoord)", "Interieuradvies Amsterdam · Flitsadvies en 3D · InHuys",
   "Interieuradvies voor je verbouwing: gratis Flitsadvies, online of in de showroom in Purmerend, of een compleet 3D-interieurontwerp. Regio Amsterdam.",
   [("p","Een verbouwing is pas af als de ruimte klopt. InHuys ontwerpt, adviseert en richt in, voor huizen in Amsterdam en omgeving. Kies de vorm die bij je vraag past."),
    ("h2","Flitsadvies · gratis"),
    ("p","Eén vraag, één uur, direct resultaat. Online of in de showroom in Purmerend. Voor een kleurkeuze, een indelingsvraag, een meubel dat niet wil passen. Je krijgt mondeling advies over stijl, materiaal, kleur of product, en als het helpt een basis 2D-vloerplan. Neem foto's en maten mee; dan kunnen we meteen concreet worden."),
    ("h2","3D-interieurontwerp compleet · prijs op aanvraag"),
    ("p","Voor een ruimte of een heel huis. We meten op, maken een plattegrond en bouwen het ontwerp in 3D, zodat je ziet hoe het wordt voordat er iets besteld is. Je krijgt een meubelvoorstel dat past bij je wensen en je budget, en een uitgewerkt moodboard met materiaal- en kleuradvies. De prijs hangt af van het aantal ruimtes; je krijgt hem vooraf, en we verrekenen hem als je de inrichting via InHuys koopt."),
    ("h2","Zo gaat het"),
    ("p","Gesprek, ontwerp in 3D, materiaal en kleur, inrichting en begeleiding. De volledige werkwijze, met doorlooptijden en tarieven, staat op de pagina Werkwijze."),
    ("h2","Plan een gesprek"),
    ("p","Vul het formulier in of bel +31 6 12932148. We reageren binnen twee werkdagen met een voorstel voor een moment, online of in de showroom.")]),
 "contact": ("Contact (bestaande pagina · nieuwe tekst voor na akkoord)", "Contact · InHuys · Purmerend en Amsterdam",
   "Neem contact op met InHuys: vragen over een product, de showroom in Purmerend of een adviesgesprek. We reageren binnen twee werkdagen.",
   [("p","Vragen over een product, de showroom of een adviesgesprek? Stuur een bericht via het formulier, of bel of app ons. We reageren binnen twee werkdagen."),
    ("p","InHuys bij Kluster<br>Netwerk 124, 1446 WR Purmerend<br>+31 6 12932148 · info@in-huys.nl<br>Showroom op afspraak")]),
}

def to_html(blocks):
    out=[]
    for tag,val in blocks:
        if tag=="h2": out.append(f"<h2>{val}</h2>")
        elif tag=="p": out.append(f"<p>{val}</p>")
        elif tag=="ul": out.append("<ul>"+"".join(f"<li>{i}</li>" for i in val)+"</ul>")
    return "\n".join(out)
def to_md(blocks):
    out=[]
    for tag,val in blocks:
        if tag=="h2": out.append(f"## {val}\n")
        elif tag=="p": out.append(re.sub(r'<br>', '  \n', re.sub(r'</?strong>','**',val))+"\n")
        elif tag=="ul": out.append("\n".join(f"- {i}" for i in val)+"\n")
    return "\n".join(out)

V={}
for i,p in enumerate(PAGES,1):
    md=[f"# {p['title']}", "", f"Handle: `/pages/{p['handle']}` · Status: concept (niet gepubliceerd) · {p['note']}", "", f"Meta-titel ({len(p['seo_title'])}): {p['seo_title']}  ", f"Meta-description ({len(p['seo_desc'])}): {p['seo_desc']}", "", "---", "", to_md(p['blocks'])]
    open(f"{OUT_DIR}/{p['handle']}.md","w",encoding="utf-8").write("\n".join(md))
    V[f"p{i}"]={"title":p['title'],"handle":p['handle'],"isPublished":False,"body":to_html(p['blocks']),
                "metafields":[{"namespace":"global","key":"title_tag","type":"single_line_text_field","value":p['seo_title']},
                              {"namespace":"global","key":"description_tag","type":"single_line_text_field","value":p['seo_desc']}]}
for h,(title,st,sd,blocks) in EXTRA.items():
    md=[f"# {title}", "", f"Handle: `/pages/{h}` · bestaande live pagina, NIET gewijzigd via de API. Deze tekst staat klaar voor na akkoord; de dienstkaarten staan in de thema-kopie.", "", f"Meta-titel ({len(st)}): {st}  ", f"Meta-description ({len(sd)}): {sd}", "", "---", "", to_md(blocks)]
    open(f"{OUT_DIR}/{h}.md","w",encoding="utf-8").write("\n".join(md))
json.dump(V,open(OUT_JSON,"w",encoding="utf-8"),ensure_ascii=False)
for p in PAGES: print(f"{p['handle']:22} seo_title={len(p['seo_title'])} seo_desc={len(p['seo_desc'])} woorden={sum(len(re.sub('<[^>]+>','',str(v)).split()) for _,v in p['blocks'])}")
