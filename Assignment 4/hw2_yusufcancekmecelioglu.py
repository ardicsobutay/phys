from hw1_yusufcancekmecelioglu import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def isValidWordforComp(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    tempHand = dict(hand)
    for c in word:
        currentLetterCount = tempHand.get(c, 0)
        if currentLetterCount == 0:
            return False
        else:
            tempHand[c] -= 1
                
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
    
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore=0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = ""
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWordforComp(word,hand,wordList):
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth
            Score =getWordScore(word,n)
            # If the score for that word is higher than your best score
            if Score > maxScore:
                # Update your best score, and best word accordingly
                maxScore=Score
                bestWord = word
    return bestWord
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
    
    totalScore=0
    
    while calculateHandlen(hand) > 0:
    
        print
        print'Current Hand:', displayHand(hand)
        
        inputWord = compChooseWord(hand,wordList,n)

        if compChooseWord(hand,wordList,n) == '':
            break

        totalScore += getWordScore(inputWord,n)
        print'"%s" earned %s points.Total:%s points.' %(inputWord, getWordScore(inputWord,n),totalScore)
        hand = updateHand(hand,inputWord) 
         
               
    
    
    print'Total score: %s points.' %totalScore
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
    HAND_SIZE = 7
    hand = ' '
    while True:

        command = raw_input ('Enter "n" to deal a new hand, "r" to replay the last hand, or "e" to end game:')
        if command == 'e':
            break
        if  command == 'r' and hand == ' ':
            print'You have not played a hand yet. Please play a new hand first!'
        elif command  != 'n' and command  != 'r':
            print 'Invalid command.'
        else:
            command2= raw_input ('Enter "u" to have yourself play, "c" to have the computer play:')
            while command2 != 'u' and command2 != 'c':
                print 'Invalid command.'    
                command2= raw_input ('Enter "u" to have yourself play, "c" to have the computer play:')
            
            
            if command2 == 'u':
                if command == 'n':
                    hand = dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                elif command == 'r':
                    playHand(hand, wordList, HAND_SIZE)
            
                
            if command2=='c':
                if command == 'n':
                    hand = dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, HAND_SIZE)
                    
                elif command == 'r':
                    compPlayHand(hand, wordList, HAND_SIZE)
                         
        
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)

