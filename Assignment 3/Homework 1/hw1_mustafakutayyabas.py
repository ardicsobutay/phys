#Read the question first. Test cases should work without editing. Please look other answers or edx test cases. AS.

#!/usr/bin/python
def decay(year):
	halflife = 5.27 #years
	initial = 10.0 #Bq
	remaining = 1 / pow(2, year / halflife) * initial
	return remaining

exposure = 0.0
thisyear = 0.0
for x in xrange(1,6):

	exposure+=thisyear
	thisyear = decay(float(x))
	print "Exposure @ year", x, "=", thisyear, "Bq"
	
	pass

print "Total Exposure =", exposure, "Bq"