# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 09:52:41 2019

@author: Student
"""

def num_bobs(s):
    return 0 if not s else \
           (s[:3] == 'bob') + num_bobs(s[1:])

print('Number of times bob occurs is:', num_bobs(s))