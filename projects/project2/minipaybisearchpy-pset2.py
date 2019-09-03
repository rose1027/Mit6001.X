# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:02:59 2019

@author: Student
"""

balance = 320000
annualInterestRate = 0.2
newbalance = balance
lowpay = balance/12
highpay = (balance*(1+annualInterestRate/12)**12)/12

epsilon = 0.01

while abs(newbalance) > epsilon:
    minipay = (lowpay + highpay)/2
    print('low=',lowpay,'high=',highpay,'minipay=',minipay)
    i = 0 
    newbalance = balance
    while i < 12:
        unPay = newbalance - minipay
        Interest = unPay * annualInterestRate/12
        newbalance = unPay + Interest
        i += 1
    print('after a year ',newbalance)
        
    #guess to small
    if newbalance > epsilon :
            lowpay = minipay
    #guess too big
    elif newbalance < -epsilon:
            highpay = minipay
    else:
        break
print('Lowest Payment: ',round(minipay,2))
        
        

   
    