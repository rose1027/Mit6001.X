# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:40:47 2019

@author: Student
"""

x = 23
#x = 23, it will print fail!!!, the abs(guess**2-x) >= epsilon will always be true!!
epsilon = 0.01
step = 0.1
guess = 0.0
num_guess = 0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
        num_guess += 1
        print("guess= "+str(guess))
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
print("number of guess= ",num_guess)