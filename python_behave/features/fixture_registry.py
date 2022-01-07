from features.fixtures import webdriver_fixture, rest_api_fixture, test_data_fixture

fixture_registry = {
    "fixture.webdriver": webdriver_fixture,
    "fixture.rest_api_handler": rest_api_fixture,
    "fixture.test_data_handler": test_data_fixture
}
