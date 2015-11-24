# Your answer is wrong. Please look other answers or edx test cases. AS.

balance = 3329
annualInterestRate = 20.0

def pay(balance, interest, payment):
    remainingBalance = balance
    for i in range(1,13):
        remainingBalance -= payment
        interest = remainingBalance*interest/1200.0
        remainingBalance += interest
    return remainingBalance

payment = 10.0
last = pay(balance, annualInterestRate, payment)

while last > 0:
    payment += 10.0
    last = pay(balance, annualInterestRate, payment)

print "Minimum Payment:",payment
