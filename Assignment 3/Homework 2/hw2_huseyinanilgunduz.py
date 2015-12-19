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
    aim=0
    for i in range(len(secretWord)):
        for j in range(len(lettersGuessed)):
            if (secretWord[i] == lettersGuessed[j]):
                aim+=1
                break
    if (aim == len(secretWord)):
        return True
    else:
        return False
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    finalstring=''
    if (lettersGuessed==''):
        for i in range(len(secretWord)):
            finalstring += '_'
        return finalstring
    for i in range(len(secretWord)):
        aim=0
        for j in range(len(lettersGuessed)):
            if (secretWord[i] == lettersGuessed[j]):
                finalstring += secretWord[i]
                break
            else:
                aim+=1
            if (aim == len(lettersGuessed)):
                finalstring += '_'
    return finalstring
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    allletters = 'abcdefghijklmnopqrstuvwxyz'
    notguessed = ''
    if (lettersGuessed==''):
        return allletters
    for i in range(len(allletters)):
        aim = 0
        for j in range(len(lettersGuessed)):
            if (allletters[i] == lettersGuessed[j]):
                break
            else:
                aim += 1
            if (aim == len(lettersGuessed) ):
                notguessed += allletters[i]
    return notguessed
    
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
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is',len(secretWord),'letters long.'
    lettersGuessed=''
    guessnumber=8
    while (isWordGuessed(secretWord, lettersGuessed)==False):
        if (guessnumber>0):
            available= getAvailableLetters(lettersGuessed)
            print '-------------'
            print 'You have',guessnumber,'guesses left.'
            print 'Available Letters:',available
            guess = raw_input('Please guess a letter:')
            guessInLowerCase = guess.lower()
            aim=0
            gw1 = getGuessedWord(secretWord, lettersGuessed)
            for i in range(len(available)):
                if (available[i]==guessInLowerCase):
                    lettersGuessed += guessInLowerCase
                    gw2 = getGuessedWord(secretWord, lettersGuessed)
                    if (gw1 == gw2):
                        print 'Oops! That letter is not in my word:',gw2
                        guessnumber-=1
                    else :
                        print 'Good guess:',gw2
                    aim=1
                    break
            if (aim==0):
                print "Oops! You've already guessed that letter:",gw1
        else:
            print '------------' 
            print 'Sorry, you ran out of guesses. The word was else.'
            break
    if (isWordGuessed(secretWord, lettersGuessed)==True):
        print '------------' 
        print 'Congratulations, you won!'

    return None
        

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
