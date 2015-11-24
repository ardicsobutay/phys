# Your answer is entirely true, but you shouldn't use 20 for declaring rate. Please look other answers or edx test cases. AS.

balance = 3329
annualInterestRate = 20

monthlyPayment = 10
monthlyInterestRate = annualInterestRate/1200.0
newbalance = balance - 10


while newbalance > 0:
    monthlyPayment += 10
    newbalance = balance
    month = 0

    while month < 12 and newbalance > 0:

        month += 1
        interest = monthlyInterestRate * newbalance
        newbalance -= monthlyPayment
        newbalance += interest

    newbalance = round(newbalance,2)


print " Lowest Payment:", monthlyPayment
