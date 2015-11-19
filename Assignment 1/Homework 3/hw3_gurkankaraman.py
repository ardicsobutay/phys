

string =raw_input('Enter your string: ')
c=0

for  i in range (len(string)):
    if string[i] == string[-(i+1)]:
        c=c+1
if c == len(string):
     print(str(string) + ' is a palindrom')
else:
    print(str(string) + ' is not a palindrom')