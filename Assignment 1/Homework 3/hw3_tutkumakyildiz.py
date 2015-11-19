# Making a copy of str is not nearly efficent.

string1 = raw_input("Enter a string: ")
string2 = string1[::-1]
if string1 == string2:
    print "%s is a palindrome" % (string1)
else:
    print "%s is NOT a palindrome" % (string1)