# Making a copy of str is not nearly efficent.

str = raw_input("Please enter a string: ")

#str[::-1] returns the reverse of the string
if str == str[::-1]:
    print str, "is a palindrome."
else:
    print str, "is NOT a palindrome."