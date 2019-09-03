# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:02:38 2019

@author: Student
"""

x = 25
epsilon = 0.01
num_guess = 0
low = 1.0
high = x;
guess = (low + high)/2.0

while abs(guess**2-x) >= epsilon:
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high+low)/2.0
    num_guess += 1
print("number of guess is "+str(num_guess))
print(guess, "is close to ", x)