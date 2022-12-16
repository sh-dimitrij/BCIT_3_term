Feature: Unique selection
    Scenario: list of numbers
    Given list of numbers: [1, 1, 3, 1, 2, 2, 3, 3]
    When start Unique iterator
    Then values, numbers [1, 3, 2]

    Scenario: list of letters
    Given list of letters: ["a", "A", "b", "B", "a", "A", "b", "B"]
    When start Unique iterator
    Then values, letters ['a', 'A', 'b', 'B']

    Scenario: list of letters with ignore_case=True
    Given list of letters: ["a", "A", "b", "B", "a", "A", "b", "B"]
    When start Unique iterator + ignore_case
    Then values, letters ['a', 'b']