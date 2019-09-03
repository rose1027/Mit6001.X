# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 09:52:59 2019

@author: Student
"""

def longest(s, cur='', lngst=''):
    if not s:
        return max(lngst, cur, key=len)
    else:
        if not cur or s[0] < cur[-1]:
            lngst = max(lngst, cur, key=len)
            cur = ''
        return longest(s[1:], cur+s[0], lngst)

print('Longest substring in alphabetical order is:', longest(s))