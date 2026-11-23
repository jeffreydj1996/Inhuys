# Wettelijke eisen en vertrouwen: toets live site www.in-huys.nl (stand 23 november 2026)

Methode: live pagina's opgehaald met `curl -sS -L -A "Mozilla/5.0"` op 23-11-2026 (alleen lezen, geen bestelling, geen formulier verstuurd). Ruwe kopieën en tekstversies staan in de scratchpad van deze sessie (niet in de repo). Bronnen voor de regels: ACM (via curl), Thuiswinkel.org (via curl), overige via zoekresultaten. Checkout zelf is niet bekeken (vereist een winkelwagen; niet gedaan).

## Verplichte bedrijfsgegevens (KvK, btw-id, adres, telefoon, e-mail)

### Takeaway
De gegevens bestaan wel, maar alleen op de door Shopify gegenereerde pagina `/policies/contact-information`, die nergens in de navigatie of footer gelinkt is. Footer en contactpagina tonen geen KvK, btw-id of adres: **onvoldoende**.

### Cited Findings
- `/policies/contact-information` (HTTP 200) toont: Handelsnaam InHuys, telefoon +31612932148, e-mail info@in-huys.nl, adres Netwerk 124, 1446 WR Purmerend, btw NL8680053B01, handelsnummer 88545857. De juridische naam Kluster ontbreekt ("Handelsnaam: InHuys", geen rechtspersoon/eigenaar) — [in-huys.nl/policies/contact-information](https://www.in-huys.nl/policies/contact-information)
- Footer van de homepage bevat alleen "Quick link" en "Company" met dezelfde vier links (Assortiment, Bestsellers, Inspiratie, Interieuradvies), "Our store", "© InHuys2026", social-iconen naar generieke `facebook.com/`, `instagram.com/`, `twitter.com/`, `pinterest.com/`, `tiktok.com/`, `youtube.com/`, `snapchat.com/` (geen eigen accounts) en een WhatsApp-link. Geen link naar contactgegevens, voorwaarden, privacy of retour — [in-huys.nl](https://www.in-huys.nl/)
- Header toont alleen info@in-huys.nl — [in-huys.nl](https://www.in-huys.nl/)
- `/pages/contact` (200) heeft een contactformulier (naam, e-mail, bericht) maar Engelse demotekst: "We would love to hear from you. If you've got great products your making or looking to work with us then drop us a line." plus een WordPress-achtige regel "Bewaar mijn naam, e-mailadres en website in deze browser…". Geen adres, telefoon, KvK of openingstijden — [in-huys.nl/pages/contact](https://www.in-huys.nl/pages/contact)
- `/policies/legal-notice` geeft 404 — [in-huys.nl/policies/legal-notice](https://www.in-huys.nl/policies/legal-notice)
- Repo-context: het plan is "InHuys is een handelsnaam van Kluster · KvK 88545857 · btw NL8680053B01" op de (concept)pagina over-inhuys en in footer/structured data (`analyse/04-voorstel-fase-2.md` r. 225; `content/paginas/over-inhuys.md` r. 33). Dat staat nog niet live.

### Inferences
- Wettelijk moet de identiteit van de verkoper (naam rechtspersoon/handelsnaam, adres, KvK, btw, e-mail, telefoon) vóór de koop "duidelijk en begrijpelijk" beschikbaar zijn; een ongelinkte Shopify-policypagina is vindbaar via de checkout-footer alleen als Shopify die daar toont, wat niet zeker is. Actie: footer-blok met "InHuys is een handelsnaam van Kluster", adres, KvK, btw, telefoon, e-mail, en links naar alle beleidspagina's.
- De demotekst op de contactpagina en de nep-socialelinks ondermijnen vertrouwen direct.

### Gaps
- Of de checkout-footer de contactgegevens-policy toont, niet gecontroleerd (geen checkout geopend).
- De formele rechtsvorm van Kluster (eenmanszaak/vof/bv) is niet geverifieerd in het KvK-register.

## Algemene voorwaarden, herroepingsrecht, modelformulier, retourbeleid, herroepingsknop

### Takeaway
**Ontbreekt**: `/policies/terms-of-service`, `/policies/refund-policy` en `/policies/shipping-policy` geven allemaal 404. Er is geen modelformulier, geen retouradres, geen regeling voor retourkosten en geen herroepingsknop, terwijl die laatste sinds juni 2026 verplicht is. De bedenktijd van klanten wordt daardoor met 12 maanden verlengd.

### Cited Findings
- 404 op terms-of-service, refund-policy, shipping-policy (pagina "Oeps! Pagina niet gevonden!") — [terms](https://www.in-huys.nl/policies/terms-of-service), [refund](https://www.in-huys.nl/policies/refund-policy), [shipping](https://www.in-huys.nl/policies/shipping-policy)
- Productpagina's tonen een korte regel "Levering & retour: Dit item wordt geleverd via onze merkpartner. Levertijd kan per variant verschillen. Retourneren kan binnen de wettelijke termijn (uitgezonderd maatwerk)." — [bank-londen-6-zits-tan](https://www.in-huys.nl/products/bank-londen-6-zits-tan), [eetkamerstoel-rock-set-van-2](https://www.in-huys.nl/products/eetkamerstoel-rock-set-van-2)
- Dezelfde productpagina toont tegelijk demo-claims uit het Minimog-thema: "Why Minimog? 100 Days Return", "Lifetime Warranty", "Invest in our activewear with absolute confidence, backed by our 30-day satisfaction guarantee" en "Free Shipping & Returns: On all orders over $75" — [bank-londen-6-zits-tan](https://www.in-huys.nl/products/bank-londen-6-zits-tan)
- ACM: bedenktijd is tot en met 14 dagen na levering; u moet dit vóór de koop vertellen — [ACM bedenktijd](https://www.acm.nl/nl/verkoop-aan-consumenten/klantenservice/bedenktijd)
- ACM: "Vertel wie het terugsturen betaalt, anders zijn deze kosten voor u. En wat dit kost als het niet door de brievenbus kan." en "U vermeldt een Nederlands retouradres als uw webwinkel in Nederland is gevestigd." — [ACM bedenktijd](https://www.acm.nl/nl/verkoop-aan-consumenten/klantenservice/bedenktijd)
- ACM: terugbetalen binnen 14 dagen, inclusief bezorgkosten (behalve bij gedeeltelijke retour); mag wachten tot product terug is of bewijs van terugzending — [ACM bedenktijd](https://www.acm.nl/nl/verkoop-aan-consumenten/klantenservice/bedenktijd)
- ACM: "De bedenktijd wordt met 1 jaar verlengd als u geen of te weinig informatie geeft." — [ACM bedenktijd](https://www.acm.nl/nl/verkoop-aan-consumenten/klantenservice/bedenktijd)
- ACM: uitzondering op bedenktijd voor "producten gemaakt volgens de specificaties van de consument, zoals een maatpak of kast op maat" — [ACM bedenktijd](https://www.acm.nl/nl/verkoop-aan-consumenten/klantenservice/bedenktijd)
- Herroepingsknop: ACM-persbericht (11-06-2026): "Vanaf 19 juni 2026 moeten webshops en apps een duidelijke zogenoemde 'ontbindings- of herroepingsknop' hebben" — [ACM herroepingsknop](https://www.acm.nl/nl/publicaties/acm-roept-online-retailers-op-zich-voor-te-bereiden-op-herroepingsknop); de ACM-pagina bedenktijd noemt echter "Vanaf 25 juni 2026" — [ACM bedenktijd](https://www.acm.nl/nl/verkoop-aan-consumenten/klantenservice/bedenktijd). Datum verschilt tussen twee ACM-pagina's; in beide gevallen is de plicht nu (november 2026) al van kracht.
- Eisen aan de knop: duidelijke naam (bv. "Koop ongedaan maken"), tijdens de hele (ook verlengde) bedenktijd eenvoudig vindbaar op de website, geen verplicht account, leidt naar bevestigingspagina met minimale gegevens, daarna bevestiging met datum en tijdstip; consumenten vóór de koop over alle manieren van ontbinden informeren — [ACM bedenktijd](https://www.acm.nl/nl/verkoop-aan-consumenten/klantenservice/bedenktijd)
- ACM: een webshop mag bovenop retourkosten geen andere kosten (zoals administratiekosten) rekenen; terugbetaling met tegoedbon alleen als klant zo betaalde — samenvatting zoekresultaten van [ACM node 17843](https://www.acm.nl/nl/node/17843) en [Kassa](https://www.bnnvara.nl/kassa/artikelen/mag-een-webwinkel-geld-vragen-voor-het-terugsturen-van-een-pakketje)
- Handhaving: ACM beboette T.O.M. bv met €500.000 voor schending van terugbetaalregels — [ACM boetebesluit](https://www.acm.nl/sites/default/files/old_publication/publicaties/16371_boetebesluit-webwinkel-tom-new.pdf)
- Repo: conceptpagina veelgestelde-vragen zegt "binnen de wettelijke termijn van veertien dagen na ontvangst, in originele staat. Maatwerk … uitgesloten" (`content/paginas/veelgestelde-vragen.md` r. 41); niet live.

### Inferences
- Zonder voorwaarden en retourinformatie draagt InHuys standaard de retourkosten, en kan een klant tot 12 maanden + 14 dagen na levering herroepen. Bij banken van €3.700–€5.700 (live in products.json) is dat een reëel financieel risico.
- "In originele staat" mag niet als voorwaarde voor herroeping; de klant mag het product beoordelen en is alleen aansprakelijk voor waardevermindering. Formulering in de FAQ-concepttekst aanpassen.
- Retourkosten voor grote meubels (niet via brievenbus/pakket): ACM eist dat de kosten (of een schatting) vooraf genoemd worden. Een concreet bedrag per categorie (pakket vs. bank) nodig.
- "Uitgezonderd maatwerk" geldt alleen voor echt naar specificatie van de klant gemaakte stukken; een kleurkeuze uit vaste varianten (tan/umber) is geen maatwerk.
- De demo-claims "100 Days Return", "Lifetime Warranty", "30-day satisfaction guarantee", "Free Shipping & Returns over $75" zijn onwaar en kunnen als misleidende handelspraktijk gelden of als toezegging worden ingeroepen. Hoogste prioriteit om te verwijderen (thema, regel 2: alleen via de thema-kopie + go-live door eigenaar).
- Herroepingsknop: in Shopify is dit niet standaard; vereist een app of eigen pagina + formulier (en link in footer en orderbevestiging). Moet vóór opschalen marketing live.

### Gaps
- Geen Orderchamp-voorwaarden voor retour van consumentenzendingen gevonden (orderchamp.com/nl/terms en help.orderchamp.com gaven 403/geen verbinding).
- Welke Shopify-app de herroepingsknop het best invult is niet onderzocht.

## Privacybeleid (AVG) en cookietoestemming

### Takeaway
Privacybeleid **aanwezig maar generiek** (Shopify-sjabloon, bijgewerkt 1 november 2026, ongelinkt in footer). Cookiebanner **aanwezig maar onzeker/onvoldoende**: Engelse themabanner ("Allow cookies"/"Decline", link naar cookiesandyou.com) naast Shopify's eigen privacy-banner-script; een Pinterest-pixel draait voor marketing.

### Cited Findings
- `/policies/privacy-policy` (200), "Laatst bijgewerkt: 1 november 2026", Shopify-standaardtekst: categorieën gegevens, doelen, delen met Shopify, rechten EER (bezwaar, intrekking toestemming), contact via info@in-huys.nl, "wij zijn de verwerkingsverantwoordelijke". Geen bewaartermijnen per categorie, geen concrete lijst verwerkers (Orderchamp, Pole To Pole, Jupiduu, Pinterest), geen naam rechtspersoon — [in-huys.nl/policies/privacy-policy](https://www.in-huys.nl/policies/privacy-policy)
- Homepage-HTML laadt `privacy-banner/privacy-banner.js` en `consent-tracking-api` (Shopify Customer Privacy) én een eigen themabanner (`cookie-banner`, tekst "This website uses cookies to ensure you get the best experience on our website. Learn more / Decline / Allow cookies", link naar www.cookiesandyou.com) — [in-huys.nl](https://www.in-huys.nl/)
- `webPixelsConfigList` bevat een app-pixel met `tagID 2613654060191` (Pinterest-tag-formaat), `privacyPurposes ["ANALYTICS","MARKETING","SALE_OF_DATA"]`, `dataSharingControls ["share_all_events"]`, plus een custom pixel (ANALYTICS, MARKETING) — [in-huys.nl](https://www.in-huys.nl/) (HTML-bron)
- Productpagina's bieden "Bekijk dit product in jouw kamer – Upload een foto van je kamer – Genereer mijn preview – AI-gegenereerde visualisatie"; het privacybeleid noemt die verwerking van foto's niet — [bank-londen-6-zits-tan](https://www.in-huys.nl/products/bank-londen-6-zits-tan)
- AP-lijn (via zoekresultaten): weigeren moet even makkelijk zijn als accepteren; impliciete toestemming (doorsurfen) geldt niet; cookiewalls in strijd met de regels; AP stuurt jaarlijks honderden websites een brief en startte in 2024 onderzoeken waarin alle onderzochte organisaties de wet overtraden — [Consumentenbond 2025](https://www.consumentenbond.nl/acties-claims/nieuws/2025/onderzoek-cookies-nog-steeds-teveel-opgedrongen), [NOS](https://nos.nl/l/2563725), [Dutch IT Channel](https://www.dutchitchannel.nl/news/421472/ap-gaat-misleidende-cookiebanners-aanpakken)
- Consumentenbond-onderzoek: 32 van 84 sites met cookiebanner (38%) voldeden niet aan de AP-richtlijnen — [Consumentenbond](https://www.consumentenbond.nl/internet-privacy/bijna-4-op-de-10-cookiebanners-niet-in-de-haak)

### Inferences
- De themabanner is Engelstalig en stuurt alleen een lokale cookie; of hij de Shopify Customer Privacy API aanstuurt (zodat de Pinterest-pixel pas na toestemming vuurt) is twijfelachtig. Advies: themabanner uitzetten en alleen de Shopify-cookiebanner (Customer Privacy, regio EU, "toestemming vereist") gebruiken, in het Nederlands, met gelijkwaardige knoppen "Accepteren"/"Weigeren" en een link naar een eigen cookieverklaring.
- Privacybeleid aanvullen met: Kluster als verwerkingsverantwoordelijke, verwerkers (Shopify, Orderchamp, merken voor bezorging, Pinterest, e-mailtool), bewaartermijnen, AI-kamerpreview (foto-upload: welk model/leverancier, bewaartermijn), klachtrecht bij de Autoriteit Persoonsgegevens.
- De nieuwsbriefclaim "receive 10% off your first order" (Engels, in footer) moet kloppen met een werkende korting; anders misleidend.

### Gaps
- Runtime-gedrag (vuurt de Pinterest-pixel vóór toestemming?) niet getest; vereist een browser met netwerkinspectie.
- AP-pagina's zelf gaven 403 via curl; AP-eisen zijn via secundaire bronnen (Consumentenbond, NOS) weergegeven.

## Prijzen incl. btw, verzendkosten en levertijd vóór de checkout

### Takeaway
Prijzen incl. btw: **aanwezig** ("Inclusief belasting."). Verzendkosten: **ontbreekt / tegenstrijdig** (alleen "Free Shipping & Returns on all orders over $75" in dollars). Levertijd: **onjuist/tegenstrijdig** (automatische "Estimated Delivery: Nov 28 - Dec 02" naast "Levertijd kan per variant verschillen").

### Cited Findings
- Productpagina: "Normale prijs €4.739,95 / Verkoopprijs €4.739,95 … Inclusief belasting."; winkelwagen: "Inclusief belasting en verzendkosten berekend bij het afrekenen" — [bank-londen-6-zits-tan](https://www.in-huys.nl/products/bank-londen-6-zits-tan), [cart](https://www.in-huys.nl/cart)
- Productpagina toont "Estimated Delivery: Nov 28 - Dec 02" (opgehaald 23-11) en "100 in voorraad" voor een 6-zits bank van €4.739,95 — [bank-londen-6-zits-tan](https://www.in-huys.nl/products/bank-londen-6-zits-tan)
- Varianten zijn foutief vertaald: "Omber" en "Bruinen" (tan → 'bruinen'), met verschillende prijzen €4.739,95 en €4.740,00 — [bank-londen-6-zits-tan](https://www.in-huys.nl/products/bank-londen-6-zits-tan)
- `/meta.json`: `ships_to_countries` bevat 41 landen, o.a. US, CA, AU, JP, KR, SG, AE, IL, NZ, GB, CH — [in-huys.nl/meta.json](https://www.in-huys.nl/meta.json)
- ACM: zonder afgesproken levertijd geldt een wettelijke termijn van 30 dagen; webwinkels moeten de verwachte levertijd juist vermelden; bij dropshipping moeten reële levertijd en land van verzending duidelijk zijn; ACM trad op tegen Grandado ("maximaal 25-30 werkdagen") en tegen "Vandaag verzonden"-beloftes — [ACM leveren en bezorgen](https://www.acm.nl/nl/verkoop-aan-consumenten/leveren-en-bezorgen), [ACM Grandado](https://www.acm.nl/nl/publicaties/webwinkel-grandadocom-informeert-consumenten-beter-over-levertijd-na-optreden-acm)
- ACM: bijkomende kosten (zoals verzendkosten) moeten vooraf vermeld worden — [ACM bijkomende kosten](https://www.acm.nl/nl/onderwerpen/verkoop-aan-consumenten/verkopen-aan-consumenten/bijkomende-kosten-vermelden)
- Repo: fase-2-voorstel wil "Levertijd concreet: '2 tot 3 weken, geleverd door onze partner'" en fase 4 stelt voor levertijd en garantie leeg te laten tot Orderchamp/de merken het schriftelijk bevestigen (`analyse/04-voorstel-fase-2.md` r. 118; `plannen/fase-4.md` r. 67).

### Inferences
- De automatische leverdatum van 4–9 dagen is vrijwel zeker onjuist voor meubels die via Orderchamp door Pole To Pole worden geleverd; dat is precies het type belofte waarop ACM handhaaft. Widget uitzetten tot per merk een schriftelijk bevestigde levertijd bekend is.
- "100 in voorraad" lijkt een Orderchamp-placeholdervoorraad; tonen van voorraadaantallen kan als schaarste-/urgentiesignaal worden gelezen en is hier niet waar. Uitzetten.
- Verzending naar 41 landen terwijl de merkpartners vermoedelijk alleen NL/BE (of EU) beleveren: risico op onleverbare orders, extra btw-plicht (OSS buiten NL) en consumentenrecht van andere landen. Advies: verzendzones beperken tot NL (en eventueel BE) tot bevestigd. Verzendkosten per zone (pakket vs. meubel) zichtbaar maken op productpagina en in een verzendbeleid.

### Gaps
- Werkelijke verzendtarieven in de Shopify-verzendinstellingen niet ingezien (checkout niet geopend).
- Levertijden van Pole To Pole en Jupiduu via Orderchamp niet bevestigd.

## Garantie (wettelijke garantie / conformiteit)

### Takeaway
**Ontbreekt**: nergens staat de wettelijke garantie (conformiteit); wel een onware "Lifetime Warranty"-claim uit het thema.

### Cited Findings
- "Lifetime Warranty – Our dedicated team provides timely assistance…" op productpagina's — [bank-londen-6-zits-tan](https://www.in-huys.nl/products/bank-londen-6-zits-tan)
- Geen voorwaarden- of garantiepagina (404 op terms-of-service) — [terms](https://www.in-huys.nl/policies/terms-of-service)

### Inferences
- Een "levenslange garantie" is een commerciële garantie die InHuys dan moet nakomen of die als misleidend geldt; verwijderen. In voorwaarden/FAQ opnemen: het product moet doen wat de klant mag verwachten (conformiteit), klant meldt gebreken binnen bekwame tijd, InHuys is aanspreekpunt (niet de merkpartner) — ook bij dropshipping.

### Gaps
- Primaire ACM-pagina over garantie niet opgehaald (tool-limiet); de bovenstaande inhoud van de wettelijke garantie is algemeen bekend Nederlands recht (Boek 7 BW) maar niet in deze notities met URL onderbouwd.

## ACM-regels voor prijsacties en urgentie; keurmerken en reviews

### Takeaway
Er zijn nu geen van-voor-prijzen live (alle `compare_at_price` leeg), maar de productpagina toont "Normale prijs" en "Verkoopprijs" naast elkaar met hetzelfde bedrag. Geen keurmerk en geen reviewsysteem: **ontbreekt**.

### Cited Findings
- products.json: alle 30 live producten `compare_at_price: None` (Pole To Pole, €23,95 tot €5.739,95) — [in-huys.nl/products.json](https://www.in-huys.nl/products.json)
- ACM-leidraad: doorhalen mag alleen als de van-prijs de laagste prijs van de 30 dagen vóór de korting is; geldt sinds 28 mei 2022; ACM beboette Koopjedeal voor kunstmatig verhoogde van-prijzen — [CMS over ACM-leidraad](https://cms.law/en/nld/publication/nieuwe-acm-leidraad-let-op-prijsinformatie), [ACM boetebesluit Koopjedeal](https://acm.nl/system/files/documents/boetebesluit-day-traders-koopjedeal.pdf), [ACM prijzen vermelden](https://www.acm.nl/nl/verkoop-aan-consumenten/consumenten-informeren/prijzen-vermelden)
- Thuiswinkel Waarborg (Thuiswinkel.org): eenmalig €75 registratie; jaarlijks certificering €390 (€345 + €45 per URL); contributie op basis van online omzet incl. btw: klasse 2 (€0–€100.000) €518, klasse 3 (€100.000–€250.000) €776 (excl. btw); audit door ICTRecht; extra kosten bij eigen aanvullende voorwaarden — [Thuiswinkel.org kosten](https://www.thuiswinkel.org/en/become-a-member/what-does-membership-of-thuiswinkel-org-cost/)
- WebwinkelKeur: officiële prijspagina niet gevonden (webwinkelkeur.nl/prijzen/ gaf 404); de site biedt "Keurmerk voor webshops", "Goedkoop Webshop Keurmerk", "Algemene voorwaarden webshop", "Privacyverklaring opstellen", reviews en "Reviews in Google" — [webwinkelkeur.nl](https://www.webwinkelkeur.nl/). Een Shopify-blog noemt keurmerkpakketten van ongeveer €10/€15/€23 per maand, maar het is onduidelijk of die bedragen bij WebwinkelKeur horen — [Shopify NL blog](https://www.shopify.com/nl/blog/webshop-keurmerk)

### Inferences
- Begin met een keurmerk + reviews (WebwinkelKeur of Kiyoh) als goedkope stap; Thuiswinkel Waarborg (± €983 eerste jaar bij <€100k omzet: €75 + €390 + €518) is pas zinvol bij hogere omzet. Beide vereisen eerst complete voorwaarden, retour- en privacybeleid.
- Bij toekomstige acties: compare_at-prijs alleen gebruiken met de laagste prijs van de afgelopen 30 dagen; de labels "Normale prijs / Verkoopprijs" bij gelijke bedragen verbergen.
- Demo-urgentiesignalen (voorraadteller, automatische leverdatum) weghalen.

### Gaps
- Geen ACM-bron gevonden specifiek over afteltimers/nepurgentie (zoekopdracht leverde dit niet op).
- WebwinkelKeur- en Kiyoh-tarieven 2026 niet geverifieerd; Trustpilot niet onderzocht.

## Betaalmethoden

### Takeaway
Shopify Payments is actief (Visa, Maestro, Mastercard, Shop Pay/versnelde knoppen). iDEAL en Klarna zijn niet publiek te verifiëren zonder checkout: **onzeker**.

### Cited Findings
- Productpagina-config: `"shopifyPaymentsEnabled":true`, `"supportedNetworks":["visa","maestro","masterCard"]`, `countryCode NL`, `currencyCode EUR`; versnelde knoppen (`shopify-payment-button`, `shop_pay`) — [bank-londen-6-zits-tan](https://www.in-huys.nl/products/bank-londen-6-zits-tan) (HTML-bron)
- Er zijn geen betaal-iconen in de footer (geen iDEAL/Klarna-logo's in de HTML) — [in-huys.nl](https://www.in-huys.nl/)
- iDEAL is veruit de populairste online betaalmethode: ±70% online marktaandeel volgens Betaalvereniging — [Betaalvereniging](https://www.betaalvereniging.nl/en/knowledge-base/online-payments/online-payment-methods/); >50% met creditcard 9% en Klarna 8% in een consumentenenquête (okt. 2025) — [ESB](https://esb.nu/online-betaalmethodes/); Stripe noemt ±75% — [Stripe](https://stripe.com/nl/resources/more/how-to-accept-online-payments-in-the-netherlands). Verschillen komen door meetmethode.
- Repo: conceptpagina FAQ belooft "iDEAL, creditcard en de andere betaalmethoden" (`content/paginas/veelgestelde-vragen.md` r. 44).

### Inferences
- In de Shopify-admin controleren of iDEAL (en eventueel Klarna/Bancontact) in Shopify Payments aanstaat, en betaal-iconen in de footer tonen. Bij bedragen van €200–€5.700 is achteraf/gespreid betalen (Klarna) relevant voor conversie.

### Gaps
- Checkout niet geopend (opdracht: geen orders); daadwerkelijk aangeboden methoden onbekend.

## Dropshipping-specifieke risico's (Orderchamp)

### Takeaway
Bij dropshipping blijft InHuys tegenover de consument volledig verantwoordelijk (levertijd, retouradres in NL, schade, garantie). De site zegt alleen "geleverd via onze merkpartner"; de afspraken met Orderchamp over retour van consumentenorders zijn niet bekend.

### Cited Findings
- De shop gebruikt de Orderchamp-app met fulfilmentdienst "Orderchamp Dropshipping" (eigen locatie) — repo `analyse/10-orderchamp-koppeling.md` r. 7
- Orderchamp-helpcentrum: schade of ontbrekende producten melden binnen 4 werkdagen na geplande of werkelijke aankomst via de backoffice; sommige claims (beschadigd/ontbrekend, defect, verkeerd) gaan direct naar het merk — [Orderchamp help](https://orderchamp.zendesk.com/hc/en-150/articles/360019677797-How-do-I-report-damaged-or-missing-products) (via zoekresultaat; directe fetch gaf 403)
- ACM: bij dropshipping reële levertijd en land van verzending vermelden; Nederlands retouradres als de webwinkel in NL gevestigd is — [ACM Grandado](https://www.acm.nl/nl/publicaties/webwinkel-grandadocom-informeert-consumenten-beter-over-levertijd-na-optreden-acm), [ACM bedenktijd](https://www.acm.nl/nl/verkoop-aan-consumenten/klantenservice/bedenktijd)

### Inferences
- Een Orderchamp-meldtermijn van 4 werkdagen voor de retailer botst met de rechten van de consument (bedenktijd 14 dagen, conformiteit langer). InHuys draagt het gat: in de voorwaarden klanten vragen schade binnen 48 uur te melden met foto's (zonder hun wettelijke rechten te beperken) en intern direct doorzetten naar Orderchamp.
- Retouradres: vaststellen of retouren naar het merk (Pole To Pole: NL?) of naar Purmerend gaan, en wie ophaalt bij grote meubels; dat bepaalt de retourkosten die vooraf gemeld moeten worden.
- Leveringsmodel en verzendlanden beperken tot wat Orderchamp/merken echt bezorgen.

### Gaps
- Orderchamp-retailervoorwaarden voor dropshipping (retour, schade, levertijd-SLA) niet ingezien (403).

## Overige vertrouwensissues gevonden op de live site

### Takeaway
Veel demo-inhoud van het Minimog-thema staat live; dat ondermijnt vertrouwen meer dan elk ontbrekend keurmerk.

### Cited Findings
- Leeftijdscheck op elke pagina: "Confirm your age – Are you 18 years old or older?" (theme `age-verifier`) — [in-huys.nl](https://www.in-huys.nl/)
- Demotekst op homepage: "Open Doors To A World Of Fashion", "The ReCotton Tee", zoeksuggesties "T-Shirt, Blue, Jacket", categorie "Accesiores", "Every Home Has Its Own Needs", "Let's get in touch", "Sign up for our newsletter and receive 10% off your first order" — [in-huys.nl](https://www.in-huys.nl/)
- Homepage spreekt de klant aan met "u" ("Mijn doel is om het voor u zo makkelijk mogelijk te maken") — [in-huys.nl](https://www.in-huys.nl/)
- `/pages/flitsadvies` geeft 404 (de dienst Flitsadvies heeft geen eigen pagina op die url) — [in-huys.nl/pages/flitsadvies](https://www.in-huys.nl/pages/flitsadvies)

### Inferences
- Snelle winst vóór marketing: leeftijdscheck uit, demo-teksten/blokken vervangen, footer met bedrijfsgegevens en beleidslinks, nep-socialelinks weg.
- Voor Flitsadvies (dienst): informatie over bedenktijd bij diensten (start binnen bedenktijd → klant betaalt naar rato) moet vooraf gegeven worden — [ACM bedenktijd](https://www.acm.nl/nl/verkoop-aan-consumenten/klantenservice/bedenktijd).

### Gaps
- Live Flitsadvies-productpagina (url onbekend) niet beoordeeld.

---

### Samenvattende checklist (stand 23-11-2026)

| Onderdeel | Status | Bewijs |
|---|---|---|
| KvK, btw, adres, telefoon in footer/contact | Onvoldoende (alleen ongelinkte policy, geen Kluster) | /policies/contact-information, /pages/contact |
| Algemene voorwaarden | Ontbreekt (404) | /policies/terms-of-service |
| Herroepingsrecht + modelformulier + retouradres + retourkosten | Ontbreekt (alleen één regel op PDP) | /policies/refund-policy, PDP |
| Herroepingsknop (verplicht sinds juni 2026) | Ontbreekt | ACM |
| Verzendbeleid / verzendkosten vooraf | Ontbreekt; "$75"-demo | /policies/shipping-policy, PDP |
| Levertijd | Onjuist (auto "Nov 28 - Dec 02") | PDP |
| Wettelijke garantie | Ontbreekt; "Lifetime Warranty"-demo | PDP |
| Privacybeleid | Aanwezig, generiek, ongelinkt | /policies/privacy-policy |
| Cookietoestemming | Onvoldoende/onzeker (Engelse themabanner + Shopify-banner, Pinterest-pixel) | homepage-HTML |
| Prijzen incl. btw | Aanwezig | PDP, cart |
| Van-voor-prijzen | N.v.t. (geen compare_at); labels verwarrend | products.json, PDP |
| Urgentie/voorraadteller | Aanwezig maar onwaar ("100 in voorraad") | PDP |
| Keurmerk / reviews | Ontbreekt | homepage |
| Betaalmethoden zichtbaar (iDEAL) | Onzeker; geen iconen | PDP-config |
| Verzendlanden | Te breed (41 landen incl. US/AU/JP) | /meta.json |
| Leeftijdscheck 18+ / demo-tekst | Aanwezig, schadelijk | homepage |
