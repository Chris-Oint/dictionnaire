# Cahier des charges — « Dictionnaire selon Malachie 4 »

## But

Construire un dictionnaire thématique fondé **uniquement sur ce que William Branham affirme et définit dans les brochures**. L’application ne doit pas ressembler à un dictionnaire général ni à une liste de contextes où un mot apparaît. Chaque fiche donne d’abord directement le sens ou l’association explicitement formulé(e), puis montre toutes les preuves sources pertinentes.

Le titre visible est exactement **Dictionnaire selon Malachie 4**. Ne pas afficher « dictionnaire des brochures », ni le numéro ou le nom d’une zone dans l’interface publique. Les entrées et les contrôles de recherche commencent sous le titre. Le périmètre de travail par source et par étape peut être conservé dans les fichiers internes et le journal de recherche.

## Ce qu’il faut relever

Parcourir intégralement chaque corpus de brochures, paragraphe par paragraphe, sans recommencer une recherche déjà consignée. Relever les nombres et chiffres (y compris zéro, un, les ordinaux et les combinaisons), mots et noms dont le sens est expliqué, phrases et formules, adages/proverbes, paraboles et leurs éléments interprétés, symboles, animaux, types/antitypes, préfigurations et représentations. Élargir aux autres objets, couleurs, gestes, lieux, personnages ou éléments bibliques quand le passage leur attribue explicitement un sens.

Les rubriques organisent le contenu; elles ne doivent pas masquer les recoupements. Une entrée peut être retrouvée sous plusieurs recherches, mais chaque source et chaque sens ne sont stockés qu’une fois dans le jeu de données consolidé.

## Règles éditoriales

La définition s’écrit comme une fiche autonome et directe, par exemple « Quarante est le chiffre de la tentation », et non « Branham parle ici de quarante dans le contexte de… ». Reprendre la portée du texte : employer « signifie », « représente », « est un type de », « est associé à » ou une formule plus prudente selon les mots effectivement prononcés.

Ne pas déduire un sens de connaissances bibliques générales, d’une simple cooccurrence, d’un décompte ou d’une référence à l’Écriture. Ne pas transformer une phrase ordinaire en adage, ni une comparaison en typologie. Les rapprochements symboliques et les types doivent être formulés dans le passage, pas ajoutés par l’éditeur. Une énumération de nombres ou d’objets sans signification explicitée peut figurer dans une rubrique clairement séparée « mentionné, sans sens précisé »; elle ne compte pas comme définition.

Quand le même sens réapparaît dans d’autres brochures, joindre **toutes** les références qui le formulent. Distinguer les sens réellement différents au lieu de les fusionner. Conserver séparément les éditions VGR et Shekinah lorsque leur contenu ou leur numérotation diffère. Une paraphrase éditoriale peut condenser la définition, mais la citation source doit rester exacte.

## Preuves et renvois

Chaque référence comprend le code de brochure, le titre et la date, l’édition, le numéro de paragraphe, une citation courte exacte et un fragment `focus` exactement présent dans le paragraphe. Avant de garder une fiche, vérifier automatiquement le code, l’édition, le paragraphe et l’ancre dans le corpus et dans les métadonnées de l’application.

Le lien ouvre le lecteur Bible sur la bonne brochure et le bon paragraphe, via les paramètres `dictCode`, `dictEdition`, `dictParagraph` et `dictFocus`. À l’arrivée, le texte ciblé doit être mis en évidence et amené à l’écran. Tester les liens réels après chaque déploiement; ne pas considérer qu’un lien fonctionne seulement parce que sa chaîne d’URL est correcte.

## Données, inventaire et avancement

Conserver un jeu de données versionné par étape, plus un inventaire durable des brochures et paragraphes examinés. Enregistrer pour chaque passage candidat : code, édition, titre, date, paragraphe, texte source, marqueurs de détection, catégories candidates et état de vérification (`candidat`, `vérifié`, `rejeté`). Une autre IA doit pouvoir reprendre cet inventaire, ignorer les passages déjà vérifiés et justifier chaque décision. Un résultat candidat automatique n’est jamais présenté comme une définition vérifiée.

Format logique suggéré : `terme`, `valeur éventuelle`, `famille`, `définitions[]` (texte direct, nature, références[]), ainsi que `mentionsSansDefinition[]`. Chaque référence garde `code`, `edition`, `brochure`, `date`, `paragraphe`, `citation`, `focus` et, si disponible, `app_index`. Garder aussi le nombre de documents et paragraphes effectivement examinés et les exclusions importantes.

## Interface et fichiers

L’interface est en français, fonctionne sans bibliothèque distante et permet de rechercher un terme, un sens, une citation ou une brochure. Les fiches sont regroupées par terme; l’ouverture montre le sens et tous ses renvois, reliés par des pointillés comme dans un dictionnaire de références. Prévoir des filtres simples par famille quand les fiches seront suffisamment nombreuses.

Livrer à chaque étape les deux fichiers : la page web du dépôt et une copie HTML autonome, téléchargeable et utilisable hors ligne. Vérifier la syntaxe, l’égalité des copies générées, le fonctionnement hors ligne/service worker et l’affichage mobile. La liste de brochures consultées demeure dans les données internes même lorsque l’interface ne mentionne pas les zones.

## Procédure à répéter

1. Charger le corpus et l’inventaire existant; noter la couverture exacte avant toute recherche.
2. Rechercher tous les marqueurs de définition, de symbolisme, de type, d’interprétation et de sens des mots; examiner les passages candidats avec leur texte source.
3. Regrouper par terme puis par sens; rechercher de nouveau chaque sens dans l’ensemble des brochures afin de rattacher toutes les occurrences pertinentes.
4. Faire les contrôles de source et d’ancre pour chaque renvoi; isoler les simples mentions et les candidats non confirmés.
5. Mettre à jour le jeu de données et l’HTML autonome, sans supprimer les entrées vérifiées des étapes antérieures.
6. Refaire les tests, publier le commit dans le dépôt, vérifier le site et les renvois réels, puis remettre l’HTML et son URL copiable.

## État actuel

La première livraison numérique a été commitée dans le dépôt; elle contenait 10 renvois de définition et deux nombres mentionnés sans définition. Le premier contrôle complet local porte sur 382 brochures et 81 237 paragraphes et a produit un inventaire de passages **candidats** à vérifier pour les nombres, définitions, symboles, types, paraboles, formules et animaux. Ces marqueurs automatiques ne constituent pas encore une validation sémantique exhaustive. L’URL GitHub Pages permanente du dépôt doit encore être activée par un administrateur du dépôt; l’intégration GitHub a refusé cette opération de réglage avec une permission insuffisante.
