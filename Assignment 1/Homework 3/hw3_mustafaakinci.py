

s=raw_input("Please enter a string: ")
is_not_palindrome=False
for i in range(len(s)/2):
	if s[i]!=s[len(s)-i-1]:
		is_not_palindrome =True
		break
if is_not_palindrome:
	print s + " is NOT a palindrome"
else:
	print s + " is a palindrome"

	