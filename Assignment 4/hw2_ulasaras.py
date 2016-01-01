from hw1_ulasaras import *
import time


#
#
# Problem #6: Computer chooses a word
#
#

def isValidWordComp(word, hand):
    """
    Returns True if word is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand.
   
    word: string
    hand: dictionary (string -> int)
    """
    temp = dict(hand)
    for c in word:
        count = temp.get(c,0)
        if count == 0:
            return False
        else:
            temp[c] -= 1
    return True
    
    
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    maxSoFar=0 
    bestSoFar = None
    for word in wordList:
        if isValidWordComp(word, hand):
            score = getWordScore(word, n)
            if score > maxSoFar:
                maxSoFar = score
                bestSoFar = word
    return bestSoFar

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
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
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    totalScore = 0
    while calculateHandlen(hand) > 0:
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)
        if word == None:
            break
        hand = updateHand(hand, word)
        totalScore += getWordScore(word, n)
        print "Word: ", word
        print "Score: ", getWordScore(word, n)
    print "Total Score: ", totalScore

#
# Problem #8: Playing a game
#
#
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
    hand = {}
    while True:
        entry_1 = raw_input("Type 'n' to play a new hand, 'r' to play last hand again, 'e' to exit the game.\n> ")
        if entry_1 not in "ner" or entry_1 == "":
            print "Your input is invalid."
            continue
        if entry_1 == "e":
            break
        if entry_1 == "r" and hand == {}:
                print "You have not played a hand yet, please play with a new hand."
                continue
        entry_2 = raw_input("Type 'c' computer to play, 'u' to play.\n>")
        if entry_2 not in "cu" or entry_2 == "":
            print "Your input is invalid."
            continue
        elif entry_1 == "n":
            hand = dict(dealHand(HAND_SIZE))
        if entry_2 == "u":
            playHand(hand, wordList, HAND_SIZE)
        else:
            compPlayHand(hand, wordList, HAND_SIZE)
        
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


