# Fase 2-generator (teksten hardgecodeerd). Vervangen door tools/md_naar_vars.py; alleen bewaard als regressiebron. Genereert content/producten/*.md, productSet-variabelen en redirects.csv.
import json, sys, re, csv
SRC, OUT_MD, OUT_DIR, OUT_REDIR = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
src = json.load(open(SRC))
ORIG_ALT = json.load(open(sys.argv[5], encoding="utf-8"))  # handle -> {url: huidige alt} uit de export vóór fase 2
by_handle = {it['handle']: it for items in src.values() for it in items}
CAT = {"stoel": "gid://shopify/TaxonomyCategory/fr-7-9", "barkruk": "gid://shopify/TaxonomyCategory/fr-7-12-2", "vaas": "gid://shopify/TaxonomyCategory/hg-3-67", "kandelaar": "gid://shopify/TaxonomyCategory/hg-3-39-2", "boekensteun": "gid://shopify/TaxonomyCategory/hg-3-12", "sofa": "gid://shopify/TaxonomyCategory/fr-22"}
COLL = {"vazen": "gid://shopify/Collection/704710672723", "windlichten": "gid://shopify/Collection/704710705491", "decoratie": "gid://shopify/Collection/704710738259"}
AANV = "[AANVULLEN]"
PRODUCTS = []
def rt(paragraphs):  # rich text metafield JSON; paragraphs: list of str or (bold, rest)
    ch = []
    for p in paragraphs:
        if isinstance(p, tuple):
            ch.append({"type": "paragraph", "children": [{"type": "text", "value": p[0], "bold": True}, {"type": "text", "value": " " + p[1]}]})
        else:
            ch.append({"type": "paragraph", "children": [{"type": "text", "value": p}]})
    return json.dumps({"type": "root", "children": ch}, ensure_ascii=False)
def product(**k): PRODUCTS.append(k)

LEVER_STOEL = "2 tot 3 weken, geleverd door onze merkpartner"
product(key="breeze", title="Breeze eetkamerstoel met armleuning (set van 2)", handle="eetkamerstoel-breeze-set-van-2", vendor="Pole To Pole", ptype="Stoelen", cat="stoel",
  tags=["eetkamerstoel", "set van 2", "armleuning", "staal", "beige", "latte", "pastelroze", "pistache", "pole-to-pole"],
  short="Lichte eetkamerstoel met hoge, zachte rug en armleuning, per set van twee.",
  ruimte="De Breeze is een eetkamerstoel voor wie lang aan tafel zit. De hoge, zachte rug steunt tot in de schouders, de armleuningen maken het verschil tussen eten en blijven zitten. Door de open vorm van het onderstel oogt hij licht, ook met zes stuks rond een ovale tafel van 220 cm. De stoel past bij tafelhoogtes van 75 tot 78 cm.",
  materiaal="De zitting en rug zijn gestoffeerd over een stevige kern; het onderstel is van gepoedercoat staal, gespoten in een tint die bij de bekleding past. De stof is verkrijgbaar in vier kleuren: beige, latte, pastelroze en pistache. Beige en latte zijn de rustige keuzes; pastelroze en pistache geven een eethoek met een houten tafel precies genoeg kleur.",
  combineren="Bij een ronde tafel in eiken of travertijn werkt de Breeze in beige of latte als rustige basis; zet er een pistache aan het hoofdeinde voor accent. Bij een zwarte keramische tafel kies je latte of beige voor contrast. Combineer met de Cloud-barkruk aan het keukeneiland in dezelfde kleur, zodat eetkamer en keuken één geheel worden.",
  specs={"afmetingen": AANV, "zithoogte": AANV, "zitdiepte": AANV, "gewicht": AANV, "materiaal_frame": "Gepoedercoat staal", "materiaal_bekleding": AANV + " (stof)", "afwerking": "Beige, latte, pastelroze of pistache", "set_inhoud": "2 stoelen", "onderhoud": "Stofzuigen met zachte borstel; vlekken deppen met lauw water en een neutraal reinigingsmiddel", "herkomst": "Pole To Pole, Nederland", "levertijd": LEVER_STOEL, "garantie": "2 jaar"},
  advies=["Ik zet de Breeze in waar mensen echt aan tafel leven: bij een gezin dat ontbijt, huiswerk en avondeten aan dezelfde tafel doet. De armleuningen maken hem comfortabel, maar vragen wel ruimte: reken op 65 cm per stoel. Bij een tafel smaller dan 90 cm zou ik voor een model zonder armleuning kiezen, zoals de Cloud."],
  faq=[("Hoeveel Breeze-stoelen passen er aan een tafel van 180 cm?", "Zes, met aan elke lange zijde drie stoelen. Reken op 65 cm per stoel vanwege de armleuningen."), ("Is de stof geschikt voor een gezin met kinderen?", "Ja. De bekleding laat zich stofzuigen en vlekken dep je met lauw water. Kies beige of latte als je weinig wilt zien."), ("Wordt de stoel gemonteerd geleverd?", "De stoelen worden per set van twee geleverd door onze merkpartner; eventuele montage beperkt zich tot het bevestigen van het onderstel."), ("Kan ik de stoel eerst zien?", "Ja, in de showroom in Purmerend, op afspraak.")],
  seo_title="Breeze eetkamerstoel met armleuning · set van 2 · InHuys", seo_desc="Eetkamerstoel met hoge zachte rug en armleuning, set van 2. In beige, latte, pastelroze en pistache op een stalen onderstel. Levertijd 2 tot 3 weken.",
  options=[("Kleur", ["Beige", "Latte", "Pastelroze", "Pistache"])],
  variants=[({"Kleur": "Beige"}, "599.80", "871974353020", "breeze-stoel-beige-set-van-2"), ({"Kleur": "Latte"}, "599.80", "871974353021", "breeze-stoel-latte-set-van-2"), ({"Kleur": "Pastelroze"}, "599.80", "871974353022", "breeze-stoel-pastel-roze-set-van-2"), ({"Kleur": "Pistache"}, "599.80", "871974353025", "breeze-stoel-pistache-set-van-2")],
  soort="eetkamerstoel", opm="Het huidige product 'Breeze Stoel Beige' bevat een afwijkende variant 'Pastelroze' van € 349,95; die is niet overgenomen. Prijs per set van twee: € 599,80 voor alle kleuren.")

