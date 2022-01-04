import os


class Config:
    browser = os.getenv('TEST_BROWSER', "chrome")  # will take browser from env variables or use "chrome" as default
    app_host = "https://chromedriver.chromium.org/"

    api_host = "http://localhost:3000"
