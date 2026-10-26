---
name: controle
description: Laat de controleur de mechanische controles draaien over teksten, concepten of de thema-kopie en vat het verdict samen. Gebruik /controle [alles|<handle>|thema|snapshot].
argument-hint: "[alles|<handle>|thema|snapshot]"
---
- `alles`: `controleur` met `check_tekst.py` op `content/producten/*.md content/paginas/*.md content/inspiratie/*.md` en `md_naar_vars.py` op alle productbestanden.
- `<handle>`: hetzelfde op één bestand, plus de feitensteekproef tegen `data/feiten/`.
- `thema`: `python3 -I tools/theme_build.py data/theme-origineel data/out/theme-new` en JSON-validatie van elk bestand in `data/out/theme-new/`; geen upload.
- `snapshot`: `lezer` maakt `data/snapshots/snapshot-<datum-tijd>.txt`; `controleur` vergelijkt met de laatste eerdere momentopname via `snapshot.py`.
Rapport aan de eigenaar: maximaal 20 regels, alleen afwijkingen; "alles in orde" als er niets is.
