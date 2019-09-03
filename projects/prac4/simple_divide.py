# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:04:17 2019

@author: Student
"""
def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]

def simple_divide(item,denom):
    try:
        return item / denom
    except ZeroDivisionError as error:
        return 0
fancy_divide([0, 2, 4], 0)