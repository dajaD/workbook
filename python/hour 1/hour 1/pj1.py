#create a greeting for the program.
#ask the user for the city that they grew up in.
#ask the user for the name of a pet.
#combine the name of their city and pet and show them their band name.
#make sure the input cursor shows on a new line


#creates a variable called greeting which holds the greeting to the user
greeting = "Hello, Let's Choose Your Band Name"
#creates a variable which takes user input
#'\n' puts a new line on the cursor
city = input("What city did you grow up in?\n")
#creates variable called petname that accepts user input
petName = input("What is the name of your pet?\n")
#creates variable bandName which combines the two user inputs
bandName = city+ " " +petName
#prints the greeting
print(greeting)
#prints the users band name
print("The name of your band is: \n" +bandName)