# Your answer is entirely true, but you shouldn't use 20.0 for declaring rate. Please look other answers or edx test cases. AS.

balance = 320000.0
interest = 20.0

def pay(balance, interestrate, payment):
    remainingBalance = balance
    for i in range(1,13):
        remainingBalance -= payment
        interest = (remainingBalance*interestrate)/1200.0
        remainingBalance += interest
    return remainingBalance

lowerBound = balance/12.0
upperBound = balance*((1+interest/1200.0)**12)

print lowerBound, upperBound

def bisection(a,b,dy):
    remaining = pay(balance, interest, ((a+b)/2.0))
    print remaining, (a+b)/2.0
    if abs(remaining) <= dy:
        return (a+b)/2.0
    if remaining*pay(balance, interest, a) > 0:
        return bisection(((a+b)/2.0), b, dy)
    if remaining*pay(balance, interest, a) < 0:
        return bisection(a ,((a+b)/2.0), dy)

print bisection(lowerBound, upperBound, 0.001)
