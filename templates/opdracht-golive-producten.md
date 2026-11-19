Zet conceptproducten live (werkmap /home/user/Inhuys). Dit is een besluit van de eigenaar (regel 2c in CLAUDE.md). status.py NIET uitvoeren. Je krijgt een lijst met per regel: handle, spatie, gid. Gebruik de gids letterlijk uit dat bestand (`cat <bestand>`), nooit uit je hoofd.

Werk in groepen van vijf producten. Per groep twee mutaties, elk met vijf aliassen (a t/m e):
1. Status: mutation($a: ProductUpdateInput!, ...) { a: productUpdate(product: $a) { product { id status } userErrors { message } } ... } met per variabele precies {"id": "<gid>", "status": "ACTIVE"} en geen enkel ander veld.
2. Publiceren: mutation($a: ID!, ..., $in: [PublicationInput!]!) { a: publishablePublish(id: $a, input: $in) { userErrors { message } } ... } met $in precies:
[{"publicationId":"gid://shopify/Publication/295833895251"},{"publicationId":"gid://shopify/Publication/295833928019"},{"publicationId":"gid://shopify/Publication/295833993555"},{"publicationId":"gid://shopify/Publication/329534734675"},{"publicationId":"gid://shopify/Publication/329534996819"}]
Meldt de beveiliging GEBLOKKEERD, stop dan met dat product, probeer niets anders en meld het letterlijk.

Verificatie aan het eind, in query's van maximaal tien aliassen: node(id) { ... on Product { handle status resourcePublicationsCount { count } } }. Verwacht: status ACTIVE en 5 publicaties.
Rapporteer in maximaal 8 regels: aantal producten ACTIVE met 5 publicaties, en per afwijking de handle met de fout of userErrors letterlijk.