product(key="cloud", title="Cloud eetkamerstoel (set van 2)", handle="eetkamerstoel-cloud-set-van-2", vendor="Pole To Pole", ptype="Stoelen", cat="stoel",
  tags=["eetkamerstoel", "set van 2", "zonder armleuning", "staal", "beige", "crème", "karamel", "naturel", "terracotta", "pole-to-pole"],
  short="Ronde, dik gevulde kuipstoel zonder armleuning; de zachtste stoel uit de collectie.",
  ruimte="De Cloud is de stoel voor een eethoek waar je wilt blijven hangen. De ronde kuip met afgeronde randen omsluit je lichtjes, zonder armleuningen die in de weg zitten bij het aanschuiven. Daardoor past hij ook aan smallere tafels vanaf 85 cm breed en kun je er bij een tafel van 160 cm zes kwijt. De vorm is zacht en laag, wat rust geeft in een ruimte met veel rechte lijnen, zoals een keuken met strakke kasten.",
  materiaal="De kuip is gevuld met schuim van hoge dichtheid, zodat de zitting na jaren zijn vorm houdt. De bekleding is er in vijf uitvoeringen: beige, crème en karamel in een gladde stof, en Safiya naturel en Safiya terracotta in een grover geweven stof met meer structuur. Het onderstel is van gepoedercoat staal.",
  combineren="Crème of beige bij een lichte eiken tafel geeft een zachte, monochrome eethoek; karamel of terracotta bij een donkere of zwarte tafel brengt warmte. Combineer de Cloud-stoel met de Cloud-barkruk aan het keukeneiland in dezelfde kleur, zodat keuken en eetkamer één taal spreken.",
  specs={"afmetingen": AANV, "zithoogte": AANV, "zitdiepte": AANV, "gewicht": AANV, "materiaal_frame": "Gepoedercoat staal", "materiaal_bekleding": "Stof over schuim met hoge dichtheid; Safiya-uitvoering in grof geweven stof", "afwerking": "Beige, crème, karamel, Safiya naturel of Safiya terracotta", "set_inhoud": "2 stoelen", "onderhoud": "Stofzuigen met zachte borstel; vlekken deppen met lauw water", "herkomst": "Pole To Pole, Nederland", "levertijd": LEVER_STOEL, "garantie": "2 jaar"},
  advies=["De Cloud is mijn eerste keuze voor een eethoek bij een open keuken: geen armleuningen, dus je schuift makkelijk aan en weer weg, en de ronde vorm verzacht de rechte lijnen van een keukenblok. Ga je voor Safiya terracotta, hou de rest van de ruimte dan rustig; die kleur is het accent."],
  faq=[("Wat is het verschil tussen de gewone stof en Safiya?", "Safiya is een grover geweven stof met zichtbare structuur en komt in naturel en terracotta. De gewone uitvoering is gladder en komt in beige, crème en karamel."), ("Hoeveel Cloud-stoelen passen er aan een ronde tafel van 120 cm?", "Vier comfortabel, vijf als het moet. Zonder armleuningen heb je per stoel circa 55 cm nodig."), ("Is de stoel geschikt voor dagelijks gebruik?", "Ja. Het schuim met hoge dichtheid houdt zijn vorm en de stof is te reinigen met lauw water."), ("Kan ik hem combineren met een barkruk?", "Ja, de Cloud-barkruk heeft dezelfde kuip en komt in crème en karamel.")],
  seo_title="Cloud eetkamerstoel · ronde kuipstoel, set van 2 · InHuys", seo_desc="Dik gevulde kuipstoel zonder armleuning, set van 2. In beige, crème, karamel of de grof geweven Safiya-stof in naturel en terracotta. Levertijd 2 tot 3 weken.",
  options=[("Kleur", ["Beige", "Crème", "Karamel", "Safiya naturel", "Safiya terracotta"])],
  variants=[({"Kleur": "Beige"}, "439.80", "871917285928", "cloud-stoel-beige-set-van-2"), ({"Kleur": "Crème"}, "439.80", "871917285924", "cloud-stoel-creme-set-van-2"), ({"Kleur": "Karamel"}, "439.80", "871917285925", "cloud-stoel-karamel-set-van-2"), ({"Kleur": "Safiya naturel"}, "479.80", "7FCA77ABFB3DBD7B", "cloud-stoel-safiya-naturel-set-van-2"), ({"Kleur": "Safiya terracotta"}, "479.80", "871917285927", "cloud-stoel-safiya-terracotta-set-van-2")],
  soort="eetkamerstoel", opm="")

product(key="cloud-barkruk", title="Cloud barkruk met rugleuning", handle="barkruk-cloud", vendor="Pole To Pole", ptype="Barstoel", cat="barkruk",
  tags=["barkruk", "keukenbarkruk", "rugleuning", "staal", "crème", "karamel", "pole-to-pole"],
  short="De ronde Cloud-kuip op barhoogte, in twee zithoogtes: voor het keukeneiland en voor de bar.",
  ruimte="Aan een keukeneiland zit je vaak langer dan je denkt: ontbijt, een glas wijn tijdens het koken, laptopwerk. De Cloud-barkruk heeft daarom een echte rugleuning en dezelfde zachte kuip als de eetkamerstoel. Hij komt in twee hoogtes: de keukenbarkruk voor bladen rond 90 cm, de barkruk voor bladen rond 105 cm. Meet de hoogte van je blad voordat je kiest; tussen zitting en blad hoort 25 tot 30 cm.",
  materiaal="De kuip is gevuld met schuim van hoge dichtheid en bekleed in crème of karamel. Het onderstel is van gepoedercoat staal met een voetsteun op de juiste hoogte, zodat je voeten niet bungelen. De kruk wordt per stuk geleverd.",
  combineren="Twee of drie krukken aan een eiland in hout of keramiek, in dezelfde kleur als de Cloud-eetkamerstoelen verderop in de ruimte, maakt keuken en eetkamer één geheel. Crème bij lichte kasten, karamel bij een donker of groen keukenblok.",
  specs={"afmetingen": AANV, "zithoogte": "Keukenbarkruk: " + AANV + " · Barkruk: " + AANV, "zitdiepte": AANV, "gewicht": AANV, "materiaal_frame": "Gepoedercoat staal met voetsteun", "materiaal_bekleding": "Stof over schuim met hoge dichtheid", "afwerking": "Crème of karamel", "set_inhoud": "1 kruk", "onderhoud": "Stofzuigen met zachte borstel; vlekken deppen met lauw water", "herkomst": "Pole To Pole, Nederland", "levertijd": LEVER_STOEL, "garantie": "2 jaar"},
  advies=["Reken op 60 cm per kruk en houd de kopse kant van het eiland vrij om langs te lopen. Kies altijd op basis van de bladhoogte, niet op het oog: een kruk die 5 cm te hoog is, zit nooit lekker. Twijfel je? Stuur de hoogte van je blad mee met een Flitsadvies."],
  faq=[("Welke hoogte heb ik nodig?", "Meet de bovenkant van je blad. Rond 90 cm: keukenbarkruk. Rond 105 cm: barkruk. Tussen zitting en blad hoort 25 tot 30 cm."), ("Is de kruk draaibaar?", "Nee, de Cloud-barkruk heeft een vast onderstel."), ("Hoeveel krukken passen er aan een eiland van 180 cm?", "Drie, met 60 cm per kruk."), ("Wordt de kruk per stuk geleverd?", "Ja, de prijs geldt per kruk.")],
  seo_title="Cloud barkruk met rugleuning · keukenbar en bar · InHuys", seo_desc="Zachte kuipkruk met rugleuning op een stalen onderstel, in crème en karamel. Twee zithoogtes: keukenbarkruk voor bladen rond 90 cm, barkruk voor 105 cm.",
  options=[("Hoogte", ["Keukenbarkruk", "Barkruk"]), ("Kleur", ["Crème", "Karamel"])],
  variants=[({"Hoogte": "Keukenbarkruk", "Kleur": "Crème"}, "279.90", "871974353026", "cloud-kitchen-barstoel-creme"), ({"Hoogte": "Barkruk", "Kleur": "Crème"}, "299.90", "871974353027", "cloud-barstoel-creme"), ({"Hoogte": "Keukenbarkruk", "Kleur": "Karamel"}, "279.90", "871974353089", "wolkenkeukenbar-stoel-karamel"), ({"Hoogte": "Barkruk", "Kleur": "Karamel"}, "299.90", "871974353090", "wolkenbar-stoel-karamel")],
  soort="barkruk", opm="Vier losse producten ('Cloud Barstoel Crème', 'Cloud Kitchen Barstoel Crème', 'Wolken barstoel karamel', 'Wolken keukenbarstoel karamel') worden één product met opties Hoogte en Kleur. Producttype wordt 'Barstoel' zodat de collectie Barkrukken hem automatisch opneemt.")

