#game of rock papaer scissors
import random



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#randomly chooses either rock paper or scissors for the computer
#using random import with .radint and a range of 0 and 2 inclusive
#to make sure all choices are accounted for.
def cpu():
    cpu = random.randint(0,2)
    if cpu == 0:
        cpu = rock
    elif cpu == 1:
        cpu = paper
    else:
        cpu = scissors
    print("Computer Chose: " + cpu)
    return cpu

#function to determine the winner
def winner(user, cu): 
    if user == cu:
        print("Its a tie! ")
    elif ((user == rock and cu == scissors) or (user == paper and cu == rock) or (user == scissors and cu == paper)):
        print("You Win! ")
    else:
        print("You Lose! ")

#function to choose the users choice.
def rps():
    #takes user input for rock, paper, or scissors and stores the input in a variable with data type int called RPS
    RPS = int(input("What do you choose? type 0 for Rock, 1 for Paper, or 2 for Scissors "))
    #checks value of user input to convert rps to either string rock, paper, or scissors
    if RPS == 0:
        RPS = rock
    elif RPS == 1:
        RPS = paper
    elif RPS == 2:
        RPS = scissors
    else:
        print("\nThat's not a choice! ")
    #prints the value of the user input
    print(f"\nYou Chose: {RPS}")
    #stores the value of RPS in variable rps to be used again
    return RPS
winner(user = rps(), cu = cpu())