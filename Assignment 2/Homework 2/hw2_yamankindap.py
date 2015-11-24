


# -*- coding: utf-8 -*-
print "Please enter the outstanding balance on the credit card."
balance = float(raw_input())
print "Please enter the annual interest rate as a decimal."
annualInterestRate = float(raw_input())  

monthlyInterestRate = (annualInterestRate) / 12.0
monthlyPayment = 0
remainingBalance = balance
while (remainingBalance>0):
    remainingBalance = balance
    monthlyPayment += 10
    for month in range(0,12):
        remainingBalance = remainingBalance - monthlyPayment
        remainingBalance = remainingBalance + (remainingBalance*monthlyInterestRate)

print "Lowest payment: " + str(monthlyPayment)