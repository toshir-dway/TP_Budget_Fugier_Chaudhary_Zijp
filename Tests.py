import pytest
import pandas as pd
import numpy as np
import random

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

