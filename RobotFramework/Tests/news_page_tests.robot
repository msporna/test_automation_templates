*** Settings ***
Documentation   test cases related to ...
Resource    ${KEYWORDS}${/}selenium_handler.robot
Resource    ${KEYWORDS}${/}shared_keywords.robot
Resource    ${KEYWORDS}${/}page_keywords${/}main_page_keywords.robot
Resource    ${KEYWORDS}${/}page_keywords${/}news_page_keywords.robot

Test Setup          Do test setup   # shared_keywords
Test Teardown       Do test teardown        # shared_keywords



*** Test Cases ***

Verify the sort combobox is present
    [Documentation]     test2
    [Tags]    NEWS_PAGE
    go to the news page     # main_page_keywords
    verify sort combobox is present     # news_page_keywords