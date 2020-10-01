from behave import step


@step('downloads page should be opened')
def verify_downloads_page_is_opened(context):
    context.cache["downloads_page"].switch_to()
    context.cache["downloads_page"].verify_title()
