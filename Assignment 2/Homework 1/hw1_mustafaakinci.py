# Your answer is entirely true, but you shouldn't use 20.0 or 4.0 for declaring rate. Please look other answers or edx test cases. AS.

balance=4842
annualinterestrate=20.0
monthlypaymentrate=4.0

remainingbalance=balance
totalpaid=0.0

for month in range(1,13):
  payment=remainingbalance*monthlypaymentrate/100.0
  remainingbalance-=payment
  interest= remainingbalance*annualinterestrate/1200.0
  remainingbalance+=interest
  totalpaid += payment
  
  print "month: " + str(month)
  print "minimum monthly payment: {0:.2f} " .format(payment)
  print "remaining balance: {0:.2f} " .format(remainingbalance)
 
print "total paid: {0:.2f}" .format(totalpaid)
print "remainingbalance: {0:.2f}" .format(remainingbalance)

