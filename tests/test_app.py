import pytest
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from app import ExpenseManager

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
# from src.app import ExpenseManager

@pytest.fixture
def manager():
    return ExpenseManager()

def test_add_expense(manager):
    manager.add_expense("Food", 100, "Lunch")
    assert len(manager.df) == 1  # One expense should be added
    assert manager.df.iloc[0]['Category'] == "Food"
    assert manager.df.iloc[0]['Value'] == -100  # Expense should be negative
    assert manager.df.iloc[0]['Description'] == "Lunch"

def test_add_invalid_expense(manager):
    with pytest.raises(ValueError):
        manager.add_expense("InvalidCategory", 100, "Lunch")
    
    
    with pytest.raises(ValueError):
        manager.add_expense("Food", "abc", "Lunch")

def test_add_revenue(manager):
    manager.add_revenue("Revenu", 500, "Salary")
    assert len(manager.df) == 1  # One revenue should be added
    assert manager.df.iloc[0]['Category'] == "Revenu"
    assert manager.df.iloc[0]['Value'] == 500  # Revenue should be positive
    assert manager.df.iloc[0]['Description'] == "Salary"

def test_invalid_revenue(manager):
    with pytest.raises(ValueError):
        manager.add_revenue("Revenu", -500, "Invalid Salary")

def test_calculate_average_expenses(manager):
    # Add expenses and revenues
    manager.add_expense("Food", 100, "Lunch")
    manager.add_expense("Transport", 50, "Bus ticket")
    manager.add_revenue("Revenu", 500, "Salary")
    
    # Calculate total balance
    total = manager.df['Value'].sum()
    assert total == 350  # 500 (Revenue) - 150 (Expenses)

def test_get_summary(manager):
    # Add  expenses
    manager.add_expense("Food", 100, "Lunch")
    manager.add_expense("Transport", 50, "Bus ticket")
    

    summary = manager.get_summary()
    assert summary.loc[summary['Category'] == 'Food', 'Value'].values[0] == -100
    assert summary.loc[summary['Category'] == 'Transport', 'Value'].values[0] == -50

def test_add_expense_interactively(monkeypatch, manager):
    inputs = iter(["Food", "Dinner", "200"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    manager.add_expense_interactively()

    assert len(manager.df) == 1
    assert manager.df.iloc[0]['Category'] == "Food"
    assert manager.df.iloc[0]['Value'] == -200
    assert manager.df.iloc[0]['Description'] == "Dinner"

def test_add_revenue_interactively(monkeypatch, manager):
    inputs = iter(["Salary", "1000"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    manager.add_revenue_interactively()

    assert len(manager.df) == 1
    assert manager.df.iloc[0]['Category'] == "Revenu"
    assert manager.df.iloc[0]['Value'] == 1000
    assert manager.df.iloc[0]['Description'] == "Salary"
