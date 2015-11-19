

print "Please enter a string:"

user_string = raw_input()

count = 0

i = 0

while i < len(user_string):
    if user_string[i:i+3] == "bob":
        count += 1
        i += 3
    else:
        i += 1

print "Number of bob is: " + str(count)