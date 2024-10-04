Feature: Ajouter une dépense
  En tant qu'utilisateur
  Je veux pouvoir ajouter une dépense
  Afin de suivre mes dépenses

  Scenario: Ajouter une dépense avec des détails valides
    Given que je suis sur la page d'ajout de dépense
    When je saisis "Alimentation" comme catégorie
    And je saisis "Food" comme description
    And je saisis "150" comme montant
    And je valide l'ajout de la dépense
    Then la dépense doit être ajoutée à ma liste de dépenses
    And le message de confirmation "Dépense ajoutée avec succès" doit s'afficher