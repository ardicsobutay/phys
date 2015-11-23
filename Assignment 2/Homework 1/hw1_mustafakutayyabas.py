

#!/usr/bin/python
#Assignment #2 Problem #1
#author Mustafa Kutay Yabas


balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPaid = 0

for month in range(1,13):

	payment = balance * monthlyPaymentRate
	balance -= payment
	totalPaid += payment
	balance += balance * (annualInterestRate / 12)

	print "Month:",str(month)
	print "Paid:","{0:.2f}".format(payment)
	print "Remain:","{0:.2f}".format(balance)

print "\nTotal Paid", "{0:.2f}".format(totalPaid)
print "Balance", "{0:.2f}".format(balance)