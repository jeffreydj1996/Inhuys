import json, sys, re
OUT_MD, OUT_JSON = sys.argv[1], sys.argv[2]
A = []
def art(**k): A.append(k)

art(key="boucle", handle="boucle-onderhouden-zo-blijft-je-bank-mooi", title="Boucle onderhouden: zo blijft je bank of stoel jaren mooi",
  tags=["boucle", "onderhoud", "banken", "stoelen"],
  seo_title="Boucle onderhouden · zo blijft je bank mooi · InHuys", summary="Boucle is zacht en sterk, maar vraagt een andere aanpak dan een gladde stof. Dit is wat wel en niet werkt, uit de praktijk van onze inrichtingen.",
  secties=[
   ("Wat boucle is en waarom het zo lekker zit", ["Boucle is een stof met kleine lusjes in het garen. Die lusjes vangen licht en geven de stof een zachte, bijna wollige structuur. Daarom voelt een bank in boucle warmer aan dan een bank in een gladde weefstof, en daarom ziet hij er in een strak interieur zo vriendelijk uit.", "Diezelfde lusjes bepalen hoe je de stof onderhoudt. Ze houden stof en haren vast, en ze kunnen uitgetrokken worden als je er met een scherpe rand overheen gaat. Wie dat weet, heeft er jaren plezier van."]),
   ("Wekelijks: stofzuigen zonder borstel", ["Zuig boucle één keer per week met het gladde mondstuk van de stofzuiger, op lage stand. Gebruik geen roterende borstel; die trekt de lusjes los. Werk in de richting van het weefsel en vergeet de naden niet, daar verzamelt het meeste stof zich.", "Heb je een hond of kat, zuig dan twee keer per week en gebruik tussendoor een kledingroller. Haren die in de lusjes blijven zitten, zijn later moeilijker te verwijderen."]),
   ("Vlekken: deppen, nooit wrijven", ["Een vlek op boucle dep je direct met een schone, witte doek en lauw water. Wrijven maakt de vlek groter en verstoort de structuur. Werk van de buitenkant van de vlek naar het midden.", "Bij vet of wijn: een druppel neutraal afwasmiddel in lauw water, deppen, daarna naspoelen met een doek met schoon water en laten drogen zonder föhn. Test elk middel eerst aan de onderkant van een kussen. Oplosmiddelen en ontvlekkers met bleek horen niet op boucle."]),
   ("Pillen en losse lusjes", ["Na een paar maanden kunnen er kleine bolletjes ontstaan op de zitting. Dat is normaal bij een stof met lus. Knip ze weg met een kleine schaar of een pluizentondeuse op de laagste stand; trek er nooit aan, dan komt het garen mee.", "Een uitgetrokken lusje duw je met een stompe naald terug in het weefsel. Niet afknippen, want dan ontstaat een open plek."]),
   ("Zon, kussens en draaien", ["Boucle verkleurt licht in direct zonlicht, net als de meeste stoffen. Staat de bank voor een raam op het zuiden, draai de losse kussens dan elke twee weken en wissel ze van plek. Zo slijt en verkleurt alles gelijkmatig.", "Schud de kussens elke week op. Een bank met schuim en vezelvulling blijft dan diep en veerkrachtig, ook na jaren."]),
   ("Welke boucle wij gebruiken", ["In onze collectie staat boucle onder meer op de Bank New York in zand en op de Cloud-serie. De weefstof die Pole To Pole gebruikt is dichtgeweven en stevig; met het onderhoud hierboven gaat hij lang mee. Twijfel je of boucle bij je huishouden past, bijvoorbeeld met jonge kinderen of huisdieren, dan adviseren we de gladde weefstof in beige of coco. Die is er in dezelfde modellen.", "Wil je de stoffen in het echt zien en voelen? In de showroom in Purmerend liggen alle stalen. Maak een afspraak via de contactpagina."])],
  links=["/collections/banken", "/products/bank-new-york", "/products/eetkamerstoel-cloud-set-van-2", "/pages/showroom"])