product(key="whale", title="Whale eetkamerstoel (set van 2)", handle="eetkamerstoel-whale-set-van-2", vendor="Pole To Pole", ptype="Stoelen", cat="stoel",
  tags=["eetkamerstoel", "set van 2", "staal", "beige", "coco", "pole-to-pole"],
  short="Eetkamerstoel met een doorlopende, gebogen rug die om je heen valt; het statement van de eethoek.",
  ruimte="De Whale dankt zijn naam aan de rugleuning: één doorlopende, gebogen lijn die als een vin om de zitting heen loopt. Daardoor is het een stoel die je van alle kanten mooi wilt zien, bijvoorbeeld aan een tafel die vrij in de ruimte staat. Hij vraagt iets meer breedte dan een rechte stoel; reken op 60 cm per stuk. Bij een tafel van 200 cm passen er zes.",
  materiaal="Zitting en rug zijn volledig gestoffeerd, in beige of in coco, een diepe bruintint. Het onderstel is van gepoedercoat staal. De stoel wordt per set van twee geleverd.",
  combineren="Beige Whale-stoelen bij een donkere tafel van keramiek met marmerlook geven contrast zonder hardheid. Coco bij een eiken tafel is warm en klassiek. Zet er geen tweede uitgesproken stoel naast; de Whale is het accent, de rest van de eethoek mag rustig zijn.",
  specs={"afmetingen": AANV, "zithoogte": AANV, "zitdiepte": AANV, "gewicht": AANV, "materiaal_frame": "Gepoedercoat staal", "materiaal_bekleding": AANV + " (stof)", "afwerking": "Beige of coco", "set_inhoud": "2 stoelen", "onderhoud": "Stofzuigen met zachte borstel; vlekken deppen met lauw water", "herkomst": "Pole To Pole, Nederland", "levertijd": LEVER_STOEL, "garantie": "2 jaar"},
  advies=["De Whale is een stoel voor een eethoek die je vanuit de woonkamer ziet; van achteren is hij net zo mooi als van voren. Ik combineer hem graag met een ronde of ovale tafel, zodat de gebogen rug terugkomt in het blad. Aan een smalle rechthoekige tafel oogt hij snel te druk."],
  faq=[("Past de Whale aan een ronde tafel van 130 cm?", "Ja, met vier stoelen. Houd 60 cm per stoel aan."), ("Zijn de kleuren in het echt te zien?", "Ja, in de showroom in Purmerend, op afspraak."), ("Hoe onderhoud ik de stof?", "Regelmatig stofzuigen met een zachte borstel; vlekken deppen met lauw water en een neutraal middel."), ("Wordt de stoel per set geleverd?", "Ja, de prijs geldt per set van twee.")],
  seo_title="Whale eetkamerstoel · gebogen rug, set van 2 · InHuys", seo_desc="Eetkamerstoel met doorlopende gebogen rugleuning op een stalen onderstel, set van 2. In beige of coco. Levertijd 2 tot 3 weken, te zien in Purmerend.",
  options=[("Kleur", ["Beige", "Coco"])],
  variants=[({"Kleur": "Beige"}, "479.80", "871917285669", "whale-stoel-beige-set-van-2"), ({"Kleur": "Coco"}, "519.80", "871917285668", "whale-stoel-coco-set-van-2")],
  soort="eetkamerstoel", opm="")

product(key="luna", title="Luna eetkamerstoel (set van 2)", handle="eetkamerstoel-luna-set-van-2", vendor="Pole To Pole", ptype="Stoelen", cat="stoel",
  tags=["eetkamerstoel", "set van 2", "staal", "mink", "karamel", "crème", "pole-to-pole"],
  short="Slanke eetkamerstoel met een zacht gestoffeerde rug en poten in een gerookt-eikentint.",
  ruimte="De Luna is de slanke stoel uit de collectie: smal in de breedte, zacht in de rug. Daardoor past hij aan tafels waar een kuipstoel te veel ruimte zou nemen, en kun je er bij een tafel van 180 cm zes kwijt zonder dat het vol voelt. De gestoffeerde rug geeft steun zonder dat de stoel zwaar oogt.",
  materiaal="Zitting en rug zijn gestoffeerd in mink (een grijsbruine tint), karamel of crème. De poten zijn afgewerkt in een gerookt-eikentint, wat de stoel een warme, organische uitstraling geeft bij een houten vloer. De stoel wordt per set van twee geleverd.",
  combineren="Mink bij een eiken tafel en een lichte vloer is tijdloos; crème bij donker hout geeft lucht; karamel bij zwart of groen brengt warmte. Omdat de Luna slank is, combineert hij goed met een forsere kop-stoel, zoals de Breeze met armleuning aan beide uiteinden.",
  specs={"afmetingen": AANV, "zithoogte": AANV, "zitdiepte": AANV, "gewicht": AANV, "materiaal_frame": AANV + " (poten in gerookt-eikentint)", "materiaal_bekleding": AANV + " (stof)", "afwerking": "Mink, karamel of crème", "set_inhoud": "2 stoelen", "onderhoud": "Stofzuigen met zachte borstel; vlekken deppen met lauw water", "herkomst": "Pole To Pole, Nederland", "levertijd": LEVER_STOEL, "garantie": "2 jaar"},
  advies=["Als een eethoek klein is of de tafel smal, is de Luna mijn eerste keuze: hij neemt weinig ruimte, zit goed en de poten in eikentint maken hem warmer dan een stoel op zwart staal. Mink is de kleur die bij bijna elke vloer past."],
  faq=[("Hoeveel Luna-stoelen passen er aan een tafel van 160 cm?", "Zes, drie aan elke lange zijde. De Luna is smal, reken op 50 tot 55 cm per stoel."), ("Welke kleur is 'mink'?", "Een warme grijsbruine tint, tussen taupe en bruin in."), ("Zijn de poten van hout?", "De poten zijn afgewerkt in een gerookt-eikentint; het exacte materiaal staat in de specificaties."), ("Wordt de stoel per set geleverd?", "Ja, de prijs geldt per set van twee.")],
  seo_title="Luna eetkamerstoel · slank, zachte rug, set van 2 · InHuys", seo_desc="Slanke eetkamerstoel met gestoffeerde rug en poten in gerookt-eikentint, set van 2. In mink, karamel of crème. Levertijd 2 tot 3 weken, te zien in Purmerend.",
  options=[("Kleur", ["Mink", "Karamel", "Crème"])],
  variants=[({"Kleur": "Mink"}, "419.80", "871974353110", "luna-chair-mink-set-van-2"), ({"Kleur": "Karamel"}, "419.80", "871974353109", "luna-stoel-caramel-set-van-2"), ({"Kleur": "Crème"}, "419.80", "871974353108", "luna-stoelcreme-set-van-2")],
  soort="eetkamerstoel", opm="Het huidige product 'Luna stoel crème' bevat een afwijkende variant 'Goud' van € 239,95; die is niet overgenomen.")

