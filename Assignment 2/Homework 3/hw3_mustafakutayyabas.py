#!/usr/bin/python
#Assignment #2 Problem #3
#author Mustafa Kutay Yabas

balance = 320000
annualInterestRate = 0.2
accuracy = 100.0; #change the accuracy for floating digits

result = 0.0
closest = 0.0

maxBalance = balance + balance * annualInterestRate

for monthlyPaymentIndex in range (int(balance/12 * accuracy), int(maxBalance/12*accuracy)):
	tempBalance = balance
	monthlyPayment = 0.0
	monthlyPayment = monthlyPaymentIndex / accuracy

	#print "\n"
	#print monthlyPayment

	for month in range (1,13):
		tempBalance -= monthlyPayment
		tempBalance += tempBalance * (annualInterestRate / 12)
		#print tempBalance

	if (closest == 0 or abs(tempBalance) < closest):
		closest = abs(tempBalance)
		result = monthlyPayment


print "Monthly Lowest Payment", result
#print "Offset at the End", "{0:.2f}".format(closest)