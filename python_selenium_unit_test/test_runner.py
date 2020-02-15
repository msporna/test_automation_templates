import os
import unittest
from HtmlTestRunner import HTMLTestRunner

from python_selenium_unit_test.tests.news_page_tests import NewsPageTests
from python_selenium_unit_test.tests.smoke_tests import SmokeTests


def prepare_suite(test_suite_to_run):
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    if test_suite_to_run=="all":
        suite.addTests(loader.loadTestsFromModule(NewsPageTests))
        suite.addTests(loader.loadTestsFromModule(SmokeTests))
    elif test_suite_to_run=="smoke_tests":
        suite.addTests(loader.loadTestsFromModule(SmokeTests))
    elif test_suite_to_run=="news_page_tests":
        suite.addTests(loader.loadTestsFromModule(NewsPageTests))
    return suite




if __name__ == '__main__':
    # print out all env vaariable values
    print("TEST_SUITE_TO_RUN : "+os.environ.get('TEST_SUITE_TO_RUN'))
    print("TEST_BROWSER : " + os.environ.get('TEST_BROWSER'))
    print("APP_URL : " + os.environ.get('APP_URL'))


    test_suite = prepare_suite(os.environ.get('TEST_SUITE_TO_RUN')) # pull tests specified in env variable to suite
    runner = HTMLTestRunner(output='')
    runner.run(test_suite) # run the tests pulled into the test_suite

