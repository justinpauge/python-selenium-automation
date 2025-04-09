Feature: Update Target search test cases and add Behave variables


##Search for color of product, click each color, verify color selected
  Scenario: Add product to cart
    Given Open target main page
    When Search for coffee
    When Add item to cart

#    Given Open target main page
#    When Search for {coffee}
#    When Add item to cart
#    Then Verify coffee in cart