Feature: Test Scenarios for Search functionality

  Scenario Outline: User can search for a product
    Given Open Google page
    When Input <search_word> into search field
    And Click on search icon
    Then Product results for <search_word> are shown
    Examples:
      | search_word |
      | Car         |


