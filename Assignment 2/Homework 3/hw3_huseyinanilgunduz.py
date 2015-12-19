

balance = float(raw_input('Please enter balance:'))
annualInterestRate = float(raw_input('Please enter annual Interest Rate:'))

monthintrate = annualInterestRate / 12.0
lowerbound = balance / 12.0
upperbound = balance*((1+monthintrate)**12) / 12.0
setbalance = balance
while upperbound > lowerbound + 0.001:
    middlebound = (lowerbound+upperbound)/2.0
    balance = setbalance
    for i in range(12):
        monthlyunpaidbalance = balance - middlebound
        updatedbalance = monthlyunpaidbalance + monthintrate * monthlyunpaidbalance
        balance = updatedbalance
    if balance > 0.0:
        lowerbound=middlebound
    elif balance < 0.0:
        upperbound=middlebound
    else:
        break
print "Lowest Payment",round(middlebound,2)