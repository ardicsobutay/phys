# Your code works, but you shouldn't use 20.0 or 4.0 for declaring rate. And you forget to round results to 2 number floating point. And where is the last 2 print. Please look other answers or edx test cases. AS.

balance = 4842
annualInterestRate = 20.0
monthlyPaymentRate = 4.0
remainingBalance = balance
totalPayment = 0

for i in range(1,13):
    payment = remainingBalance*monthlyPaymentRate/100.0
    remainingBalance -= payment
    interest = remainingBalance*annualInterestRate/1200.0
    remainingBalance += interest
    totalPayment += payment

    print "Month: ", i
    print "Remaining Balance: ", remainingBalance
    print "Total Payment: ", totalPayment