product(key="boog", title="Boog eetkamerstoel (set van 2)", handle="eetkamerstoel-boog-set-van-2", vendor="Pole To Pole", ptype="Stoelen", cat="stoel",
  tags=["eetkamerstoel", "set van 2", "staal", "karamel", "crème", "pole-to-pole"],
  short="Eetkamerstoel met een gebogen rugleuning en poten in dezelfde kleur als de stof.",
  ruimte="De Boog is genoemd naar zijn rugleuning: een zachte boog die de rug steunt zonder de stoel breed te maken. Het is een stoel die goed werkt in een eethoek met veel licht en weinig tierelantijnen; de vorm doet het werk. Zes stuks passen aan een tafel van 180 cm.",
  materiaal="Zitting en rug zijn bekleed in een zachte stof, in karamel of crème. Bijzonder is het onderstel: gepoedercoat staal in dezelfde kleur als de stof, zodat de stoel één geheel vormt. De stoel wordt per set van twee geleverd.",
  combineren="Crème Boog-stoelen bij een lichte eiken tafel geven een eethoek die bijna wegvalt in de ruimte; dat is precies de bedoeling als de keuken of een kunstwerk de aandacht moet krijgen. Karamel bij een zwarte of donkergroene tafel is warmer en meer aanwezig.",
  specs={"afmetingen": AANV, "zithoogte": AANV, "zitdiepte": AANV, "gewicht": AANV, "materiaal_frame": "Gepoedercoat staal, in de kleur van de bekleding", "materiaal_bekleding": AANV + " (stof)", "afwerking": "Karamel of crème", "set_inhoud": "2 stoelen", "onderhoud": "Stofzuigen met zachte borstel; vlekken deppen met lauw water", "herkomst": "Pole To Pole, Nederland", "levertijd": LEVER_STOEL, "garantie": "2 jaar"},
  advies=["Kies de Boog als je wilt dat de stoelen één kleur zijn, van zitting tot poot. Dat geeft rust in een eethoek met een drukke vloer of veel glas. Ik zet hem liever niet naast een stoel met een zwart onderstel; dan verlies je precies het effect."],
  faq=[("Zijn de poten echt in de kleur van de stof?", "Ja, het stalen onderstel is gepoedercoat in een bijpassende tint."), ("Hoeveel stoelen passen er aan een tafel van 200 cm?", "Zes tot acht, met 55 cm per stoel."), ("Is crème niet te gevoelig?", "De stof is te reinigen met lauw water; voor een gezin met jonge kinderen is karamel de veiligere keuze."), ("Wordt de stoel per set geleverd?", "Ja, de prijs geldt per set van twee.")],
  seo_title="Boog eetkamerstoel · gebogen rug, set van 2 · InHuys", seo_desc="Eetkamerstoel met gebogen rugleuning en stalen poten in de kleur van de stof, set van 2. In karamel of crème. Levertijd 2 tot 3 weken.",
  options=[("Kleur", ["Karamel", "Crème"])],
  variants=[({"Kleur": "Karamel"}, "319.80", "871974353094", "boogstoel-karamel-set-van-2"), ({"Kleur": "Crème"}, "319.80", "871974353091", "boogstoelcreme-set-van-2")],
  soort="eetkamerstoel", opm="De bestaande collectie 'Bow' en de concepten 'Rainbow'/'Regenboogstoel' lijken hetzelfde model in andere kleuren; in fase 3 samenvoegen zodra dat bevestigd is.")

product(key="scandi", title="Scandi eetkamerstoel (set van 2)", handle="eetkamerstoel-scandi-set-van-2", vendor="Pole To Pole", ptype="Stoelen", cat="stoel",
  tags=["eetkamerstoel", "set van 2", "tan", "pole-to-pole"],
  short="Rechte, rustige eetkamerstoel in tan; de stoel die bij alles past.",
  ruimte="De Scandi is de stille kracht van de collectie: rechte lijnen, een lichte rug en een zitting op de juiste hoogte voor tafels van 75 tot 78 cm. Hij valt niet op, en dat is zijn kwaliteit. In een eethoek waar de tafel of de lamp het verhaal vertelt, is dit de stoel die niet in de weg zit.",
  materiaal="Zitting en rug zijn gestoffeerd in tan, een warme, lichtbruine tint die bij vrijwel elke houtsoort past. De stoel wordt per set van twee geleverd. Overige kleuren uit deze serie zijn op aanvraag beschikbaar.",
  combineren="Tan bij eiken of essen is een klassieke, Scandinavische combinatie; bij een zwarte tafel krijgt de stoel juist contrast. Combineer met een linnen tafelkleed en een travertijn vaas voor een eethoek die rustig blijft, ook als er veel op tafel staat.",
  specs={"afmetingen": AANV, "zithoogte": AANV, "zitdiepte": AANV, "gewicht": AANV, "materiaal_frame": AANV, "materiaal_bekleding": AANV + " (stof)", "afwerking": "Tan", "set_inhoud": "2 stoelen", "onderhoud": "Stofzuigen met zachte borstel; vlekken deppen met lauw water", "herkomst": "Pole To Pole, Nederland", "levertijd": LEVER_STOEL, "garantie": "2 jaar"},
  advies=["Als je twijfelt, kies de Scandi. Hij maakt geen statement, maar hij maakt ook nooit iets kapot: hij past bij de tafel die je al hebt en bij de tafel die je straks koopt. Ik zet hem graag in als er al een uitgesproken lamp boven tafel hangt."],
  faq=[("Zijn er meer kleuren dan tan?", "Ja, de serie bestaat ook in okura en umber. Vraag ernaar; we bestellen ze op aanvraag."), ("Hoeveel stoelen passen er aan een tafel van 180 cm?", "Zes, met 55 cm per stoel."), ("Is de stoel geschikt voor een eetbank aan de andere kant?", "Ja, de zithoogte sluit aan bij gangbare eetbanken."), ("Wordt de stoel per set geleverd?", "Ja, de prijs geldt per set van twee.")],
  seo_title="Scandi eetkamerstoel in tan · set van 2 · InHuys", seo_desc="Rustige eetkamerstoel met rechte lijnen in warm lichtbruin (tan), set van 2. Past bij eiken, essen en zwarte tafels. Levertijd 2 tot 3 weken.",
  options=[("Kleur", ["Tan"])],
  variants=[({"Kleur": "Tan"}, "379.80", "871974353219", "scandi-stoel-tan-set-van-2")],
  soort="eetkamerstoel", opm="De concepten 'Scandi voorzitter Okura' en 'Scandi voorzitter Umber' (vertaalfout voor 'chair') worden in fase 3 als kleurvarianten toegevoegd.")

