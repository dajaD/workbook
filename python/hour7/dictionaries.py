programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    123: "The action of doing something over and over again. ",
}
#^^ ideal structure. 

#prints the value of the keys
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])
print(programming_dictionary[123])

#add new entry to the dictionary
programming_dictionary["key4"] = "definition: the action of doing something over and over again"
#prints all the keys and values of the dictionary
print(programming_dictionary)


#creating an empty dictionary
empty_dictionary = {}
print(empty_dictionary)

#wiping an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#edit an existing dictionary
programming_dictionary["Bug"] = 'A moth in your computer'
print(programming_dictionary)

#loop through a dictionary 
for something in programming_dictionary:
    #prints the keys only
    print(something)
    #prints the value only
    print(programming_dictionary[something])
