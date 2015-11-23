

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12.0
remainingBalance = balance
totalPaid = 0.0

for i in range(1, 13):
    minimumMonthlyPayment = remainingBalance * monthlyPaymentRate
    totalPaid += minimumMonthlyPayment
    remainingBalance -= minimumMonthlyPayment
    remainingBalance = remainingBalance * (1.0 + monthlyInterestRate)
    print "Month:", i
    print "Minimum monthly payment:", round(minimumMonthlyPayment, 2)
    print "Remaining balance:", round(remainingBalance, 2)

print "Total paid:", round(totalPaid, 2)
print "Remaining balance:", round(remainingBalance, 2)