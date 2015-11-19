# '_' variables are just for special occasions. Don't use them unless you absolutely need this notation. AS.

#!/usr/bin/python
#Assignment #1 Problem #2
#author Mustafa Kutay Yabas
#
print "bob finder\n"
#text = "aaabobobabobaaabobbob"
text = raw_input("Please enter a string: ")
catch = "bob"
_c  = 0

i = 0;
while i < len(text) - len(catch) + 1:
	if (text[i]+text[i+1]+text[i+2] == catch):
		_c+=1
		i+=2
	i+=1

print _c