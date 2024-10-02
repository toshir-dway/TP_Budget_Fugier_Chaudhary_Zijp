Feature: Calculer le solde total
  En tant qu'utilisateur
  Je veux pouvoir voir mon solde total
  Afin de savoir où j'en suis financièrement

  Scenario: Calculer le solde total avec des dépenses et des revenus
    Given que j'ai ajouté une dépense de "150"
    And j'ai ajouté une source de revenu de "2000"
    When je demande à voir mon solde total
    Then le solde total doit être "1850"