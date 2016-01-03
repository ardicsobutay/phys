# Applied 3 tests 1 for each method, your program only passed 2 of them. So 6 points for 2 success, 1 point for contribution. Please look at the other answers or edx test cases. AS.

# -*- coding: utf-8 -*-
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
    
    if len(aStr)==1:
        return aStr
    else:
        return aStr[::-1]

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
    if len(x)==1:
        if x in word:
            return True
        else:
            return False
    else:
        if x[0] in word:
            i=word.find(x[0])
            return x_ian(x[1:],word[i+1:])
        else:
            return False
        

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
    text=text.split()
    if len(text) <= lineLength:
        return text

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
        