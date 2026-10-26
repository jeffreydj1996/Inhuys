# Genereert de aangepaste thema-bestanden voor de fase 2-werkversie uit de originelen (alleen-lezen kopie van het live thema).
import json, re, sys, os, copy
SRC, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
def load_json(rel):
    s = open(f"{SRC}/{rel}", encoding="utf-8").read()
    s = re.sub(r'^/\*.*?\*/\s*', '', s, flags=re.S)
    return json.loads(s)
def dump(rel, data, as_json=True):
    path = f"{OUT}/{rel}"; os.makedirs(os.path.dirname(path), exist_ok=True)
    txt = json.dumps(data, ensure_ascii=False, separators=(",", ":")) if as_json else data
    open(path, "w", encoding="utf-8").write(txt); return txt
LOG = []
def log(f, what): LOG.append((f, what))

ANCHOR = "#shopify-section-17709804707992f0a4"  # formulier-sectie op de Interieuradvies-pagina
TAGLINE = "ontwerp, advies en inrichting"

# ---------------- config/settings_data.json ----------------
sd = load_json("config/settings_data.json"); cur = sd["current"]
cs = cur["color_schemes"]
cs["default"]["settings"].update({"background": "#faf8f5", "background_secondary": "#dfd5c7", "border": "#e4ddd3",
    "price_sale": "#222222", "price_regular": "#222222", "button": "#695b4d", "button_label": "#ffffff",
    "button_hover": "#4f4338", "button_text_hover": "#ffffff", "outline_button_label": "#695b4d", "form_field": "#ffffff"})
cs["footer"]["settings"].update({"background": "#dfd5c7", "background_secondary": "#faf8f5", "text": "#222222", "subtext": "#5a524a",
    "heading_text": "#222222", "button": "#695b4d", "button_label": "#ffffff", "button_hover": "#4f4338", "border": "#cfc5b8", "price_sale": "#222222", "price_regular": "#222222"})
for b in ("badge-hot", "badge-new", "badge-sale"):
    cs[b]["settings"].update({"background": "#695b4d", "text": "#ffffff", "heading_text": "#ffffff", "subtext": "#ffffff"})
cs["scheme-09e5b5b4-774c-4b6c-8025-416ced49cc74"]["settings"].update({"button": "#695b4d", "button_hover": "#4f4338", "price_sale": "#222222", "heading_text": "#222222"})
cs["scheme-cee058e4-58e3-46aa-9af9-219dadc79066"]["settings"].update({"background": "#f4f0ea", "button": "#695b4d", "button_hover": "#4f4338", "price_sale": "#222222"})
cs["scheme-b756afa5-764f-4f80-958d-8afdb78a6ce0"]["settings"].update({"button": "#faf8f5", "button_label": "#222222", "button_hover": "#dfd5c7", "button_text_hover": "#222222", "price_sale": "#f5f5f5"})
log("config/settings_data.json", "Kleurschema's: gebroken wit #faf8f5 als achtergrond, zand #dfd5c7 als tweede vlak en footer, knop #695b4d (hover #4f4338), geen kortingsrood (actieprijs = tekstkleur), badges in merkbruin.")
cur.update({"type_header_font": "ebgaramond_n5", "use_custom_font_heading": False, "custom_heading_weight": "500", "type_header_base_size": 40})
log("config/settings_data.json", "Koppen: EB Garamond 500 uit de Shopify-fontbibliotheek (ebgaramond_n5) in plaats van de eigen Jost-upload; basisgrootte koppen 40 px. Lopende tekst en knoppen blijven Jost.")
for k in list(cur.keys()):
    if k.startswith("social_") and k.endswith("_link") and "whatsapp" not in k: cur[k] = ""
    if k.startswith("social_") and k.endswith("_label"): cur[k] = ""
cur["contact_phone_number"] = "+31 6 12932148"; cur["contact_email"] = "info@in-huys.nl"
cur["cookie_consent_theme"] = "white"
cur["cookie_consent_message"] = "We gebruiken cookies om de site te laten werken en om te zien welke pagina's bezocht worden. Geen advertentiecookies zonder je toestemming."
cur["cookie_consent_allow"] = "Akkoord"; cur["cookie_consent_decline"] = "Weigeren"; cur["cookie_consent_learnmore"] = "Privacybeleid"; cur["cookie_consent_learnmore_link"] = "/policies/privacy-policy"
log("config/settings_data.json", "Placeholder-sociallinks en neplabels verwijderd (WhatsApp blijft); telefoonnummer en e-mail ingevuld; cookiebanner licht en in het Nederlands.")
dump("config/settings_data.json", sd)

