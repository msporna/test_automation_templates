from behave import use_fixture, fixture
from features.fixtures import webdriver_fixture


def before_all(context):
    # init cache dictionary that will hold objects required for tests
    # and will be cleared after each test (scenario)
    context.cache = {}
    

def before_scenario(context, scenario):
    use_fixture(webdriver_fixture, context)


def after_scenario(context, scenario):
    # clear the cache
    context.cache.clear()  # clear the cache dict in case anything went in there
