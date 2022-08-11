#greeting
greeting = "Welcome to the Tip Calculator"

#prints greeting
print(greeting)

#takes the user input to see what the total bill was
bill = input("What was the total bill?\n")
#prints the type of the user input
print(type(bill))
#type casts the user input to float
bills = float(bill)
#prints the type of bill
print(type(bills))

#takes user input for the total amount they would like to tip
tipa = input("What percentage tip would you like to give?\n")
#prints the type of the user input
print(type(tipa))
#type casts the user input to float
tips = int(tipa)
#converts tips to percentage
tips = tips / 100
#prints the type of tipa after the type cast
print(type(tips))
#takes user input to see how many people will split the bill
people = input("How many people to split the bill?\n")
#prints the type for people
print(type(people))
#type cast people to int
peoples = int(people)
#prints the type after the type cast
print(type(people))

total = (bills + (bills * tips))/peoples
total = '{0:.2f}'.format(round(total, 2))

print(f"Each person should pay: ${total}")