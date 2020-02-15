from robot.libraries.BuiltIn import BuiltIn


class Generic:

    __version__='0.1'

    def __init__(self):
        print("inited")

    def prepare_webdriver_and_go_to_main_page(self,browser):
        '''
        determines what browser to use
        and calls keyword preparing that browser
        '''
        if browser=="chrome":
            return BuiltIn().run_keyword("create chrome driver")
        elif browser=="firefox":
            return BuiltIn().run_keyword("create ff driver")


