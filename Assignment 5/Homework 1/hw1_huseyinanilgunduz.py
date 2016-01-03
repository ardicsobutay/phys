# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    coder = {}
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase    
    for i in lower:
        coder[i] = lower[(lower.index(i)+shift)%26]
    for i in upper:
        coder[i] = upper[(upper.index(i)+shift)%26]
    return coder  
    
def applyCoder(text, coder):
    ourstr = ""
    for i in text:
        if i in coder:
            ourstr += coder[i]  
        else:
            ourstr += i
    return ourstr          

def applyShift(text, shift):
    return applyCoder(text, buildCoder(shift))       

# Problem 2: Decryption
def findBestShift(wL, text):
    letters = string.ascii_letters
    count1 = 0
    num = 0
    for i in range(26):
        text1 = applyShift(text, i)
        wordsintext1 = text1.split()
        count2 = 0
        for word in wordsintext1:
            word1 = ""
            for c in word:
                if c in letters:
                    word1 += c
            if word1 in wL:
                count2 += 1
        if count2>count1:
            count1 = count2
            num = i
    return num     

def decryptStory():
    story = getStoryString()
    bestShift = findBestShift(loadWords(), story)
    return applyShift(story, bestShift)    
#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    print s
    bestShift = findBestShift(wordList, s)
    print applyShift(s, bestShift) == 'Hello, world!'
    print decryptStory()
