*** Settings ***
Documentation   test cases related to ...
Library    ${LIBRARY}${/}Generic.py
Library    ${LIBRARY}${/}page_objects${/}MainPage.py
Library    ${LIBRARY}${/}page_objects${/}NewsPage.py

Test Setup          do_test_setup   # generic.py
Test Teardown       do_test_teardown    # generic.py



*** Test Cases ***

Verify the sort combobox is present
    [Documentation]     test2
    [Tags]    NEWS_PAGE
    go to the news page     # main_page.py
    verify sort combobox is present     # news_page.py