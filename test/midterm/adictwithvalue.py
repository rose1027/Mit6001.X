# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:14:05 2019

@author: Student
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here 
    L = []
    for k in aDict:
        if aDict[k] == target:
                L.append(k)
        L.sort()
    return L

temp = keysWithValue({0: 0, 1: 2, 3: 0, 5: 2, 6: 2, 7: 0, 8: 0, 10: 1}, 4)
print(temp)        