import pytest
import pandas as pd
import numpy as np
import random
import unittest





def calculer_moyenne_depenses_par_categorie(df, categories):
    resultats = {}
    for cat in categories:
        data = df[df['category'] == cat]
        depenses = data['value'].to_list()
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

#python -m unittest <nom_du_fichier>.py





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



