

s = str(raw_input("Please enter a string: "))

c = 0

if len(s) <= 1:
    print str(s) + " is a palindrome."
else:
    for i in range(len(s)/2):
        if s[i] == s[i - ( 2*i + 1 )]:
            c += 1

    if c == len(s)/2:
        print str(s) + " is a palindrome."
    else:
        print str(s) + " is NOT a palindrome."