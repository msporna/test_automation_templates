# What is this?
The  repo currently has 3 project templates for selenium and python testing- each enabling slightly different approach. Find description of those templates below.

The templates contain 2 simple sample tests for Sony Playstation store.

# Robot Framework ("robot_framework")

It has keywords divided nicely by page to make it similar to page object pattern. Pure robot framework approach.
Good for: scenarios when team has people not familiar with python and want to write custom keywords besides tests. Then keywords are written in plain english like text 
using robot's libraries and keywords. Python is used occasionally for scenarios that robot cannot do or is difficult to do in robot. Downdside is that maintanance 
of such written logic can get difficult with time.
Starting command in run.bat - it also has required parameters such as starting browser and app url.

# Robot Framework and Python-only keywords ("robot_framework_extended")

It has keywords written only in python (previous template involved keywords written in robot framework's syntax) and page object pattern. No keyword is written in plain english like text. Tests consume python keywords and are in english like text .
This requires team to be able to write and maintain python in order to create new keywords. However it's good because writing in python makes it easier to maintain and understand. It also can be used in mixed skills team -people with python knowledge can code keywords and non-python people can consume those keywords to create tests.

# Python + unittest ("python_selenium_unit_test")

Pure python with selenium executed by unittest framework and html test runner. Html report is poor compared to what robot framework gives but custom reporer can be written to improve that.
No framework means the highest level of control and flexibility and clarity but requires highest python knowledege from team members.



## Each template has its own extended and detailed readme.