# features/example.feature
Feature: Expense Calculation

  Scenario: Calculating the average expenses per category
    Given I have the following expenses
      | category   | value |
      | Food       | 100   |
      | Transport  | 200   |
      | Food       | 300   |
    When I calculate the average expenses per category
    Then the average for "Food" should be 200
    And the average for "Transport" should be 200
    And the average for "Utilities" should be 0
