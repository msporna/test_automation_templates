from robot_framework_extended.Library.library_manager import get_library_instance


class MainPage:

    __version__='0.1'

    # locators
    sony_icon_url_selector_css='header > div > div > div.container > a.make-believe-header__icon'
    news_url_selector_css='div.application-container > div > div > div > div.left-panel > ul:nth-child(2) > a:nth-child(1)'

    # instances
    web_driver=None

    def __init__(self):
        self.web_driver=get_library_instance("generic").web_driver
        print("INITED MainPage")

    def say_hello(self):
        return self.__version__

    
    def get_sony_icon_url(self):
        icon_url=self.web_driver.find_element_by_css_selector(self.sony_icon_url_selector_css).get_attribute('href')
        return icon_url

    def go_to_the_news_page(self):
        self.web_driver.find_element_by_css_selector(self.news_url_selector_css).click()
        # find news page library and verify web driver navigated there
        get_library_instance("news_page").wait_for_news_page_to_be_loaded()
