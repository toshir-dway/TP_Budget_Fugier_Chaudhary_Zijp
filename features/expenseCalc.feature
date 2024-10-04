# features/example.feature
Feature: Expense Calculation

  Scenario: Calculating the average expenses per category
    Given I have the following expenses
      | Category   | value | Type    | Description |
      | Food       | 100   | Expense | mcdo        |
      | Transport  | 200   | Expense | pizza       |
      | Food       | 300   | Expense | chiken      |
    When I calculate the average expenses per category
    Then the average for "Food" should be 200
    And the average for "Transport" should be 200
    And the average for "Utilities" should be 0
