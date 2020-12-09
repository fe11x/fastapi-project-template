Feature: Validate email
    User email gets validated before a new user tries to register

Scenario: Validate correct email
    Given there's no user with email nancy@example.com
    When a user tries to check if nancy@example.com is a valid email
    Then the result is True

Scenario: Validate incorrect email
    Given there's no user with email nancy@.com
    When a user tries to check if nancy@.com is a valid email
    Then the result is False

Scenario: Validate invalid email
    Given there's no user with email nancy@dispostable.com
    When a user tries to check if nancy@dispostable.com is a valid email
    Then the result is False

Scenario: Validate unavailable email
    Given user with email nancy@example.com
    When a user tries to check if nancy@example.com is a valid email
    Then the result is False
