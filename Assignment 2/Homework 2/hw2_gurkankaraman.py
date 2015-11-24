# Your answer is wrong. Please look other answers or edx test cases. AS.

balance = 3329
annual_interest_rate = 0.20
monthly_interest_rate = (annual_interest_rate/12)
minimum_monthly_payment = (balance * monthly_interest_rate)
month = 0
while month <= 12:
    balance = ((balance - minimum_monthly_payment) * (1 + monthly_interest_rate))
    month = 1 + month
    if balance <= 0 and month == 12:
        break
    elif balance > 0 and month == 12:
        month = 0
        minimum_monthly_payment + 1.00

print str('Lowest Payment: ' + str(round(minimum_monthly_payment, 2)))