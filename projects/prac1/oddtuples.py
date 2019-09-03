# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:11:28 2019

@author: Student
"""

def oddTuples(aTup):
    words = ()
    i = 0
    while i < len(aTup):
       words += aTup[i:i+1]
       i += 2
    return words
print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))