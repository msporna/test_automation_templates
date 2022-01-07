from src.common.web_page_template import WebPageTemplate
from src.locators.downloads_page_locators import DownloadsPageLocators


class DownloadsPage(WebPageTemplate):


    def get_title(self):
        title_element = self.get_element(DownloadsPageLocators.title_span)
        return title_element

    def verify_title(self):
        assert self.get_title().text == "Downloads", "downloads page's title is invalid!"
