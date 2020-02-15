import os

from selenium import webdriver


def setup_webdriver():
    web_driver=None
    browser_to_use=os.environ.get('TEST_BROWSER')     #simply set TEST_BROWSER env variable before the test to set desired browser
    if browser_to_use==None:
        raise Exception("Unable to identify test browser. Set the environment variable {TEST_BROWSER} with one of the values: chrome,firefox")
    print("using browser:"+browser_to_use)
    if browser_to_use=="chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--window-size=1420,1080")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-default-apps")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--user-agent=secret')  # just to ilustrate how to set chrome options that have value assigned
        web_driver = webdriver.Chrome(desired_capabilities=chrome_options.to_capabilities())
        web_driver.delete_all_cookies()  # we want to start fresh
    elif browser_to_use=="firefox":
        pass #todo, setup firefox here
    return web_driver