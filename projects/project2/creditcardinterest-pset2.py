# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 08:52:07 2019

@author: Student
"""

i = 0
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
#newB = 0
while i < 12:
    minPay = balance * monthlyPaymentRate
    unPay = balance - minPay
    Interest = unPay * annualInterestRate/12
    balance = unPay + Interest
    #print("mouth ",i+1,'remaining new balance= ',round(balance,2))
    i += 1
  
    