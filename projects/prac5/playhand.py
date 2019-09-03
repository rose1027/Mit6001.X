# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 10:13:30 2019

@author: Student
"""

def playGame(wordList):
    """ playGame uses try except to catch lack of hand if played without first dealing """
    while True:
        choice = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if choice == 'n':
            hand = dealHand(HAND_SIZE)
        elif choice == 'r':
            pass
        elif choice == 'e':
            break
        else:
            print('Invalid command.')
            continue
        try:
            playHand(hand, wordList, HAND_SIZE)
        except NameError:
            print('You have not played a hand yet. Please play a new hand first!\n')