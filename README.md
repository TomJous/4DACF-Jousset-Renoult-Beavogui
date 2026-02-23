
# 4-DAFC : création d'un flux de données sur l'analyse clientèle d'une entreprise

## Auteur : Julien RENOULT - Tom JOUSSET - Béatrice BEAVOGUI
## Promo : SUPINFO Programme Grande École 4ème année 
## Spécialité : Ingénierie Data
### *Date : 23/02/2026*

Dans le cadre de ce projet, nous devions créer un processus de flux de données afin de l'anonymiser, nettoyer puis l'analyser à travers deux outils :
- Apache nifi : pour l'anonymisation et le nettoyage des données par un ETL en utilisant deux scripts python
- Power BI : pour la création du rapport/dashboard avec deux vue d'analyse, une portant sur les bénéfices et de l'autre sur le profil de la clientèle

Nous étions trois à faire ce projet et nous l'avons répartie de la façon suivante :
- Tom JOUSSET : il s'occupait de la création des deux scripts python sur l'anonymisation d'une part et le nettoyage d'autre part
- Béatrice BEAVOGUI : elle s'occupait de la création de l'ETL sur apache nifi en exécutant les deux scripts python
- Julien RENOULT : il s'occupait de la création du rapport sous Power BI afin d'analyser d'une part les bénéfices de l'entreprise et d'autre part le profil du client

Il existe trois dossiers dans ce projet qui répartissent le travail :
- script_python : les deux scripts python utilisées par Apache nifi
- apache_nifi : là où on trouve le flux de données et la capture d'écran de ce schéma
- dashboard : le rapport Power BI analysant les données préparées



