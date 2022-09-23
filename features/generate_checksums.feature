Feature: As an API user
  I want to be able to asynchronously generate checksums for files
  So that I can see if files have changed

  Scenario: Calling the checksum generation endpoint
      When I do a POST request to /checksums with body
        """
        {
          "test": "kek"
        }
        """
      Then the response code should be 200
      And the JSON response should be
        """
        {
          "checksum": "a3423j4jk23h423bh4324jb23h4234kj234"
        }
        """
