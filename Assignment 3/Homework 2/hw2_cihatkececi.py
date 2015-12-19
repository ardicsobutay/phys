# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for ch in secretWord:
        if ch not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = ""
    for ch in secretWord:
        if ch in lettersGuessed:
            result = result + ch
        else:
            result = result + "_ "
    return result



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    result = ""
    for ch in string.ascii_lowercase:
        if ch not in lettersGuessed:
            result = result + ch
    return result

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is {0} letters long.".format(len(secretWord))
    leftGuesses = 8
    lettersGuessed = []
    won = False
    while leftGuesses > 0:
        print "You have {0} guesses left.".format(leftGuesses)
        print "Available letters:{0}".format(getAvailableLetters(lettersGuessed))
        guessedLetter = raw_input("Please guess a letter:").lower()
        
        if guessedLetter in lettersGuessed:
            lettersGuessed.append(guessedLetter)
            print "Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed)
            
        elif guessedLetter in secretWord:
            lettersGuessed.append(guessedLetter)
            print "Good guess:", getGuessedWord(secretWord, lettersGuessed)
            
        else:
            lettersGuessed.append(guessedLetter)
            print "Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed)
            leftGuesses -= 1
        
        if isWordGuessed(secretWord, lettersGuessed):
            print "Congratulations, you won!"
            won = True
            break
        else:
            print "------------"
    if not won:
        print "Sorry, you ran out of guesses. The word was '{0}'".format(secretWord)


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
