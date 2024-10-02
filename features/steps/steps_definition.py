from behave import given, when, then

class FinancialApp:
    def __init__(self):
        self.expenses = []
        self.incomes = []

    def add_expense(self, category, description, amount):
        self.expenses.append({'category': category, 'description': description, 'amount': amount})

    def add_income(self, category, description, amount):
        self.incomes.append({'category': category, 'description': description, 'amount': amount})

    def total_balance(self):
        total_expenses = sum(exp['amount'] for exp in self.expenses)
        total_incomes = sum(inc['amount'] for inc in self.incomes)
        return total_incomes - total_expenses

    def expense_summary_by_category(self):
        summary = {}
        for expense in self.expenses:
            summary[expense['category']] = summary.get(expense['category'], 0) + expense['amount']
        return summary

app = FinancialApp()

@given("que je suis sur la page d'ajout de dépense")
def step_impl(context):
    pass  # No action needed for this step

@when('je saisis "{category}" comme catégorie')
def step_impl(context, category):
    context.category = category

@when('je saisis "{description}" comme description')
def step_impl(context, description):
    context.description = description

@when('je saisis "{amount}" comme montant')
def step_impl(context, amount):
    context.amount = float(amount)

@when('je valide l\'ajout de la dépense')
def step_impl(context):
    app.add_expense(context.category, context.description, context.amount)

@then('la dépense doit être ajoutée à ma liste de dépenses')
def step_impl(context):
    assert any(exp['description'] == context.description for exp in app.expenses)

@then('le solde total doit être "{expected_balance}"')
def step_impl(context, expected_balance):
    assert app.total_balance() == float(expected_balance)
