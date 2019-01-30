# HOW TO RUN PROPERLY: 

in terminal, while in folder with the test script do: `py test_runner.py`
if you run `python -m unittest test_runner.py `then code inside __main__ will not be triggered so test runner will not be used and no reporting.

python3 required

before test, set below env variables

# ENV VARIABLES

it is a good idea to use env variables set before test run for example in jenkins or in other way to setup tests. It is a better idea to use that and not some yaml file - you don't keep config in repo, repo is transparent, tests get cloned, env variables such as browser to use, software under test url etc. injected and used 
--it seems safe: if run on linux, env variables injected by shell script (eg: run by jenkins build step before testing starts) exist only for duration of process and then dissapear. if other job starts,with other test suite at the same time, it has copy of system env variables and modifies them in its own scope, not other job's.
--source:https://stackoverflow.com/questions/496702/can-a-shell-script-set-environment-variables-of-the-calling-shell

list:
<p>TEST_BROWSER - chrome,ff etc. on what browser test?
<p>TEST_SUITE_TO_RUN - what tests should be run? (all,news_page,smoke_tests)
<p>APP_URL - url to software under tests

NOTE: don't forget to reload your terminal after updating env variables. 


# REPORTS

reports are stored in the /reports folder

# FLOW
each test class has setup and teardown. Setup creates
webdriver and then creates main page instance and navigates to main page
and instances of webdriver and main page are returned to test class
and held there throughout the test (new instance of webdriver and 
main page are created before each test and then discarded, never reused by next tests)