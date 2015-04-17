Feature: Take HDD G/s
Scenario: When creating a new HDD

Given An HDD
      Then Require a G/s

Given An HDD
      When Updating the G/s
      Then Update the G/s