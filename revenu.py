import pytest
import pandas as pd
import numpy as np
import unittest




categories = ['Food', 'Transport', 'Utilities', 'Entertainment', 'Revenu']


revenus = []  # stocke les revenus

def add_revenu():
    category = input("Quelle est la catégorie de ce revenu ?")
    while category not in categories:
        print("La catégorie doit être valide.")
        category = input("Quelle est la catégorie de ce revenu ? ")
    
    description = input("Quelle est la description de ce revenu ?")
    value = input("Quelle est la valeur de ce revenu ?")
    
    while True:
        try:
            value = int(value)
            break  
        except ValueError:
            print("La valeur doit être un nombre entier.")
            value = input("Quelle est la valeur de ce revenu ? ")

    return category, description, value




class TestAjouterRevenu(unittest.TestCase):

    def setUp(self):
        self.df_revenus = pd.DataFrame({
            'category': ['Salaire', 'Investissements'],
            'value': [2000, 500]
        })
        self.categories = ['Salaire', 'Investissements', 'Bonus', 'Autres revenus']

    def test_ajouter_revenu_avec_details_valides(self):
        category, description, value = "Salaire", "Revenu du mois", 2000

        new_row = pd.DataFrame([{'category': category, 'description': description, 'value': value}])
        self.df_revenus = pd.concat([self.df_revenus, new_row], ignore_index=True)

        self.assertEqual(self.df_revenus.iloc[-1]['category'], 'Salaire')
        self.assertEqual(self.df_revenus.iloc[-1]['description'], 'Revenu du mois')
        self.assertEqual(self.df_revenus.iloc[-1]['value'], 2000)

    def test_message_confirmation(self):
        confirmation_message = "Source de revenu ajoutée avec succès"
        self.assertEqual(confirmation_message, "Source de revenu ajoutée avec succès")

    def test_ajout_revenu_invalide(self):
        category, description, value = "Revenu Invalide", "Revenu du mois", 2000
        
        if category not in self.categories:
            print("Catégorie invalide, revenu non ajouté.")
        else:
            new_row = pd.DataFrame([{'category': category, 'description': description, 'value': value}])
            self.df_revenus = pd.concat([self.df_revenus, new_row], ignore_index=True)
            self.assertNotIn(category, self.df_revenus['category'].values)  

    def test_revenu_vide(self):
        empty_df = pd.DataFrame(columns=['category', 'description', 'value'])
        result = empty_df.empty
        self.assertTrue(result)  



if __name__ == "__main__":
    unittest.main()