# ---------------- sections/header-group.json ----------------
hg = load_json("sections/header-group.json")
ann = hg["sections"]["annoucement"]; ann["settings"]["show_announcement"] = False
for bid, b in ann["blocks"].items(): b["settings"]["message"] = "Showroom in Purmerend · bezoek op afspraak"; b["settings"]["message_link"] = "/pages/showroom"
hd = hg["sections"]["header"]["settings"]
hd.update({"logo_text": "InHuys", "logo_max_width": 150, "sticky_logo_max_width": 120, "mobile_logo_max_width": 110, "main_menu": "hoofdmenu-fase-2", "mobile_menu": "hoofdmenu-fase-2", "show_compare_icon": False})
for bid, b in hg["sections"]["header"]["blocks"].items():
    if b["type"] == "topbar":
        b["settings"]["alert_message"] = f'<span>InHuys · {TAGLINE} · <a class="m-link-underline" href="/pages/showroom">Showroom in Purmerend, op afspraak</a></span>'
        b["settings"]["show_email"] = True; b["settings"]["show_phone_numb"] = True; b["settings"]["show_social_links"] = False
log("sections/header-group.json", "Aankondigingsbalk uit (tekst alvast Nederlands); topbalk toont de tagline en de showroom in plaats van 'Open Doors To A World Of Fashion'; logo 150 px; nieuw hoofdmenu 'hoofdmenu-fase-2'.")
dump("sections/header-group.json", hg)

# ---------------- sections/footer-group.json ----------------
fg = load_json("sections/footer-group.json"); ft = fg["sections"]["footer"]
ft["settings"].update({"copyright": f"© InHuys 2026 · {TAGLINE}", "show_social_links": False, "show_payment_icons": True, "show_menu_item_divider": False})
menus_seen = 0
for bid, b in ft["blocks"].items():
    t = b["type"]; s = b["settings"]
    if t == "newsletter":
        s.update({"title": "Eens per maand", "description": "Eén project, één materiaal, één idee. Geen aanbiedingen, wel inzicht.", "email_placeholder": "Je e-mailadres", "button_label": "Inschrijven", "show_social": False})
    elif t == "menu":
        menus_seen += 1
        if menus_seen == 1: s.update({"menu": "footer-inhuys", "title": "InHuys"})
        else: s.update({"menu": "footer-service", "title": "Service"})
    elif t == "our_store":
        s.update({"title": "Showroom", "description": "<p>InHuys bij Kluster<br>Netwerk 124, 1446 WR Purmerend<br>Op afspraak, ook 's avonds</p><p>InHuys is een handelsnaam van Kluster<br>KvK 88545857 · btw NL8680053B01</p>", "show_email": True, "show_phone": True, "show_socials_link": False})
log("sections/footer-group.json", "Footer: Nederlandse koppen, nieuwsbrief zonder kortingsbelofte, menu's 'InHuys' en 'Service', showroomadres en bedrijfsgegevens, betaaliconen aan, copyright met tagline.")
dump("sections/footer-group.json", fg)

# ---------------- templates/index.json ----------------
ix = load_json("templates/index.json"); old = ix["sections"]
new = {}
sl = copy.deepcopy(old["1621243260e1af0c20"]); first = copy.deepcopy(sl["blocks"]["1621243260e1af0c20-0"])
first["settings"].update({"background": "shopify://shop_images/Keizersgracht_213A-26.jpg", "content_position": "left middle", "text_color": "white",
    "subheading": f"InHuys · {TAGLINE}", "title": "Een verbouwing is pas af<br>als de ruimte klopt", "description": "<p>Interieurstyling en 3D-ontwerp voor verbouwingen in Amsterdam en omgeving. Showroom in Purmerend.</p>",
    "button_text": "Plan een adviesgesprek", "button_link": "/pages/interieuradvies", "button_style": "m-button--primary", "second_button_text": "Bezoek de showroom", "second_button_link": "/pages/showroom", "second_button_style": "m-button--secondary",
    "show_footer": False, "footer_text": "", "footer_button": "", "enable_preload_image": True})
