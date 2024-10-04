
import pandas as pd

class ExpenseManager:
    def __init__(self):
        # Initialize an empty DataFrame to store expenses
        self.df = pd.DataFrame(columns=['Category', 'Value', 'Type', 'Description'])
        self.categories = ['Food', 'Transport', 'Utilities', 'Entertainment', 'Revenu']

    def add_expense(self, category, value, description):
        if category not in self.categories:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {', '.join(self.categories)}")
        try:
            value = float(value)
        except ValueError:
            raise ValueError(f"Invalid value: {value}. The value must be a number.")

        new_row = {'Category': category, 'Value': -abs(value), 'Type': 'expense', 'Description': description}
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
    
    def add_revenue(self, category, value, description):
        if category not in self.categories:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {', '.join(self.categories)}")
        
        try:
            value = float(value)
        except ValueError:
            raise ValueError(f"Invalid value: {value}. The value must be a number.")

        if value < 0:
            raise ValueError("Revenue cannot be negative.")
    
        new_row = {'Category': category, 'Value': value, 'Type': 'Revenu', 'Description': description}
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)

    def calculate_average_expenses(self):
        # Calculate the average expenses per category
        averages = self.df.groupby('Category')['Value'].mean().reset_index()
        return averages

    def get_summary(self):
        # Get a summary of expenses by category
        summary = self.df.groupby('Category')['Value'].sum().reset_index()
        return summary

    def add_expense_interactively(self):
        category = input("Quelle est la categorie de cette depense ? 'Food', 'Transport', 'Utilities', 'Entertainment', 'Revenu' ")
        while category not in self.categories:
            print("La valeur doit être une categorie valide.")
            category = input("Quelle est la catégorie de cette dépense ? 'Food', 'Transport', 'Utilities', 'Entertainment', 'Revenu'")

        description = input("Quelle est la description de cette depense ? ")
        value = input("Quelle est la valeur de cette depense ? ")
        while True:
            try:
                value = int(value)
                break  # Exit the loop if the conversion is successful
            except ValueError:
                print("La valeur doit être un nombre entier.")
                value = input("Quelle est la valeur de cette dépense ? ")

        self.add_expense(category, value, description)
        print("Dépense ajoutée avec succès.")

    def add_revenue_interactively(self):
        category = "Revenu"
        description = input("Quelle est la description de ce revenu ? ")
        value = input("Quelle est la valeur de ce revenu ? ")

        while True:
            try:
                value = int(value)
                break  # Exit the loop if the conversion is successful
            except ValueError:
                print("La valeur doit être un nombre entier.")
                value = input("Quelle est la valeur de ce revenu ? ")

        self.add_revenue(category, value, description)
        print("Revenu ajouté avec succès.")

    def accueil(self):
        while True:
            print("\nMenu:")
            print("1: Ajouter une dépense")
            print("2: Ajouter un revenu")
            print("3: Calculer le solde total")
            print("4: Calculer la répartition par catégories")
            print("5: Quitter")
            choice = input("Choisissez une option: ")

            if choice == "1":
                self.add_expense_interactively()
                print(self.df)  # Display the updated DataFrame
            
            if choice == "2":
                self.add_revenue_interactively()
                print(self.df)  # Display the updated DataFrame

            elif choice == "3":
                # Calculate total balance
                print("Calcul du solde total...")
                total = self.df['Value'].sum()
                print(f"Le solde total est: {total}")

            elif choice == "4":
                # Calculate expenses summary by category
                print("Calcul de la répartition par catégories...")
                summary = self.get_summary()
                print(summary)

            elif choice.lower() == "5":
                print("Au revoir!")
                break  # Exit the loop

            else:
                print("Option invalide, veuillez réessayer.")

if __name__ == '__main__':
    expense_manager = ExpenseManager()
    expense_manager.accueil()

    


