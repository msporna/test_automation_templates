from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Generic:

    __version__='0.1'

    # instances
    web_driver=None

    def __init__(self):
        print("inited")

    def prepare_webdriver_and_go_to_main_page(self):
        '''
        determines what browser to use
        and calls keyword preparing that browser
        '''
        browser=BuiltIn().get_variable_value("${BROWSER}")
        main_page_url=BuiltIn().get_variable_value("${APP_URL}")

        if browser=="chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--window-size=1420,1080")
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("--disable-default-apps")
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument('--user-agent=secret')  # just to ilustrate how to set chrome options that have value assigned
            self.web_driver = webdriver.Chrome(desired_capabilities=chrome_options.to_capabilities())
            self.web_driver.delete_all_cookies()  # we want to start fresh
        elif browser=="firefox":
            return BuiltIn().run_keyword("create ff driver")
        # open browser and go to app url
        self.web_driver.get(main_page_url)

    def do_test_setup(self):
        self.prepare_webdriver_and_go_to_main_page()
        WebDriverWait(self.web_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.store-logo'))
        )

        

    def do_test_teardown(self):
        self.web_driver.close()

    def say_hello(self):
        return self.__version__