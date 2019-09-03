# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:41:05 2019

@author: Student
"""

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False
#search([18,19,26], 19)
newsearch([18,19,26],19)