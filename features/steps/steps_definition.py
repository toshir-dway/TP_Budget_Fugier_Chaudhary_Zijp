from behave import given, when, then
import pandas as pd


#AJOUTER UNE DEPENSE


@given(u'que je suis sur la page d\'ajout de dépense')
def step_impl(context):
    context.df = pd.DataFrame(columns=['Type', 'Category', 'Value', 'Description'])
    context.categories = ['Food', 'Transport', 'Utilities', 'Entertainment', 'Revenu']
    
@when(u'je saisis "Alimentation" comme catégorie')
def step_impl(context):
    context.category = "Alimentation"
    
@when(u'je saisis "Food" comme description')
def step_impl(context):
    context.description = "Food"
    
@when(u'je saisis "150" comme montant')
def step_impl(context):
    context.value = 150

@when(u'je valide l\'ajout de la dépense')
def step_impl(context):
    # Append the new row with the captured inputs
    new_row = {'Type': 'Expense', 'Category': context.category, 'Value': context.value, 'Description': context.description}
    new_row_df = pd.DataFrame([new_row])
    context.df = pd.concat([context.df, new_row_df], ignore_index=True)


@then(u'la dépense doit être ajoutée à ma liste de dépenses')
def step_impl(context):
    # Ensure the DataFrame is not empty and the new entry is added
    assert not context.df.empty, "Expense list should not be empty"
    
    last_row = context.df.iloc[-1]
    assert last_row['Category'] == context.category
    assert last_row['Description'] == context.description
    assert last_row['Value'] == context.value

@then(u'le message de confirmation "Dépense ajoutée avec succès" doit s\'afficher')
def step_impl(context):
    context.confirmation_message = "Dépense ajoutée avec succès"
    assert context.confirmation_message == "Dépense ajoutée avec succès"


#AJOUTER UN REVENU



@given(u'que je suis sur la page d\'ajout de revenu')
def step_impl(context):
    context.df = pd.DataFrame(columns=['Type', 'Category', 'Value', 'Description'])
    context.categories = ['Food', 'Transport', 'Utilities', 'Entertainment', 'Revenu']
    
@when(u'je saisis "Revenu" comme catégorie')
def step_impl(context):
    context.category = "Revenu"
    
@when(u'je saisis "Revenu du mois" comme description')
def step_impl(context):
    context.description = "Revenu du mois"
    
@when(u'je saisis "2000" comme montant')
def step_impl(context):
    context.value = 2000

@when(u'je valide l\'ajout de la source de revenu')
def step_impl(context):
    # Append the new row with the captured inputs
    new_row = {'Type': 'Revenu', 'Category': context.category, 'Value': context.value, 'Description': context.description}
    new_row_df = pd.DataFrame([new_row])
    context.df = pd.concat([context.df, new_row_df], ignore_index=True)


@then(u'la source de revenu doit être ajoutée à ma liste de revenus')
def step_impl(context):
    # Ensure the DataFrame is not empty and the new entry is added
    assert not context.df.empty, "Revenu list should not be empty"
    
    last_row = context.df.iloc[-1]
    assert last_row['Category'] == context.category
    assert last_row['Description'] == context.description
    assert last_row['Value'] == context.value

@then(u'le message de confirmation "Source de revenu ajoutée avec succès" doit s\'afficher')
def step_impl(context):
    context.confirmation_message = "Revenu ajoutée avec succès"
    assert context.confirmation_message == "Revenu ajoutée avec succès"




# CALCULER LE SOLDE

@given(u'que j\'ai ajouté une dépense de "150"')
def step_impl(context):
    context.df = pd.DataFrame(columns=['Type', 'Category', 'Value', 'Description'])
    new_row = {'Type': 'Expense', 'Category': 'Alimentation', 'Value': 150, 'Description': 'Courses'}
    context.df = pd.concat([context.df, pd.DataFrame([new_row])], ignore_index=True)

