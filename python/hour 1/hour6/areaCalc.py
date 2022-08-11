#you're painting a wall. the instructions on the paint can says that 1 can of paint
#can cover 5 square meters of wall. given a random height and width of the wall, 
#calculate how many cans of paint you will nbeed to buy.
#number of cans = (wall height * wall width) / coverage per can
#e.g. height = 2, width = 4, coverage = 5
#number of cans = ( 2 x 4) / 5 = 1.6
#but because you can't buy 0.6 of a can of paint the result should be rounded up to 2 cans.
#important: notice the name of the function and the parameters must match those on line for the code
#to work
#hint: make sure you name your function/parameters the same as when it's called on the last 
#line of code.

import math

#creates a function that will calculate the area of the wall
#has 3 parameters height, width, and cover
def paintCalc(height, width, cover):
    #variable total will have the answer to the following math equation
    #math equation gives the total number of cans needed to paint the wall
    #calls math module which has the ceil(), ceil() will round up
    total = math.ceil((height * width) / cover)
    #prints the answer
    print(f"You'll need {total} cans of paint")

#accepts user input to get the height and the width
testH = int(input("What is the height of the wall: "))
testW = int(input("What is the Width of the wall: "))
#assigns the coverage to 5
coverage = 5
#calls the function
paintCalc(height = testH, width = testW, cover = coverage)