sl["blocks"] = {"hero": first}; sl["block_order"] = ["hero"]; sl["settings"].update({"show_dots": False, "autorotate": False})
new["1621243260e1af0c20"] = sl
new["werkwijze"] = {"type": "icon-box", "blocks": {
    "stap1": {"type": "iconbox", "settings": {"title": "1 · Gesprek", "description": "<p>Online of in de showroom. Je vertelt, wij luisteren en kijken mee naar plattegrond en foto's.</p>", "button_label": "", "button_link": "", "button_style": "m-button--plain"}},
    "stap2": {"type": "iconbox", "settings": {"title": "2 · Ontwerp in 3D", "description": "<p>Plattegrond, indeling en een 3D-beeld van de ruimte, zodat je ziet hoe het wordt voordat er iets besteld is.</p>", "button_label": "", "button_link": "", "button_style": "m-button--plain"}},
    "stap3": {"type": "iconbox", "settings": {"title": "3 · Materiaal en kleur", "description": "<p>Een moodboard met stalen van bekleding, hout, steen en verf. Alles te zien en te voelen in de showroom.</p>", "button_label": "", "button_link": "", "button_style": "m-button--plain"}},
    "stap4": {"type": "iconbox", "settings": {"title": "4 · Inrichting en begeleiding", "description": "<p>Bestelling, levering en plaatsing, tot en met de laatste vaas. Maatwerk ontwerpen we zelf.</p>", "button_label": "", "button_link": "", "button_style": "m-button--plain"}}},
    "block_order": ["stap1", "stap2", "stap3", "stap4"],
    "settings": {"container": "container", "color_scheme": "", "heading": "Zo werken we", "heading_size": "h3", "subheading": "Van eerste gesprek tot laatste vaas", "description": "", "header_alignment": "center", "item_per_row": 4, "item_gap": 30, "item_gap_mobile": 10, "card_style": "vertical", "image_max_width": "70px", "content_alignment": "left", "enable_slider": False, "show_pagination": False, "show_navigation": False, "use_scroll_mobile": True, "use_grid_column_mb": False, "padding_top": 70, "padding_bottom": 40, "custom_class": "", "animations": "inherit"}}
new["projecten"] = {"type": "multiple-image-with-text", "blocks": {
    "project1": {"type": "image_with_text", "settings": {"image": "shopify://shop_images/Keizersgracht_213A-26.jpg", "title": "[Project 1 · plaats]", "sub_title": "Verbouwing en inrichting", "text": "<p>[Plaatshouder: opgave, keuzes en resultaat in drie zinnen. Wordt vervangen door een echt project zodra de foto's er zijn.]</p>", "text_size": "medium", "text_alignment": "left", "button_label": "Bekijk het project", "button_link": "/pages/projecten", "button_style": "m-button--link"}},
    "project2": {"type": "image_with_text", "settings": {"image": "shopify://shop_images/Kopie_van_Schetsindeling_meubels.jpg", "title": "[Project 2 · plaats]", "sub_title": "3D-ontwerp en maatwerk", "text": "<p>[Plaatshouder: opgave, keuzes en resultaat in drie zinnen.]</p>", "text_size": "medium", "text_alignment": "left", "button_label": "Bekijk het project", "button_link": "/pages/projecten", "button_style": "m-button--link"}}},
    "block_order": ["project1", "project2"],
    "settings": {"heading": "Projecten", "heading_size": "h3", "subheading": "Wat we maken, van plattegrond tot laatste vaas", "header_alignment": "center", "container": "container-fluid", "color_scheme": "", "column_gap": 60, "column_gap_mobile": 16, "show_pagination": False, "show_navigation": True, "autorotate": False, "padding_top": 40, "padding_bottom": 40, "custom_class": "", "animations": "inherit"}}
