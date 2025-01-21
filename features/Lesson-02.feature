Feature: Ebay.com regression-01

  Scenario: Validate the search functionality
    Given Go to ebay.com
    Then In search field type "iPhone"
    And Click the "Search"
    Then the first result item is "iPhone"