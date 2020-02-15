*** Settings ***
Documentation   keywords for the main page

Resource    ${KEYWORDS}${/}selenium_handler.robot
Resource    ${KEYWORDS}${/}page_keywords${/}news_page_keywords.robot
Library           Selenium2Library      15      1       Capture Page Screenshot
Library     ${LIBRARY}${/}Generic.py
Library     Screenshot

*** Variables ***
${sony_icon_url_selector_css}=      header > div > div > div.container > a.make-believe-header__icon
${news_url_selector_css}=   div.application-container > div > div > div > div.left-panel > ul:nth-child(2) > a:nth-child(1)

*** Keywords ***

Get sony icon url 
    ${sony_icon_url}=       Get element attribute       css:${sony_icon_url_selector_css}       href
    [Return]        ${sony_icon_url}

Go to the news page 
    Click element       css:${news_url_selector_css}
    wait for news page to be loaded     # news_page_keywords




