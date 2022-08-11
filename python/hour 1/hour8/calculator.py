from re import L
from struct import calcsize
from art import logo
import os


#individual operation functions

def add(n1, n2):
    return n1+n2
def sub(n1, n2):
    return n1-n2
def mul(n1, n2):
    return n1*n2
def div(n1, n2):
    return n1/n2

#dictionary that holds all the operants

operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}
#function that will calculate user input
def calc():
    #prints the user logo
    print(logo)
    #variable that accepts the users first number
    fNumber = float(input("What's the first number?: "))
    #for loop that loops through the dictionary and prints each operator available in the calculator
    for op in operation:
        print(op)
    #while true
    while(True):
        #user chooses an operant
        operant = input("Pick an operation: ")
        #user chooses a second number
        sNumber = float(input("What's the second number?: "))
        #vairable holds the 'value' of the dictionary 'key' at the given 'operant'
        operators = operation[operant]
        #the answer of the function stored in variable 'answer
        answer = operators(fNumber, sNumber)
        #print a visual of the equation
        print(f"{fNumber} {operant} {sNumber} = {answer}")
        #asks the user if they want use the previous answer or start over
        redo = input(f"Type 'y' to continue calculating with {answer}, or 'n to start a new calculation:  ")
#     #checks if yes
        if(redo == 'y' or redo == 'Y'):
            #changes the value to the previous answer
           fNumber = answer
        else:
            #clears the screen
            os.system('cls')
            #calls the function again
            calc()
calc()


