
import unittest

from python_selenium_unit_test.helpers.util import open_browser_and_visit_app_url


class SmokeTests(unittest.TestCase):

    def setUp(self):
        self.web_driver,self.main_page=open_browser_and_visit_app_url()
    
    def tearDown(self):
        self.web_driver.close()


    def test_if_sony_logo_points_to_correct_url(self):
        sony_icon_url=self.main_page.get_sony_icon_url()
        self.assertEqual(sony_icon_url,'http://www.sony.net/SonyInfo/',"sony icon has invalid url!")


    @unittest.skip("This is a skipped test.")
    def test_skip_exmaple(self):
        self.assertTrue(1,1)