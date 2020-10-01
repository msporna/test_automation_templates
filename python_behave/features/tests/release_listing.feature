Feature: release listing
  verify that main chromedriver website shows valid release versions and it is possible to navigate to Downloads

  Background:
    Given chromedriver page is opened

  @smoke_tests
  Scenario: latest stable and beta releases are listed on main page
    Then latest stable release should be "ChromeDriver 85.0.4183.87"
    And latest beta release should be "ChromeDriver 86.0.4240.22"

  @smoke_tests
  Scenario: clicking on Downloads link redirects to downloads page
    When downloads link is clicked
    Then downloads page should be opened

