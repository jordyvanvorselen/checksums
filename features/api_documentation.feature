Feature: As an API user
  I want to have API documentation
  So that I know how to use the program.

  Scenario: Opening the API documentation
      When I do a GET request to /docs
      Then the response code should be 200
      And the API documentation is returned

  Scenario: Fetching the openapi specification
      When I do a GET request to /openapi.json
      Then the response code should be 200
      And the API specification is returned