colls = [("banken", "Banken"), ("stoelen", "Stoelen"), ("fauteuils", "Fauteuils en loungestoelen"), ("barkrukken", "Barkrukken"), ("tafels", "Tafels"), ("vazen", "Vazen"), ("windlichten-en-kaarsenhouders", "Windlichten en kaarsenhouders"), ("decoratie", "Decoratie"), ("maatwerk", "Maatwerk")]
cl = copy.deepcopy(old["collection_list_tjXYY7"])
cl["blocks"] = {f"col_{h.replace('-', '_')}": {"type": "collection_block", "settings": {"collection": h, "title": t}} for h, t in colls}
cl["block_order"] = list(cl["blocks"].keys())
cl.pop("custom_css", None)
cl["settings"].update({"heading": "Collectie", "subheading": "", "description": "Stukken uit onze projecten, per categorie. Alles is te zien in de showroom in Purmerend.", "button_label": "Plan een adviesgesprek", "button_link": "/pages/interieuradvies", "show_product_count": False, "count_inline_title": False, "image_rounded": False, "items_per_row": 3, "item_gap": 30, "container": "container-fluid", "header_alignment": "center", "text_alignment": "center", "padding_top": 40, "padding_bottom": 40})
new["collection_list_tjXYY7"] = cl
cc = copy.deepcopy(old["custom_content_KiFzqG"])
cc["blocks"]["text_ADAEHz"]["settings"].update({"title": "Ontwerp dat past", "subheading": "Elk huis vraagt iets anders", "text": "<p>Elke woning heeft een eigen stijl en een eigen licht. Wij vertalen die naar een plan dat klopt in detail: van indeling tot de laatste vaas.</p>", "button_label": "Lees onze werkwijze", "button_link": "/pages/werkwijze"})
cc["blocks"]["image_comparison_fRB8LR"]["settings"].update({"before_heading": "Voor", "after_heading": "Na"})
new["custom_content_KiFzqG"] = cc
sy = copy.deepcopy(old["image_with_text_kLGNNN"]) if "image_with_text_kLGNNN" in old else copy.deepcopy(old["image_with_text_kLGLNN"])
sy["settings"].update({"title": "Ik ben Sylvana", "sub_title": "Interieurstylist en eigenaar van InHuys", "text": "<p>Elke dag help ik mensen hun huis samen te stellen: de indeling, de meubels, de materialen en de laatste laag die een ruimte afmaakt. Ik hou van interieurs die rust geven en kloppen in de details.</p><p>Wil je weten hoe ik werk? Begin met een gesprek, online of in de showroom in Purmerend.</p>", "button_label": "Lees meer over InHuys", "button_link": "/pages/over-inhuys"})
new["image_with_text_kLGLNN"] = sy
new["showroom"] = {"type": "image-with-text", "settings": {"heading": "", "heading_size": "h3", "subheading": "", "container": "container-fluid", "color_scheme": "", "item_gap": 100, "item_gap_mobile": 30, "layout": "right", "image_column_size": "6", "image_overlap": False, "show_image_reverse": False, "hover_effect": False, "image_animation": "none", "image": "shopify://shop_images/Kopie_van_Schetsindeling_meubels.jpg", "link": "/pages/showroom", "second_image_offset_top": 10,
    "title": "Showroom in Purmerend", "sub_title": "Bij Kluster · Netwerk 124", "text": "<p>Een stoel kies je met je rug, niet met je ogen. In de showroom zie en voel je de stoelen, banken en stalen uit de collectie, en bekijk je het 3D-ontwerp van je eigen huis. Op afspraak, ook 's avonds.</p>", "text_size": "medium", "content_alignment": "left", "button_label": "Plan een bezoek", "button_link": "/pages/showroom", "button_style": "m-button--primary", "button_size": "", "padding_top": 50, "padding_bottom": 50, "custom_class": "", "animations": "inherit"}}
bp = copy.deepcopy(old["blog_posts_pyG6yW"]); bp.pop("disabled", None)
bp["settings"].update({"heading": "Inspiratie", "subheading": "", "description": "", "blog": "trends", "limit": 3, "column": 3, "article_show_tags": False, "button_text": "Alle artikelen", "button_link": "/blogs/trends", "show_button_on_header": True})
new["blog_posts_pyG6yW"] = bp
ap = copy.deepcopy(old["apps_6qnUth"])
ap["settings"].update({"heading": "Plan een adviesgesprek", "subheading": "Vul het formulier in; we reageren binnen twee werkdagen."})
for bid, b in ap["blocks"].items(): b["settings"].update({"text_color": "#222222", "button_background_color": "#695b4d", "button_label_color": "#FFFFFF", "links_color": "#695b4d"})
new["apps_6qnUth"] = ap
ix["sections"] = new
ix["order"] = ["1621243260e1af0c20", "werkwijze", "projecten", "collection_list_tjXYY7", "custom_content_KiFzqG", "image_with_text_kLGLNN", "showroom", "blog_posts_pyG6yW", "apps_6qnUth"]
log("templates/index.json", "Homepage in de goedgekeurde volgorde: één slide met projectbeeld en twee knoppen; werkwijze in vier stappen; projectenblok met plaatshouders; collectie in negen categorietegels gekoppeld aan de nieuwe collecties; 'Ontwerp dat past' vertaald; Sylvana in je-vorm met link naar Over InHuys; showroomblok; inspiratie (blog Trends) ingeschakeld; adviesformulier als afsluiter. Verwijderd: 'New Arrivals'-slides, 'The Coastal Edition', productbundels, merkenlijst.")
dump("templates/index.json", ix)

