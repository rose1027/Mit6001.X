# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 15:00:49 2019

@author: Student
"""

def simpleArraySum(ar):
    #
    # Write your code here.
    #
    sum = 0
    for i in range(len(ar)):
        sum += i
    return sum
arr = [1,2,3,4,10,11]

def compareTriplets(a, b):
    suma = 0
    sumb = 0
    for c1,c2 in zip(a,b):
        if c1 > c2:
            suma += 1
        elif c1 == c2:
            suma += 0
        else:
            sumb += 1
    return [suma,sumb]

#sum = simpleArraySum(arr)
#print(sum)
a = [5,6,7]
b = [3,6,10]
arr = compareTriplets(a,b)
print(arr)