#from ps4a import *
from hw1_mustafakutayyabas import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
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
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)

    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = ''
    bestScore = 0
    tempScore = 0
    lenght = len(wordList)


    ## if there is just one letter left it is impossible to construct a word
    if len(hand) < 2:
        return None

    ## if there is not any vowels it is impossible to construct a word
    for letter in hand:
        if letter in list(VOWELS):
            break
    else:
        return None

    ## search words in wordlist
    for word in wordList:
        if lenght % 10000 == 0:
            print 'searching',lenght

        lenght -= 1
        if isValidWord(word, hand, wordList):
            tempScore = getWordScore(word, n)
            if tempScore > bestScore:
                bestWord = word
                bestScore = tempScore
        pass

    if len(bestWord) > 0:
        return bestWord
    else:
        return None

    # For each word in the wordList

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth

            # If the score for that word is higher than your best score

                # Update your best score, and best word accordingly


    # return the best word you found.


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
    
    score = 0
    # As long as there are still letters left in the hand:
    


    while 1:
    # Display the hand
        for letter,times in hand.items():
            for x in xrange(0,times):
                print letter,
                pass

            pass
        print '\n'
        
        compInput = compChooseWord(hand,wordList,n)
        # If the input is a single period:
        if compInput == None:
            break # End the game (break out of the loop)

        print compInput
        tempScore = getWordScore(compInput, n)
        score += tempScore
        print "Score from this word",tempScore
        print "Total Score",score
        hand = updateHand(hand,compInput)

        pass

    print "No More Words!"
    print "Total Score",score
    
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
    # TO DO... <-- Remove this comment when you code this function
    hand = dealHand(HAND_SIZE)

    while 1:

        userInput = raw_input('n for new, r for repeat, e for exit: ')

        if userInput == 'n':
            hand = dealHand(HAND_SIZE)

            userInput = raw_input('u for user, m for The Machine, s for Samaritan: ') 
            if userInput == 'u':
                playHand(hand, wordList, HAND_SIZE)
            elif userInput == 'c' or userInput == 's' or userInput == 'm':
                compPlayHand(hand, wordList, HAND_SIZE)
            else:
                print "Invalid Input"

        elif userInput == 'r':

            userInput = raw_input('u for user, m for The Machine, s for Samaritan: ')
            if userInput == 'u':
                playHand(hand, wordList, HAND_SIZE)
            elif userInput == 'c' or userInput == 's' or userInput == 'm':
                compPlayHand(hand, wordList, HAND_SIZE)
            else:
                print "Invalid Input"

        elif userInput == 'e':
            break
        else:
            print "Invalid Input"

        pass

    print "Good Bye!"

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


