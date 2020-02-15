
*** Settings ***
Documentation   keywords for the news page

Resource    ${KEYWORDS}${/}selenium_handler.robot
Library           Selenium2Library      15     1       Capture Page Screenshot
Library     ${LIBRARY}${/}Generic.py
Library     Screenshot

*** Variables ***
${title_selector_css}=     div.grid-header > h3
${sort_combobox_selector_css}=      div.grid-header__right > div:nth-child(2) > div.select-dropdown

*** Keywords ***

wait for news page to be loaded
    Wait until element is visible       css:${title_selector_css}
    Element Text Should Be      css:${title_selector_css}       Nowości

verify sort combobox is present
    Page should contain element     css:${sort_combobox_selector_css}