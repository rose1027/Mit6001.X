# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 08:08:23 2019

@author: Student
"""

def genPrimes():
    guess = 3
    p = [2]
    yield(p[0])
    while True:
# =============================================================================
#         if all(guess%e!=0 for e in p):
#             p.append(guess)
# =============================================================================
        p = [guess for e in p if guess % e !=0]
        yield(guess)       
        guess+=2
            
generator = genPrimes()
print(generator.__next__())
#generator.next()
    
        
    