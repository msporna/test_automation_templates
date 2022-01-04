Feature: release listing
  verify that main chromedriver website shows valid release versions and it is possible to navigate to Downloads

  Background:
    Given chromedriver page is opened

   @smoke_tests @fixture.webdriver
  Scenario: latest stable and beta releases are listed on main page
    Then latest stable release should be "ChromeDriver 96.0.4664.45"
    And latest beta release should be "ChromeDriver 97.0.4692.36"

  @smoke_tests @fixture.webdriver
  Scenario: clicking on Downloads link redirects to downloads page
    When downloads link is clicked
    Then downloads page should be opened

