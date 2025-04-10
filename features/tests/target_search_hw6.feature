


Scenario: "Your cart is empty" message is shown for empty cart
  Given Open target.com
  When Open cart page
  Then Verify 'Your car is empty' message is shown