# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:28:51 2019

@author: Tingting
"""
count = 0;
s = 'azcbobobegghakl'
s1 = ''
s2 = 'null'
if len(s2) == 0:
        print('Number of vowels: '+str(count))
else:
    for c in s2:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            count += 1
    print('Number of vowels: '+str(count))