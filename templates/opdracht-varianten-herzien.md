Herzie bestaande productbestanden in /home/user/Inhuys/content/producten/ zodat ze kloppen met de actuele varianten van het Orderchamp-concept. Orderchamp heeft na het schrijven kleuren samengevoegd of gesplitst; Orderchamp is de basis en gaat vóór de oudere export en de fabrikant.

Per bestand staat de actuele stand in data/orderchamp/verificatie/varianten-afwijkingen-2026-11-19.txt (zoek de regel die met de handle begint): achter "Orderchamp" staat per variant (naam, SKU, prijs, voorraad).

Wat je per bestand doet:
1. Variantentabel: precies de varianten van Orderchamp, met de variantnaam letterlijk zoals Orderchamp hem geeft (ook vertaalfouten als Bruinen, Omber, Kokos, room, Nerts, Roodachtig), de prijs in de schrijfwijze van de bestaande tabel (€ 249,95) en de SKU. Houd de kolomkoppen en de bronhandle in de laatste kolom zoals ze zijn.
2. Titel, zin onder de titel, meta-titel, meta-description, tags, lopende tekst, specificatierij afwerking, FAQ: laat ze aansluiten op de varianten MET voorraad (voorraad > 0). In lopende tekst gebruik je de gewone kleurnaam (tan voor Bruinen, umber voor Omber, coco voor Kokos, crème voor room, mink voor Nerts, reddish voor Roodachtig, zandwit voor Zand Wit). Een variant met voorraad 0 staat alleen in de variantentabel en onder "Opmerking". Is er nog maar één variant, dan gaat de tekst alleen over die variant.
3. Kleur- en stoffeiten per kleur alleen uit het feitenbestand van het model in data/feiten/ (zoek het met Glob op de modelnaam); staat een kleur daar niet in, noem dan alleen de kleurnaam. Noem geen prijzen in lopende tekst of FAQ.
4. Verwijst de tekst met een markdown-link naar een "apart product" voor een kleur die nu als variant in dit product zit, haal die verwijzing dan weg. Laat de rij `| hoofdproduct | … |` staan waar hij staat.
5. Onder "Opmerking": één regel "Varianten bijgewerkt naar de stand in Orderchamp op 19 november 2026" met de vertaalde variantnamen, en bij prijsverschillen tussen varianten (set tegenover stuk) één regel dat de prijzen de Orderchamp-prijzen zijn.
6. Verander verder zo weinig mogelijk: koppen, tabelopbouw, Handle-regel, Categorie en specificaties blijven. Regels: je-vorm, InHuys; maten verweven, nooit als losse mededeling; geen circa, ongeveer, zo'n of ca.; meta-titel maximaal 60 tekens en eindigt op " · InHuys", meta-description 120 tot 160 tekens (tel ze).

Rapporteer in maximaal 2 regels per bestand: wat is veranderd, lengte meta-titel en meta-description.