# ---------------- templates/product.json ----------------
pj = load_json("templates/product.json"); main = pj["sections"]["main"]
main["blocks"]["variant_picker"]["settings"]["size_title"] = "Maat"
main["blocks"]["inventory_status_wbzGXC"]["settings"].update({"backordered_text": "<p>Op bestelling</p>", "low_text": "", "normal_text": "", "outofstock_text": "<p>Tijdelijk niet leverbaar</p>"})
main["blocks"]["shipping_VBJFtx"]["settings"].update({"deliver_text": "Verwachte levering:", "deliver_days": "14", "date_format": "%d %b", "shipping_text": "<p><strong>Levering</strong> via onze merkpartner; de levertijd staat bij elk product. <strong>Vragen?</strong> Plan een gratis Flitsadvies.</p>"})
main["blocks"]["trust_badge_NyBMd4"]["settings"]["trust_badges_text"] = "<p>Veilig afrekenen met iDEAL, creditcard en meer</p>"
SPECS_LIQUID = """{%- assign keys = "afmetingen|zithoogte|zitdiepte|gewicht|materiaal_frame|materiaal_bekleding|afwerking|set_inhoud|onderhoud|herkomst|levertijd|garantie" | split: "|" -%}
{%- assign labels = "Afmetingen (h × b × d)|Zithoogte|Zitdiepte|Gewicht|Materiaal frame|Materiaal bekleding|Kleur en afwerking|Set-inhoud|Onderhoud|Herkomst|Levertijd|Garantie" | split: "|" -%}
{%- assign has = false -%}
{%- for k in keys -%}{%- assign v = product.metafields.inhuys[k] -%}{%- if v != blank -%}{%- assign has = true -%}{%- endif -%}{%- endfor -%}
{%- if has -%}
<style>.inhuys-specs{margin-top:28px}.inhuys-specs h3{margin-bottom:10px}.inhuys-specs table{width:100%;border-collapse:collapse;font-size:14px}.inhuys-specs th{text-align:left;font-weight:500;padding:8px 0;border-bottom:1px solid #e4ddd3;width:46%;vertical-align:top}.inhuys-specs td{padding:8px 0;border-bottom:1px solid #e4ddd3}</style>
<div class="inhuys-specs"><h3 class="h5">Specificaties</h3><table>
{%- for k in keys -%}{%- assign v = product.metafields.inhuys[k] -%}{%- if v != blank -%}<tr><th>{{ labels[forloop.index0] }}</th><td>{{ v }}</td></tr>{%- endif -%}{%- endfor -%}
</table></div>
{%- endif -%}"""
ADVIES_LIQUID = """{%- if product.metafields.inhuys.advies != blank -%}
<style>.inhuys-advies{margin-top:24px;padding:20px 22px;background:#f4f0ea}.inhuys-advies h3{margin-bottom:8px}.inhuys-advies p:last-child{margin-bottom:0}</style>
<div class="inhuys-advies"><h3 class="h5">Advies van InHuys</h3>{{ product.metafields.inhuys.advies | metafield_tag }}</div>
{%- endif -%}"""
main["blocks"]["short_description_inhuys"] = {"type": "short_description", "settings": {}}
main["blocks"]["specificaties_inhuys"] = {"type": "custom_liquid", "settings": {"custom_liquid": SPECS_LIQUID}}
main["blocks"]["advies_inhuys"] = {"type": "custom_liquid", "settings": {"custom_liquid": ADVIES_LIQUID}}
main["block_order"] = ["badge_ChqgGj", "title", "short_description_inhuys", "price", "variant_picker", "ai_room_preview_dygHXd", "inventory_status_wbzGXC", "buy_buttons", "shipping_VBJFtx", "trust_badge_NyBMd4", "description_d6MgGK", "specificaties_inhuys", "advies_inhuys"]
ib = pj["sections"]["icon_box_9UtNky"]; ib["settings"]["heading"] = "Waarom InHuys"
texts = [("Advies inbegrepen", "<p>Twijfel je over maat, kleur of combinatie? Plan een gratis Flitsadvies, online of in de showroom.</p>", "/pages/interieuradvies"),
         ("Levering via onze merkpartners", "<p>De levertijd staat bij elk product. Bij een inrichting via InHuys zijn we bij de levering aanwezig.</p>", "/pages/veelgestelde-vragen"),
         ("Showroom in Purmerend", "<p>Kom proefzitten en voel de stalen. Op afspraak, ook 's avonds. Netwerk 124, bij Kluster.</p>", "/pages/showroom")]
for (bid, b), (t, d, l) in zip(ib["blocks"].items(), texts): b["settings"].update({"title": t, "description": d, "button_label": "Meer", "button_link": l, "link": l})
ct = pj["sections"]["collapsible_tabs_JndiBV"]; ct.pop("disabled", None); ct["settings"].update({"heading": "Veelgestelde vragen", "padding_top": 60, "padding_bottom": 40})
ct["blocks"] = {"faq_product": {"type": "liquid", "settings": {"header": "Over dit product", "custom_liquid": "{%- if product.metafields.inhuys.faq != blank -%}{{ product.metafields.inhuys.faq | metafield_tag }}{%- else -%}<p>Stel je vraag via een gratis Flitsadvies; we antwoorden binnen twee werkdagen.</p>{%- endif -%}"}},
                "faq_algemeen": {"type": "item", "settings": {"header": "Levering, retour en advies", "text_size": "h4", "content": "<p>Levertijden staan bij elk product. Retourneren kan binnen veertien dagen; maatwerk is uitgezonderd. Meer antwoorden vind je op de pagina Veelgestelde vragen.</p>", "open": False}}}
