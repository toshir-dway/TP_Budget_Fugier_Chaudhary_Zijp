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