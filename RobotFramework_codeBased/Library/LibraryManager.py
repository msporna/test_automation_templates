from robot.libraries.BuiltIn import BuiltIn




def get_library_instance(name):
    '''
    gets instance of library created by robot framework
    (that's why those classes are not used directly from python because we want to use 1 instance creted
    by robot at the start)
    '''
    if name=="main_page":
        main_page_library_instance=BuiltIn().get_library_instance('MainPage')
        print("Got instance of {main page} in a version of "+main_page_library_instance.say_hello())
        return main_page_library_instance
    elif name=="generic":
        generic_library_instance=BuiltIn().get_library_instance('Generic')
        print("Got instance of {generic library} in a version of "+generic_library_instance.say_hello())
        return generic_library_instance
    elif name=="news_page":
        news_page_library_instance=BuiltIn().get_library_instance('NewsPage')
        print("Got instance of {news page library} in a version of "+news_page_library_instance.say_hello())
        return news_page_library_instance
