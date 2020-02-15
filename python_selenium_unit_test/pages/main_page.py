import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from python_selenium_unit_test.pages.news_page import NewsPage


class MainPage:

    # locators
    sony_icon_url_selector_css='header > div > div > div.container > a.make-believe-header__icon'
    news_url_selector_css='div.application-container > div > div > div > div.left-panel > ul:nth-child(2) > a:nth-child(1)'
    store_logo_selector_css='a.store-logo'

    def __init__(self,web_driver):
        self.web_driver=web_driver



    def visit(self):
        self.web_driver.get(os.environ.get('APP_URL'))
        WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.store_logo_selector_css))
        )

    def get_sony_icon_url(self):
        icon_url=self.web_driver.find_element_by_css_selector(self.sony_icon_url_selector_css).get_attribute('href')
        return icon_url

    def go_to_news_page(self):
        self.web_driver.find_element_by_css_selector(self.news_url_selector_css).click()
        news_page=NewsPage(self.web_driver)
        return news_page
