

sum = 0
s = raw_input("Please enter a string: ")

for i in range(len(s)):
    if s[i] == 'o':
        sum += i
        
print "Sum of indices is", sum