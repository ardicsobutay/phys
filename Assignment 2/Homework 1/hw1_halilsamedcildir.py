# Where is the last 2 print? Please look other answers or edx test cases. AS.

def func(balance, annualInterestRate, monthlyPaymentRate):
	for i in range(0, 12):
		mmp = balance * monthlyPaymentRate;
		balance -= mmp;
		balance *= (1 + annualInterestRate / 12);

		print "Month: " + str(i + 1);
		print "Minimum monthly payment: " + format(mmp, '.2f');
		print "Remaining balance: " + format(balance, '.2f');



func(4842, 0.2, 0.04)