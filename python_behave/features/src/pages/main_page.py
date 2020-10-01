from features.config import Config
from features.src.locators.main_page_selectors import MainPageSelectors
from features.src.pages.downloads_page import DownloadsPage
from features.src.util.web_page_template import WebPageTemplate


class MainPage(WebPageTemplate):

    def visit(self):
        self.visit_and_verify(Config.app_host, MainPageSelectors.title_span)

    def switch_to(self):
        self.verify_page_has_been_loaded(MainPageSelectors.title_span)

    def get_stable_version_label(self):
        stable_version_label = self.get_element(MainPageSelectors.stable_version_release_label)
        return stable_version_label

    def get_beta_version_label(self):
        beta_version_label = self.get_element(MainPageSelectors.beta_version_release_label)
        return beta_version_label

    def get_downloads_url(self):
        downloads_url = self.get_element(MainPageSelectors.downloads_link)
        return downloads_url

    def navigate_to_downloads(self):
        self.get_downloads_url().click()
        self.context.cache["downloads_page"] = DownloadsPage(self.context)

    def verify_stable_release_version(self, expected_version):
        stable_version = self.get_stable_version_label().text
        assert stable_version == expected_version, f"Stable release version is not what was expected ({expected_version})"

    def verify_beta_release_version(self, expected_version):
        beta_version = self.get_beta_version_label().text
        assert beta_version == expected_version, f"Beta release version is not what we expected ({expected_version})"
