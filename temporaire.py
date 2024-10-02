import pandas as pd




def add_expense(categories):
    category = input("Quelle est la categorie de cette depense ?")
    while category not in categories:
        print("La valeur doit être une categorie valide.")
        category = input("Quelle est la catégorie de cette dépense ? ")
    
    description = input("Quelle est la description de cette depense ?")
    value = input("Quelle est la valeur de cette depense ?")
    while True:
            try:
                value = -abs(int(value))
                break  # Exit the loop if the conversion is successful
            except ValueError:
                print("La valeur doit être un nombre entier.")
                value = input("Quelle est la valeur de cette dépense ? ")

    return category, description, value


def test_add_expense():
    pass


def accueil(categories, df):
    while True:  # Create a loop to allow repeated menu access
        print("Ajouter une dépense : 1")
        print("Ajouter un revenu : 2")
        print("Calculer le solde total : 3")
        print("Calculer la répartition par catégories : 4")
        print("Quitter : q")  # Option to exit the loop
        fonctionnalite = input("Choisissez une option: ")

        if fonctionnalite == "1":
            category, description, value = add_expense(categories)
            # Create a new row as a dictionary
            new_row = pd.DataFrame({'Category': [category], 'Description': [description], 'Value': [value], 'Type': ['expense']})
            # Append the new row to the DataFrame
            df = pd.concat([df, new_row], ignore_index=True)
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

df=pd.DataFrame(data=None, columns=['Type', 'Category', 'Value', 'Description'])
categories = ['Food', 'Transport', 'Utilities', 'Entertainment']


# Call the accueil function to run the menu
accueil(categories, df)