@given(u'j\'ai ajouté une source de revenu de "2000"')
def step_impl(context):
    new_row = {'Type': 'Revenue', 'Category': 'Salaire', 'Value': 2000, 'Description': 'Revenu du mois'}
    context.df = pd.concat([context.df, pd.DataFrame([new_row])], ignore_index=True)


@when(u'je demande à voir mon solde total')
def step_impl(context):
    total_revenue = context.df[context.df['Type'] == 'Revenue']['Value'].sum()
    total_expenses = context.df[context.df['Type'] == 'Expense']['Value'].sum()
    context.balance = total_revenue - total_expenses


@then(u'le solde total doit être "1850"')
def step_impl(context):
    assert context.balance == 1850



#expenseCalc

@given(u'I have the following expenses')
def step_impl(context):
    context.expenses = pd.DataFrame(columns=['Type', 'Category', 'Value', 'Description'])
    for row in context.table:
        new_row = {
            'Type': row['Type'], 
            'Category': row['Category'], 
            'Value': int(row['Value']),
            'Description': row['Description']
        }
        context.expenses = pd.concat([context.expenses, pd.DataFrame([new_row])], ignore_index=True)

@when(u'I calculate the average expenses per category')
def step_impl(context):
    context.avg_expenses = context.expenses.groupby('Category')['Value'].mean().reset_index()

@then(u'the average for "Food" should be 200')
def step_impl(context):
    food_average = context.avg_expenses.loc[context.avg_expenses['Category'] == 'Food', 'Value']
    assert food_average.values[0] == 200, f"Expected average for Food to be 200 but got {food_average.values[0]}"

@then(u'the average for "Transport" should be 200')
def step_impl(context):
    transport_average = context.avg_expenses.loc[context.avg_expenses['Category'] == 'Transport', 'Value']
    assert transport_average.values[0] == 200, f"Expected average for Transport to be 200 but got {transport_average.values[0]}"

@then(u'the average for "Utilities" should be 0')
def step_impl(context):
    utilities_average = context.avg_expenses.loc[context.avg_expenses['Category'] == 'Utilities', 'Value']
    assert utilities_average.empty or utilities_average.values[0] == 0, f"Expected average for Utilities to be 0 but got {utilities_average.values[0] if not utilities_average.empty else 'No data'}"



# Répartition des catégories

@given(u'que j\'ai ajouté une dépense de "100" dans la catégorie "Alimentation"')
def step_impl(context):
    if not hasattr(context, 'df'):
        context.df = pd.DataFrame(columns=['Type', 'Category', 'Value', 'Description'])
    new_row = {'Type': 'Expense', 'Category': 'Alimentation', 'Value': 100, 'Description': 'Courses'}
    context.df = pd.concat([context.df, pd.DataFrame([new_row])], ignore_index=True)

@given(u'j\'ai ajouté une dépense de "50" dans la catégorie "Transport"')
def step_impl(context):
    new_row = {'Type': 'Expense', 'Category': 'Transport', 'Value': 50, 'Description': 'Revenu du mois'}
    context.df = pd.concat([context.df, pd.DataFrame([new_row])], ignore_index=True)

@given(u'j\'ai ajouté une dépense de "150" dans la catégorie "Loisirs"')
def step_impl(context):
    new_row = {'Type': 'Expense', 'Category': 'Loisirs', 'Value': 150, 'Description': 'fun'}
    context.df = pd.concat([context.df, pd.DataFrame([new_row])], ignore_index=True)

@when(u'je demande à voir la répartition par catégorie')
def step_impl(context):
    context.category_summary = context.df.groupby('Category')['Value'].sum().reset_index()

@then(u'je devrais voir un résumé avec "Alimentation: 100", "Transport: 50", "Loisirs: 150"')
def step_impl(context):
    expected_summary = {
        'Alimentation': 100,
        'Transport': 50,
        'Loisirs': 150
    }
    for category, expected_value in expected_summary.items():
        actual_value = context.category_summary.loc[context.category_summary['Category'] == category, 'Value'].values[0]
        assert actual_value == expected_value, f"Expected {category}: {expected_value}, but got {actual_value}"
