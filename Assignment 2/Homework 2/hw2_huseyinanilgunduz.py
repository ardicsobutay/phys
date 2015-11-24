

balance = float(raw_input('Please enter balance:'))
annualInterestRate = float(raw_input('Please enter annual Interest Rate:'))

monthintrate = annualInterestRate / 12.0
lowestpayment=0
balanceset=balance
while balance>0:
    balance=balanceset
    lowestpayment+=10
    for i in range(12):
        monthlyunpaidbalance = balance - lowestpayment
        updatedbalance = monthlyunpaidbalance + monthintrate * monthlyunpaidbalance
        balance = updatedbalance
print "Lowest Payment:",lowestpayment