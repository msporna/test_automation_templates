from features.config import Config
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait


class WebDriverHandler:

    def setup_webdriver(self):
        browser_to_use = Config.browser
        print(f"starting driver for browser: {browser_to_use}")
        if browser_to_use == None:
            raise Exception(
                "Unable to identify test browser. Set the environment variable {TEST_BROWSER} with one of the values: chrome,firefox")
        if browser_to_use == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--window-size=1420,1080")
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("--disable-default-apps")
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--headless") # comment if you want to use headless mode
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument(
                '--user-agent=secret')  # just to ilustrate how to set chrome options that have value assigned
            self.web_driver_instance = webdriver.Chrome(desired_capabilities=chrome_options.to_capabilities())
            self.web_driver_instance.delete_all_cookies()  # we want to start fresh
        elif browser_to_use == "firefox":
            # todo, setup firefox here
            raise NotImplementedError("firefox support is *todo* ")

    def find_element(self, selector):
        element = self.web_driver_instance.find_element_by_css_selector(selector)
        return element

    def find_element_with_explicit_wait(self, selector, timeout=15):
        element = WebDriverWait(self.web_driver_instance, timeout).until(
            lambda x: x.find_element_by_css_selector(selector))
        return element

    def visit(self, url):
        self.web_driver_instance.get(url)

    def is_element_stale(self, element):
        try:
            # Calling any method forces a staleness check
            element.is_enabled()
            return False
        except StaleElementReferenceException:
            return True

    def quit(self):
        self.web_driver_instance.quit()

    def close(self):
        self.web_driver_instance.close()

    def select_tab(self, index):
        self.web_driver_instance.switch_to.window(self.web_driver_instance.window_handles[index])
