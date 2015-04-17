Feature: Preset speeds for certain cars
=======================================

Scenario: When creating a new Car
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **Given** a new car
| **When** given a preset car make and no speed
| **Then** set speed to preset

| **Given** a new car
| **When** given a preset car make and a speed
| **Then** set speed to passed speed
