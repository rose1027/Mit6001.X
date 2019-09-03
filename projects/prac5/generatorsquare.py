# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:09:26 2019

@author: Student
"""

def squareNum():
    guess = 1
    p = []
    while True:
        a = guess*guess
        p.append(a)
        yield(a)
        guess += 1
    
s = squareNum()

print(s.__next__())
print(s.__next__())
        