art(key="ronde-tafel", handle="eetkamerstoelen-bij-een-ronde-tafel", title="Eetkamerstoelen bij een ronde tafel: hoeveel passen er en welke werken",
  tags=["eetkamerstoelen", "tafels", "indeling"],
  seo_title="Stoelen bij een ronde tafel · aantal en keuze · InHuys", summary="Een ronde tafel is gezelliger, maar vergeeft minder. Dit zijn de maten die we in onze inrichtingen aanhouden en de stoelen die er goed bij staan.",
  secties=[
   ("Waarom een ronde tafel anders werkt", ["Aan een rechthoekige tafel zit je in rijen; aan een ronde tafel zit iedereen even dicht bij elkaar. Dat maakt een ronde tafel de beste keuze voor een gezin dat lang aan tafel zit en voor een eethoek die vrij in de ruimte staat. Het nadeel: elke stoel is van alle kanten zichtbaar, en er passen er minder aan dan je denkt."]),
   ("Hoeveel stoelen passen er", ["Reken met de omtrek van de tafel en de breedte van de stoel. Een stoel zonder armleuning vraagt 55 cm, een stoel met armleuning 65 cm. Deze aantallen houden we aan:", "- Tafel Ø 100 cm: 3 tot 4 stoelen zonder armleuning.\n- Tafel Ø 120 cm: 4 stoelen, 5 als het moet.\n- Tafel Ø 130 cm: 4 stoelen met armleuning of 5 zonder.\n- Tafel Ø 150 cm: 6 stoelen zonder armleuning.\n- Tafel Ø 160 cm en groter: 6 tot 8 stoelen.", "Houd rondom de tafel 80 cm vrij om te kunnen aanschuiven en langslopen. Een tafel van 120 cm in een eethoek van 3 bij 3 meter is daarom al vol."]),
   ("Welke stoelen goed staan", ["Bij een ronde tafel werkt een stoel met een ronde of gebogen rug het best; de vorm komt terug in het blad. De Cloud met zijn ronde kuip en de Whale met zijn doorlopende gebogen rug zijn hier voor gemaakt. Een rechte stoel zoals de Scandi kan ook, maar oogt aan een ronde tafel wat strenger.", "Een stoel met armleuning, zoals de Breeze, neemt meer ruimte en past daarom pas vanaf Ø 130 cm. Hij zit wel het langst comfortabel."]),
   ("Eén soort stoel of mengen", ["Aan een ronde tafel staat één model het rustigst, omdat je alle stoelen tegelijk ziet. Wil je toch variatie, kies dan één model in twee kleuren uit dezelfde serie, bijvoorbeeld de Cloud in crème en karamel om en om. Mengen van modellen doen we liever aan een lange tafel, met een kopstoel aan beide einden."]),
   ("Tafelhoogte en zithoogte", ["De meeste eettafels zijn 75 tot 78 cm hoog. Daar hoort een zithoogte van 46 tot 48 cm bij; tussen zitting en blad moet 28 tot 30 cm vrij blijven. Controleer dit bij een lage of juist hoge designtafel, en meet ook de hoogte van de armleuning: die moet onder het blad kunnen schuiven."]),
   ("Hulp bij de keuze", ["Stuur de maat van je tafel en een foto van de eethoek mee met een Flitsadvies, dan rekenen we het aantal en het model voor je uit. In de showroom in Purmerend staan de modellen uit dit artikel; je kunt ze er aan een ronde tafel proberen."])],
  links=["/collections/stoelen", "/products/eetkamerstoel-cloud-set-van-2", "/products/eetkamerstoel-whale-set-van-2", "/products/eetkamerstoel-breeze-set-van-2", "/pages/interieuradvies"])

