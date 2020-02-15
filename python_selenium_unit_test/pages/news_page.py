
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewsPage:
    # locators
    title_selector_css = 'div.grid-header > h3'
    sort_combobox_selector_css = 'div.grid-header__right > div:nth-child(2) > div.select-dropdown'

    def __init__(self,webdriver):
        self.web_driver=webdriver
        self.wait_for_news_page_to_be_loaded()

    def wait_for_news_page_to_be_loaded(self):
        WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.title_selector_css))
        )

    def verify_sort_combobox_is_present(self):
        WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.sort_combobox_selector_css))
        )
        return True # exception before dishonor!