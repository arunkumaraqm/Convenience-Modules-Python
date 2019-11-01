"""
This module provides shortcuts to call the help and dir functions.

Import the module this way:
    from helper import h, d
    
You can call the help function by either:
    h> obj
    obj -h
    
You can print the list of attributes by either:
    d> obj
    obj -d
"""

class Helper:
	def __gt__(self, other):
		help(other)

	def __rsub__(self, other):
                help(other)

h = Helper()

class Director:
        def __gt__(self, other):
                print(dir(other))
                
        def __rsub__(self, other):
                print(dir(other))

d = Director()
