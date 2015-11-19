# It's probably the most inefficent way to summing indices. Please look other answers. AS.

s=raw_input("Enter a string: ")
i=0
count=0
while i<len(s)-1:
    i+=1
    if s[i:i+1]=="o":
        count+=i
print ("Sum of indices is " + str(count))