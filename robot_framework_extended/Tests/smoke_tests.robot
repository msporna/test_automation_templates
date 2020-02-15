*** Settings ***
Documentation   test cases related to ...
Library    ${LIBRARY}${/}Generic.py
Library    ${LIBRARY}${/}page_objects${/}MainPage.py
Library    ${LIBRARY}${/}page_objects${/}NewsPage.py


Test Setup          do_test_setup   # generic
Test Teardown       do_test_teardown    # generic



*** Test Cases ***

Verify sony logo has a correct related link
    [Documentation]     test1
    [Tags]    SMOKE_TESTS
    ${sony_icon_url}=       get sony icon url   # main_page.py
    Should be equal     ${sony_icon_url}      http://www.sony.net/SonyInfo/