product(key="agano", title="Agano vaas van travertijn", handle="vaas-agano-travertijn", vendor="MOOISA", ptype="Vazen", cat="vaas",
  tags=["vaas", "travertijn", "natuursteen", "mooisa"], collections=[COLL["vazen"]],
  short="Vaas gedraaid uit één blok travertijn, in twee maten; zwaar, rustig en het mooist met droge takken.",
  ruimte="Een vaas van steen doet iets anders dan een vaas van glas: hij geeft gewicht aan een oppervlak. Zet de Agano op een dressoir, een lage kast of het midden van een grote tafel, en de ruimte eromheen wordt rustiger. De medium maat (23 cm hoog) werkt op tafel; de grote maat (31 cm) hoort op een dressoir of op de vloer naast een fauteuil.",
  materiaal="De Agano is gedraaid uit één blok travertijn, een kalksteen met open poriën en een zachte, beige tekening. Elke vaas is daardoor anders; de steen bepaalt het patroon. Travertijn is poreus: zet de vaas niet op een onbeschermd houten blad als er water in staat, en gebruik voor verse bloemen een glazen inzet. Hij is niet volledig waterdicht.",
  combineren="Droge takken, pampasgras of een enkele eucalyptus doen het mooist; de steen vraagt niet om een bos. Combineer met de Craft-salontafel met travertijn blad of zet de medium en de grote maat naast elkaar op een dressoir in eiken.",
  specs={"afmetingen": "M: Ø 20 × 23 cm · L: Ø 20 × 31 cm", "gewicht": "Tot 10 kg (L)", "materiaal_frame": "Massief travertijn", "afwerking": "Natuurlijke beige steen, elke vaas uniek", "set_inhoud": "1 vaas", "onderhoud": "Afnemen met een droge of licht vochtige doek; geen zuren of schuurmiddelen; voor water een glazen inzet gebruiken", "herkomst": "MOOISA", "levertijd": "1 tot 2 weken", "garantie": "2 jaar"},
  advies=["Eén grote Agano op een leeg dressoir is sterker dan drie kleine objecten. Ik zet hem bijna altijd iets uit het midden, met één tak erin, en laat de rest van het blad leeg. Let op het gewicht: op een zwevende plank hoort hij niet."],
  faq=[("Kan ik er verse bloemen in zetten?", "Alleen met een glazen inzet. De steen is poreus en niet volledig waterdicht."), ("Is elke vaas hetzelfde?", "Nee. De tekening en de poriën verschillen per blok steen; je ontvangt dus een uniek exemplaar."), ("Hoe zwaar is de vaas?", "De grote maat weegt tot 10 kg. Zet hem op een stevig blad."), ("Hoe maak ik hem schoon?", "Met een droge of licht vochtige doek. Geen zuren, geen schuurmiddelen.")],
  seo_title="Agano travertijn vaas · Ø 20 cm, 23 of 31 cm hoog · InHuys", seo_desc="Vaas gedraaid uit één blok travertijn, in twee maten. Rustig en zwaar, het mooist met droge takken; voor water een glazen inzet. Levertijd 1 tot 2 weken.",
  options=[("Maat", ["M · Ø 20 × 23 cm", "L · Ø 20 × 31 cm"])],
  variants=[({"Maat": "M · Ø 20 × 23 cm"}, "194.95", None, "travertine-agano-vaas"), ({"Maat": "L · Ø 20 × 31 cm"}, "219.95", None, "travertine-agano-vaas")],
  soort="vaas", opm="Beide maten delen de beelden van het bestaande product.")

product(key="waxinelicht", title="Marmeren waxinelichthouder", handle="waxinelichthouder-marmer", vendor="MOOISA", ptype="Accessoires", cat="kandelaar",
  tags=["waxinelichthouder", "kaarsenhouder", "marmer", "natuursteen", "mooisa"], collections=[COLL["windlichten"]],
  short="Kleine cilinder van massief marmer voor een waxinelicht, in drie hoogtes om te stapelen in een groep.",
  ruimte="Kaarslicht op steen is zachter dan op glas. Deze waxinelichthouders zijn kleine cilinders van massief marmer, in drie hoogtes van 4, 7 en 10 cm. Eén exemplaar op een nachtkastje is genoeg; een groep van drie in verschillende hoogtes op de eettafel maakt een avond af zonder dat het druk wordt.",
  materiaal="Elke houder is gedraaid uit een blok marmer, met de aders die bij dat blok horen. De diameter is 6 cm bij alle maten. Marmer is gevoelig voor zuren; zet er geen citroen of wijn naast en veeg gemorste was weg zodra die hard is.",
  combineren="Zet de drie maten naast elkaar op een schaal of een plank van hout, of combineer één hoge houder met de Agano-vaas op een dressoir. Bij een tafel in keramiek met marmerlook kies je liever een andere kleur steen, zodat de houders niet wegvallen.",
  specs={"afmetingen": "Ø 6 × 4 cm · Ø 6 × 7 cm · Ø 6 × 10 cm", "materiaal_frame": "Massief marmer", "afwerking": "Natuurlijke steen, elke houder uniek", "set_inhoud": "1 houder, geschikt voor een standaard waxinelicht", "onderhoud": "Afnemen met een droge doek; geen zuren; was verwijderen als die hard is", "herkomst": "MOOISA", "levertijd": "1 tot 2 weken", "garantie": "2 jaar"},
  advies=["Koop ze per drie, in de drie hoogtes. Eén maat herhalen ziet er geordend uit, drie maten zien eruit alsof ze er altijd hebben gestaan. Op een houten tafel leg ik er een plateau onder, voor de was."],
  faq=[("Past er een standaard waxinelicht in?", "Ja, alle drie de maten zijn gemaakt voor een standaard waxinelicht van 3,8 cm."), ("Wordt het marmer heet?", "Het marmer wordt warm, niet heet. Zet de houder wel op een hittebestendige ondergrond."), ("Zijn de aders bij elk exemplaar hetzelfde?", "Nee, elke houder komt uit een ander stuk steen."), ("Kan ik ze buiten gebruiken?", "Op een beschut terras in de zomer wel; niet buiten laten staan bij vorst of regen.")],
  seo_title="Marmeren waxinelichthouder · 4, 7 of 10 cm hoog · InHuys", seo_desc="Waxinelichthouder van massief marmer, Ø 6 cm, in drie hoogtes om te stapelen in een groep. Natuurlijke aders, elke houder uniek. Levertijd 1 tot 2 weken.",
  options=[("Maat", ["Ø 6 × 4 cm", "Ø 6 × 7 cm", "Ø 6 × 10 cm"])],
  variants=[({"Maat": "Ø 6 × 4 cm"}, "16.95", "8720648589966", "marmer-waxinelichthouder"), ({"Maat": "Ø 6 × 7 cm"}, "25.95", "8720648589959", "marmer-waxinelichthouder"), ({"Maat": "Ø 6 × 10 cm"}, "31.95", "8720648589973", "marmer-waxinelichthouder")],
  soort="waxinelichthouder", opm="")

product(key="boekensteun", title="Boekensteun van mangohout", handle="boekensteun-mangohout", vendor="Kluster", ptype="Accessoires", cat="boekensteun",
  tags=["boekensteun", "mangohout", "hout", "kluster"], collections=[COLL["decoratie"]],
  short="Boekensteun van donker mangohout; houdt een rij boeken overeind op een plank of dressoir.",
  ruimte="Een boekensteun lost een klein probleem op dat je elke dag ziet: een rij boeken die omvalt. Deze steun van donker mangohout houdt een stapel van zo'n 30 cm overeind op een plank, een dressoir of een bureau, en is zwaar genoeg om niet mee te schuiven.",
  materiaal="Gemaakt van massief mangohout met een donkere afwerking, waardoor de nerf zichtbaar blijft. Mangohout is hard en zwaar; elke steun heeft een eigen tekening.",
  combineren="Op een eiken plank geeft het donkere hout contrast; op een zwart stalen rek valt hij juist weg en zie je alleen de boeken. Combineer met de marmeren waxinelichthouder of een kleine keramische vaas naast de boeken voor een plank die bewoond voelt.",
  specs={"afmetingen": AANV, "gewicht": AANV, "materiaal_frame": "Massief mangohout, donker afgewerkt", "afwerking": "Donkerbruin, nerf zichtbaar", "set_inhoud": "1 boekensteun", "onderhoud": "Afstoffen; af en toe behandelen met meubelolie", "herkomst": "Kluster", "levertijd": "1 tot 2 weken", "garantie": "2 jaar"},
  advies=["Gebruik hem niet alleen voor boeken. Een rij kookboeken op het aanrecht of platen naast de platenspeler worden er rustiger van. Twee stuks, aan weerszijden van een rij, oogt het meest bewust."],
  faq=[("Is de steun zwaar genoeg voor grote boeken?", "Ja, mangohout is zwaar. Voor een rij van meer dan 40 cm adviseren we twee steunen."), ("Is de afwerking kleurecht?", "Hout verkleurt licht in de zon; zet hem niet maandenlang in direct zonlicht."), ("Wordt hij per stuk geleverd?", "Ja, de prijs geldt per stuk.")],
  seo_title="Boekensteun van donker mangohout · Kluster · InHuys", seo_desc="Zware boekensteun van massief mangohout met donkere afwerking, voor plank, dressoir of bureau. Per stuk. Levertijd 1 tot 2 weken.",
  options=[("Uitvoering", ["Donker mangohout"])],
  variants=[({"Uitvoering": "Donker mangohout"}, "59.95", None, "boekhouder")],
  soort="boekensteun", opm="Het bestaande product heet 'Boekhouder'; de juiste term is boekensteun.")

