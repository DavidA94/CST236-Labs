Feature: Read distances and connection speeds from file
Scenario: When researching speeds

Given an estimated speed
      When researching speeds
      Then determine if network or driving is faster