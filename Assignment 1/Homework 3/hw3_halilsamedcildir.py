

s = raw_input ("Enter a string: ")

isPal = True

for i in range (len (s)/2):
 if s[i] != s[len(s) - 1 - i]:
  isPal = False
  break

if isPal:
 print s + " is a palindrome"
else:
 print s + " is NOT a palindrome"