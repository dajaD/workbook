#you are going to write a program which will mark a spot wwith an x
#the map is made of 3 rows of blank squares
#the program should allow you to enter the position of the treasure using 
#a two digit system. the first digit is the verticle column number and
#the second digit is the horizontal row number. e.g.:
#example input 23
#example output
#[' ', ' ', 'X']
#[' ', ' ', ' ']
#[' ', ' ', ' ']

#this will work as the map
row = [" "," "," "]
row1 = [" "," "," "]
row2 = [" "," "," "]

#creates a list of the map
#nested list called 'map' which holds the three rows.
map = [row, row1, row2]

position = input("where do you want to put the treasure? ")

#splits the string into horizontal and verticle
#map can only use int can't use str needs to be casted
horizontal = int(position[0])
#gives access to the 'selected row'
verticle = int(position[1])

#specifies positions in list
#selects the desired row
# selectedRow = (map[verticle -1])
# #needs to be shifted by one to enure that there is not an issue with index
# #using the selected row, it will then go to the desired column, and change the value to the 'X'
# selectedRow[horizontal -1] = 'X'

#^^^ instead of using the above line of code can simplify as the following 
#this will take the intial list 'verticle -1' and then look for the column in that row/list 'horizontal -1'
map[verticle-1][horizontal-1] = 'X'

#will print a 3x3 square
print(f"{row}\n{row1}\n{row2}")