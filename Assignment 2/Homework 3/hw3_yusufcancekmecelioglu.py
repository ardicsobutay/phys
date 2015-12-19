# Your answer is wrong. Please look other answers. AS.

firstbalance=320000
annualInterestRate=0.2
monthlyInterestRate = annualInterestRate / 12.0
low = firstbalance/12
high = (firstbalance*(1 + monthlyInterestRate)**12)/12.0
dy=0.001
payment=0

def func(payment):
    balance=firstbalance 
    month=0
    while month <= 12:
        balance = balance - payment
        balance += balance * monthlyInterestRate 
        month+=1
    return balance
def solve(f, a, b, dy):
    middle = (a + b) / 2.0
    value = f(middle)
    
    if value <= dy:
        return middle

    valueAtA = f(a)
    
    if valueAtA * value < 0:
        return solve(f, a, middle, dy)
    else:
        return solve(f, middle, b, dy)

print "Minimum Payment: {0:.2f}".format(solve(func, low, high, dy))