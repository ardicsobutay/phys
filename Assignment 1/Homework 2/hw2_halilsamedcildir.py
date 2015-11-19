

s = raw_input ("Enter a string: ")

count = 0

i=0
while i < len (s):
 if s[i:i+3] == "bob":
  count+=1
  i+=2
 i+=1
		
	 

print "Number of non-intersecting bobs is: " + str(count)