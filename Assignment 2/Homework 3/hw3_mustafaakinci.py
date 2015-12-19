# Your answer is entirely true, but you shouldn't use 20.0 for declaring rate. Please look other answers or edx test cases. AS.

balance=32000
annualinterestrate=20.0
lowerbound=balance/12
upperbound=balance*((1+annualinterestrate/1200)**12)/12
remainingbalance=balance
payment=0.0
totalpaid=0.0
while upperbound-lowerbound>=0.1:
 payment=(lowerbound+upperbound)/2
 remainingbalance=balance
 for month in range(1,13):
  remainingbalance-=payment
  interest= remainingbalance*annualinterestrate/1200.0
  remainingbalance+=interest
 if remainingbalance<0:
  upperbound=payment
 else:
  lowerbound=payment
 
print "lowest payment: {0:.2f}" .format(payment)
