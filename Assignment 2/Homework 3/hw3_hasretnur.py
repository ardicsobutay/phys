# Your answer is entirely true, but you shouldn't use 20.0 for declaring rate. Please look other answers or edx test cases. AS.

balance=320000
annualInterestRate=20.0
monthlyInterestRate=annualInterestRate/12.0

upper=(balance*(1+pow(monthlyInterestRate,12)))/12.0
lower=balance/12
epsilon=0.01

def f(x):
    updatedBalance=balance
    
    for month in range(1,13):
        updatedBalance -= x
        updatedBalance *= (1 + (annualInterestRate / 1200))
    return updatedBalance
    
    
while (upper-lower)>epsilon:
    point=(upper+lower)/2
   
        
    if f(point)>0:
        lower=point
    else:
        upper=point
        
if (upper - lower)<epsilon :
        print "lowest payment= {0:.2f}".format(point)
    