print "Please enter the outstanding balance on the credit card."
balance = float(raw_input())
print "Please enter the annual interest rate as a decimal."
annualInterestRate = float(raw_input())  

remainingBalance = balance
monthlyInterestRate =  annualInterestRate / 12.0
lowerBound = balance / 12.0
upperBound = (balance * (1 + monthlyInterestRate) ** 12 ) / 12.0
monthlyPayment = (lowerBound + upperBound) * 0.5

while(True):
    remainingBalance = balance
    for month in range(0,12):
        remainingBalance = remainingBalance - monthlyPayment
        remainingBalance =  remainingBalance + (monthlyInterestRate * remainingBalance) 
    if(remainingBalance <= 0 and remainingBalance >= -0.01):
        break
    elif(remainingBalance > 0):
        lowerBound = monthlyPayment
    else:
        upperBound = monthlyPayment
    monthlyPayment = (lowerBound + upperBound) * 0.5           

print('Lowest Payment: '+str(round(monthlyPayment,2)))
