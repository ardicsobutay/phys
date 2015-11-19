

s = raw_input("Please enter a string >")
count = 0
for i in range(len(s)):
    if s[i] == "o":
        count += i   
print "Sum of indices is", count