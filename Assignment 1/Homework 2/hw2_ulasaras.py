# result: 9

s = raw_input("Please enter a string >")
i = 0
count = 0
while i < len(s):
    if s[i:i+3] == "bob":
        count +=1
        i += 3
    else:
        i +=1
print "Number of bobs is", count