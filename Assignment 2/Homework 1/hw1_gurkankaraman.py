# Where is the last 2 print? Please look other answers or edx test cases. AS.

balance = 4842
annual_interest_rate = 0.2
monthly_payment_rate =0.04
monthly_interest_rate = annual_interest_rate / 12
monthly_payment = monthly_payment_rate * balance
new_balance= (balance - monthly_payment) * (1 + monthly_interest_rate)

for month in range(1, 13):
    monthly_payment = monthly_payment_rate * balance
    balance = (balance - monthly_payment) * (1 + monthly_interest_rate)

    print('Month: ' + str(month))
    print('Minimum monthly payment: ' + str(round(monthly_payment,2)))
    print('Remaining balance: '+ str(round(balance,2)))
    
