import pytest
from src.pages.main_page import MainPage


class TestFrontend:

    @pytest.mark.smoke_gui
    def test_latest_stable_and_beta_releases_are_listed_on_main_page(self, webdriver_handler):
        main_page=MainPage(webdriver_handler)
        main_page.visit()
        main_page.verify_stable_release_version("ChromeDriver 96.0.4664.45")
        main_page.verify_beta_release_version("ChromeDriver 97.0.4692.36")


    @pytest.mark.smoke_gui
    def test_downloads_page_is_opened_when_downloads_link_is_clicked(self, webdriver_handler):
        main_page = MainPage(webdriver_handler)
        main_page.visit()
        downloads_page=main_page.navigate_to_downloads()
        downloads_page.verify_title()


