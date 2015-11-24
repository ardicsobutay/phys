# Your answer is entirely true, but you shouldn't use 20.0 for declaring rate. Please look other answers or edx test cases. AS.

balance=3329
annualinterestrate=20.0
payment=-10
remainingbalance=balance

totalpaid=0.0
while remainingbalance>0 :
 payment+=10
 remainingbalance=balance
 for month in range(1,13):
  remainingbalance-=payment
  interest= remainingbalance*annualinterestrate/1200.0
  remainingbalance+=interest

 
print "lowest payment: {0:.2f}" .format(payment)
