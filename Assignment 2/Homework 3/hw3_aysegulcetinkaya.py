balance = 320000
annualInterestRate = 0.2
lowerBound = balance / 12.0
upperBound = (balance * ((1.0 + annualInterestRate/12.0)**12))/12.0
payment = (lowerBound + upperBound) / 2.0
remainingBalance = balance

def Unpaid(balance,payment,annualInterestRate):
    
    remainingBalance = balance
    for i in range(1,13): 
        remainingBalance -= payment
        interest = remainingBalance*annualInterestRate/12.0
        remainingBalance +=interest
    return remainingBalance

while(abs(remainingBalance)>0.01):
    remainingBalance = Unpaid(balance,payment,annualInterestRate)
    if (remainingBalance > 0):
        lowerBound = payment
        payment = (lowerBound + upperBound) / 2.0
    else :
        upperBound = payment
        payment = (lowerBound + upperBound) / 2.0
        
print "Minimum monthly payment:{0:.2f} ".format(payment)