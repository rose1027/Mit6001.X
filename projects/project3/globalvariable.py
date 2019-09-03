# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:05:38 2019

@author: Student
"""



def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    for c in secretWord:
        if c not in lettersGuessed:
            return False
        else:
            global le
            le = ''
            le += c
            return False
    
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    #result = ''
    if not isWordGuessed(secretWord, lettersGuessed):
        global le
        le += '_ '
    else:
        return secretWord
        

        
secretWord = 'apple' 
lettersGuessed = ['a', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord,lettersGuessed))
            
        
            
                   
       
           
          
   