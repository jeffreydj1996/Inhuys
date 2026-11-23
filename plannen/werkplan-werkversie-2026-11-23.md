# Werkplan werkversie · 23 november 2026

Bron: `analyse/19-werkversie-test-2026-11-23.md` (browsertest van de voorvertoning, nummers T1–T15) en `analyse/20-open-punten-2026-11-23.md` (67 punten, nummers P1–P67).
Er wordt niets gepubliceerd. Agents werken alleen op de thema-kopie `210233098579`, concept-menu's, concept-pagina's en -artikelen, en in bestanden.

## Wie doet wat nu

| Spoor | Agent | Punten | Resultaat |
|---|---|---|---|
| A · Thema-kopie | thema-agent (sonnet, skill `/thema`) | T5 variantfoto's (oorzaak in het thema zoeken, eerst), T2/T4 collectietegels homepage naar de nieuwe collecties, T3/T5 `/collections` Nederlands en alleen de 9 categorieën, T7 + P21 Engelse tekst in de hele kopie, P20 lege knoplinks en demo-instellingen, T11 h1 op homepage, T8 levertijdzin alleen tonen als `inhuys.levertijd` gevuld is, T13 cookiebanner mobiel compacter | gewijzigde bestanden op de kopie, `analyse/07` bijgewerkt |
| B · Menu's (concept) | uitvoerder (sonnet) | P42 `hoofdmenu-fase-2`: onder "Collectie" de 9 categoriecollecties; `footer-service`: link naar `/pages/herroepen` | menu's bijgewerkt en teruggelezen |
| C · Redirects en runbook | onderzoeker/controleur (sonnet) | P39 21 doelen die concept blijven, P40 14 actieve producten met ander doel, P38: voorstel per regel en `analyse/redirects.csv` bijgewerkt; P47 runbook per publicatiestap in `plannen/fase-4.md` | CSV, `analyse/13` en `plannen/fase-4.md` |
| D · Teksten (concept) | schrijver + uitvoerder | P36 paginateksten `inspiratie` en `collecties` als bestand; P34 interne links in de 4 concept-artikelen naar de nieuwe collecties en pagina's; daarna de artikelen als concept bijwerken | `content/paginas/`, `content/inspiratie/`, concept-artikelen |
| E · Controle | controleur + browseragent | na A–D: de browsertest opnieuw (desktop en mobiel, ook winkelwagen), JSON-LD uit de voorvertoning, `/controle thema` (P29) | `analyse/19` tweede ronde |

Volgorde: A, B, C en D lopen tegelijk; E daarna. De geplande winkelcontrole van 24 november 12:40 blijft staan (P54).

## Bij de eigenaar (blokkeert publicatie)

1. Beleid plakken uit `content/beleid/html/` (retour, verzending, voorwaarden, privacy) en de bedragen bevestigen (P4, P5): productpagina's linken nu naar een retourbeleid dat niet bestaat (T4).
2. Verzendlanden alleen Nederland, verzendtarieven controleren met een testadres (P9, T14); iDEAL staat al in de checkout.
3. Herroepknop of -formulier (P7); de footerlink zetten wij.
4. Flitsadvies: prijs € 0,00 en of het product in `live_tekst` mag, zodat onze diensttekst erop kan (T6, P13).
5. Homepagetitel en -omschrijving in Online Store > Voorkeuren (P25, T9); voorstel in `analyse/07`.
6. Kleurnamen van 5 producten in Orderchamp aanpassen (P53).
7. Besluiten uit `plannen/fase-4.md` (dunne collecties, producten zonder voorraad, garantie, levertijdregel) en het akkoord op fase 4 met de guard-opening per stap (P45).
