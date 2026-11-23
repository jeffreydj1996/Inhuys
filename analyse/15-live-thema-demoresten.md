# Live thema: demoresten en herstellijst (actie A1)

Thema `gid://shopify/OnlineStoreTheme/200751743315` ("minimog-5-7-0 Met foto upload mogelijkheden"), rol MAIN bevestigd op 23 november 2026. Alleen gelezen; er is niets gemuteerd. De herstelbestanden staan in `data/out/live-thema-fix/` (zelfde paden als in het thema, commentaarkop van Shopify behouden, JSON valide zonder die kop; controle: `python3 -I data/out/live-thema-fix/verifieer.py`). Uploaden naar het live thema vraagt `INHUYS_GOLIVE=1` van de eigenaar, of de eigenaar doet het in de thema-editor aan de hand van de tabel.

Let op: de herstelbestanden zijn overgenomen uit de API-uitvoer en niet byte-vergeleken met Shopify (de opmaak die Shopify opslaat wijkt af van wat de API teruggeeft). Upload ze daarom als vervanging van het hele bestand of pas dezelfde regels in de editor aan.

## Tabel

| Demobelofte | Bestand | Blok of instelling | Herstelstap | In fix |
|---|---|---|---|---|
| "100 Days Return", "Lifetime Warranty", "30-day satisfaction guarantee" | `templates/product.json` | sectie `icon_box_9UtNky` (blokken `iconbox_pJbJGA`, `iconbox_RW46nE`, `iconbox_EiwgTg`, kop "Why Minimog?") | sectie `"disabled": true` | ja |
| "Free Shipping & Returns ... $75" en "Estimated Delivery" (automatische leverdatum, 7 dagen) | `templates/product.json` | sectie `main`, blok `shipping_VBJFtx`: `show_delivery_times`, `deliver_text`, `show_shipping_text`, `shipping_text` | blok `"disabled": true`; beide schakelaars uit en teksten leeg | ja |
| "100 in voorraad" en voorraadbalk | `templates/product.json` | sectie `main`, blok `inventory_status_wbzGXC`. Oorzaak: themadefaults `inventory_visibility=always` en `show_inventory_count=always` (niet in `settings_data.json` gezet) | blok `"disabled": true` | ja |
| "Guarantee safe & secure checkout" (vertrouwensregel) | `templates/product.json` | blok `trust_badge_NyBMd4`, `trust_badges_text` | tekst "Veilig afrekenen" (geen garantiebelofte) | ja |
| Tabkop "Shipping & Return" (inhoud is al Nederlands) | `templates/product.json` | `product-details-tabs`, blok `tab`, `header` | "Levering & retour" | ja |
| Veelgestelde vragen met Engelse leertekst | `templates/product.json` | sectie `collapsible_tabs_JndiBV` | staat al `"disabled": true`; niets te doen | n.v.t. |
| Leeftijdscheck | `sections/footer-group.json` | sectie `age-verifier-popup`: `enable` staat al `false` | extra `"disabled": true` op de sectie als dubbele zekerheid | ja |
| "10% off" nieuwsbrief | `sections/footer-group.json` | blok `7b0bf4c6-3873-4222-b8d6-ce009e710078` (`title`, `description`, `email_placeholder`, `button_label`) | Nederlandse tekst zonder korting: "Blijf op de hoogte", "Schrijf je in voor de nieuwsbrief van InHuys", "Vul je e-mailadres in", "Inschrijven" | ja |
| "Open Doors To A World Of Fashion" | `sections/header-group.json` | sectie `header`, blok `5e153016-a9d7-46c9-a10e-30d16446793d`, `alert_message` | "InHuys · ontwerp, advies en inrichting" (tagline) | ja |
| Aankondiging "Free shipping ... $60+" | `sections/header-group.json` | sectie `annoucement` | staat al `"disabled": true`; niets te doen | n.v.t. |
| Zoeksuggesties "T-Shirt, Blue, Jacket" | `config/settings_data.json` | `popular_search_queries` ontbreekt, dus de themadefault geldt | instelling toegevoegd: "Bank, Stoel, Vaas, Kaarshouder" (komt overeen met de categorieën op de homepage) | ja |
| Engelse cookiebanner | `config/settings_data.json` | `show_cookie_consent` blijft `true`; `cookie_consent_message`, `_allow`, `_decline`, `_learnmore`, `_learnmore_link` ontbraken (Engelse defaults) | Nederlandse teksten gezet ("Accepteren", "Weigeren", "Meer informatie"); link naar cookiesandyou.com leeg (verbergt de link) | ja |
| Lege social-links ("300k Followers", "100k Followers", facebook.com, instagram.com enz.) | `config/settings_data.json` | `social_twitter/facebook/pinterest/instagram/snapchat/youtube/tiktok_link` en `_label` | alle op leeg; WhatsApp blijft | ja |
| Merkenslider met mooisa en jesper-home | `templates/collection.json` | sectie `brands_list_c4BqNb` | sectie `"disabled": true` | ja |
| Merkenslider op de homepage | `templates/index.json` | sectie `brands_list_XfN79B` | staat al `"disabled": true`; niets te doen (index.json is niet gewijzigd) | n.v.t. |
| "Redden" | `locales/nl.json` (sleutel `cart.save`, mislukte vertaling van "Save") | niet in de zes gevraagde bestanden; het live bestand is niet gelezen (checksum wijkt af van de lokale werkversie) | alleen via Thema-editor > Taal bewerken, of `locales/nl.json` bij een volgende leesronde aanpassen naar "Opslaan" | nee |

