# Your answer is wrong, and I can't fix it or understand what you are trying because of magic numbers '0.18?!'. You should avoid using undescriptive declarations. And where is the last 2 print? Please look other answers or edx test cases. AS.

balance = 4842
annual_interest_rate = 0.2
monthly_payment_rate = 0.04

for i in range(0,12):
    minimum_monthly_payment = monthly_payment_rate*balance
    balance = balance - minimum_monthly_payment
    remaining_balance = balance + balance*0.18/12
    balance = remaining_balance
    
    print "Month:", i
    print "Minimum Monthly Payment:", round(minimum_monthly_payment,2)
    print "Remaining Balance:", round(remaining_balance,2)
    print "------------------------------"