LEVER_BANK = "6 tot 8 weken, geleverd en geplaatst in overleg"
product(key="bank-amsterdam", title="Bank Amsterdam", handle="bank-amsterdam", vendor="Pole To Pole", ptype="Banken", cat="sofa",
  tags=["bank", "hoekbank", "ottoman", "wit", "pole-to-pole"],
  short="Lage, royale bank met strakke lijnen en diepe zit, in vier opstellingen van 2,5-zits tot hoekbank met ottoman.",
  ruimte="De Amsterdam is een bank voor een woonkamer waar de bank het middelpunt is: laag, breed, met een diepe zit en losse kussens waarin je kunt liggen. De strakke buitenlijn houdt hem rustig, ook in de grote opstellingen. Kies de opstelling op basis van de plattegrond: de 2,5-zits met ottoman voor een ruimte tot 25 m², de 4-zits voor een lange wand, de 6-zits hoekbank met ottoman voor een open woonkamer waar de bank de zithoek afbakent.",
  materiaal="Het frame is massief; de kussens zijn gevuld met schuim en vezel voor een zit die diep is maar terugveert. De bekleding is Glyphs, een stevige weefstof in wit met een subtiele structuur. Het blad van de ottoman en de poef is in dezelfde stof. Opstellingen: 2,5-zits met ottoman, 4-zits, 4-zits met poef, en 6-zits hoekbank met ottoman.",
  combineren="Een witte bank vraagt om warmte eromheen: een vloerkleed in zand of terracotta, een salontafel van travertijn, een Panda-fauteuil in coco. Zet de ottoman los van de bank als er bezoek is; hij werkt dan als extra zitplek.",
  specs={"afmetingen": AANV + " per opstelling", "zithoogte": AANV, "zitdiepte": AANV, "gewicht": AANV, "materiaal_frame": AANV + " (massief frame)", "materiaal_bekleding": "Glyphs weefstof, wit", "afwerking": "Wit", "set_inhoud": "Per opstelling, inclusief losse kussens; ottoman of poef waar vermeld", "onderhoud": "Kussens regelmatig opschudden en draaien; stofzuigen met zachte borstel; vlekken deppen met lauw water", "herkomst": "Pole To Pole, Nederland", "levertijd": LEVER_BANK, "garantie": "2 jaar"},
  advies=["Een witte bank is mooier dan mensen denken, maar alleen in een huis zonder huisdieren en met de wil om kussens te draaien. Ik teken hem altijd eerst in de plattegrond: de 6-zits hoekbank is een meubel van bijna drie meter en vraagt om ruimte rondom. Twijfel je over de maat? Stuur de plattegrond mee met een Flitsadvies."],
  faq=[("Welke opstelling past in mijn woonkamer?", "Vuistregel: minstens 80 cm looproute rondom en de bank niet breder dan tweederde van de wand. We tekenen het graag in met een Flitsadvies."), ("Is wit praktisch?", "De Glyphs-stof is stevig en te reinigen, maar wit blijft wit: niet bij huisdieren of jonge kinderen."), ("Kan de ottoman los staan?", "Ja, de ottoman en de poef zijn losse elementen."), ("Hoe wordt de bank geleverd?", "In overleg geleverd en geplaatst; bij een inrichting via InHuys zijn we erbij.")],
  seo_title="Bank Amsterdam · 2,5-zits tot hoekbank met ottoman · InHuys", seo_desc="Lage, royale bank met diepe zit in witte Glyphs-weefstof. Vier opstellingen, van 2,5-zits met ottoman tot 6-zits hoekbank. Levering 6 tot 8 weken.",
  options=[("Opstelling", ["2,5-zits met ottoman", "4-zits", "4-zits met poef", "6-zits hoekbank met ottoman"])],
  variants=[({"Opstelling": "2,5-zits met ottoman"}, "3700.00", "871974353034", "bank-amsterdam-2-5-zits-ottoman-wit-glyphs"), ({"Opstelling": "4-zits"}, "4000.00", "871974353035", "bank-amsterdam-4-zits-wit-glyphs"), ({"Opstelling": "4-zits met poef"}, "4700.00", "871974353036", "bank-amsterdam-4-zits-poef-wit-glyphs"), ({"Opstelling": "6-zits hoekbank met ottoman"}, "7000.00", "871974353113", "bank-amsterdam-6-zits-hoekbank-ottoman-bank-wit-glyphs")],
  soort="bank", opm="Vier conceptproducten worden één product met optie Opstelling. Categorie corrigeert van 'Poefs' naar 'Sofa's'.")

