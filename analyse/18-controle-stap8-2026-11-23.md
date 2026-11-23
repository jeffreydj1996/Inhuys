# Controle stap 8 · 23 november 2026

Doel: vóór de publicatie kloppen producten, kleuren, foto's en collecties.

| Controle | Uitkomst |
|---|---|
| Foto per kleur op de winkel (`tools/winkel_controle.py`, 77 actieve producten) | 77 van 77 goed; uitzondering Raffles XL (niet leverbaar, geen bron) |
| Machinevertaalde kleurnamen | 5 producten: `ballenbak`, `holzrutsche-binnen`, `schommel-play-chill`, `springplek-binnen`, `whale-stoel-coco-set-van-2`. Orderchamp maakt de optiewaarden bij elke synchronisatie opnieuw aan (ballenbak en whale om 12:05, 25 minuten na onze hernoeming). Hernoemen via de API houdt geen stand; aanpassen in Orderchamp (eigenaar). |
| Onze teksten op de live producten (`tools/verifieer_overzetting.py`, 70 producten) | 70 gelijk; bij `barkruk-japandi-tan-set-van-2` staat daarnaast het metaveld `inhuys.hoofdproduct` (voor de regel "Onderdeel van"), geen afwijking in de tekst |
| Collecties (25) | 9 nieuwe categoriecollecties hebben een beeld (concept, nog niet gepubliceerd); `maatwerk` bewust leeg; 15 oude modelcollecties zonder beeld verdwijnen bij de publicatie uit de navigatie |
| Lege alt-teksten bij live producten | 0 (39 ingevuld in stap 7) |
| Beveiliging (`guard_shopify.py --test`) | 37 van 37 |

Details: `analyse/18-winkelcontrole-2026-11-23.txt`, `data/orderchamp/verificatie/verschillen-stap8-2026-11-23.txt`, `data/tmp/collecties-2026-11-23.json`.
Besluit eigenaar 23 november: schelpenketting H1 blijft zoals het is.
Open na 24 uur (geplande controle 24 november 12:40): opnieuw de winkelcontrole; daarna `media_varianten` leeg.
