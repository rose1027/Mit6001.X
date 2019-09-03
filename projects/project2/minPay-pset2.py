# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:51:18 2019

@author: Student
"""


balance = 3329
annualInterestRate = 0.2
newbalance = balance
minPay = 10
while newbalance > 0:
    i = 0 
    newbalance = balance
    while i < 12:
        unPay = newbalance - minPay
        Interest = unPay * annualInterestRate/12
        newbalance = unPay + Interest
        print('balance= ',round(newbalance,2))
    #print("mouth ",i+1,'remaining new balance= ',round(balance,2))
        i += 1
    if newbalance < 0:
       print('Lowest Payment: ',minPay)
    else:
        minPay += 10
        print('Lower Payment: ',minPay)
#print('Lowest Payment: ',minPay-10)   


   
