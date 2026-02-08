Feature: Update Target search test cases and add Behave variables


##Search for color of product, click each color, verify color selected
  Scenario: Add product to cart
    Given Open target product {x-ray-men-s-cable-knit-cowl-neck-sweater/-/A-1001689658} page
    Then Click through colors and verify selection
