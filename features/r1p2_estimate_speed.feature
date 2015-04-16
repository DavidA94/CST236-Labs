Feature: Read distances and connection speeds from file
Scenario: When researching speeds

Given I'm researching estimated speeds
      When given an estimated speed
      Then determine if network or driving is faster