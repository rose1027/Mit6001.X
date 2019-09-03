# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:54:09 2019

@author: Student
"""

def iterPower(base, exp):
    '''
     base: int or float.
     exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result
print(iterPower(2,3))