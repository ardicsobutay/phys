# Your answer is entirely true, but you shouldn't use 20.0 for declaring rate. Please look other answers or edx test cases. AS.

balance = 3329
annualInterestRate = 20.0

remainingBalance=balance
lowestPayment=10.0


while remainingBalance > 0.0:
    for i in range(1, 13):
        unpaidBalance = remainingBalance - lowestPayment
        remainingBalance = unpaidBalance + unpaidBalance * annualInterestRate/1200
    if remainingBalance > 0.0:
        lowestPayment += 10.0
        remainingBalance = balance
            
print "Lowest payment: {0:.2f}".format(lowestPayment)