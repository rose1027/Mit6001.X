# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:43:04 2019

@author: Student
"""

def fancy_divide(list_of_numbers, index):
    try:
        try:
            print(11)
            raise Exception("0")
            print(12)
        finally:
            print(21)
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                print(22)
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(31)
        print(ex)
        print(32)
fancy_divide([0, 2, 4], 0)