import pytest
from src.config import Config
from src.util.api_manager import ApiManager


@pytest.fixture(scope="session")
def api_manager():
    return ApiManager(Config.app_host)


@pytest.fixture(scope="function")
def disposable_example():
    """
    function scope - fixture is destroyed after each test
    :return:
    """
    var1 = "x"  # this could be a webdriver
    yield var1  # test executed here
    var1 = "y"  # cleaning (not used in test but can do some cleanup with still existing var1 obj)
