# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:06:16 2019

@author: Student
"""

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words +(t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return(min_nums, max_nums, unique_words)
    
(small, large, words) = get_data(((1, 'mine'),(3, 'yours'),(5, 'ours'),(7, 'mine')))
print((small, large, words))