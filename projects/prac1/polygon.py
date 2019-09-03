# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 08:06:16 2019

@author: Student
"""

from math import *
def polysum(n,s):
    
    polyarea = (0.25*n*s**2)/tan(pi/n)
    polyPeri = s*n
    sum = polyarea + polyPeri**2
    return round(sum,4)
print(polysum(53,40))