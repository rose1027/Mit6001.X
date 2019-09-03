# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 15:42:30 2019

@author: Student
"""

def fancy_divide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            print('*')
            raise Exception("0 is err")
            print('22')
    except Exception as ex:
        print('11')
        print('ex=',ex)
def fancy_divide1(list_of_numbers, index):
    try:
        try:
            print('11')
            raise Exception("0 is err")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print('22')
        print('ex=',ex)
#fancy_divide([0, 2, 4], 0)
fancy_divide1([0, 2, 4], 0)