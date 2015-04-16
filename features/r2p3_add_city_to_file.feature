Feature: Add city to file
Scenario: When adding a new city

Given A new city
      Then Append that city to the cities file

Scenario: When removing a city
Given A city to be removed
      Then Remove city and update file