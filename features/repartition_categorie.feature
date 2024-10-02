Feature: Calculer la répartition par catégorie
  En tant qu'utilisateur
  Je veux pouvoir voir un résumé de mes dépenses par catégorie
  Afin de mieux gérer mes finances

  Scenario: Voir la répartition des dépenses par catégorie
    Given que j'ai ajouté une dépense de "100" dans la catégorie "Alimentation"
    And j'ai ajouté une dépense de "50" dans la catégorie "Transport"
    And j'ai ajouté une dépense de "150" dans la catégorie "Loisirs"
    When je demande à voir la répartition par catégorie
    Then je devrais voir un résumé avec "Alimentation: 100", "Transport: 50", "Loisirs: 150"