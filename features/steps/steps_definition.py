from behave import given, when, then

@given(u'que je suis sur la page d\'ajout de dépense')
def step_impl(context):
    # Code to navigate to the expense addition page
    pass

@when(u'je valide l\'ajout de la dépense')
def step_impl(context):
    # Code to validate adding the expense
    pass

@then(u'la dépense doit être ajoutée à ma liste de dépenses')
def step_impl(context):
    # Code to check if the expense is in the list
    pass

@then(u'le message de confirmation "Dépense ajoutée avec succès" doit s\'afficher')
def step_impl(context):
    # Code to check for the confirmation message
    pass

@given(u'que je suis sur la page d\'ajout de revenu')
def step_impl(context):
    # Code to navigate to the income addition page
    pass

@when(u'je valide l\'ajout de la source de revenu')
def step_impl(context):
    # Code to validate adding the income source
    pass

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
