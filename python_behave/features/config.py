import os


class Config:
    """
    it attempts to take each configurable value from env variables
    if not found, default is used (usable for local testing - don't specify env variables, just use defaults
    however-remember that this file goes to git, so mind other team members when doing changes to defaults)
    """
    browser = os.getenv('TEST_BROWSER', "chrome")  # will take browser from env variables or use "chrome" as default
    app_host = "https://chromedriver.chromium.org/"

    versions_api_host = "http://localhost:3000"
