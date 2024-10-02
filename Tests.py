import pytest
import pandas as pd
import numpy as np
import random
import unittest

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define the number of rows
num_rows = 10

# Create random data
categories = ['food', 'house', 'travels']
descriptions = [
    'This is a description of item A.',
    'This is a description of item B.',
    'This is a description of item C.',
    'This item is related to A.',
    'This item is related to B.',
    'This item is related to C.',
    'Additional information for A.',
    'Additional information for B.',
    'Additional information for C.',
    'Generic item description.'
]

# Generate random data for DataFrame
data = {
    'category': [random.choice(categories) for _ in range(num_rows)],
    'description': [random.choice(descriptions) for _ in range(num_rows)],
    'values': np.random.randint(1, 100, size=num_rows)
}

# Create DataFrame
df = pd.DataFrame(data)

print(df)


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

category, description, value = add_expense()
print(category, description, value)

def test_add_expense():
    pass
















# Exemple de fonction existante (avec un bug potentiel)
def calculer_moyenne_depenses(depenses):
    return sum(depenses) / len(depenses)

class TestCalculerMoyenneDepenses(unittest.TestCase):
    
    def test_depenses_avec_valeurs(self):
        # Test avec des dépenses non nulles
        depenses = [100, 200, 300]
        resultat = calculer_moyenne_depenses(depenses)
        self.assertEqual(resultat, 200)

    def test_depenses_vides(self):
        # Test avec une liste vide, doit lever une exception ou retourner 0
        depenses = []
        with self.assertRaises(ZeroDivisionError):
            calculer_moyenne_depenses(depenses)

if __name__ == '__main__':
    unittest.main()






#Corriger la fonction pour passer le test

def calculer_moyenne_depenses(depenses):
    if not depenses:  # Si la liste est vide
        return 0  # On retourne 0 au lieu de lever une erreur
    return sum(depenses) / len(depenses)


#Améliorer les tests

class TestCalculerMoyenneDepenses(unittest.TestCase):
    
    def test_depenses_avec_valeurs(self):
        depenses = [100, 200, 300]
        resultat = calculer_moyenne_depenses(depenses)
        self.assertEqual(resultat, 200)

    def test_depenses_vides(self):
        depenses = []
        resultat = calculer_moyenne_depenses(depenses)
        self.assertEqual(resultat, 0)  # Vérifie que le résultat est 0 pour une liste vide

    def test_depenses_negatives(self):
        depenses = [-50, -150, -100]
        resultat = calculer_moyenne_depenses(depenses)
        self.assertEqual(resultat, -100)

    def test_depenses_avec_zero(self):
        depenses = [0, 0, 0]
        resultat = calculer_moyenne_depenses(depenses)
        self.assertEqual(resultat, 0)

if __name__ == '__main__':
    unittest.main()


#pour lancer le  test
#python -m unittest <nom_du_fichier>.py