product(key="bank-new-york", title="Bank New York", handle="bank-new-york", vendor="Pole To Pole", ptype="Banken", cat="sofa",
  tags=["bank", "loungebank", "boucle", "beige", "coco", "zand", "pole-to-pole"],
  short="Zachte loungebank met ronde vormen, in 2,5- en 4-zits, met of zonder lounge-element rechts, in drie stoffen.",
  ruimte="De New York is de zachte tegenhanger van de Amsterdam: ronde armen, een lage rug en een zit waarin je wegzakt. Hij is er als 2,5-zits en als 4-zits, elk met of zonder een lounge-element aan de rechterkant waar je de benen op kunt leggen. De 2,5-zits past in een zithoek tot 20 m²; de 4-zits met lounge vult een open woonkamer.",
  materiaal="De bekleding komt in drie uitvoeringen: beige en coco in een gladde weefstof, en zand in boucle, een stof met kleine lusjes die licht vangt. Coco is de donkere, bruine variant. Het frame is massief, de kussens zijn gevuld met schuim en vezel.",
  combineren="Zand boucle bij een lichte vloer en een travertijn salontafel is zacht en monochroom; coco bij eiken en een wollen kleed is warm en klassiek. Een Kathmandu- of Mars-fauteuil in een andere stof ertegenover geeft de zithoek diepte.",
  specs={"afmetingen": AANV + " per opstelling", "zithoogte": AANV, "zitdiepte": AANV, "gewicht": AANV, "materiaal_frame": AANV + " (massief frame)", "materiaal_bekleding": "Weefstof (beige, coco) of boucle (zand)", "afwerking": "Beige, coco of zand boucle", "set_inhoud": "Per opstelling, inclusief losse kussens", "onderhoud": "Kussens opschudden en draaien; stofzuigen met zachte borstel; boucle niet borstelen", "herkomst": "Pole To Pole, Nederland", "levertijd": LEVER_BANK, "garantie": "2 jaar"},
  advies=["De New York is de bank voor avonden op de bank, niet voor rechtop zitten met visite. Het lounge-element rechts is heerlijk, maar bepaalt de indeling: de open zijde moet naar de ruimte wijzen. Laat me de plattegrond zien voordat je kiest tussen links en rechts; 'rechts' is gezien vanaf de zitpositie."],
  faq=[("Wat betekent 'lounge rechts'?", "Een verlengd zitelement aan de rechterkant, gezien als je op de bank zit, waar je de benen op legt."), ("Is boucle praktisch?", "Boucle is stevig maar vangt stof; stofzuigen zonder borstel. Bij huisdieren adviseren we de gladde weefstof."), ("Kan ik de bank proberen?", "Ja, in de showroom in Purmerend staat de serie, op afspraak."), ("Hoe lang is de levertijd?", "6 tot 8 weken; de bank wordt per opstelling gemaakt.")],
  seo_title="Bank New York · loungebank in boucle en weefstof · InHuys", seo_desc="Zachte loungebank met ronde vormen, 2,5- of 4-zits, met of zonder lounge-element. In beige, coco of zand boucle. Levering 6 tot 8 weken, te zien in Purmerend.",
  options=[("Opstelling", ["2,5-zits", "2,5-zits met lounge rechts", "4-zits", "4-zits met lounge rechts"]), ("Kleur", ["Beige", "Coco", "Zand boucle"])],
  variants=[({"Opstelling": "2,5-zits", "Kleur": "Beige"}, "2240.00", "871917285937", "bank-new-york-2-5-zits-beige"), ({"Opstelling": "2,5-zits", "Kleur": "Coco"}, "2480.00", "871917285933", "bank-new-york-2-5-zits-coco"), ({"Opstelling": "2,5-zits", "Kleur": "Zand boucle"}, "2240.00", "871917285929", "bank-new-york-2-5-zits-sand-boucle"),
            ({"Opstelling": "2,5-zits met lounge rechts", "Kleur": "Beige"}, "2740.00", "871917285938", "bank-new-york-2-5-zits-rechter-lounge-beige"), ({"Opstelling": "2,5-zits met lounge rechts", "Kleur": "Coco"}, "2980.00", "871917285934", "bank-new-york-2-5-zits-rechter-lounge-coco"), ({"Opstelling": "2,5-zits met lounge rechts", "Kleur": "Zand boucle"}, "2740.00", "871917285930", "bank-new-york-2-5-zits-rechter-lounge-sand-boucle"),
            ({"Opstelling": "4-zits", "Kleur": "Beige"}, "3200.00", "871917285939", "bank-new-york-4-zits-beige"), ({"Opstelling": "4-zits", "Kleur": "Coco"}, "3480.00", "871917285935", "bank-new-york-4-zits-coco"), ({"Opstelling": "4-zits", "Kleur": "Zand boucle"}, "3200.00", "871917285931", "bank-new-york-4-zits-zand-boucle"),
            ({"Opstelling": "4-zits met lounge rechts", "Kleur": "Beige"}, "3740.00", "871917285952", "bank-new-york-4-zits-rechter-lounge-beige"), ({"Opstelling": "4-zits met lounge rechts", "Kleur": "Coco"}, "3980.00", "871917285936", "bank-new-york-4-zits-rechter-lounge-coco"), ({"Opstelling": "4-zits met lounge rechts", "Kleur": "Zand boucle"}, "3740.00", "71917285932", "bank-new-york-4-zits-rechter-lounge-sand-boucle")],
  soort="bank", opm="Twaalf conceptproducten worden één product met opties Opstelling en Kleur. De sku '71917285932' mist vermoedelijk een cijfer; te controleren bij Pole To Pole.")

product(key="bank-londen", title="Bank Londen", handle="bank-londen", vendor="Pole To Pole", ptype="Banken", cat="sofa",
  tags=["bank", "ottoman", "tan", "umber", "pole-to-pole"],
  short="Modulaire bank met hoge rug en losse ottoman, als 3-zits of 6-zits, in tan en umber.",
  ruimte="De Londen is de bank voor een grote woonkamer of een zithoek waar meer mensen samenkomen. De 3-zits is een volwaardige bank voor een stadswoning; de 6-zits is een landschap van bijna drie meter voor een open ruimte. Beide zijn er met een losse ottoman, waarmee je de hoek sluit of een chaise maakt. De hogere rug steunt ook als je rechtop zit.",
  materiaal="De bekleding komt in tan, een warme lichtbruine tint, en umber, een diep donkerbruin. Het frame is massief; de kussens zijn gevuld met schuim en vezel. De ottoman is in dezelfde stof. Opstellingen: 3-zits, 3-zits met ottoman, 6-zits, 6-zits met ottoman.",
  combineren="Tan bij een lichte vloer en veel daglicht; umber bij een donkere vloer, een open haard of een bibliotheekwand. Een lage salontafel in travertijn en een groot windlicht op de vloer maken de zithoek af.",
  specs={"afmetingen": AANV + " per opstelling", "zithoogte": AANV, "zitdiepte": AANV, "gewicht": AANV, "materiaal_frame": AANV + " (massief frame)", "materiaal_bekleding": AANV + " (stof)", "afwerking": "Tan of umber", "set_inhoud": "Per opstelling; ottoman waar vermeld", "onderhoud": "Kussens opschudden en draaien; stofzuigen met zachte borstel; vlekken deppen met lauw water", "herkomst": "Pole To Pole, Nederland", "levertijd": LEVER_BANK, "garantie": "2 jaar"},
  advies=["De 6-zits is indrukwekkend, maar ik zie hem te vaak in een ruimte die hem niet kan dragen. Vuistregel: de bank mag niet meer dan tweederde van de wand innemen en er moet 80 cm vrij blijven om te lopen. Past dat niet, dan is de 3-zits met ottoman bijna net zo royaal en veel beter in verhouding."],
  faq=[("Wat is het verschil tussen tan en umber?", "Tan is warm lichtbruin, umber is diep donkerbruin. Beide zijn in de showroom te zien."), ("Kan de ottoman aan beide kanten?", "Ja, de ottoman is los en kan links of rechts staan."), ("Is de 3-zits ook in tan zonder ottoman leverbaar?", "Op aanvraag; standaard bieden we de 3-zits zonder ottoman in umber aan."), ("Hoe lang is de levertijd?", "6 tot 8 weken; de bank wordt per opstelling gemaakt.")],
  seo_title="Bank Londen · 3-zits en 6-zits met ottoman · InHuys", seo_desc="Modulaire bank met hoge rug en losse ottoman, als 3-zits of 6-zits, in tan of umber. Levering 6 tot 8 weken, in overleg geplaatst. Te zien in Purmerend.",
  options=[("Opstelling", ["3-zits", "3-zits met ottoman", "6-zits", "6-zits met ottoman"]), ("Kleur", ["Tan", "Umber"])],
  variants=[({"Opstelling": "3-zits", "Kleur": "Umber"}, "3500.00", "871974353295", "londen-3-zits-umber"), ({"Opstelling": "3-zits met ottoman", "Kleur": "Tan"}, "4500.00", "871974353296", "londen-3-zits-ottoman-tan"), ({"Opstelling": "3-zits met ottoman", "Kleur": "Umber"}, "4500.00", "871974353297", "londen-3-zits-ottoman-umber"), ({"Opstelling": "6-zits", "Kleur": "Tan"}, "4740.00", "871974353298", "londen-met-6-zitje-tan"), ({"Opstelling": "6-zits", "Kleur": "Umber"}, "4740.00", "871974353299", "londen-6-zitter-umber"), ({"Opstelling": "6-zits met ottoman", "Kleur": "Tan"}, "5740.00", "871974353300", "london-6-seater-ottoman-tan"), ({"Opstelling": "6-zits met ottoman", "Kleur": "Umber"}, "5740.00", "8719743533011", "londen-6-zitter-ottoman-umber")],
  soort="bank", opm="Zeven conceptproducten (met vertaalfouten als 'Londen met 6 zitje tan' en 'London 6 SEATER') worden één product. De combinatie 3-zits tan bestaat niet in de brondata en is niet aangemaakt. De sku '8719743533011' heeft een cijfer te veel; te controleren bij Pole To Pole.")

