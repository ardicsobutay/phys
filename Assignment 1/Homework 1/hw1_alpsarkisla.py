

word = raw_input("Please enter a string: ")
sum_o=0
for i in range (len(word)):
    if word[i] == "o":
        sum_o += i

print "Sum of indices is " + str(sum_o )
    