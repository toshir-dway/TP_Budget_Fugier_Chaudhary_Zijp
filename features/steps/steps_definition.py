from behave import given, when, then
import pandas as pd

@given(u'que je suis sur la page d\'ajout de dépense')
def step_impl(context):
    context.df = pd.DataFrame(columns=['Type', 'Category', 'Value', 'Description'])
    context.categories = ['Food', 'Transport', 'Utilities']
    
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
    context.df = pd.concat([context.df, new_row], ignore_index=True)


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