ct["block_order"] = ["faq_product", "faq_algemeen"]
pj["sections"]["product-details-tabs"]["blocks"]["description"]["settings"]["header"] = "Omschrijving"
pj["sections"]["product-details-tabs"]["blocks"]["tab"]["settings"]["header"] = "Levering en retour"
pj["sections"]["recent-viewed-products"]["settings"]["heading"] = "Recent bekeken"
pj["sections"]["product-recommendations"]["settings"]["heading"] = "Anderen bekeken ook"
pj["order"] = ["breadcrumb", "main", "product-details-tabs", "collapsible_tabs_JndiBV", "product-recommendations", "icon_box_9UtNky", "recent-viewed-products"]
log("templates/product.json", "Productpagina: labels in het Nederlands ('Maat', 'Op bestelling', 'Verwachte levering', verzendtekst zonder dollars); korte omschrijving onder de titel (metaveld descriptor.short_description); specificatietabel en 'Advies van InHuys' uit de inhuys-metavelden; FAQ-sectie ingeschakeld met productvragen uit metaveld inhuys.faq; 'Why Minimog?' vervangen door drie echte beloftes; 'Recently Viewed Products' → 'Recent bekeken'.")
dump("templates/product.json", pj)

# ---------------- templates/page.contact.json ----------------
pc = load_json("templates/page.contact.json")
pc["sections"]["contact-form"]["settings"].update({"title": "Neem contact op", "description": "<p>Vragen over een product, de showroom of een adviesgesprek? Stuur een bericht, of bel of app +31 6 12932148. We reageren binnen twee werkdagen.</p>", "show_phone": True})
pc["sections"]["main"]["blocks"] = {"showroom": {"type": "textblock", "settings": {"title": "Showroom", "content": "InHuys bij Kluster\nNetwerk 124, 1446 WR Purmerend\nOp afspraak, ook 's avonds\nInHuys is een handelsnaam van Kluster · KvK 88545857 · btw NL8680053B01"}}, "contact": {"type": "textblock", "settings": {"title": "Contact", "content": "+31 6 12932148 (bellen of WhatsApp)\ninfo@in-huys.nl"}}}
pc["sections"]["main"]["block_order"] = ["showroom", "contact"]
log("templates/page.contact.json", "Contactpagina: Nederlandse introductie, telefoonveld aan, blokken met showroomadres en contactgegevens.")
dump("templates/page.contact.json", pc)

# ---------------- templates/page.collecties.json ----------------
pcol = load_json("templates/page.collecties.json")
pcol["sections"]["custom_content_eJNxbn"]["disabled"] = True
cl2 = pcol["sections"]["collection_list_YpVbzr"]
cl2["blocks"] = {f"col_{h.replace('-', '_')}": {"type": "collection_block", "settings": {"collection": h, "title": t}} for h, t in colls + [("kinderkamer", "Kinderkamer")]}
cl2["block_order"] = list(cl2["blocks"].keys())
cl2["settings"].update({"heading": "Collectie", "text_alignment": "center", "show_product_count": False})
log("templates/page.collecties.json", "Collecties-pagina: vier 'Example collection title'-tegels vervangen door de tien categoriecollecties; blok met de plaatshoudertekst 'lijst met collecties' uitgeschakeld.")
dump("templates/page.collecties.json", pcol)

# ---------------- templates/page.inspiratie.json ----------------
pi = load_json("templates/page.inspiratie.json")
pi["sections"]["blog_posts_hnM7z9"]["settings"].update({"subheading": "Inspiratie", "description": "Elke maand nieuwe tips en inzichten over verbouwen, inrichten en de keuzes die daarbij horen.", "button_text": "Meer artikelen", "blog": "trends", "button_link": "/blogs/trends"})
log("templates/page.inspiratie.json", "Inspiratie-pagina: ontbrekend woord in de introzin hersteld, knop 'View More' → 'Meer artikelen', artikelen uit blog Trends.")
dump("templates/page.inspiratie.json", pi)

