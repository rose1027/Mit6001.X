# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 15:10:00 2019

@author: Student
"""

def recur_multi(base,exp):
    '''
     base: int or float.
     exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base*recur_multi(base,exp-1)

print(recur_multi(4,3))