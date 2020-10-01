# overview

This folder contains sample backend tests in pytest framework (https://docs.pytest.org/en/stable/). The sample tests are for mock rest api.

# How to run the example

1. install json server for starting the rest api mock : 
npm install -g json-server

more: https://github.com/typicode/json-server#getting-started

 * this mock will be tested by the sample behave tests
 * run with: `json-server --watch data.json`
 * host is `http://localhost:3000`
 * sample GET is: `http://localhost:3000/posts/1`

2. run the tests via `pytest -s -m smoke` (-s flag enables printing to be printed
in the console as tests are being executed by pytest)
3. tests will run against the mock rest api

# allure reports

to enable allure reports:
1. run with command: `py.test -s -m smoke --alluredir=allure-results`
2. serve the allure report: `allure serve allure-results` (requires to have installed Allure Framework)

reference:
https://pypi.org/project/allure-pytest/