# ---------------- generatie ----------------
def html_desc(p):
    return (f"<h3>Zo werkt het in de ruimte</h3><p>{p['ruimte']}</p>"
            f"<h3>Materiaal en maakwijze</h3><p>{p['materiaal']}</p>"
            f"<h3>Combineren</h3><p>{p['combineren']}</p>")
redirects = [("oude_handle", "nieuwe_handle", "model")]
batches = {}
for p in PRODUCTS:
    files, seen = [], set()
    base = p['title'].split(' (')[0]
    srcs = [srch for (_, _, _, srch) in p['variants']]
    def label(ov, srch):
        if srcs.count(srch) == len(srcs): return ""  # alle varianten delen dezelfde beelden
        return ", " + ", ".join(v.lower() for v in ov.values())
    alts, beoogd = {}, []
    for (ov, price, sku, srch) in p['variants']:
        it = by_handle[srch]
        if srch in seen: continue
        seen.add(srch)
        n = len(it['images'])
        for i, im in enumerate(it['images'], 1):
            a = f"{base}{label(ov, srch)}, afbeelding {i} van {n}"
            beoogd.append((im['url'], a))
            # Shopify hergebruikt het bestaande beeldbestand (gedeeld met het live product); daarom de huidige alt ongewijzigd meegeven.
            cur = ORIG_ALT.get(srch, {}).get(im['url'])
            f = {"originalSource": im['url'], "contentType": "IMAGE"}
            if cur: f["alt"] = cur
            files.append(f)
            if i == 1: alts[srch] = cur
    variants = []
    for (ov, price, sku, srch) in p['variants']:
        it = by_handle[srch]
        v = {"optionValues": [{"optionName": k, "name": val} for k, val in ov.items()], "price": price, "inventoryItem": {"tracked": False}}
        if sku: v["sku"] = sku
        if it['images']:
            v["file"] = {"originalSource": it['images'][0]['url'], "contentType": "IMAGE"}
            if alts[srch]: v["file"]["alt"] = alts[srch]
        variants.append(v)
        if srch not in [r[0] for r in redirects]: redirects.append((srch, p['handle'], p['key']))
    mfs = [{"namespace": "descriptor", "key": "short_description", "type": "single_line_text_field", "value": p['short']}]
    for k, v in p['specs'].items():
        if v and AANV not in v: mfs.append({"namespace": "inhuys", "key": k, "type": "single_line_text_field", "value": v})
    mfs.append({"namespace": "inhuys", "key": "advies", "type": "rich_text_field", "value": rt(p['advies'])})
    mfs.append({"namespace": "inhuys", "key": "faq", "type": "rich_text_field", "value": rt([(q, a) for q, a in p['faq']])})
    inp = {"title": p['title'], "handle": p['handle'], "status": "DRAFT", "vendor": p['vendor'], "productType": p['ptype'], "tags": p['tags'], "category": CAT[p['cat']],
           "descriptionHtml": html_desc(p), "seo": {"title": p['seo_title'], "description": p['seo_desc']},
           "productOptions": [{"name": name, "position": i + 1, "values": [{"name": v} for v in vals]} for i, (name, vals) in enumerate(p['options'])],
           "variants": variants, "files": files, "metafields": mfs}
    if p.get('collections'): inp["collections"] = p['collections']
    batches[p['key']] = inp
    # markdown
    L = [f"# {p['title']}", "", f"Handle: `/products/{p['handle']}` · Status: **concept** (DRAFT) in Shopify · Merk: {p['vendor']} · Producttype: {p['ptype']}", "",
         f"Tags: {', '.join(p['tags'])}  ", f"Categorie: {CAT[p['cat']]}  ", f"Collecties: {', '.join(p.get('collections') or []) or '-'}", "",
         f"Meta-titel ({len(p['seo_title'])}): {p['seo_title']}  ", f"Meta-description ({len(p['seo_desc'])}): {p['seo_desc']}", "",
         f"**Zin onder de titel:** {p['short']}", "", "## Varianten en prijzen", "", "| " + " | ".join(n for n, _ in p['options']) + " | Prijs | SKU | Bron (oud product) |", "|" + "---|" * (len(p['options']) + 3)]
    for (ov, price, sku, srch) in p['variants']:
        L.append("| " + " | ".join(ov[n] for n, _ in p['options']) + f" | € {price.replace('.', ',')} | {sku or '-'} | `{srch}` |")
    L += ["", "## Beschrijving", "", "### Zo werkt het in de ruimte", p['ruimte'], "", "### Materiaal en maakwijze", p['materiaal'], "", "### Combineren", p['combineren'], "",
          "## Specificaties (metavelden `inhuys.*`)", "", "| Veld | Waarde |", "|---|---|"]
    L += [f"| {k} | {v} |" for k, v in p['specs'].items() if v]
    L += ["", "## Advies van InHuys", "", *p['advies'], "", "## Veelgestelde vragen", ""]
    L += [f"**{q}**  \n{a}\n" for q, a in p['faq']]
    w0 = by_handle[p['variants'][0][3]]['images'][0]['w'] if by_handle[p['variants'][0][3]]['images'] else '-'
    L += ["## Beelden", "", f"{len(files)} beelden overgenomen van de bestaande producten (resolutie {w0} px; vervangen door beeld van minimaal 2000 px zodra beschikbaar).", "",
          "Shopify koppelt hierbij hetzelfde beeldbestand als het live product; de alt-tekst is een eigenschap van dat bestand en dus gedeeld. De alt-teksten zijn daarom nog niet aangepast. Beoogde alt-teksten, toe te passen in fase 3 zodra de oude producten uit de lucht gaan:", ""]
    L += [f"- `{u.split('/files/')[-1].split('_')[0][:8]}…` → {a}" for u, a in beoogd]
    L += [""]
    if p['opm']: L += ["## Opmerking", "", p['opm'], ""]
    L += ["## Aan te vullen door de eigenaar", "", "Alle velden met `[AANVULLEN]` in de specificaties (afmetingen, zithoogte, zitdiepte, gewicht, materiaal) komen uit het specificatieblad van de leverancier. Zolang ze leeg zijn, toont de productpagina die rij niet.", ""]
    open(f"{OUT_MD}/{p['handle']}.md", "w", encoding="utf-8").write("\n".join(L))
groups = [["breeze", "cloud", "cloud-barkruk"], ["whale", "luna", "boog", "scandi"], ["agano", "waxinelicht", "boekensteun"], ["bank-amsterdam", "bank-new-york", "bank-londen"]]
for i, g in enumerate(groups, 1):
    v = {f"p{j+1}": batches[k] for j, k in enumerate(g)}
    json.dump(v, open(f"{OUT_DIR}/products-vars-{i}.json", "w", encoding="utf-8"), ensure_ascii=False)
    print(f"batch {i}: {g} -> {len(json.dumps(v, ensure_ascii=False))} tekens")
with open(OUT_REDIR, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=";"); w.writerows(redirects)
print("producten:", len(PRODUCTS), "redirects:", len(redirects) - 1)
for p in PRODUCTS: print(f"  {p['key']:14} seo_title={len(p['seo_title'])} seo_desc={len(p['seo_desc'])} woorden={len((p['ruimte']+' '+p['materiaal']+' '+p['combineren']).split())}")
