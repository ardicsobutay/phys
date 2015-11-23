

balance = float(raw_input('Please enter balance:'))
annualInterestRate = float(raw_input('Please enter annual Interest Rate:'))
monthlyPaymentRate = float(raw_input('Please enter monthly Payment Rate:'))

monthintrate = annualInterestRate / 12.0
totalpaid=0.0
for i in range(12):
    minmonthpay = monthlyPaymentRate * balance
    monthlyunpaidbalance = balance - minmonthpay
    updatedbalance = monthlyunpaidbalance + monthintrate * monthlyunpaidbalance
    balance = updatedbalance
    totalpaid += minmonthpay
    print "Month:",i+1,"\nMinimum monthly payment:",(round(minmonthpay,2)),"\nRemaining balance:",(round(updatedbalance,2))
print "Total paid:",(round(totalpaid,2)),"\nRemaining balance:",(round(updatedbalance,2))