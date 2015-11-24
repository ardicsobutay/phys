

balance = 3329
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
lowestPayment = 10

while True:
    remainingBalance = balance
    for i in range(1, 13):
        remainingBalance -= lowestPayment
        remainingBalance *= 1.0 + monthlyInterestRate
    
    if remainingBalance <= 10.0:
        break
    else:
        lowestPayment += 10

print "Lowest Payment:", lowestPayment