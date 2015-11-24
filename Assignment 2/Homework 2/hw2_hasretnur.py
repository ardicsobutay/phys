# Your answer is entirely true, but you shouldn't use 20.0 for declaring rate. Please look other answers or edx test cases. AS.

balance=3329
annualInterestRate=20.0



monthlyPayment = 0.0
updatedBalance = balance
while updatedBalance > 0.0:
    updatedBalance=balance
    monthlyPayment += 10
    for month in range(1,13):
        updatedBalance -= monthlyPayment
        updatedBalance *= (1 + (annualInterestRate / 1200))
print("Lowest payment: {0:.2f}".format(monthlyPayment))