art(key="verbouwing", handle="interieur-inrichten-na-een-verbouwing", title="Je interieur inrichten na een verbouwing: wanneer je begint en wat je eerst kiest",
  tags=["verbouwing", "interieuradvies", "werkwijze"],
  seo_title="Inrichten na een verbouwing · zo pak je het aan · InHuys", summary="De muren staan, de vloer ligt, en dan? Dit is de volgorde die we aanhouden als we een verbouwd huis inrichten, en het moment waarop advies het meeste oplevert.",
  secties=[
   ("Begin eerder dan je denkt", ["De meeste mensen beginnen met de inrichting als de aannemer klaar is. Dan zijn de keuzes die het meeste bepalen al gemaakt: waar de stopcontacten zitten, waar het licht hangt, hoe breed de doorgang naar de keuken is. Wij schuiven het liefst aan als de tekening er ligt en de aannemer nog niet is begonnen. Dan kost een wijziging een potloodstreep in plaats van een hakwerk."]),
   ("Eerst de plattegrond, dan de stijl", ["Een goede inrichting begint met een plattegrond op schaal. Daarop tekenen we de zithoek, de eethoek en de looproutes, met de echte maten van meubels. Pas als dat klopt, kiezen we materialen en kleuren. Wie andersom werkt, koopt een bank die niet door de deur past of een tafel waar maar vier stoelen aan kunnen.", "Vuistregels die we aanhouden: 80 cm looproute rondom tafel en bank, een bank niet breder dan tweederde van de wand, en een vloerkleed waar de voorpoten van de bank op staan."]),
   ("Grote stukken eerst, in deze volgorde", ["1. De bank. Die bepaalt de zithoek en de looplijn in de woonkamer.\n2. De eettafel en de stoelen. Samen de grootste groep meubels in huis.\n3. Verlichting. Een hanglamp boven tafel moet op de juiste plek hangen; dat regel je met de elektricien, niet achteraf.\n4. Kasten en opbergen.\n5. Vloerkleed, gordijnen, accessoires.", "Accessoires komen als laatste, maar ze maken het verschil tussen een ingerichte en een bewoonde ruimte. Een vaas van travertijn op een leeg dressoir doet meer dan drie kleine objecten."]),
   ("Kleur en materiaal: drie, niet tien", ["Een rustig interieur heeft een palet van drie materialen en drie kleuren. Bijvoorbeeld: eiken, travertijn en een zachte weefstof; zand, crème en coco. Alles wat je daarna kiest, moet in dat palet passen. Dat klinkt beperkend, maar het is precies waarom sommige huizen zo rustig aanvoelen."]),
   ("Wat advies oplevert", ["Een Flitsadvies is gratis: stuur een plattegrond en foto's, en je krijgt binnen een paar dagen een opzet van de indeling en een voorstel voor de belangrijkste stukken. Een 3D-interieurontwerp gaat verder: je ziet de ruimte met de gekozen meubels, stoffen en lichtval voordat je iets koopt. De kosten daarvan verrekenen we bij aankoop van de inrichting.", "We werken in de regio Amsterdam en ontvangen je in de showroom in Purmerend, waar de banken, stoelen en materialen uit dit artikel staan."])],
  links=["/pages/interieuradvies", "/pages/werkwijze", "/collections/banken", "/collections/vazen", "/pages/showroom"])

