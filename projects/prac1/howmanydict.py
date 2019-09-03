# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 10:02:46 2019

@author: Student
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
def how_many(aDict):
    '''
     aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    
    '''
    temp = []
    for k in aDict:
        temp.extend(aDict[k])
    #print(temp)
    return len(temp)
        
print(how_many(animals))

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    big = 0
    biggestK = ''
    if aDict == {}:
        return None
    else:
        for k in aDict:
            if(big < len(aDict[k])):
                big = len(aDict[k])
                biggestK = k
        return biggestK
print(biggest(animals))
            