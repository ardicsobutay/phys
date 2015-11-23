

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

totalpaid = 0
monthlyInterestRate = annualInterestRate/12 

for i in range(12):
    minimumpayment = (monthlyPaymentRate) * (balance)
    totalpaid +=  minimumpayment
    balance = balance - minimumpayment
    balance = balance * (monthlyInterestRate+1)
    print "Month: " +str(i+1)
    print "Minimum monthly payment: " + str(round(minimumpayment,2))
    print "Remaining balance: " + str(round(balance, 2))
print "Total paid: " + str (round(totalpaid,2))
print "Remaining balance: " + str(round(balance, 2))