art(key="travertijn", handle="travertijn-in-huis-onderhoud-en-combineren", title="Travertijn in huis: hoe je het onderhoudt en waar het mooi staat",
  tags=["travertijn", "natuursteen", "vazen", "tafels", "onderhoud"],
  seo_title="Travertijn onderhouden en combineren · InHuys", summary="Travertijn is zacht, warm en poreus. Dat maakt het mooi en kwetsbaar tegelijk. Dit is wat we klanten vertellen bij een vaas of salontafel van travertijn.",
  secties=[
   ("Wat travertijn is", ["Travertijn is een kalksteen die ontstaat bij warme bronnen. Het gas dat daarbij vrijkomt laat open poriën achter; die gaatjes en de zachte beige tekening zijn het kenmerk van de steen. Elk stuk is anders. Een vaas of tafelblad van travertijn is daarom nooit precies gelijk aan de foto, en dat is de bedoeling."]),
   ("Poreus: wat dat betekent in de praktijk", ["De poriën nemen vocht op. Een glas water dat overloopt laat een donkere plek achter die weer wegtrekt; rode wijn, koffie of olie kunnen blijvend vlekken. Zuren zoals citroen en azijn etsen het oppervlak dof. Daarom geven we bij een travertijn tafelblad altijd het advies om onderzetters te gebruiken en gemorste vloeistof direct op te nemen.", "Een vaas van travertijn is niet volledig waterdicht. Zet er droge takken in, of gebruik een glazen inzet voor verse bloemen."]),
   ("Onderhoud: weinig, maar wel het juiste", ["- Afnemen met een droge of licht vochtige doek.\n- Geen zuren, geen schuurmiddelen, geen allesreiniger.\n- Een tafelblad één keer per jaar impregneren met een middel voor kalksteen; dat sluit de poriën deels af zonder de kleur te veranderen.\n- Vlekken die niet weggaan: een pasta van baksoda en water, een nacht laten intrekken, afnemen. Test eerst aan de onderkant."]),
   ("Waar travertijn mooi staat", ["Travertijn werkt het best als rustpunt in een ruimte met hout en textiel. Een salontafel met travertijn blad bij een bank in zand boucle; een grote Agano-vaas op een eiken dressoir; twee kleine kandelaars van steen op een eettafel. Combineer het niet met keramiek in marmerlook op dezelfde plek, dan vechten de twee steenpatronen om aandacht.", "Op een zwevende plank of een licht tafeltje hoort travertijn niet: een grote vaas weegt tot 10 kg."]),
   ("In onze collectie", ["De Agano-vaas van MOOISA is gedraaid uit één blok travertijn en komt in twee maten. Salontafels met travertijn blad staan in de showroom in Purmerend; daar zie je ook hoe de steen verandert bij daglicht en kunstlicht."])],
  links=["/collections/vazen", "/products/vaas-agano-travertijn", "/collections/tafels", "/pages/showroom"])

def html(a):
    parts = [f"<p>{a['summary']}</p>"]
    for kop, pars in a['secties']:
        parts.append(f"<h2>{kop}</h2>")
        for p in pars:
            if p.startswith("- "):
                parts.append("<ul>" + "".join(f"<li>{li[2:]}</li>" for li in p.split("\n")) + "</ul>")
            elif re.match(r"^\d+\. ", p):
                parts.append("<ol>" + "".join(f"<li>{re.sub(r'^\d+\. ', '', li)}</li>" for li in p.split("\n")) + "</ol>")
            else:
                parts.append(f"<p>{p}</p>")
    return "".join(parts)
vars_ = {}
for i, a in enumerate(A, 1):
    body = html(a)
    vars_[f"a{i}"] = {"blogId": "gid://shopify/Blog/119658316115", "title": a['title'], "handle": a['handle'], "author": {"name": "Sylvana, InHuys"}, "isPublished": False, "tags": a['tags'], "summary": f"<p>{a['summary']}</p>", "body": body,
                      "metafields": [{"namespace": "global", "key": "title_tag", "type": "single_line_text_field", "value": a['seo_title']}, {"namespace": "global", "key": "description_tag", "type": "single_line_text_field", "value": a['summary'][:160]}]}
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    md = [f"# {a['title']}", "", f"Handle: `/blogs/trends/{a['handle']}` · Status: **concept** (niet gepubliceerd) in blog Trends · Auteur: Sylvana, InHuys · {words} woorden", "",
          f"Meta-titel ({len(a['seo_title'])}): {a['seo_title']}  ", f"Samenvatting / meta-description: {a['summary']}", "", f"Interne links in het artikel (te zetten bij publicatie, zodra de doelpagina's live zijn): {', '.join('`'+l+'`' for l in a['links'])}", ""]
    for kop, pars in a['secties']:
        md += [f"## {kop}", ""]
        for p in pars: md += [p, ""]
    open(f"{OUT_MD}/{a['handle']}.md", "w", encoding="utf-8").write("\n".join(md))
    print(a['key'], words, "woorden; seo_title", len(a['seo_title']))
json.dump(vars_, open(OUT_JSON, "w", encoding="utf-8"), ensure_ascii=False)
