# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:44:07 2019

@author: Student
"""

s = 'azcbobobegghakl'
count = 0
#get index of string in python
for i in range(len(s)): 
    if s[i] == "b":
       # print(i)
        next = i+1
        nn = i+3
       
        #slice the string, the format is [:]
        if s[next:nn] == "ob":
            count += 1
            
    else:
        continue
print('Number of times bob occurs is: '+str(count))