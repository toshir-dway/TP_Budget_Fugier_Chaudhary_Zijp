Feature: Ajouter une source de revenu
  En tant qu'utilisateur
  Je veux pouvoir ajouter une source de revenu
  Afin de suivre mes revenus

  Scenario: Ajouter une source de revenu avec des détails valides
    Given que je suis sur la page d'ajout de revenu
    When je saisis "Salaire" comme catégorie
    And je saisis "Salaire du mois" comme description
    And je saisis "2000" comme montant
    And je valide l'ajout de la source de revenu
    Then la source de revenu doit être ajoutée à ma liste de revenus
    And le message de confirmation "Source de revenu ajoutée avec succès" doit s'afficher