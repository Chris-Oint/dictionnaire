# Dictionnaire selon Malachie 4

## État de la livraison

La page et le fichier HTML autonome s’intitulent **Dictionnaire selon Malachie 4**; l’interface publique n’affiche pas d’identifiant de zone. La version actuellement vérifiée conserve les définitions numériques déjà sourcées. Elle n’est pas encore l’index exhaustif de tous les mots, formules, animaux, symboles, types et paraboles demandés : les passages candidats doivent être confirmés avant de devenir des fiches.

L’ancienne version contenait quatre nombres définis (3, 7, 40, 50), dix renvois de preuve et deux mentions (12, 24) sans sens précisé dans la citation. Le nouveau scan automatisé a couvert 382 brochures et 81 237 paragraphes. Il a généré 2 374 paragraphes candidats, avec leur code, édition, titre, date, paragraphe, extrait court et empreinte. Ces candidats ne sont pas des définitions validées.

## Sources de travail et fichiers

Les textes viennent du corpus du dépôt [Elie-le-Prophete-Shekinah-VGR](https://github.com/Chris-Oint/Elie-le-Prophete-Shekinah-VGR). `data/zone1-passage-inventory.jsonl` conserve les passages à examiner afin de ne pas recommencer les recherches; `data/zone1-passage-inventory-summary.json` en résume la couverture. `scripts/scan_zone1_candidates.py` reconstruit cet inventaire depuis le corpus. Toute fiche retenue doit encore être confirmée dans le paragraphe source.

`index.html` est la page du dictionnaire et `dictionnaire-selon-malachie-4.html` sa copie autonome hors ligne. `data/zone-1-nombres.json` conserve les fiches numériques initiales. `scripts/build_dictionary.py` génère les pages HTML; `sw.js` sert leur cache hors ligne. Le cahier des charges réutilisable se trouve dans `docs/cahier-des-charges.md`.

Les fiches regroupent chaque sens directement, puis rattachent toutes ses brochures/éditions/paragraphe-source. Les liens transmettent code, édition, paragraphe et ancre au lecteur Bible; les citations doivent être testées dans l’application, pas seulement formées en URL.

## Publication

Les commits de cette étape sont poussés dans les deux dépôts. GitHub Pages n’est pas encore activé pour ce dépôt; l’intégration GitHub n’a pas la permission de modifier le réglage Pages. Tant que **Settings → Pages → main / root** n’est pas activé par un administrateur, l’URL permanente ne sert pas cette page.
