# from replit import clear
#^^ not able to be used in visual studio
import os
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.")

#determines who the highest bidder is
#function that accepts a parameter bidRecord
def highestBidder(bidRecord):
    #initializes variable highest to zero
    highest = 0
    #initializes variable winner as an empty string
    winner = ""
    #for loop checks for a bidder in the bidrecords
    for bidder in bidRecord:
        #changes the bidamount for every record in the dictionary
        bidAmount = bidRecord[bidder]
        #checks if the bid amount is higher than the bid amount
        if bidAmount > highest:
            #changes the value of higest to the bidamount
            highest = bidAmount
            #changes the name of the bidder to the winner
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}")
#needs to be declared outside of while loop or it will declare every time it is ran
bidders = {}

#creating a function called bidding
def bidding():
    #accepts user string input for the bidders name
    name = input("What is your name? ")
    #accepts user int input for a bidders bid
    bid = int(input("What is your starting bid? $"))
    #adds the user input as a key and value in a dictionary
    bidders[name] = bid
    #prints the value for the dictionary
    #checks to make sure tht the correct values are inputted
    #print(bidders)
    #while true
    while(True):
        #asks the user if there is another bidder
        redo = input("Is there someone else who wants to bid? type Yes or No ")
        #checks if yes
        if(redo == 'yes' or redo == 'Yes' or redo == 'YES'):
            #clears the screen, and calls the bidding function again
            os.system('cls')
            bidding()
        #checks if no
        elif(redo == 'no' or redo =='No' or redo == 'NO'):
            #checks for the highest bidder ----> calls the function
            highestBidder(bidders)
            #breaks out of the while loop
            break
#calls the function bidding            
bidding()