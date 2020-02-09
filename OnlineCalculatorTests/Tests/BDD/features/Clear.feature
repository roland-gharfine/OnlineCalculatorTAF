Feature: Clearing calculator result display
    As a user, I want to be able to clear my current calculation on the online calculator website, and see the cleared state displayed

Scenario: Clear a cleared calculator
    Given that the user is on the Online Calculator webpage
    When they enter clear
    And they click the clear button
    Then the result of cleared should be displayed


Scenario: Clear after entering one number
    Given that the user is on the Online Calculator webpage
    When they enter 9
    And they click the clear button
    Then the result of cleared should be displayed


Scenario: Clear after entering a complex operation
    Given that the user is on the Online Calculator webpage
    When they enter 7
    And they click the division button
    And they enter 1
    And they click the equals button
    And they click the clear button
    Then the result of cleared should be displayed

Scenario: Clear after error
    Given that the user is on the Online Calculator webpage
    When they enter 1
    And they click the division button
    And they enter 0
    And they click the equals button
    And they click the clear button
    Then the result of cleared should be displayed