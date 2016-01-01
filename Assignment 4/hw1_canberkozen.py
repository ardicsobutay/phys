# Test file has 3 tests, your program only passed 1 of them. So 3 points for 1 success, 1 point for contribution. Please look at the other answers or edx test cases. AS.

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def loadWords():
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
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

# (end of helper code) -----------------------------------------------------------------

def getWordScore(word, n):
    score = 0

    for harf in word:
        score += SCRABBLE_LETTER_VALUES[harf]

    score *= len(word)

    if len(word) == n:
        score += 50

    return score
    

def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line
    

def dealHand(n):
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
    temporary_hand = dict(hand)
    


def isValidWord(word, hand, wordList):
    if not word in wordList:
        return False

    for harf in hand:
        if not harf in word:
            return False

    return True
    

def calculateHandlen(hand):
    return sum(hand.values())
    

def playHand(hand, wordList, n):
    score = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print "hand: ",displayHand(hand)
        # Ask user for input
        word = raw_input('enter a word, or "." to end the game:')
        # If the input is a single period:
        if word == '.':
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(word, hand, wordList):
                # Reject invalid word (print a message followed by a blank line)
                print "invalid word, rejected.\n"
            # Otherwise (the word is valid):
            else:
                word_score = getWordScore(word, n)
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score += word_score
                print word_score, "points earned. ", "total score is", score, ".\n"
                # Update the hand
            
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if calculateHandlen(hand) == 0:
        print "game is over. your total score is ", score

def playGame(wordList):
    hand = None

    while True:
        user_input = raw_input("enter n to play a new hand, r to replay the last hand, or e to exit the game:" )

        if user_input == 'n':
            hand = dealHand(7)
            playHand(hand, wordList, 7)
        elif user_input == 'r':
            if hand is not None:
                playHand(hand, wordList, 7)
            else:
                print "you have no hand. please enter n to play a new hand."
        elif user_input == e:
            break
        else:
            print "invalid input"


if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)