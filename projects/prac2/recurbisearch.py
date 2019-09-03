# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 07:08:23 2019

@author: Student
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
       return False
   
    elif len(aStr) == 1:
       return aStr == char
    else:
       mid = len(aStr)//2
       #print(mid)
       if char == aStr[mid]:
           return True
       else:
           if char > aStr[mid]:
               aStr = aStr[mid+1:]
              # return isIn(char,aStr[mid+1:])
           else:
               aStr = aStr[:mid]
               
           return isIn(char,aStr)
    
foo = 'd'
s = 'abcdfgiklm'
print(isIn(foo,s))