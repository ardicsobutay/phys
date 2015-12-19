def func2(balance, annualInterestRate, monthlyPayment):
	for i in range(0, 12):
		balance -= monthlyPayment;
		balance *= (1 + annualInterestRate / 12);

	return balance;

def func(balance, annualInterestRate):
	low = balance / 12;
	upp = balance * ((1 + annualInterestRate / 12) ** 12) / 12;

	while upp - low >= 0.01:
		if func2(balance, annualInterestRate, (low + upp) / 2) < 0:
			upp = (low + upp) / 2;
		else:
			low = (low + upp) / 2;

	print "Lowest Payment: " + format(low, '.2f');


func(320000, 0.2)