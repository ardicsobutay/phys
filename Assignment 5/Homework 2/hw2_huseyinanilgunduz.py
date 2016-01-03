# Applied 3 tests 1 for each method, your program only passed 2 of them. So 6 points for 2 success, 1 point for contribution. Please look at the other answers or edx test cases. AS.


# 6.00x Problem Set 6
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    if len(aStr)==1:
        return aStr
    return reverseString(aStr[1:len(aStr)])+aStr[0]
#

# Problem 4: X-ian
#
def x_ian(x, word):
    if len(x)==0:
        return True;
    elif len(word)==0:
        return False;
    elif x[0]==word[0]:
        return x_ian(x[1:len(x)],word[1:len(word)])
    else:
        return x_ian( x,word[1:len(word)] )
        
        
#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
#I put a space deliberately ,if it is not "\n" but another word after the word,  .
#If there is "\n" it means a new line, no space needed before or after "\n" is needed, I thought.
    if len(text)<=lineLength:
        return text
    index = 0
    for x in range(lineLength-1,len(text)):
        if text[x]==' ':
            index = x
            break 
            
    rev=text[:index]+'\n'+insertNewlines(text[index+1:],lineLength)
    return rev

#Test1
print reverseString("abcdefg")
print ""

#Test2
if x_ian('eric', 'meritocracy'):
    print "TRUE"
else:
    print "FALSE"
print ""
if x_ian('eric', 'cerium'):
    print "TRUE"
else:
    print "FALSE"
print ""

#Test3
print insertNewlines("MERHABA TELEVOLE", 4)