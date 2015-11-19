

givenstring = raw_input('Please enter a string:')
lenght = 0
myrange = 0 
lenght = len(givenstring)
myrange = int(lenght/2)
count = 0
i = 0
while givenstring[i] == givenstring[-(i+1)] and i < myrange:
        i +=1
        count +=1 
if count == myrange:
    print ("%s is a palindrome." % givenstring)
else:    
    print ("%s is NOT a palindrome." % givenstring)