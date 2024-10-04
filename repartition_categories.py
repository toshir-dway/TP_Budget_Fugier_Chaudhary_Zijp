import unittest
import pandas as pd


class ExpenseManager:
    def __init__(self):
        self.df = pd.DataFrame(columns=['Category', 'Value', 'Type', 'Description'])

    def add_expense(self, category, value, Type, Description):
        new_row = {'Category': category, 'Value': int(value), 'Type': Type, 'Description': Description}
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)

    def get_summary(self):
        return self.df.groupby('Category')['Value'].sum().reset_index()

class TestExpenseManager(unittest.TestCase):

    def setUp(self):
        """Set up a fresh ExpenseManager instance for each test."""
        self.manager = ExpenseManager()

    def test_summary_with_expenses(self):
        """Test the summary when multiple expenses are added."""
        # Adding expenses
        self.manager.add_expense('Alimentation', 100, 'Expense', 'Courses')
        self.manager.add_expense('Transport', 50, 'Expense', 'Bus ticket')
        self.manager.add_expense('Loisirs', 150, 'Expense', 'Cinema ticket')

        # Calculating the summary
        summary = self.manager.get_summary()

        # Expected results
        expected_summary = {
            'Alimentation': 100,
            'Transport': 50,
            'Loisirs': 150
        }

        actual_summary = dict(zip(summary['Category'], summary['Value']))

        self.assertEqual(actual_summary, expected_summary)

    def test_summary_with_no_expenses(self):
        """Test that summary is empty when no expenses are added."""
        summary = self.manager.get_summary()
        self.assertTrue(summary.empty, "Expected summary to be empty when no expenses are added.")

    def test_summary_with_single_expense(self):
        """Test the summary with a single expense."""
        # Adding a single expense
        self.manager.add_expense('Utilities', 0, 'Expense', 'Electricity bill')
        
        # Calculating the summary
        summary = self.manager.get_summary()

        expected_summary = {
            'Utilities': 0
        }

        actual_summary = dict(zip(summary['Category'], summary['Value']))

        self.assertEqual(actual_summary, expected_summary)

if __name__ == '__main__':
    unittest.main()
