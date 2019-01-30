from helpers.DriverHandler import setup_webdriver
from pages.MainPage import MainPage


def open_browser_and_visit_app_url():
    web_driver=setup_webdriver()
    main_page=MainPage(web_driver)
    main_page.visit()
    return web_driver,main_page