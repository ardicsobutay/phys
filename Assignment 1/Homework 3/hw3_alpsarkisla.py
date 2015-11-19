

word = raw_input("Please enter a string: ")
middle = len(word)/2
for i in range (middle):
    if word[i] != word[len(word)-i-1]:
        print word ,"is NOT a palindrome"
        break
else:
    print word ,"is a palindrome"
    
