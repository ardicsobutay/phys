

string=raw_input('Enter a string: ')
num=0
i=0
while i < len(string):
    if string[i:i+3] == 'bob':
        num+=1
        i+=3
    else:
        i+=1
    
print('non_intersecting bobs in the string '+str(string)+' is ' +str(num))
    