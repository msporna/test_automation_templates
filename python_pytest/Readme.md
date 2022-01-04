# overview

This folder contains sample backend tests in pytest framework (https://docs.pytest.org/en/stable/). The sample tests are for mock rest api.

# How to run the example

1. install json server for starting the rest api mock : 
npm install -g json-server

more: https://github.com/typicode/json-server#getting-started

 * this mock will be tested by the sample tests
 * run with: `json-server --watch db.json`
 * host is `http://localhost:3000`
 * sample GET is: `http://localhost:3000/versions`

2. run the tests via `pytest -s -m smoke_api` or `pytest -s -m smoke_gui` (-s flag enables printing to be printed
in the console as tests are being executed by pytest)
3. tests will run against the mock rest api

# allure reports

to enable allure reports:
1. run with command: `pytest -s -m smoke_gui --alluredir=allure-results`
2. serve the allure report: `allure serve allure-results` (requires to have Allure Framework installed)

reference:
https://pypi.org/project/allure-pytest/



