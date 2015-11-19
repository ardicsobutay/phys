

num = 0

s = raw_input("Please enter a string: ")

i = 0
while i < (len(s) - 2):
    if s[i:i+3] == "bob":
        num += 1
        i += 3
    else:
        i += 1
    
print "Number of non-intersecting bobs is:", num