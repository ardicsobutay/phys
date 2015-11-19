

string = raw_input("Please enter a string: ")
 
son = -1

palindrome = True

for i in range(len(string)/2):
    
    if string[i] != string[son]:
        palindrome = False
        break
        
    son -= 1
 
if palindrome:
    print string, "is a palindrome."

else:
    print string, "is NOT a palindrome."
