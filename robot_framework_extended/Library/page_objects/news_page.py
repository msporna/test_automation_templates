
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from robot_framework_extended.Library.library_manager import get_library_instance


class NewsPage:

    __version__='0.1'

    # locators
    title_selector_css = 'div.grid-header > h3'
    sort_combobox_selector_css = 'div.grid-header__right > div:nth-child(2) > div.select-dropdown'

    # instances
    web_driver=None


    def __init__(self):
        self.web_driver=get_library_instance("generic").web_driver
        print("INITED MainPage")

    def say_hello(self):
        return self.__version__

    def verify_sort_combobox_is_present(self):
        WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.sort_combobox_selector_css))
        )

    def wait_for_news_page_to_be_loaded(self):
        WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.title_selector_css))
        )

