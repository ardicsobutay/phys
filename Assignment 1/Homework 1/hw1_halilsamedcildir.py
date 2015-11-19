

s = raw_input ("Please enter a string: ")
sum = 0

for i in range (len (s)):
 if s[i] == 'o':
  sum += i

print "Sum of indices is " + str(sum)