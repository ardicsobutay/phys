

givenstring = raw_input('Please enter a string:')
count = 0
i = 0 
while i < len(givenstring):
    if givenstring[i:i+3] == "bob":
        count += 1
        i += 3
    else: 
        i += 1       
print "Number of times bob occur is: " + str(count)