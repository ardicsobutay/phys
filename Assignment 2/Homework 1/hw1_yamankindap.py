

print "Please enter the outstanding balance on the credit card."
balance = float(raw_input())
print "Please enter the annual interest rate as a decimal."
annualInterestRate = float(raw_input())  
print "Please enter the minimum monthly payment rate as a decimal."
monthlyPaymentRate = float(raw_input())


monthlyInterestRate = (annualInterestRate) / 12.0

month = 1
totalPaid = 0
while month <= 12:
    minimumMonthlyPayment = monthlyPaymentRate * balance
    totalPaid += minimumMonthlyPayment
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    remainingBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    print "Month: " + str(month)
    month += 1
    print "Minimum monthly payment: " + str(round(minimumMonthlyPayment,2))
    print "Remaining Balance: " + str(round(remainingBalance,2))
    balance = remainingBalance
    
print "Total Paid: " + str(round(totalPaid,2))
print "Remaining Balance: " + str(round(remainingBalance,2))