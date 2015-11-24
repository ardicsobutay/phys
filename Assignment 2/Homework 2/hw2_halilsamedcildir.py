


def func(balance, annualInterestRate):
	answer = 0;
	remaining = balance;

	while remaining > 0:
		remaining = balance;
		answer += 10;
		for i in range(0, 12):
			remaining -= answer;
			remaining *= (1 + annualInterestRate / 12);

	print "Lowest Payment: " + str(answer);


func(3329, 0.2)