---
name: faseplan
description: Sluit de lopende fase af en schrijft het plan voor de volgende fase in plannen/fase-<n>.md, inclusief kostenraming, lijst van grote ingrepen voor de eigenaar en een toets of de agents nog passen. Gebruik /faseplan <n>.
argument-hint: <nummer van de nieuwe fase>
---
Schrijf `plannen/fase-<n>.md` met precies deze secties:

1. **Afsluiting fase <n-1>**: wat is opgeleverd (met paden en gids), wat open bleef, wat de meting zegt (laatste `analyse/gsc-rapport-*.md`).
2. **Doel van fase <n>** in drie zinnen.
3. **Stappen**: genummerd, per stap de skill en de agent(s), de batchgrootte en het resultaat.
4. **Kostenraming**: aantal modellen of teksten, per stap het model (haiku/sonnet/opus) en de verwachte tokens of credits op basis van de laatste proefdraai of batch (`/cost`).
5. **Grote ingrepen die de eigenaar vooraf goedkeurt**: alles wat live gaat, prijzen, structuur, juridische gegevens, nieuwe agents of rechten, uitgaven buiten de raming (zie CLAUDE.md).
6. **Agents**: tabel per agent met taak in deze fase, nog passend ja/nee, en zo nee wat er verandert (model, tools, script, nieuwe agent). Agents die een fase niet nodig zijn: "uit" (niet verwijderen).
7. **Verificatie**: hoe we aan het eind zien dat de fase klaar is (momentopname, controles, meting).

Leg het plan voor aan de eigenaar en wacht op akkoord; fase <n> start pas daarna. Verwijs in `README.md` naar het nieuwe faseplan.
