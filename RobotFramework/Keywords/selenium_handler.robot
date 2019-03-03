*** Settings ***
Documentation   keywords used for managing selenium web driver

Library           Selenium2Library      15      1       Capture Page Screenshot
Library     ${LIBRARY}${/}Generic.py
Library     Screenshot


*** Keywords ***

Create chrome driver
    ${options}=      BuiltIn.Evaluate        sys.modules['selenium.webdriver'].ChromeOptions()       sys
    Call Method          ${options}          add_argument        --headless
    Call Method          ${options}          add_argument        --window-size=1420,1080
    Call Method          ${options}          add_argument        --no-sandbox
    Call Method          ${options}          add_argument        --disable-extensions
    Call Method          ${options}          add_argument        --disable-infobars
    Call Method          ${options}          add_argument        --disable-default-apps
    Call Method          ${options}          add_argument        --disable-popup-blocking
    Call Method          ${options}          add_argument        'loggingPrefs':{'driver':'ALL','server':'ALL'}
    ${options}=          Call Method         ${options}          to_capabilities
    Open browser        ${APP_URL}      browser=chrome       desired_capabilities=${options}