# if module (no class,static) is in parent directory, this little hack is needed to import it:
# source: https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import LibraryManager # this is in parent dir, what I want to import

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewsPage:

    __version__='0.1'

    # locators
    title_selector_css = 'div.grid-header > h3'
    sort_combobox_selector_css = 'div.grid-header__right > div:nth-child(2) > div.select-dropdown'

    # instances
    web_driver=None


    def __init__(self):
        self.web_driver=LibraryManager.get_library_instance("generic").web_driver
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

