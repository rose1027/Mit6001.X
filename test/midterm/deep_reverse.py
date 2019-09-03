# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:14:24 2019

@author: Student
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    
    L.reverse()
    print(L)
    
    #print(L)
    for ele in L:
        ele.reverse()
        #print(ele)
        #colon_l.append(ele)
    #print('colon_l',colon_l)
    #L = colon_l[:]
    #print(L)
    #return L
L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
#L = L[::-1]
#print(L)
deep_reverse(L) 
print(L)