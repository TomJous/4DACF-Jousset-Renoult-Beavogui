#####################################-
# Sujet : anonymisation des données dans le cadre du RGPD
# Auteurs : Julien RENOULT - Tom JOUSSET - Béatrice BEAVOGUI
# Date : 23/02/2026
#####################################-

# Script final pour l'anonymisation
import pandas as pd
from faker import Factory
from io import StringIO
import sys

# Construction du Faker
fake = Factory.create()

# Lecture du fichier
#df = pd.read_csv("../data/dataset_projet_evaluation.csv", sep = ",", header=0)
# Lire le CSV envoyé par NiFi via stdin
input_data = sys.stdin.read()
df = pd.read_csv(StringIO(input_data), sep=",", header=0)

# 1ère étape  : Suppression des données trop sensibles
df.drop(["Ville", "CodePostal", # Informations géographiques sensibles
              "DateNaissance", "Sexe", # Informations concernant la personne trop sensible et discriminatoire (sexe)
              "TypeCarteCrédit", "DateExpirationCarte", "SoldeCompte", "StatutCompte", # Informations sensibles sur la carte bleu du client concerné
              "Nom", "Prénom", "Adresse" # Suppresion des noms et prénoms car on a déjà l'id anonyme pour le client
             ],axis=1,
            inplace=True)

# 2ème étape : Agrégation + transformation en bon type des données
df["Âge"] = pd.cut(df["Âge"], [18, 30, 50, 70, 99], include_lowest=True)
df["DernierAchat"] = pd.to_datetime(df["DernierAchat"], format="mixed")

# 3ème étape : Pseudonymisation/Anonymisation
EmailList = [fake.email() for i in range (len(df["Email"])) ]
df["Email"] = EmailList
# Harmonisation des formats de téléphone
df["Téléphone"] = df["Téléphone"].str.replace(r'\d', '*', regex=True)
# Anonymisation des cartes de crédits
df['NuméroCarteCrédit'] = df['NuméroCarteCrédit'].astype("string").str.replace(r'\d', r'*', regex=True)
df['NuméroCarteCrédit'] = df['NuméroCarteCrédit'].astype("string")

# Renvoyer le CSV modifié
#df.to_csv("../data/anonymised_data.csv", index=False, header=True, sep=",")
print(df.to_csv(index=False, header=True, sep=","))