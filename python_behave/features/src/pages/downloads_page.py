from features.src.locators.downloads_page_selectors import DownloadsPageSelectors
from features.src.util.web_page_template import WebPageTemplate


class DownloadsPage(WebPageTemplate):

    def switch_to(self):
        self.select_tab(1)  # downloads page is opened in a new tab, so need to switch to tab with index 1 to continue
        self.verify_page_has_been_loaded(DownloadsPageSelectors.title_span)

    def get_title(self):
        title_element = self.get_element(DownloadsPageSelectors.title_span)
        return title_element

    def verify_title(self):
        assert self.get_title().text == "Downloads", "downloads page's title is invalid!"
