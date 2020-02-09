Feature: Perform subtraction calculation on Online Calculator
    As a user, I want to perform a subtraction calculation on the online calculator website, and see the result displayed on the top of the animation.

Scenario: Subtract two positive numbers with a positive result
    Given that the user is on the Online Calculator webpage
    When they enter 5
    And they click the subtraction button
    And they enter 3
    And they click the equals button
    Then the result of 2 should be displayed


Scenario: Subtract two positive numbers with a negative result
    Given that the user is on the Online Calculator webpage
    When they enter 5
    And they click the subtraction button
    And they enter 6
    And they click the equals button
    Then the result of -1 should be displayed


Scenario: Subtract the same number to get a result of zero
    Given that the user is on the Online Calculator webpage
    When they enter 5
    And they click the subtraction button
    And they enter 5
    And they click the equals button
    Then the result of 0 should be displayed