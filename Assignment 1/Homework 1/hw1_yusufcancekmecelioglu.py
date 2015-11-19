

givenstring = raw_input('Please enter a string:')
sum = 0
for i in range(len(givenstring)):
    if givenstring[i] == 'o':
        sum += i
print ("Sum of the indices: %s" % sum) 
