

balance=3329
annualInterestRate=0.2

payment=0
month=0

while month <= 12:
    
    if balance > 0 and month==12:
         payment += 10
         balance=3329
         month=0
    elif balance<=0 and month==12:
        break
    balance = balance - payment
    balance += balance * (annualInterestRate/12.0)  
    month+=1
print "Minimum Payment: {0:.2f}".format(payment)