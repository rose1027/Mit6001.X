# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 21:10:35 2019

@author: Student
"""

low = 0
high = 100
guess = 0
print('Please think of a number between 0 and 100!')
while low <= high:
    guess = int((low + high)/2)
    print('Is your secret number ',guess,'?')
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",end=' ')
    userIn = input('')
    if userIn == 'h':
        high = guess
    elif userIn == 'l':
        low = guess
    elif userIn == 'c': 
         print('Game over. Your secret number was:',guess)
         break
    else:
        print('Sorry, I did not understand your input.')        
       