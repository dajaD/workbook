#you are goinbg to write a program that tests the compatibility between two people
#were going to use the super scientific method recommended by buzzfeed.
#take both peopl's name and check for the number of times the letters in the word
#TRUE occurs. then check for the number of times the letters in the word love occurs
#then combine these numbers to make 2 digit number.
#for love scores less that 10 or greater than 90, the message should be:
#"your score is 'x' you go together like coke and mentos".
#your love score is between 40 and 50, the message should be:
#"your score is y, you are alright together"
#otherwise, the message will just be their score. e.g.:
#your score is z

from itertools import count


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#converts the user input string to lower case
name3 = name1 + name2
print (name3)

#method will count the number of times "lo", "o", "v", and "e" appear in the parameter given
#will add the values up and store them in a variable called count
#prints the total value of the variable count
#stores that value to be useed in the scoring method
def counterLove(names):
    print("L: " + str(names.count("l")))
    print("O: " + str(names.count("o")))
    print("V: " + str(names.count("v")))
    print("E: " + str(names.count("e")))
    count = names.count("l") + names.count("o") + names.count("v") + names.count("e")
    print("The total is: " + str(count))
    return str(count)

#method will count the number of times "t", "r", "u", and "e" appear in the parameter given
#will add the values up and store them in a variable called count
#prints the total value of the variable count
#stores that value to be useed in the scoring method
def counterTrue(names):
    print("T: " + str(names.count("t")))
    print("R: "+ str(names.count("r")))
    print("U: " +str(names.count("u")))
    print("E: " +str(names.count("e")))
    count = names.count("t") + names.count("r") + names.count("u") + names.count("e")
    print("The total is: " + str(count))
    return str(count)

#calls the previous methods, and checks the score 
#will print the response according to the love score
def score():
    score1 = counterLove(name3)
    score2 = counterTrue(name3)
    total = (score1) + (score2)
    if (int(total)) < 10 or (int(total)) > 90:
        print(f"your score is {total} you go together like coke and mento")
    elif (int(total)) >= 40 or (int(total)) <= 50:
        print(f"your score is {total}, you are alright together")
    else:
        print(f"your score is: {total}")


score()

# counterTrue(name3)