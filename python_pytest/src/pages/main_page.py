from config import Config
from src.common.web_page_template import WebPageTemplate
from src.locators.main_page_locators import MainPageLocators
from src.pages.downloads_page import DownloadsPage


class MainPage(WebPageTemplate):

    def visit(self):
        self.visit_and_verify(Config.app_host, MainPageLocators.title_span)

    def switch_to(self):
        self.verify_page_has_been_loaded(MainPageLocators.title_span)

    def get_stable_version_label(self):
        stable_version_label = self.get_element(MainPageLocators.stable_version_release_label)
        return stable_version_label

    def get_beta_version_label(self):
        beta_version_label = self.get_element(MainPageLocators.beta_version_release_label)
        return beta_version_label

    def get_downloads_url(self):
        downloads_url = self.get_element(MainPageLocators.downloads_link)
        return downloads_url

    def navigate_to_downloads(self):
        self.get_downloads_url().click()
        return DownloadsPage(self.web_driver_handler)

    def verify_stable_release_version(self, expected_version):
        stable_version = self.get_stable_version_label().text
        assert stable_version == expected_version, f"Stable release version is not what was expected ({expected_version})"

    def verify_beta_release_version(self, expected_version):
        beta_version = self.get_beta_version_label().text
        assert beta_version == expected_version, f"Beta release version is not what we expected ({expected_version})"
