# Program is not working properly. I can't fix it even if I change 3 or more rows. AS.

x=raw_input()
bobs=0

for i in range(0,len(x)-2):
    if x[i]=="b" and x[i+1]=="o" and x[i+2]=="b":
        bobs+=1
        if x[i-1]=="o" and x[i-2]=="b":
            bobs-=1

print bobs