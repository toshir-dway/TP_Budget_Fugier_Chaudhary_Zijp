import pandas as pd
import numpy as np
import unittest
from app import *


class TestCalculerMoyenneDepenses(unittest.TestCase):

    def setUp(self):
        # Créer un DataFrame d'exemple
        self.df = pd.DataFrame({
            'category': ['Food', 'Transport', 'Food', 'Utilities'],
            'value': [100, 200, 300, 400]
        })
        self.categories = ['Food', 'Transport', 'Utilities', 'Entertainment', 'Revenu']
    
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

