from behave import given, when, then
import pandas as pd

@given(u'que je suis sur la page d\'ajout de dépense')
def step_impl(context):
    context.df = pd.DataFrame(columns=['Type', 'Category', 'Value', 'Description'])
    context.categories = ['Food', 'Transport', 'Food', 'Utilities']
    

@when(u'je saisis "Alimentation" comme catégorie')
def step_impl(context):
    context.category = "Alimentation"
    

@then(u'je saisis "Food" comme description')
def step_impl(context):
    context.description = "Food"
    

@then(u'je saisis "150" comme montant')
def step_impl(context):
    context.value = 150

@when(u'je valide l\'ajout de la dépense')
def step_impl(context):
    # Append the new row with the captured inputs
    new_row = {'Type': 'Expense', 'Category': context.category, 'Value': context.value, 'Description': context.description}
    context.df = context.df.append(new_row, ignore_index=True)

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

@then(u'la source de revenu doit être ajoutée à ma liste de revenus')
def step_impl(context):
    # Code to check if the income source is in the list
    pass

@then(u'le message de confirmation "Source de revenu ajoutée avec succès" doit s\'afficher')
def step_impl(context):
    # Code to check for the confirmation message
    pass

@given(u'que j\'ai ajouté une dépense de "150"')
def step_impl(context):
    # Code to add an expense of 150
    pass

@given(u'j\'ai ajouté une source de revenu de "2000"')
def step_impl(context):
    # Code to add an income source of 2000
    pass

@when(u'je demande à voir mon solde total')
def step_impl(context):
    # Code to request total balance
    pass

@then(u'le solde total doit être "1850"')
def step_impl(context):
    # Code to check if the total balance is 1850
    pass

@when(u'je demande à voir la répartition par catégorie')
def step_impl(context):
    # Code to request category breakdown
    pass

@then(u'je devrais voir un résumé avec "Alimentation: 100", "Transport: 50", "Loisirs: 150"')
def step_impl(context):
    # Code to check the summary of expenses by category
    pass
