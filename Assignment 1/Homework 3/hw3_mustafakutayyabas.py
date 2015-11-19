

#!/usr/bin/python
#Assignment #1 Problem #3
#author Mustafa Kutay Yabas
#

#text = "ABBaaBBA";
print "palindrome tester\n"
text = raw_input("Please enter a string: ")
length = len(text)

if (length%2 == 1):
	length -= 1

for i in range(0, length):
	if (text[i] != text[len(text) - 1 - i]):
		print text, 'is not a palindrome'
		break
else:
	print text, 'is a palindrome'