# if module (no class,static) is in parent directory, this little hack is needed to import it:
# source: https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import LibraryManager # this is in parent dir, what I want to import

class MainPage:

    __version__='0.1'

    # locators
    sony_icon_url_selector_css='header > div > div > div.container > a.make-believe-header__icon'
    news_url_selector_css='div.application-container > div > div > div > div.left-panel > ul:nth-child(2) > a:nth-child(1)'

    # instances
    web_driver=None

    def __init__(self):
        self.web_driver=LibraryManager.get_library_instance("generic").web_driver
        print("INITED MainPage")

    def say_hello(self):
        return self.__version__

    
    def get_sony_icon_url(self):
        icon_url=self.web_driver.find_element_by_css_selector(self.sony_icon_url_selector_css).get_attribute('href')
        return icon_url

    def go_to_the_news_page(self):
        self.web_driver.find_element_by_css_selector(self.news_url_selector_css).click()
        # find news page library and verify web driver navigated there
        LibraryManager.get_library_instance("news_page").wait_for_news_page_to_be_loaded()
