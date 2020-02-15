*** Settings ***
Documentation   keywords used for managing selenium web driver

Resource    ${KEYWORDS}${/}selenium_handler.robot
Library           Selenium2Library      15      1       Capture Page Screenshot
Library     ${LIBRARY}${/}Generic.py
Library     Screenshot

*** Keywords ***

Go to main page
    prepare_webdriver_and_go_to_main_page       ${BROWSER}      # generic.py
    Wait until element is visible       css:a.store-logo

Do test setup 
    go to main page     # this

Do test teardown
    Close All Browsers



