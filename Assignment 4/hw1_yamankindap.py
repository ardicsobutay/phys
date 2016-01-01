# Your update hand method has just 1 wrong line :/ It fails all tests. So 6 points for other 2 methods, 1 point for contribution. Please look at the other answers or edx test cases. AS.

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.
    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
  
    score = 0

    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
        
    score = score * len(word)
    
    if len(word) == n:
        score += 50

    return score
   

def displayHand(hand):
    """
    Displays the letters currently in the hand.
    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.
    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.
    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.
    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    
    newHand = {}
    
    for c in word:
        newHand[c] = newHand[c] - 1
    
    return newHand

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    
    if word not in wordList:
        return False
        
    tempHand = dict(hand)
    
    for c in word:
        currentLetterCount = tempHand.get(c, 0)
        if currentLetterCount == 0:
            return False
        else:
            tempHand[c] -= 1
    
    return True
        
        
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    
    length = 0
    
    for (letter, count) in hand:
        length += count
    
    return length
            

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:
    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."
      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """

    score = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print("Current Hand: "),
        displayHand(hand)
        # Ask user for input
        inputWord = raw_input('Enter word, or a "." to indicate that you are finished: ') 
        # If the input is a single period:
        if inputWord == '.':
            # End the game (break out of the loop)
            break
        
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(inputWord, hand, wordList):
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again.")
                print
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score += getWordScore(inputWord, n)
                print('%s earned %d points. Total: %d points.') % (inputWord, getWordScore(inputWord, n), score)
                print
                # Update the hand
                hand = updateHand(hand, inputWord)
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if calculateHandlen(hand) == 0:
        print('Run out of letters. Total score: %d') %score
    else:
        print('Goodbye! Total score: %d') %score

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    n = HAND_SIZE
    command = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:" )
    while command == 'r':
        print("You have not played a hand yet. Please play a new hand first!")
        print
        command = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:" )
    while not (command == 'e'):
        control = 0
        if command == 'n':
            prevHand = dealHand(n)
            hand = playHand(prevHand, wordList, n)
            control = 1
        if command == 'r':
            hand = prevHand.copy()
            control = 1
        if control == 0:
            print("Invalid command.")
        command = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game")
    
    
#Part b after this line:
    
    
def compChooseWord(hand, wordList):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.
    This word should be calculated by considering all possible
    permutations of lengths 1 to HAND_SIZE.
    If all possible permutations are not in wordList, return None.
    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """

    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0

    # Create a new variable to store the best word seen so far (initially None)
    bestWord = None

    # For each word in the wordList
    for word in wordList:

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList) == True:


            # Find out how much making that word is worth
            score = getWordScore(word, n)

            # If the score for that word is higher than your best score
            if score > maxScore:

                # Update your best score, and best word accordingly
                maxScore = score
                bestWord = word

    # return the best word you found.
    return bestWord

def compPlayHand(hand, wordList):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.
    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
    hand: dictionary (string -> int)
    wordList: list (string)
    """
    totalScore = 0
    origHandlen = calculateHandlen(hand)
    while calculateHandlen(hand) > 0:
        print "Current Hand:",
        displayHand(hand)
        word = compChooseWord(hand, wordList)
        if word == None:
            break
        else:
            totalScore = totalScore + getWordScore(word, origHandlen)
            print '"%s" earned %d points. Total: %d points' % (word, getWordScore(word, origHandlen), totalScore)
            hand = updateHand(hand, word)
    print 'Total score: ' + str(totalScore) + ' points.'

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.
    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.
    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.
    4) After the computer or user has played the hand, repeat from step 1
    wordList: list (string)
    """
    n = HAND_SIZE
    control = 0

    while True:
        command = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')

        if command == 'n':
            hand = dealHand(n)
            control = 1
            while True:
                playCommand = raw_input('Enter u for the user to play the hand, or c for the computer to play the hand: ')
                if playCommand == 'u':
                        playHand(hand.copy(), wordList, n)
                        break
                elif playCommand == 'c':
                        compPlayHand(hand.copy(), wordList)
                        break
                else:
                        print "Invalid command."

        elif command == 'r':
            if control == 0:
                print 'You have not played a hand yet. Please play a new hand first!'
            else:
                while True:
                       playCommand = raw_input('Enter u for the user to play the hand, or c for the computer to play the hand: ')
                       if playCommand == 'u':
                           playHand(hand.copy(), wordList, n)
                           break
                       elif playCommand == 'c':
                           compPlayHand(hand.copy(), wordList)
                           break
                       else:
                           print "Invalid command."

        elif command == 'e':
            return
            break
        else:
            print "Invalid command."




