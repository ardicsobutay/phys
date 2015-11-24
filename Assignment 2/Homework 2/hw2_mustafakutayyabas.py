

#!/usr/bin/python
#Assignment #2 Problem #2
#author Mustafa Kutay Yabas

balance = 3329
annualInterestRate = 0.2

result = 0

maxBalance = balance + balance * annualInterestRate

monthlyPayment = 0;

while 1:
	monthlyPayment+=10
	tempBalance = balance
	for month in range (1,13):

		tempBalance -= monthlyPayment
		tempBalance += tempBalance * (annualInterestRate / 12)


	result = monthlyPayment
	if (tempBalance < 0):
		break

print "Monthly Lowest Payment", result