# overview

This folder contains sample frontend tests written in Python along with Behave framework (BDD). 
I created a sample test that will go to 'https://chromedriver.chromium.org/' website and check if latest stable
and beta releases listed over there are '85.0.4183.87' and '86.0.4240.22' (the latest at this moment).

If the https://chromedriver.chromium.org/ page lists different version on the main page now, update the tests with
the latest numbers or see them fail which will prove the tests are working.

In real life, if it wasn't just a test project template, I'd probably inject the versions into the backend so it'd  
always be the same version number and the test would be unbreakable, just checking if frontend displays the 
correct version.

# How to run the example

1. download chromedriver for your platform and add it to PATH (in real life can be done via docker)
2. ensure you have chrome installed
3. from the root folder run `behave --tags @smoke_tests`

# Additional knowledge & tricks

## test suites

Usually tests must be organized in some kind of a test suites, to be able to split tests for different purposes like nigthly regression and post-deployment smoke tests. In behave it can be achieved through using tags. Steps:

1. simply add a `@ImATag` tag above a scenario name
2. run tests with only given tag: 
3. or run tests with more than 1 tags: 

more: https://behave.readthedocs.io/en/latest/tutorial.html#controlling-things-with-tags

## reports

I recommend Allure Framework for the test reporting. Allure can be nicely and easily integrated with behave tests: `https://docs.qameta.io/allure/#_behave`

steps:
0. install allure-behave package via PyPi
1. add line `allure = allure_behave.formatter:AllureFormatter` to behave.ini under section named `[behave.formatters]`
2. run tests with slightly modified command: `behave -f allure -o allure-results --tags @smoke_tests`
3. tests will output results to `allure-results`
4. now serve the reports via command: `allure serve allure-results` (you must have allure installed)

references:
 https://pypi.org/project/allure-behave/
 https://docs.qameta.io/allure/#_installing_a_commandline

## flaky tests

often times there are tests that are flaky or broken - usually failing due to environmental problems, issues with test code itself and rarely due to real bug. If test code was checked and everything is fine there, try to enable re-running failed scenarios.

Re-running failed scenarios might solve issues with tests that sometimes pass, in general a valid tests but tend to fail due to unexpected reasons and not a bug. When re-running such scenario, most likely it will pass (if there is no bug out there of course). 

Re-run happens automatically right after test suite execution is done, and latest result from rerun scenarios is present on test report so if this solves the problem, reports will be nicer and there will be one less thing to investigate for QA personnel. 

Remember that you first should attempt to investigate and fix flaky test's code, rerun is the last resort if you are sure the test code is fine!

How to do it in behave:

1. add this line to `behave.ini`: `outfiles = rerun.txt` and `format = rerun`
2. run the tests as usual: `behave --tags @smoke_tests`
3. failed scenarios will be output to "rerun.txt" file 
4. re-run with command: `behave @rerun.txt`
 

# webdriver

chrome driver is attached to this project (85.0.4183.87 which is the latest stable at this moment).
If you are trying to run this project later on, update chrome driver binaries in the "chromedriver" root folder.

# gherkin reference

https://cucumber.io/docs/gherkin/reference/