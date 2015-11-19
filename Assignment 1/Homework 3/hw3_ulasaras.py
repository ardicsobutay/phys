

s = raw_input("Please enter a string >")
palindrome = True
for i in range(len(s)/2):
    if s[i] != s[-1-i]:
        palindrome = False
        break
if palindrome == True:
    print s, "is a palindrome"
else:
    print s, "is not a palindrome"
