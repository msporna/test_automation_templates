This example shows use case of robot framework with test
keywords written only in custom libraries - robot files are created only for tests. Tests are written
in robot framework. There are no keywords written in robot framework, only in python. 
Team members without python skills can still utilize keywords in english like plain text and python 
devs maintain the scripts. This approach is a hybrid approach:
-python for better readability, flexibility and control
-robot frameowkr for ease of writing tests, great reports

HOW TO's:

1. each test file must import all libraries,even if some is not used (libraries are compiled and loaded into memory by robot framework at startup and then this instance of library is reused by python scripts)
2. LibraryManager.py gets library instance from robot framework on demand, it's not holding anything in memory , robot framework is doing that so when for instance Generic library is needed because it has webdriver instance, some library calls LibraryManager.get_library_instance and it gets library instance from robot via robot's BuiltIn library: BuiltIn().get_library_instance('MainPage')
a) this can be done once on library init, save related library instance for later. WARNING: if your library is inited before related library you want to obtain, it will give nullpointer - in that case 
--influence script execution order to make your script be executed after related script 
--assign instance of related lirbary later, when it's needed
3. besides that, everything is as in pure python+selenium


related docs:
https://github.com/robotframework/robotframework/blob/master/doc/userguide/src/ExtendingRobotFramework/CreatingTestLibraries.rst#what-methods-are-considered-keywords