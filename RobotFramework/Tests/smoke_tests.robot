*** Settings ***
Documentation   test cases related to ...
Resource    ${KEYWORDS}${/}selenium_handler.robot
Resource    ${KEYWORDS}${/}shared_keywords.robot
Resource    ${KEYWORDS}${/}page_keywords${/}main_page_keywords.robot

Test Setup          Do test setup       # shared_keywords
Test Teardown       Do test teardown        # shared_keywords



*** Test Cases ***

Verify sony logo has a correct related link
    [Documentation]     test1
    [Tags]    SMOKE_TESTS
    ${sony_icon_url}=       get sony icon url       # main_page_keywords
    Should be equal     ${sony_icon_url}      http://www.sony.net/SonyInfo/