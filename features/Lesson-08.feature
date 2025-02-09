# Created by Anthony at 2/5/2025
Feature: Ebay.com Lesson-08 Exceptions, explicit wait, few filters validation

  Background:
    When start, set default sleep time to 20

  Scenario: Filter search data for mismatches
    Given In search field type Iphone
    And Click the "Search" button
    Then Use smart filter, page quantity is 3
      | Filter_name | Filter_value     |
      | Network     | Verizon          |
      | Model       | Apple iPhone 11  |
      | Lock Status | Factory Unlocked |