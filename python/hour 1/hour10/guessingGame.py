import random
from art import logo

answer = 0
chances = 0


#function that detemines the number of chances a player will have
def levelDiff():
    #variable that asks the user to choose between hard and easy
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    #if/elif statement that assigns the value of chances based on easy or hard
    if (difficulty == "easy"):
        chances = 10
        return chances
    elif(difficulty == "hard"):
        chances = 5
        return chances

#function that checks the user input to see if it is correct
#takes 3 parameters, guesses, answer, and chances
def checkerAnswer (guesses, answer, chances):
    #tells the user its too low, and removes a chance
    #if the answer is greater than the guess
    if guesses < answer:
        print(f"Too low.")
        return chances - 1
        #tells the user its too low, and removes a chance
    #if the answer is less than the guess
    elif guesses > answer:
        print(f"Too high.")
        return chances - 1
        #tells the user they have the correct answer
    else:
        print("That's correct! Great guess!")

#function that actually runs the game
def startGame():
    #prints the logo
    print(logo)
    #prints the welcome
    print("Welcome to the Number Guessing Game! ")
    print("I'm thinking of a number between 1 and 100. ")
    #chooses a random number and assigns it to answer
    answer = random.randint(1,100)
    #prints the answer 
    print(f"The correct answer is: {answer} ")
    #assigns the chances to variable chances by running function levelDiff()
    chances = levelDiff()
    #initializes guess to have 0 
    guesses = 0
    #while loop that continues as long as guesses is not the correct answer
    while (guesses != answer):
        #prints the users remaining chances
        print (f"You have {chances} attempts remaining to guess the number. ")
        #assigns the caluse of guesses to user input which has been casted as a integer
        guesses = int(input("Make a guess: "))
        #reassigns the value of chances from the above to, check the answer the user input
        chances = checkerAnswer (guesses, answer, chances)
        #checks to see if the user has any chances left
        if chances == 0:
            print("Game over! You ran out of guesses.")
            return
        elif (guesses != answer and chances != 0):
            print("Please Guess Again!")
startGame()
