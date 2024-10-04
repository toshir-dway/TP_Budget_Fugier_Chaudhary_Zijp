import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
import unittest
from app import ExpenseManager  # Make sure to import your ExpenseManager class


class TestExpenseManager(unittest.TestCase):

    def setUp(self):
        """Set up an ExpenseManager instance for testing."""
        self.manager = ExpenseManager()
        
        # Add example expenses directly to the manager's DataFrame for testing
        self.manager.df = pd.DataFrame({
            'Category': ['Food', 'Transport', 'Food', 'Utilities'],
            'Value': [-100, -200, -300, -400],
            'Type': ['expense', 'expense', 'expense', 'expense'],
            'Description': ['Groceries', 'Bus fare', 'Dinner', 'Electricity bill']
        })

    def test_average_expenses_with_categories(self):
        """Test with existing expenses."""
        expected_avg_food = (-100 - 300) / 2  
        expected_avg_transport = -200 
        expected_avg_utilities = -400 
        
        summary = self.manager.calculate_average_expenses()
       
        self.assertAlmostEqual(summary.loc[summary['Category'] == 'Food', 'Value'].values[0], expected_avg_food)
        self.assertAlmostEqual(summary.loc[summary['Category'] == 'Transport', 'Value'].values[0], expected_avg_transport)
        self.assertAlmostEqual(summary.loc[summary['Category'] == 'Utilities', 'Value'].values[0], expected_avg_utilities)

    def test_expenses_without_category(self):
        """Test with a category that has no expenses."""
        summary = self.manager.get_summary()
        # Ensure 'Entertainment' is not in summary
        self.assertNotIn('Entertainment', summary['Category'].values)

    def test_empty_expenses(self):
        """Test with an empty DataFrame."""
        empty_manager = ExpenseManager()  # A new instance
        empty_summary = empty_manager.get_summary()
        self.assertTrue(empty_summary.empty)  # Check if summary is empty

    def test_add_expense(self):
        """Test adding an expense."""
        initial_count = len(self.manager.df)
        self.manager.add_expense('Food', 150, 'Snacks')
        self.assertEqual(len(self.manager.df), initial_count + 1)
        self.assertEqual(self.manager.df.iloc[-1]['Category'], 'Food')
        self.assertEqual(self.manager.df.iloc[-1]['Value'], -150)
        self.assertEqual(self.manager.df.iloc[-1]['Description'], 'Snacks')

    def test_add_revenue(self):
        """Test adding a revenue."""
        initial_count = len(self.manager.df)
        self.manager.add_revenue('Revenu', 500, 'Salary')
        self.assertEqual(len(self.manager.df), initial_count + 1)
        self.assertEqual(self.manager.df.iloc[-1]['Category'], 'Revenu')
        self.assertEqual(self.manager.df.iloc[-1]['Value'], 500)  # Should be positive for revenue

if __name__ == '__main__':
    unittest.main()
