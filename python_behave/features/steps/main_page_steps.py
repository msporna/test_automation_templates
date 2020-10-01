from behave import step
from features.src.pages.main_page import MainPage


@step('chromedriver page is opened')
def open_main_page(context):
    """
    visit main page and put main page instance in the context's cache
    :param context:
    :return:
    """
    context.cache["main_page"] = MainPage(context)
    context.cache["main_page"].visit()


@step('latest {version_type} release should be "{expected_release_version}"')
def verify_release_version(context, version_type, expected_release_version):
    if version_type == "stable":
        context.cache["main_page"].verify_stable_release_version(expected_release_version)
    else:
        context.cache["main_page"].verify_beta_release_version(expected_release_version)


@step('downloads link is clicked')
def navigate_to_downloads(context):
    context.cache["main_page"].navigate_to_downloads()
