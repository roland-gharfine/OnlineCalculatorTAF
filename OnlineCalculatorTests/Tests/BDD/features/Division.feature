Feature: Perform division calculation on Online Calculator
    As a user, I want to perform a division calculation on the online calculator website, and see the result displayed on the top of the animation.

Scenario: Divide two positive numbers
    Given that the user is on the Online Calculator webpage
    When they enter 6
    And they click the division button
    And they enter 3
    And they click the equals button
    Then the result of 2 should be displayed


Scenario: Divide a positive number by a negative number
    Given that the user is on the Online Calculator webpage
    When they enter 5
    And they click the division button
    And they enter 5
    And they click the plus minus button
    And they click the equals button
    Then the result of -1 should be displayed


Scenario: Handle division by zero
    Given that the user is on the Online Calculator webpage
    When they enter 5
    And they click the division button
    And they enter 0
    And they click the equals button
    Then the result of Error should be displayed