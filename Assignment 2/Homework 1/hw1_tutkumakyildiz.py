# Your answer is entirely true, but you shouldn't use 20.0 or 4.0 for declaring rate. Please look other answers or edx test cases. AS.

balance=4842
annualInterestRate=20.0
monthlyPaymentMinimum=4.0

remainingBalance=balance
totalPaid=0

for month in range(1, 13):
    payment = remainingBalance * monthlyPaymentMinimum/100.0
    remainingBalance -= payment
    interest = remainingBalance * annualInterestRate/1200.0
    remainingBalance += interest
    totalPaid += payment
    
    print "Month: " + str(month)
    print "Minimum monthly payment: {0:.2f}".format(payment)
    print "Remaining balance: {0:.2f}".format(remainingBalance)
    
print "Total paid: {0:.2f}".format(totalPaid)
print "Remaining balance: {0:.2f}".format(remainingBalance)