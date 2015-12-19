
balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12 
monthlypaymentlow = balance/12
monthlypaymentup = (balance/12.0) * ((1+monthlyInterestRate)**12)
monthlypayment = (monthlypaymentup+monthlypaymentlow)/2

def canpay(monthlypayment,balance):
    for i in range(12):
        balance = balance - monthlypayment
        balance = balance * (monthlyInterestRate+1)
    if round(balance,2) == 0:
        return 0
    elif balance < 0 :
        return -1
    elif balance > 0 :
        return +1


while True:
    
    if canpay(monthlypayment,balance) == 0:
        break
    elif canpay(monthlypayment,balance) == -1 :   
        monthlypaymentup = monthlypayment
    elif  canpay(monthlypayment,balance) == +1 : 
        monthlypaymentlow = monthlypayment
    monthlypayment = (monthlypaymentup+monthlypaymentlow)/2

print "Lowest Payment: " + str(round(monthlypayment,2))
        


