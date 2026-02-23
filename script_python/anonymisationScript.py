import pandas as pd

import faker

fake = faker.Faker()

def categorieAge(valeur):
    if valeur < 18:
        return "0-17"
    elif valeur <= 30:
        return "18-30"
    elif valeur <= 40:
        return "31-40"
    elif valeur <= 60:
        return "41-60"
    else:
        return "60-120"

# filtrage des utilisateurs avec un bénéfice négatif 

#lecture du fichier
df = pd.read_csv("../data/dataset_projet_evaluation.csv", sep = ",")

#Agrégation
df["CatégorieÂge"] = df["Âge"].apply(categorieAge) #permet d'appliqué ligne par ligne la func

df["DernierAchat"] = pd.to_datetime(df["DernierAchat"]).dt.year
#pseudonymisation

df.drop(["Prénom", "Nom", "Âge"], axis = 1, inplace=True)




EmailList = [fake.email() for i in range (len(df["Email"])) ]

df["Email"] = EmailList

# Suppression des données trop sensibles

df.drop(["Sexe", "NuméroCarteCrédit", "TypeCarteCrédit", "DateExpirationCarte", "TypePaiementFavori"], axis = 1, inplace=True)

# print(df.columns)

#
#print(df.head(10))
# result = df.loc(df["ClientID"] == )


