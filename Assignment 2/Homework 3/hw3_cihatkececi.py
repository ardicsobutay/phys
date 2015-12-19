

# -*- coding: utf-8 -*-
balance = 320000
annualInterestRate = 0.2
tolerance = 0.01
monthlyInterestRate = annualInterestRate / 12.0
lowestPaymentUpperBound = balance * (pow(1 + monthlyInterestRate, 12)) / 12.0
lowestPaymentLowerBound = balance / 12.0
lowestPayment = 0.0

while True:
    remainingBalance = balance
    lowestPayment = (lowestPaymentUpperBound + lowestPaymentLowerBound) / 2.0
    for i in range(1, 13):
        remainingBalance -= lowestPayment
        remainingBalance *= (1.0 + monthlyInterestRate)
    if abs(remainingBalance) <= tolerance:
        break
    else:
        if remainingBalance < 0.0:
            lowestPaymentUpperBound = lowestPayment
        else:
            lowestPaymentLowerBound = lowestPayment

print "Lowest Payment:", round(lowestPayment, 2)