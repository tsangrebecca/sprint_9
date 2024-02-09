### IN style_example.py FILE###
'''
module docstring
'''
#what would you say if you were working with someone and this is the code they gave you?

import math
import sys

    def example_1():
        '''function docstring'''
        # THIS IS A LONG COMMENT AND should be wrapped to fit 
        #     within a 72 character limit
        some_tuple = (1, 2, 3, 'a')
        some_variable = {
                        "long": '''LONG CODE LINES should be wrapped within 
                                79 character to prevent page cutoff stuff''',
                        "other": [math.pi, 100, 200, 300, 9999292929292, 
                                "This IS a long string that looks gross and goes beyond what it should"], 
                        "more": {
                            "inner": "THIS whole logical line should be wrapped"
                            },
                        "data": [444, 5555, 222, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5]
                        }
        return (some_tuple, some_variable)

    def example_2():
        '''function docstring'''
        return {"has_key() is deprecated": True}


class Example3(object):
    '''class and method docstring'''
    def __init__(self, number):   # no bar, no foo
        self.number = number

    
    def my_method(self):
    '''function docstring'''
        if self.number:
            self.number += 1
            self.number = self.number * self.number
            return self.number
        
        some_string = """INDENTATION IN MULTIPLE STRINGS SHOULD NOT BE TOUCHED 
        only actual code should be reindented, THIS IS MORE CODE"""
        return (sys.path, some_string)
    
    def my_method2(self):
    '''function docstring'''
        return self.number * 10
    