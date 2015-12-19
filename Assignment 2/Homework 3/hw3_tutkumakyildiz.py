# Your answer is entirely true, but you shouldn't use 20.0 for declaring rate. Please look other answers or edx test cases. AS.

balance = 320000
annualInterestRate = 20.0

monthlyInterestRate = annualInterestRate / 1200
lowerBound = balance / 12
upperBound = (balance * (1 + annualInterestRate / 1200) ** 12) / 12
originalBalance = balance
epsilon= 0.01 


while abs(balance) > epsilon:
   
    balance = originalBalance
   
    payment = (upperBound - lowerBound) / 2 + lowerBound

    
    for month in range(12):
        balance -= payment
        balance *= 1 + monthlyInterestRate

    
    if balance > 0:
     
        lowerBound = payment
    else:
       
        upperBound = payment

print "Lowest Payment: {0:.2f}".format(payment)