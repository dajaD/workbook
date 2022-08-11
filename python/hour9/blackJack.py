############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import os
import random
from secrets import choice
from art import logo

#list of card and their points
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#dictionary that has the face as keys and the value as the points of the cards so the users knows what card they have
cardFaces = {
    "Ace": cards[0],
    "Two": cards[1],
    "Three": cards[2],
    "Four": cards[3],
    "Five": cards[4],
    "Six": cards[5],
    "Seven": cards[6],
    "Eight": cards[7],
    "Nine": cards[8],
    "Ten": {"Ten": cards[9]},
    "Jack": cards[10],
    "Queen": cards[11],
    "King": cards[12],
}

def getCardName(val):
    for key, value in cardFaces.items():
        if val == value:
            return key



def deal_card():
    #choose a random card out the list
    choice = random.choice(cards)
    # print(choice)
    return choice
  
# deal_card()

def restartGame(a: list):
    a.clear()
    a.append(deal_card())
    a.append(deal_card())
    print(a)
    # calculate_score(a)
    return a


#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(a: list):
    score = sum(a)
    blackJack = 21
    if (score == blackJack):
        return 0
    elif(score > blackJack):
        if(11 in set(a)):
            a.remove(11)
            a.append(1)
            print(a)
            calculate_score(a)
    elif(score < blackJack):
        if (score < 17):
            print(f'Drawing another card for {a}, current score {score}, is less than 17')
            a.append(deal_card())
            print(a)
            calculate_score(a)
        else:
            print(f"{a} current score is {score}")
            draw = input('Do you want to draw another card? Yes or No ')
            if(draw == 'yes' or draw == 'Yes'):
                a.append(deal_card())
                print(a)
                calculate_score(a)
    return score

def compare(userScore: list, cpuScore: list):
    # userScore = calculate_score(a)
    # cpuScore = calculate_score(b)
    if (userScore == cpuScore):
        print ("It's a draw!")
    elif cpuScore == 0:
        print ("Computer is the winner!")
    elif userScore == 0:
        print ("User is the winner!")
    elif userScore > 21:
        print ("You went over!")
    elif cpuScore > 21:
        print ("Computer went over!")
    elif userScore > cpuScore:
        print ("You are the winner!")
    else:
        print ("You lose!")

def playGame():
    print (logo)
    #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(f"User cards are {user_cards}")
    print(f"Computer cards are {computer_cards}")
    userScore = calculate_score(user_cards)
    cpuScore = calculate_score(computer_cards)
    compare(userScore, cpuScore)
    while(True):
        restart = input("Do you want to play again? Yes or No? ")
        if (restart == 'Yes' or restart == 'yes'):
            os.system('cls')
            playGame()
        else: 
            print("Goodbye!")
            break
            

playGame()

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. 
# #If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer 
# #has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, 
# #then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.