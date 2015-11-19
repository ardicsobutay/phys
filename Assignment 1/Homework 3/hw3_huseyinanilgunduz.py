

s = raw_input('Please enter a string: ')
palindrome = True
for i in range(len(s)/2):
    if s[i] != s[len(s)-1-i]:
        print s,"is NOT a palindrome"
        palindrome = False
        break
if palindrome == True :
    print s,"is a palindrome"    
        