# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 22:23:18 2019

@author: Student
"""

def gcdRecur(a,b):
     if b == 0:
        return a
     else:
        return gcdRecur(b,a%b)
print(gcdRecur(6,12))