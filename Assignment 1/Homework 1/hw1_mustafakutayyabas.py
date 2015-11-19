# '_' variables are just for special occasions. Don't use them unless you absolutely need this notation. AS.

print "o index summation\n"
text = raw_input("Please enter a string : ")
_sum = 0

for i in range(0, len(text)):
	if (text[i] == 'o'):
		_sum+=i
		
print _sum