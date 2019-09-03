# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:07:08 2019

@author: Student
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    if len(L) == 0:
        return 0
    def inner(x):
        sum = 0
        n = len(L)-1
        for i in range(len(L)):
            sum += L[i]*x**n
            n -= 1
        return sum
    return inner
        
    