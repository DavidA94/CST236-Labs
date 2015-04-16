Feature: Read distances and connection speeds from file
Scenario: When researching speeds

Given I'm researching speeds with little space
      When more space is needed
      Then increase HDD size