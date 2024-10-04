import pytest
import pandas as pd
import numpy as np
import unittest


categories = []
df = pd.DataFrame()

def calculer_moyenne_depenses_par_categorie(df, categories):
    resultats = {}
    for cat in categories:
        data = df[df['category'] == cat]
        depenses = data['value'].to_list()
        if len(depenses) == 0:
            resultats[cat] = 0
        else:
            resultats[cat] = sum(depenses) / len(depenses)

    return resultats


class TestCalculerMoyenneDepenses(unittest.TestCase):

    def setUp(self):
        # Créer un DataFrame d'exemple
        self.df = pd.DataFrame({
            'category': ['Food', 'Transport', 'Food', 'Utilities'],
            'value': [100, 200, 300, 400]
        })
        self.categories = ['Food', 'Transport', 'Utilities', 'Entertainment']
    
    def test_depenses_avec_categorie(self):
        # Test avec des dépenses existantes
        resultats = calculer_moyenne_depenses_par_categorie(self.df, self.categories)
        self.assertEqual(resultats['Food'], 200.0)  # (100 + 300) / 2
        self.assertEqual(resultats['Transport'], 200.0)  # valeur unique 200
        self.assertEqual(resultats['Utilities'], 400.0)  # valeur unique 400

    def test_depenses_sans_categorie(self):
        # Test avec une catégorie sans dépenses
        resultats = calculer_moyenne_depenses_par_categorie(self.df, self.categories)
        self.assertEqual(resultats['Entertainment'], 0)  # Pas de dépenses pour 'Entertainment'

    def test_depenses_vide(self):
        # Test avec un DataFrame vide
        empty_df = pd.DataFrame(columns=['category', 'value'])
        resultats = calculer_moyenne_depenses_par_categorie(empty_df, self.categories)
        self.assertEqual(resultats['Food'], 0)  # Pas de dépenses pour 'Food'
        self.assertEqual(resultats['Transport'], 0)  # Pas de dépenses pour 'Transport'

if __name__ == '__main__':
    unittest.main()

#python -m unittest Tests.py





def add_expense():
    category = input("Quelle est la categorie de cette depense ?")
    while category not in categories:
        print("La valeur doit être une categorie valide.")
        category = input("Quelle est la catégorie de cette dépense ? ")
    
    description = input("Quelle est la description de cette depense ?")
    value = input("Quelle est la valeur de cette depense ?")
    while True:
            try:
                value = int(value)
                break  # Exit the loop if the conversion is successful
            except ValueError:
                print("La valeur doit être un nombre entier.")
                value = input("Quelle est la valeur de cette dépense ? ")

    return category, description, value


def test_add_expense():
    pass


def accueil():
    while True:  # Create a loop to allow repeated menu access
        print("Ajouter une dépense : 1")
        print("Ajouter un revenu : 2")
        print("Calculer le solde total : 3")
        print("Calculer la répartition par catégories : 4")
        print("Quitter : q")  # Option to exit the loop
        fonctionnalite = input("Choisissez une option: ")

        if fonctionnalite == "1":
            category, description, value = add_expense()
            # Create a new row as a dictionary
            new_row = {'Category': category, 'Description': description, 'Value': value, 'Type': 'expense'}
            # Append the new row to the DataFrame
            df = df.append(new_row, ignore_index=True)
            print("Dépense ajoutée avec succès.")
            print(df)  # Display the updated DataFrame

        elif fonctionnalite == "2":
            # Fonction ajouter un revenu
            print("Ajout d'un revenu...")
            # Call the function to add a revenu here
        elif fonctionnalite == "3":
            # Fonction calculer le solde total
            print("Calcul du solde total...")
            # Call the function to calculate the total balance here
        elif fonctionnalite == "4":
            # Fonction calculer la répartition par catégories
            print("Calcul de la répartition par catégories...")
            # Call the function to calculate the category breakdown here
        elif fonctionnalite.lower() == "q":  # Allow user to quit
            print("Au revoir!")
            break  # Exit the loop
        else:
            print("Option invalide, veuillez réessayer.")

# Call the accueil function to run the menu
accueil()
