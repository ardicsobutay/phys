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
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    # FILL IN YOUR CODE HERE...
    for c in secretWord:
        if c not in lettersGuessed:
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
    guessedWord = ""
    for c in secretWord:
        if c in lettersGuessed:
            guessedWord += c
        else:
            guessedWord += "_"
            
    return guessedWord
    

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    availableLetters = ''
    
    for c in alphabet:
        if c not in lettersGuessed:
            availableLetters += c
            
            
    return availableLetters
    

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
    print('This is a game of Hangman.')
    print('The secret word is '+ str(len(secretWord)) +' letters long.')
    
    lettersGuessed = []
    mistakes = 0
    
    while mistakes < 8:
        availableLetters = getAvailableLetters(lettersGuessed)
        print('-------------')
        print('You have ' + str(8-mistakes) + ' guesses left.')
        print('Available letters: ' + availableLetters)
        guess = raw_input('Please guess a letter: ').lower()
        
        if guess in lettersGuessed:
            print guess +(' has already been guessed. Please pick another letter: ' + getGuessedWord(secretWord, lettersGuessed))
        elif guess in secretWord:
            lettersGuessed += guess
            print('Your guess is right. ' + getGuessedWord(secretWord, lettersGuessed))
            if isWordGuessed(secretWord, lettersGuessed):
              break
        else:
            lettersGuessed += guess
            mistakes += 1
            print guess + (' is not in secret word. ' + getGuessedWord(secretWord, lettersGuessed))

    correct = isWordGuessed(secretWord, lettersGuessed)
    print('---')
    if correct:
        print('You guessed the secret word.')
    else:
        print('You ran out of guesses. The word was ') + secretWord

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

    
