Feature: As an API user
  I want to have API documentation
  So that I know how to use the program.

  Scenario: Opening the API documentation
      When I open the API documentation
      Then the response code should be 200
      And the API documentation will be returned
