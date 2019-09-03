# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 09:51:52 2019

@author: Student
"""

def num_vowels(s):
    if not s:
        return 0 
    else:
        return (s[0] in 'aeiou') + num_vowels(s[1:])

print('Number of vowels:', num_vowels(s))