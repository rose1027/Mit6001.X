# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

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
        
    
    return True

def printGuessWord(letter,s):
    '''
    if letter is not in s then return '_ '
    else return that letter
    '''
    for e in s:
        if letter == e:
            return letter
    return '_ '
    
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    s = ''
    result = ''

    for c in lettersGuessed:
        if c in secretWord:
            s += c
    for letter in secretWord:
        result += printGuessWord(letter,s)
       
    return result
                
            



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    if lettersGuessed == []:
        return string.ascii_lowercase
    else:
        alpha = string.ascii_lowercase
        for c in lettersGuessed:
            avaletter = alpha.replace(c,'')
            alpha = avaletter
        return avaletter
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('I am thinking of a word that is',len(secretWord),'letters long.')
    totalnum = 8
    print('----------------')
    lettersGuessed = []
    availableLetters = ''
    while totalnum > 0:
        print('You have',totalnum,'guesses left.')
        availableLetters = getAvailableLetters(lettersGuessed)
        print('Available Letters:', availableLetters)
        letter = input("Please guess a letter: ")
        #print('letter= ',letter)
        letterInlow = letter.lower()
        #print('letterinlow= ',letter)
        if letterInlow not in availableLetters:
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed))
            print('-----------')
        else:
            lettersGuessed += letterInlow
            #print('lettersGuessed= ',lettersGuessed)
            #when isWordGuessed == False, it has two results. one is wrong letter, the other is guessed right letter but total guessed letter is not secretWord yet
            if not isWordGuessed(secretWord,lettersGuessed):              
               guess = ''
               #for letterInlow in lettersGuessed:
               if letterInlow in secretWord:
                       guess = getGuessedWord(secretWord,lettersGuessed)
                       print('Good guess:',guess)
                       print('-----------')
                       
               else:
                       totalnum -= 1
                       print('Oops! That letter is not in my word:',getGuessedWord(secretWord,lettersGuessed))
                       print('-----------')
              
            else:
               print('Good guess:',secretWord)
               print('-----------')
               print('Congratulations, you won!')
               break
    if totalnum == 0:
        print('Sorry, you ran out of guesses. The word was',secretWord)
               
            






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
