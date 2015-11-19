# If I delete 2 spesific lines your program still works. Please look other answers. AS.

print "Please enter a string:"

user_string = raw_input()

count = 0

sum = 0

for c in user_string:
    if c == "o":
        sum = sum + count
    
    count = count + 1

print "Sum of indices is " + str(sum)