

s = raw_input("Please enter a string: ")

numBobs = 0
i = 0

while i in range(len(s)):
    if s[i:i+3] == "bob":
        numBobs += 1
        i += 3
    else:
        i += 1
           
print 'Number of non-intersecting bobs is:', numBobs