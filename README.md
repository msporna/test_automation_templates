# Robot Framework

Based on ps store page. Contains 2 sample tests.
It has keywords divided nicely by page to make is similar to page object pattern. Pure robot framework approach.
Good for: scenarios when team has people not familiar with python and want to write keywords besides tests. Then keywords are written in plain english like text 
using robot's libraries and keywords. Python is used occasionally for scenarios that robot cannot do or is difficult to do in robot. Downdside is that maintanance 
of such written logic can be difficult to maintain with time.
Starting command in run.bat - it also has required parameters such as starting browser and app url.

# Robot Framework and Python-only keywords 

Based on ps store page. Contains 2 sample tests.
It has keywords only in python and page object pattern. No keyword is written in plain english like text. Tests consume python keywords and are in english like text .
This requires team to be able to write and maintain python in order to create new keywords. However it's good because writing in python makes it easier to maintain and understand.

# Python + unittest

pure python with selenium run by unittest framework and html test runner. Html report is poor compared to what robot framework gives but custom reporer can be written.
no framework means the highest level of control and flexibility and clarity but requires highest python knowledege from team members.