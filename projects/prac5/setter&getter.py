# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 22:02:28 2019

@author: Student
"""

class Mine():
    def __init__(self, deep):
        self.deep = deep

    @property
    def deep(self):
        if self.__deep > 1000:
            return 1000
        return self.__deep

    @deep.setter
    def deep(self, deep):
        if deep > 2000:
            self.__deep = 2000
        elif deep <= 0:
            self.__deep = 0
        else:
            self.__deep = deep

# and try it out by creating an instance 
SilverDollar = Mine(-400)
print(SilverDollar.deep)
SilverDollar.deep = 5055
print(SilverDollar.deep)