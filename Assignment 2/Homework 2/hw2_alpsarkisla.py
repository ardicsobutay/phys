

balance = 3329
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12 
monthlypayment = 0

def canpay(monthlypayment,balance):
    for i in range(12):
        balance = balance - monthlypayment
        balance = balance * (monthlyInterestRate+1)
    if balance <=0:
        return True
    else :
        return False 

while True:
    if canpay(monthlypayment,balance) == True:
        break
    else:
        monthlypayment += 10 

print "Lowest Payment: " + str(monthlypayment)    