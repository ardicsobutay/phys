

s=raw_input("Enter a string: ")
i=0
n=len(s)-1

while i<=(len(s)-1)/2 :
    if s[i]==s[n]:
        n-=1
        i+=1
    else:
        break

if i==n+2 or i==n+1:
    print (str(s)+" is a palindrom")
else:
    print (str(s)+" is not a palindrom")