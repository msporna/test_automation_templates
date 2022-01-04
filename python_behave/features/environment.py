from behave.fixture import use_fixture_by_tag
from features.fixture_registry import fixture_registry


def before_all(context):
    # init cache dictionary that will hold objects required for tests
    # and will be cleared after each test (scenario)
    context.cache = {}

def before_tag(context, tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry)

def after_scenario(context, scenario):
    # clear the cache
    context.cache.clear()  # clear the cache dict in case anything went in there
