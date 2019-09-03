# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 22:09:23 2019

@author: Student
"""

def gcdIter(a,b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
   
    if a < b:
        result = a
        bigger = b
        smaller = a
    else:
        result = b
        bigger = a
        smaller = b
    while result > 0:
        if bigger % result == 0 and smaller % result == 0:
            return result
            break
        else:
            result -= 1
    return 1
print(gcdIter(2,12))
        