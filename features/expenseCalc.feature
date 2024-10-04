# features/example.feature
Feature: Expense Calculation

  Scenario: Calculating the average expenses per category
    Given I have the following expenses
      | category   | value | Type
      | Food       | 100   | Expense
      | Transport  | 200   | Expense
      | Food       | 300   | Expense
    When I calculate the average expenses per category
    Then the average for "Food" should be 200
    And the average for "Transport" should be 200
    And the average for "Utilities" should be 0
