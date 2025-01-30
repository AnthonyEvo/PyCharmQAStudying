# Created by Anthony at 1/26/2025
Feature: Ebay.com regression-04

  Scenario: Filter checkboxes testing
    Then In search field type Iphone
    And Click the "Search" button
    Then Select filter Verizon in Network list
    Then Select filter Apple iPhone 11 in Model list
    Then Select filter Factory Unlocked in Lock Status list
    Then Get all items which not contains "iPhone" from 1 pages