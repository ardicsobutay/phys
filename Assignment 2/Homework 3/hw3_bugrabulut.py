# Your answer is wrong. Please look other answers. AS.

balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12

count = 0
maxCount = 50

tolerance = 0.01

lowerBound = balance / 12
upperBound = (balance*pow((1+monthlyInterestRate), 12))/12

def f(x):
    remainingBalance = balance
    for i in range(1, 13):
        unpaidBalance = remainingBalance - x
        remainingBalance = unpaidBalance + unpaidBalance * annualInterestRate/1200
    return remainingBalance

while count <= maxCount:

    newPoint = (lowerBound + upperBound) / 2

    if f(newPoint) == 0 or (upperBound - lowerBound)/2 < tolerance:
        print "Lowest Payment: " + str(newPoint)
        break
        
    count += 1
    
    if f(newPoint)/lowerBound > 0:
        lowerBound = newPoint
    else:
        upperBound = newPoint

if (upperBound - lowerBound)/2 >= tolerance:
    print "Please increase maxCount and try again"
