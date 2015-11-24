# Your answer is entirely true, but you wrote 'balance = 3329' for two times, hard to understand implemtation. Please look other answers. AS.

balance = 3329
annualInterestRate = 0.20
remainingBalance = balance
payment = 0

while (remainingBalance>0):
    balance = 3329
    remainingBalance = balance
    payment += 10
      
    for i in range(1,13):  
        remainingBalance -= payment
        interest = remainingBalance*annualInterestRate/12.0
        remainingBalance +=interest
    
    
print "Lowest payment :",payment