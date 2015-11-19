

s=raw_input("Please enter a string: ")
count=0
i=0
while i<len(s):
	if s[i:i+3]=="bob":
		i+=3
		count+=1
	else :
	 i+=1
print "Number of non-intersecting bob is: "+str(count)		
		
	