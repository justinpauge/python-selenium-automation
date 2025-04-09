Feature: Update Target search test cases and add Behave variables


##Open Target Circle and verify 10 benefit cells
  Scenario: User can open Target Circle with 10 benefit cells
    Given Open Target circle page
    Then Verify 10 or more benefit cells


## Add a Target product to cart And Verify it is there
  Scenario: Add product to cart
    Given Open target main page
    When Search for coffee
    When Add item to cart
    Then Verify coffee in cart