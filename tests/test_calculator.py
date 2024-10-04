import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
import unittest
from app import ExpenseManager 
from unittest.mock import patch

class TestExpenseManager(unittest.TestCase):

    def setUp(self):
        """Set up an ExpenseManager instance for testing."""
        self.manager = ExpenseManager()
        
        # Add MOCK
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
        self.assertNotIn('Entertainment', summary['Category'].values)

    def test_empty_expenses(self):
        """Test with an empty DataFrame."""
        empty_manager = ExpenseManager() 
        empty_summary = empty_manager.get_summary()
        self.assertTrue(empty_summary.empty)  

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
        self.assertEqual(self.manager.df.iloc[-1]['Value'], 500)  

    # invalid expense
    def test_invalid_expense(self):
        """Test that invalid expenses are not added."""
        initial_count = len(self.manager.df)
        with self.assertRaises(ValueError):
            self.manager.add_expense('Food', 'invalid', 'Snacks')  
        self.assertEqual(len(self.manager.df), initial_count)

    # invalid revenue
    def test_invalid_revenue(self):
        """Test that invalid revenues are not added."""
        initial_count = len(self.manager.df)
        with self.assertRaises(ValueError):
            self.manager.add_revenue('Revenu', 'invalid', 'Bonus')  
        self.assertEqual(len(self.manager.df), initial_count)

    # negative revenue
    def test_negative_revenue(self):
        """Test that negative revenues are not allowed."""
        initial_count = len(self.manager.df)
        with self.assertRaises(ValueError):
            self.manager.add_revenue('Revenu', -500, 'Salary')  
        self.assertEqual(len(self.manager.df), initial_count)

    # empty description
    def test_empty_description(self):
        """Test adding an expense with an empty description."""
        initial_count = len(self.manager.df)
        self.manager.add_expense('Food', 50, '') 
        self.assertEqual(self.manager.df.iloc[-1]['Description'], '')  
        self.assertEqual(len(self.manager.df), initial_count + 1)

    # invalid category
    def test_invalid_category(self):
        """Test adding an expense with a non-existing category."""
        initial_count = len(self.manager.df)
        with self.assertRaises(ValueError):
            self.manager.add_expense('InvalidCategory', 100, 'Test')  
        self.assertEqual(len(self.manager.df), initial_count)

    # adding an expense with zero value
    def test_zero_value_expense(self):
        """Test adding an expense with a value of zero."""
        initial_count = len(self.manager.df)
        self.manager.add_expense('Food', 0, 'Free meal') 
        self.assertEqual(self.manager.df.iloc[-1]['Value'], 0)
        self.assertEqual(len(self.manager.df), initial_count + 1)


class TestExpenseManagerInteractive(unittest.TestCase):
    def setUp(self):
        self.manager = ExpenseManager()

    @patch('builtins.input', side_effect=['Food', 'Test Description', '100'])
    def test_add_expense_interactively_valid(self, mock_input):
        """Test adding a valid expense interactively."""
        initial_count = len(self.manager.df)
        self.manager.add_expense_interactively()
        self.assertEqual(len(self.manager.df), initial_count + 1)
        self.assertEqual(self.manager.df.iloc[-1]['Category'], 'Food')
        self.assertEqual(self.manager.df.iloc[-1]['Value'], -100)
        self.assertEqual(self.manager.df.iloc[-1]['Description'], 'Test Description')

    @patch('builtins.input', side_effect=['InvalidCategory', 'Food', 'Test Description', '100'])
    def test_add_expense_interactively_invalid_category(self, mock_input):
        """Test re-prompting for a valid category."""
        result = self.manager.add_expense_interactively()  # Call the method
        self.assertFalse(result)  # Check if the method returned False due to invalid category
        self.assertEqual(len(self.manager.df), 0)

    @patch('builtins.input', side_effect=['Food', 'Test Description', 'invalid_value'])
    def test_add_expense_interactively_invalid_value(self, mock_input):
        """Test re-prompting for a valid integer value."""
        result = self.manager.add_expense_interactively()  # Call the method
        self.assertFalse(result) 
        self.assertEqual(len(self.manager.df), 0)


if __name__ == '__main__':
    unittest.main()
