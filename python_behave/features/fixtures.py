from behave import fixture
from features.src.util.driver_handler import WebDriverHandler
from features.src.util.rest_api_handler import RestApiHandler
from features.src.util.test_data_handler import TestDataHandler


@fixture
def webdriver_fixture(context):
    context.web_driver_handler = WebDriverHandler()
    context.web_driver_handler.setup_webdriver()
    context.add_cleanup(context.web_driver_handler.quit)  # will automatically call quit() after scenario


@fixture
def rest_api_fixture(context):
    context.rest_api_handler = RestApiHandler()


@fixture
def test_data_fixture(context):
    context.test_data_handler = TestDataHandler()
