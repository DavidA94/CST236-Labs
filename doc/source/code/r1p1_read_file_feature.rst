Feature: Read distances and connection speeds from file
=======================================================

Scenario: When researching speeds with file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **Given** I'm researching speeds
| **When** given a file
| **Then** read in data

Scenario: When creating a bad city
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **Given** I'm researching speeds
| **When** making a bad city
| **Then** make city attributes None and log error

Scenario: When adding a bad city
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **Given** I'm researching speeds
| **When** adding a bad city
| **Then** put error in log and don't add

Scenario: When removing a city
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **Given** I'm researching speeds
| **When** wanting to remove a city
| **Then** remove city

Scenario: When removing a bad city
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **Given** I'm researching speeds
| **When** wanting to remove a bad city
| **Then** put error in log and don't remove anything
