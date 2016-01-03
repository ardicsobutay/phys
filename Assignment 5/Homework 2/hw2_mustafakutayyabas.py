# 6.00x Problem Set 6
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    rStr = ""
    if len(aStr) > 0:
        rStr =  reverseString(aStr[1:]) + aStr[0]
    return rStr
    

#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    ###TODO.
    tempX = ""
    jStart = 0;
    for i in xrange(0, len(x)):
        for j in xrange(jStart, len(word)):
            if x[i] == word[j]:
                tempX = tempX + word[j]
                i += 1 #to eliminate unnecessary loop
                jStart = j #to pass previous chars
                break

    print tempX
    if x == tempX:
        return 1
    else:
        return 0


#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    ### TODO.

    counter = 0
    rText = ""

    for char in text:
        rText = rText + char
        counter = counter + 1
        if counter == lineLength:
            rText = rText + "\n"
            counter = 0

    return rText


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