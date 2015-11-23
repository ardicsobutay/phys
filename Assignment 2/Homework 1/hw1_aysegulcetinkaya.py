

balance = 4842
annualInterestRate = 0.20
monthlyPaymentRate = 0.04
remainingBalance = balance
totalPaid = 0

for month in range(1,13):
    payment = remainingBalance*monthlyPaymentRate
    remainingBalance -= payment
    interest = remainingBalance*annualInterestRate/12.0
    remainingBalance +=interest
    totalPaid += payment
    
    print "Month: " + str(month)
    print "Minimum monthly payment:{0:.2f} ".format(payment)
    print "Remaining Balance:{0:.2f} ".format(remainingBalance) 
    
print "Total paid: {0:.2f}".format(totalPaid)
print "Remaining Balance: {0:.2f}".format(remainingBalance)