
import unittest

from python_selenium_unit_test.helpers.util import open_browser_and_visit_app_url


class NewsPageTests(unittest.TestCase):

    def setUp(self):
        # webdriver and main_page are always created before each test, so test starts while browser
        # is opened on main page of tested app
        self.web_driver ,self.main_page =open_browser_and_visit_app_url()

    def tearDown(self):
        self.web_driver.close()


    def test_sort_combobox_is_present(self):
        news_page=self.main_page.go_to_news_page() # navigate to the news page and return news page page object
        self.assertTrue(news_page.verify_sort_combobox_is_present() ,"sort combobox not found on news page!")


