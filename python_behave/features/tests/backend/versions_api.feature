Feature: versions api
  verify that the api (mock) returns expected chromedriver versions

  @smoke_tests_api @fixture.rest_api_handler @fixture.test_data_handler
  Scenario: verify rest api returns both stable and beta versions of chromedriver
    Given request is made
      | request_type | endpoint  | api_name |
      | GET          | /versions | versions |
    Then verify the status code is 200
    And the json response contains
      | json_path       | expected_value |
      | values[0].title | stable         |
      | values[1].title | beta           |
      | values[0].ver   | 96.0.4664.45   |
      | values[1].ver   | 97.0.4692.36   |

  @smoke_tests_api @fixture.webdriver @fixture.rest_api_handler @fixture.test_data_handler
  Scenario: verify a new chromedriver version can be added
    Given request is made
      | request_type | endpoint  | payload                           | api_name |
      | POST         | /versions | {"title": "test", "ver": "2021" } | versions |
    When request is made
      | request_type | endpoint  | api_name |
      | GET          | /versions | versions |
    Then the json response matches json from test data file "expected_response_1.json"