# ---------------- templates/page.interieuradvies.json ----------------
pa = load_json("templates/page.interieuradvies.json")
cards = pa["sections"]["custom_content_rVw6MQ"]["blocks"]
cards["text_card_with_image_UQL9Jn"]["settings"].update({"link": "/pages/werkwijze", "title": "<strong>3D-interieurontwerp compleet</strong>", "text": "<p>Prijs op aanvraag; het bedrag verrekenen we bij aankoop van de inrichting via InHuys.</p><h4>Opmeting en plattegrond</h4><p>Indeling, looproutes en de plek van elk meubel.</p><h4>Ontwerp in 3D</h4><p>Je ziet hoe de ruimte wordt voordat er iets besteld is.</p><h4>Meubelvoorstel en moodboard</h4><p>Passend bij je wensen en budget, met materiaal- en kleuradvies.</p>", "button_label": "Vraag het 3D-ontwerp aan", "button_link": ANCHOR})
cards["text_card_with_image_B87UDz"]["settings"].update({"link": "/pages/werkwijze", "title": "<strong>Flitsadvies</strong>", "text": "<p>Gratis. Online of in de showroom in Purmerend, ongeveer een uur.</p><h4>Eén vraag, direct antwoord</h4><p>Stijl, materiaal, kleur of een meubel dat niet wil passen.</p><h4>2D-vloerplan als dat helpt</h4><p>Een basisplattegrond om een nieuwe indeling te zien.</p>", "button_label": "Plan een Flitsadvies", "button_link": ANCHOR})
pa["sections"]["rich_text_rWADei"]["blocks"]["text_" + list(pa["sections"]["rich_text_rWADei"]["blocks"].keys())[0].split("_", 1)[1]] if False else None
for bid, b in pa["sections"]["rich_text_rWADei"]["blocks"].items():
    if b["type"] == "text": b["settings"]["text"] = "<h3><em>Kies de vorm die bij je vraag past</em></h3>"
for bid, b in pa["sections"]["rich_text_67JWrW"]["blocks"].items():
    if b["type"] == "button": b["settings"].update({"button_label": "Plan een gesprek", "button_link": ANCHOR})
fs = pa["sections"]["favorite_product_slider_ydVL4g"]["settings"]
fs.update({"heading": "Flitsadvies", "subheading": "Kort advies met direct resultaat", "description": "Eén vraag, één uur, online of in de showroom. Persoonlijk advies over stijl, indeling, materiaal en kleur, met als het helpt een beknopt 2D-vloerplan. Gratis.", "button_label": "Plan een Flitsadvies", "button_link": ANCHOR})
pa["sections"]["image_with_text_2_pwc7gk"]["settings"].update({"subtitle": "Flitsadvies en 3D-ontwerp · Amsterdam en omgeving"})
log("templates/page.interieuradvies.json", "Interieuradvies: dienstkaarten herschreven (3D-ontwerp met vanaf-prijs, Flitsadvies gratis), knoppen linken naar het aanvraagformulier op dezelfde pagina in plaats van naar de pagina zelf; 'Shop now' → 'Plan een Flitsadvies'. De paginatekst zelf (live) is niet gewijzigd.")
dump("templates/page.interieuradvies.json", pa)

# ---------------- layout/theme.liquid ----------------
tl = open(f"{SRC}/layout/theme.liquid", encoding="utf-8").read()
tl2 = tl.replace('<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=0">', '<meta name="viewport" content="width=device-width, initial-scale=1">')
tl2 = tl2.replace("{% render 'theme-data' %}", "{% render 'theme-data' %}\n    {% render 'inhuys-schema' %}")
assert tl2 != tl
log("layout/theme.liquid", "Viewport-meta zonder zoomblokkade (toegankelijkheidsfout uit PageSpeed); snippet 'inhuys-schema' gerenderd in de head.")
dump("layout/theme.liquid", tl2, as_json=False)

