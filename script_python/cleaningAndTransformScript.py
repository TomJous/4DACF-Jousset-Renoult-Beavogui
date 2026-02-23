import pandas as pd


df = pd.read_csv("../data/dataset_projet_evaluation.csv", sep = ",")


#nettoyage des données

#Identifier et corriger les valeurs manquantes en les remplacant par des valeurs par défault

df[df.select_dtypes(include='string').columns] = df.select_dtypes(include='string').fillna("null")

df[df.select_dtypes(include='number').columns] = df.select_dtypes(include='number').fillna(-1)

df[df.select_dtypes(include='boolean').columns] = df.select_dtypes(include='boolean').fillna(False)


#Harmonisation des formats de date

df["DateNaissance"] = pd.to_datetime(df["DateNaissance"], format='%Y-%m-%d')


#Harmonisation des formats de téléphone

df["Téléphone"] = df["Téléphone"].str.replace(r'[\d, \D]', '*', regex=True)

#Supprimer les doublons et les valeurs aberrantes

df.drop_duplicates(subset=["ClientID"], inplace=True)

#Création de nouvelles colonnes dérivées

df["Bénéfice"] = df["MontantTotalAchats"] - df["MontantTotalRemboursé"]

df.loc[df["Bénéfice"] < 0, "Bénéfice"] = 0


# print(df.columns)
# print(df.head(10)["Téléphone"])