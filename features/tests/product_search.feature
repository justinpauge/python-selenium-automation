Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input 'Car' into Search field
    And Click on Search link
    Then Product results for 'Car' are shown
