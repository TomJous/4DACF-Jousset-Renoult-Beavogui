#####################################-
# Sujet : nettoyage des données dans le cadre du RGPD
# Auteurs : Julien RENOULT - Tom JOUSSET - Béatrice BEAVOGUI
# Date : 23/02/2026
#####################################-

# Script final pour le nettoyage des données
import pandas as pd
from io import StringIO
import sys

# Lecture du fichier CSV
#df = pd.read_csv("../data/anonymised_data.csv", sep = ",", header=0)
input_data = sys.stdin.read()
df = pd.read_csv(StringIO(input_data), sep=",", header=0)

# Nettoyage des données

# 1ère étape : Supprimer les doublons
df.drop_duplicates(subset=["ClientID"], inplace=True)

# 2ème étape : Identifier et corriger les valeurs manquantes 
# en les remplacant par des valeurs par défaut ou la médiane pour les champs numériques

# Pour les colonnes catégoriques
df[df.select_dtypes(include=['string', 'object']).columns] = df.\
    select_dtypes(include=['string', 'object']).fillna("null")

# Pour les colonnes numériques
colonnes_numbers = [col for col in df.columns if df[col].dtype in ("float", "int")]

# Remplacer chaque valeur manquante de la colonne numérique par sa médiane
for col_number in colonnes_numbers:
    # Avoir la valeur de la médiane sans les valeurs négatives et nulles
    median_number = df[~(df[col_number].isna()) | (df[col_number] > 0)][col_number].median()
    #print(median_number)
    # Capturer les valeurs négatives et nulles
    dataset_neg_na = df[(df[col_number].isna()) | (df[col_number] < 0)]
    #print(dataset_neg_na[col_number])
    nb_na_neg = dataset_neg_na.shape[0]
    dataset_neg_na[col_number] = [median_number for _ in range(nb_na_neg)]
    #print(dataset_neg_na[col_number])
    df[(df[col_number].isna()) | (df[col_number] < 0)] = dataset_neg_na

# Remplir les valeurs nulles par des valeurs booléennes pour les colonnes booléennes
df[df.select_dtypes(include='boolean').columns] = df.select_dtypes(include='boolean').fillna(False)

# 3ème étape : Création de nouvelles colonnes dérivées + filtrage des données
df["Bénéfice"] = df["MontantTotalAchats"] - df["MontantTotalRemboursé"]
# Enlever ceux qui ont un bénéfice négatif
df_filtrage_benefice = df[df["Bénéfice"] >= 0]
# Enlever ceux qui n'ont pas fait d'achats
df_filtrage_nb_montant = df_filtrage_benefice[
    (df_filtrage_benefice["NombreAchats"] > 0) & (df_filtrage_benefice["MontantTotalAchats"] > 0)
    ] 
df_filtrage_nb_montant["Fidélité"] = pd.cut(df_filtrage_nb_montant["ScoreFidélité"], 
            bins=[0, 20, 40, 60, 80, 100], labels=["Très faible", "Faible", "Moyen", "Fort", "Très fort"], 
            include_lowest=True)

# Renvoyer le CSV modifié
#df_filtrage_nb_montant.to_csv("../data/prepared_data.csv", index=False, header=True, sep=",")
print(df_filtrage_nb_montant.to_csv(index=False, header=True, sep=","))