# Dictionnaire des brochures — première livraison

## Livré

**Zone 1 · nombres** : dictionnaire regroupé par nombre, avec définitions explicites et liens qui ouvrent la brochure à la référence exacte dans l’application Bible. Le paragraphe source est surligné à l’arrivée.

- 4 nombres avec au moins une signification explicitement énoncée : **3, 7, 40 et 50**.
- 10 liens de preuve vers des paragraphes sources, regroupés sous les nombres correspondants.
- 2 nombres (**12 et 24**) apparaissent dans une énumération des « chiffres de Dieu », sans sens particulier précisé dans ce passage; ils sont rangés à part et non présentés comme des définitions.
- HTML autonome, sans bibliothèque ni ressource externe : après téléchargement, recherche et fiches restent consultables hors ligne.

L’ancienne liste de 69 entrées hétérogènes a été remplacée pour cette étape par une source structurée et attribuée paragraphe par paragraphe. Aucun sens symbolique non attesté n’est ajouté.

## Fichiers

- `index.html` : édition web.
- `dictionnaire-zone-1-nombres.html` : copie HTML téléchargeable et autonome.
- `data/zone-1-nombres.json` : données et références structurées.
- `scripts/build_dictionary.py` : reconstruit les deux HTML à partir des données.
- `sw.js` : cache hors ligne pour les pages de cette livraison.

## Sources et limites

Les citations proviennent du corpus de brochures zone 1 du dépôt [Elie-le-Prophete-Shekinah-VGR](https://github.com/Chris-Oint/Elie-le-Prophete-Shekinah-VGR). Les renvois conservent le code, l’édition et le paragraphe afin de distinguer notamment Shekinah et VGR.

Cette étape ne prétend pas épuiser les cinq zones : elle couvre la première famille demandée — les nombres — dans la zone 1. Les nombres supplémentaires seront ajoutés uniquement si leur signification est réellement explicitée dans les brochures.
