# I tried so hard to get your code together which is not a fair move for other students. Still can't find the getGuessedWord() function. Sorry. AS.


import random
import string

#Change the filename to your word.txt's directory
WORDLIST_FILENAME = "words.txt"



def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

wordlist = loadWords()

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
 
    for c in secretWord:
        if c not in lettersGuessed:
            return False
        return True

def getAvailableLetters(lettersGuessed):
    
    alphabet = 'abcdefghijklmnoprstuvyz'
    availableLetters = ''
    for i in alphabet:
        if c not in lettersGuessed:
            availableLetters +=c
    return availableLetters

def getAvailableLetters(lettersGuessed):
    import string
    strAvailable = ''
    strList = []
    for i in string.ascii_lowercase:
        strList.append(i)
    for letter in lettersGuessed:
        if letter in strList:
            strList.remove(letter)
    strAvailable =strAvailable.join(strList)
    return strAvailable

def hangman(secretWord):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {0:d} letters long".format(len(secretWord)))
    gameOver = False
    guessesLeft = 8
    lettersGuessed = []
    while not gameOver:
        print("-" * 11)
        print("You have {0:d} guesses left".format(guessesLeft))
        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available Letters: {0:s}".format(availableLetters))
        guess = raw_input("Please guess a letter: ")
        guess = guess[0].lower()
        if guess in availableLetters:
            lettersGuessed.append(guess)
            if guess in secretWord:
                response = "Good guess:"
                if isWordGuessed(secretWord, lettersGuessed):
                    gameOver = True
            else:
                guessesLeft -= 1
                response = "Oops! That letter is not in my word:"
                if guessesLeft == 0:
                    gameOver = True
        else:
            response = "Oops! You've already guessed that letter:"
        print("{0:s} {1:s}".format(response, getGuessedWord(secretWord, lettersGuessed)))
    print("-" * 11)
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was {0:s}.".format(secretWord))

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)