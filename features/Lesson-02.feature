Feature: Ebay.com regression-01

  Scenario: Validate the search functionality
    Given Go to ebay.com
    Then In search field type Iphone
    And Click the "Search" button
    Then the first result item is "iPhone"