from hw1_huseyinanilgunduz import *
import time
def compChooseWord(hand, wordList, HAND_SIZE):
    ourscore = 0
    ourword = None
    for i in wordList:
        if isValidWord(i, hand, wordList)==True:
            if getWordScore(i, HAND_SIZE) > ourscore:
                ourscore = getWordScore(i,HAND_SIZE)
                ourword = i
    return ourword
def compPlayHand(hand, wordList, HAND_SIZE):
    score = 0
    word = compChooseWord(hand, wordList, HAND_SIZE)
    while word != None:
        print 'Current Hand: ',
        displayHand(hand)
        tmp = getWordScore(word, HAND_SIZE)
        score += tmp
        hand = updateHand(hand, word)
        print "\n\"" + str(word) + "\" earned " + str(tmp) + " points. Total: " + str(score) + " points\n"
        word = compChooseWord(hand, wordList, HAND_SIZE)
    else:
        if calculateHandlen(hand)!=0:
            print 'Current Hand: ',
            displayHand(hand)
        print "\nTotal score: " + str(score) + " points."


# Problem #8: Playing a game
#
#
def playGame(wordList):
    flag = 0
    letter = ""

    while letter!="e":
        letter = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if letter == "r":
            if flag == 0:
                print "You have not played a hand yet. Please play a new hand first!\n"
            else:
                letter2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if letter2 == "u":
                    playHand(hand, wordList, HAND_SIZE)
                    flag = 1
                elif letter2 == "c":
                    compPlayHand(hand, wordList, HAND_SIZE)
                    flag = 1
                else :
                    print "Invalid command." 
        elif letter == "n":
            letter2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
            hand = dealHand(HAND_SIZE)
            if letter2 == "u":
                playHand(hand, wordList, HAND_SIZE)
                flag = 1
            elif letter2 == "c":
                compPlayHand(hand, wordList, HAND_SIZE)
                flag = 1
            else :
                print "Invalid command." 
        elif letter!="e":
            print "Invalid command."    
    
    
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
 
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


