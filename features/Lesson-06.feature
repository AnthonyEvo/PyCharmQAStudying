# Created by Anthony at 1/29/2025

Feature: Ebay.com Lesson-06 advanced cycles and Behave tables

  Background:
    When go set default sleep time to 3

  Scenario Outline: Filter checkboxes testing
    Given In search field type Iphone
    And Click the "Search" button
    Then Select filter <Filter_01_value> in <Filter_01_list> list
    Then Select filter <Filter_02_value> in <Filter_02_list> list
    Then Select filter <Filter_03_value> in <Filter_03_list> list
    Then Get all items which not contains "AT&T" from 2 pages

    Examples:
      | Filter_01_list | Filter_01_value | Filter_02_list | Filter_02_value | Filter_03_list | Filter_03_value  |
      | Network        | Verizon         | Model          | Apple iPhone 11 | Lock Status    | Factory Unlocked |
      | Network        | T-Mobile        | Model          | Apple iPhone 12 | Lock Status    | Not Specified    |