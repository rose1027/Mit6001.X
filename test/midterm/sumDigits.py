# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:41:08 2019

@author: Student
"""

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    sum = 0
    if N // 10 == 0:
        sum += N
        return sum 
    else:
       sum += N % 10
       print('sum=',sum)
       N = N // 10
       print('N=',N)
       return sum+sumDigits(N)
     
s = sumDigits(123)
#print(s)