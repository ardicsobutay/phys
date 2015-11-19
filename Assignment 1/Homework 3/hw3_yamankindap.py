# Making a copy of str is not nearly efficent.

print "Please enter a string:"

user_string = raw_input()

half = len(user_string)/2

firstHalf = user_string[0:half]

if len(user_string)%2 == 0:
    secondHalf = user_string[half:len(user_string)]
else:
    secondHalf = user_string[half+1:len(user_string)]
y=""
for c in range(half):
    x = secondHalf[half-1-c]
    y = y + x
if y == firstHalf:
    print user_string + " is a palindrome."
else:
    print user_string + " is NOT a palindrome."