SCHEMA = """{%- comment -%} InHuys · Organization/LocalBusiness, WebSite en BreadcrumbList (fase 2) {%- endcomment -%}
{%- liquid
  assign home = shop.url
  assign crumbs = ''
  case request.page_type
    when 'product'
      assign c = collection
      if c == blank
        assign c = product.collections.first
      endif
      if c != blank
        assign crumbs = crumbs | append: '{"@type":"ListItem","position":2,"name":' | append: c.title | json | append: ',"item":"' | append: home | append: c.url | append: '"},'
        assign crumbs = crumbs | append: '{"@type":"ListItem","position":3,"name":' | append: product.title | json | append: ',"item":"' | append: home | append: product.url | append: '"}'
      else
        assign crumbs = crumbs | append: '{"@type":"ListItem","position":2,"name":' | append: product.title | json | append: ',"item":"' | append: home | append: product.url | append: '"}'
      endif
    when 'collection'
      assign crumbs = crumbs | append: '{"@type":"ListItem","position":2,"name":' | append: collection.title | json | append: ',"item":"' | append: home | append: collection.url | append: '"}'
    when 'page'
      assign crumbs = crumbs | append: '{"@type":"ListItem","position":2,"name":' | append: page.title | json | append: ',"item":"' | append: home | append: page.url | append: '"}'
    when 'article'
      assign crumbs = crumbs | append: '{"@type":"ListItem","position":2,"name":' | append: blog.title | json | append: ',"item":"' | append: home | append: blog.url | append: '"},'
      assign crumbs = crumbs | append: '{"@type":"ListItem","position":3,"name":' | append: article.title | json | append: ',"item":"' | append: home | append: article.url | append: '"}'
  endcase
-%}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "LocalBusiness",
      "@id": "{{ home }}/#organization",
      "name": "InHuys",
      "legalName": "Kluster",
      "alternateName": ["In-Huys", "In Huys", "InHuys · ontwerp, advies en inrichting"],
      "vatID": "NL8680053B01",
      "identifier": {"@type": "PropertyValue", "propertyID": "KvK", "value": "88545857"},
      "description": "Interieurstyling, 3D-interieurontwerp en inrichting voor verbouwingen in Amsterdam en omgeving. Showroom in Purmerend.",
      "url": "{{ home }}",
      "logo": "{{ 'Logo_InHuys.png' | file_url }}",
      "image": "{{ 'Logo_InHuys.png' | file_url }}",
      "telephone": "+31612932148",
      "email": "info@in-huys.nl",
      "address": {"@type": "PostalAddress", "streetAddress": "Netwerk 124", "postalCode": "1446 WR", "addressLocality": "Purmerend", "addressRegion": "Noord-Holland", "addressCountry": "NL"},
      "areaServed": [{"@type": "City", "name": "Amsterdam"}, {"@type": "City", "name": "Purmerend"}, {"@type": "AdministrativeArea", "name": "Noord-Holland"}],
      "priceRange": "€€€",
      "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "21:00", "description": "Alleen op afspraak, ook 's avonds; zaterdag in overleg"}
    },
    {
      "@type": "WebSite",
      "@id": "{{ home }}/#website",
      "url": "{{ home }}",
      "name": "InHuys",
      "publisher": {"@id": "{{ home }}/#organization"},
      "inLanguage": "nl",
      "potentialAction": {"@type": "SearchAction", "target": "{{ home }}/search?q={search_term_string}", "query-input": "required name=search_term_string"}
    }{%- if crumbs != blank -%},
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "{{ home }}"},
        {{ crumbs }}
      ]
    }{%- endif -%}
  ]
}
</script>
"""
log("snippets/inhuys-schema.liquid", "Nieuw: LocalBusiness-markup (naam, tagline als alternateName, adres showroom, telefoon, werkgebied), WebSite met SearchAction en BreadcrumbList voor product-, collectie-, pagina- en artikelpagina's.")
dump("snippets/inhuys-schema.liquid", SCHEMA, as_json=False)

# ---------------- batches ----------------
files = {}
for rel in ["config/settings_data.json", "sections/header-group.json", "sections/footer-group.json", "layout/theme.liquid", "snippets/inhuys-schema.liquid",
            "templates/index.json", "templates/page.contact.json", "templates/page.collecties.json", "templates/page.inspiratie.json", "templates/page.interieuradvies.json", "templates/product.json"]:
    files[rel] = open(f"{OUT}/{rel}", encoding="utf-8").read()
batches = [["config/settings_data.json", "sections/header-group.json", "sections/footer-group.json", "layout/theme.liquid", "snippets/inhuys-schema.liquid"],
           ["templates/index.json", "templates/page.contact.json", "templates/page.collecties.json", "templates/page.inspiratie.json"],
           ["templates/page.interieuradvies.json", "templates/product.json"]]
for i, b in enumerate(batches, 1):
    v = {"files": [{"filename": f, "body": {"type": "TEXT", "value": files[f]}} for f in b]}
    json.dump(v, open(f"{OUT}/../theme-vars-{i}.json", "w", encoding="utf-8"), ensure_ascii=False)
    print(f"batch {i}: {b} -> {sum(len(files[f]) for f in b)} tekens")
# JSON-validatie van alle json-bestanden
for rel, txt in files.items():
    if rel.endswith(".json"): json.loads(txt)
print("alle JSON valide")
open(f"{OUT}/../theme-changelog.json", "w", encoding="utf-8").write(json.dumps(LOG, ensure_ascii=False, indent=1))
