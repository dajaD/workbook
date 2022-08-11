import string

#function that accepts user input for the first name and last name
#uses the return and .title()
def formatName():
    fName = input('what is your first name? ')
    lname = input('what is your last name? ')
    fullName = fName.title() + ' ' +  lname.title()
    print(fullName)
    return fullName
#calls function
formatName()
#function that has two parameters: first name and last name
#prints the first and last name
def anotherWay(fname, lname):
    firstName = fname.title()
    lastName = lname.title()
    print(f"{firstName} {lastName}")
#calls the function with paramters
anotherWay("aNOTHEr", "naME")