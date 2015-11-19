

string = raw_input("Please enter a string:")

counter = 0

for i in range(len(string)):
    if string[i] == "o":
        counter += i

        
print "Sum of indices is: " + str(counter)
