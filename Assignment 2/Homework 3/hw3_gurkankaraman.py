# Your answer is wrong. Please look other answers. AS.

first_balance = 320000
annual_interest_rate = 0.2
monthly_interest = annual_interest_rate / 12
low = first_balance/12
high = (first_balance*(1 + monthly_interest)**12)/12
epsilon = 0.01
min_payment = (high + low)/2.0

while min_payment*12 - first_balance >= epsilon:
    for month in range(0, 12):
        balance = (first_balance - min_payment) * (1+monthly_interest)

    if balance < 0:
        low = min_payment
    elif balance > 0:
        high = min_payment
        min_payment = (high + low)/2.0
print ('lowest payment: ' + str(round(balance,2)))