## Alleen in de thema-editor of buiten deze bestanden

1. App-blokken: `config/settings_data.json` bevat het app-embed `shopify://apps/forms/...` (Shopify Forms, actief) en op de homepage sectie `apps_6qnUth` met formulier `864729`. Een kortingspopup of "10% off" in die app staat in de Forms-app zelf, niet in het thema. Controleer in Shopify Forms en zet het formulier uit of pas de tekst aan.
2. `locales/nl.json`: "Redden" en overige letterlijke Engelse of onjuiste vertalingen (zie hierboven).
3. Cookiebanner: het thema-venster is nu Nederlands, maar het is een eenvoudige banner. Controleer of de Shopify-privacybanner (Instellingen > Klantprivacy) niet dubbel staat; de eigenaar beslist of de themabanner uit moet.
4. `ai_room_preview_dygHXd` (product.json) verwijst naar een externe Cloud Run-endpoint; Nederlandse tekst is er al. Let op de AVG voor geüploade kamerfoto's; valt buiten A1.

## Andere Engelse of demo-resten (niet in A1, wel zichtbaar)

- Homepage `templates/index.json`: slider met "New Arrivals", "Creative Together", "Shop Now" (knoplinks leeg), "Design That Fits", "Every Home Has Its Own Needs", sectietitel "Populaire Categorieën" (spelling), "Accesiores", collectieblokken zonder link, en u-vorm in "Ik ben Sylvana" (schrijfregel: je-vorm).
- `sections/footer-group.json`: menutitels "Quick link", "Company", "Our store"; beide menu's gebruiken `main-menu`; `show_payment_icons` staat uit.
- `templates/product.json`: tabkop "Product description", kop "Recently Viewed Products", maatkop "Size".
- `config/settings_data.json`: `theme_currencies` "USD | EUR | GBP | VND" (wisselaar is verborgen), `cart_estimate_shipping` en `show_delivery_days` staan aan (indicatie komt uit echte Shopify-tarieven; controleren of dit klopt).
- De volledige vervanging door de werkversie (`data/theme-origineel`, kopie 210233098579) lost deze resten structureel op; A1 is alleen de noodstap.
