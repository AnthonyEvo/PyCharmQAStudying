Feature: Ebay.com regression

  Scenario: Validate the search functionality
    Given Go to ebay.com
    When In search field type "iPhone"
    And Click the "Search"
    Then the first result item is "iPhone"