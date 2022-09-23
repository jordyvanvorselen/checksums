Feature: As an API user
  I want to be able to asynchronously generate checksums for files
  So that I can see if files have changed

  Scenario: Calling the checksum generation endpoint
      When I do a POST request to /checksums with file test_file
      Then the response code should be 200
      And the JSON response should be
        """
        {
          "checksum": "824ae91e13ce0834e6dba82b32e342ac"
        }
        """
