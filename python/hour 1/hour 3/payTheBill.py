#write a program which will select a random name from a list of names
#the person selected will have to pay for everybody's food bill.
#important your are not allowed to use the choice() function
#line 8 splits the string names_string into individual names and puts them
#inside a list called names for this to work you must enter all the names
#as name followed by comma then space, e.g. name, name, name
#example input
#angela, ben, jenny, michael, chloe
#note: notice that there is a space between the command and the next name
#example output
#michael is going to but a meal today!
#hint
#might need to use the len() function

#import random module
import random

#split string method
nameString = input("Give me everybody's name, seperated by a comma. ")
#split() allows you to split a string into separate components 
#this will remove the comma and space between names
#puts everything as a seperate item inside the list
names = nameString.split(", ")

#prints the new list that was created by the user 
#each name is now represented as an element value inlist 'names'
#uses len() to get the length of the list

print("The person who will be responsible for the bill will be "+names[random.randint(0, len(names) - 1)])