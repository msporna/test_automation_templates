from python_selenium_unit_test.helpers.driver_handler import setup_webdriver
from python_selenium_unit_test.pages.main_page import MainPage


def open_browser_and_visit_app_url():
    web_driver=setup_webdriver()
    main_page=MainPage(web_driver)
    main_page.visit()
    return web_driver,main_page