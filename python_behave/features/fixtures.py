from behave import fixture
from features.src.util.driver_handler import WebDriverHandler


@fixture
def webdriver_fixture(context):
    context.web_driver_handler = WebDriverHandler()
    context.web_driver_handler.setup_webdriver()
    context.add_cleanup(context.web_driver_handler.quit)  # will automatically call quit() after scenario
