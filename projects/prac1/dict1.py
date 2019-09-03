# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 08:54:40 2019

@author: Student
"""

def lyrics_to_frequency(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

she_loves_you = ['she','loves','you','yeah','yeah','yeah',
                 'she','loves','you','yeah','yeah','yeah',
                 'she','loves','you','yeah','yeah','yeah',
                 
                 'you','think',"you've",'lost','your','love',
                 'well','i','saw','her','yesterday-yi-yay',
                 ]
beatle = lyrics_to_frequency(she_loves_you)
print(beatle)

def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words,best)

(w,b) = most_common_words(beatle)
print((w,b))

def words_often(freqs,minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        #temp is tuple,temp[1] = best
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

print(words_often(beatle,3))
           