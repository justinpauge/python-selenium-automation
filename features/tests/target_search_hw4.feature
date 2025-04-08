Feature: Update Target search test cases and add Behave variables


##Open Target Circle and verify 10 benefit cells
  Scenario: User can open Target Circle with 10 benefit cells
    Given Open Target Circle page
    When Click on Target Circle icon
    Then Verify 10 or more benefit cells


## Add a Target product to cart And Verify it is there
  Scenario: Add product to cart
    Given Open Target main page
    When Add item to cart
    Then Verify item in cart