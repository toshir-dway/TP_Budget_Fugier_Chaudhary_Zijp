
import pandas as pd
import numpy as np
import unittest


# Global variables for categories and DataFrame
categories = ['Food', 'Transport', 'Utilities', 'Entertainment']
df = pd.DataFrame(columns=['Category', 'Description', 'Value', 'Type'])

def add_expense():
    category = input("Quelle est la catégorie de cette dépense ? ")
    while category not in categories:
        print("La valeur doit être une catégorie valide.")
        category = input("Quelle est la catégorie de cette dépense ? ")

    description = input("Quelle est la description de cette dépense ? ")
    value = input("Quelle est la valeur de cette dépense ? ")
    
    # Ensure the value is an integer
    while True:
        try:
            value = int(value)
            break
        except ValueError:
            print("La valeur doit être un nombre entier.")
            value = input("Quelle est la valeur de cette dépense ? ")

    # Return the values to be appended
    return category, description, value

def add_revenue():
    category = 'Revenu'
    description = input("Quelle est la description de ce revenu ? ")
    value = input("Quelle est la valeur de ce revenu ? ")

    # Ensure the value is an integer
    while True:
        try:
            value = int(value)
            break
        except ValueError:
            print("La valeur doit être un nombre entier.")
            value = input("Quelle est la valeur de ce revenu ? ")

    # Return the values to be appended
    return category, description, value

def calculate_total_balance(df):
    # Calculate total revenues and expenses
    expenses = df[df['Type'] == 'expense']['Value'].sum()
    revenues = df[df['Type'] == 'revenue']['Value'].sum()
    
    return revenues - expenses

def calculer_moyenne_depenses_par_categorie(df, categories):
    resultats = {}
    for cat in categories:
        data = df[df['Category'] == cat]
        depenses = data['Value'].to_list()
        if len(depenses) == 0:
            resultats[cat] = 0
        else:
            resultats[cat] = sum(depenses) / len(depenses)

    return resultats

if __name__ == '__main__':
    unittest.main()

