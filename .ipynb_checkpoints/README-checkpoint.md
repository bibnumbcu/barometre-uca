Ce travail consiste en une modification et une adaptation du baromètre Lorrain https://scienceouverte.univ-lorraine.fr/barometre-lorrain-de-la-science-ouverte/

lui même inspiré inspiré du Baromètre français de la Science Ouverte : https://ministeresuprecherche.github.io/bso/

1) Téléchargez l'ensemble du Baromètre UCA sur le bureau en utilisant le bouton "Download".

2) Installez le logiciel Jupyter Lab (ou la suite Anaconda).

3) Lancez Jupyter Lab. Le dossier du Baromètre UCA téléchargé sur le bureau apparaît.

4) Remplacez les données de l'Université de l'UCA par celles de votre établissement. 
Les extractions dans les bases de données doivent se faire exactement comme c'est expliqué dans le notebook qui s'appelle "Etape 1 - nettoyage_donnees"

5) Dans le dossier qui est sur le bureau, enlever les fichiers UCA dans le dossier Data/raw et les remplacer par les vôtres. 
Attention, il faut reproduire très exactement le nommage des fichiers. Le séparateur des fichiers csv est la virgule.

6) Ouvrir le notebook "Etape 1 - nettoyage_donnees". 

7) Exécutez le notebook "nettoyage_donnees" en lisant bien les instructions à chaque étape.

8) Ouvrir le notebook "Etape 2 - enrichissement_donnees_uca". 

7) Exécutez le notebook "Etape 2 - enrichissement_donnees_uca" en lisant toutes les instructions.

8) Ouvrez le notebook "Etape 3 - génération_graphiques_uca". Ce notebook génère les graphiques du baromètre à partir du fichier de données créé par le notebook 2. Lisez les instructions avant d'executer le code

9) Les graphiques ont été automatiquement générés dans le dossier Data/outputs.