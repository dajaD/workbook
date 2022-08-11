#I was reading this article by Tim Urban - your Life in Weeks and realised
#just how little time we actually have.
#create a program using maths and f-strings that tells us how many
#days, weeks, months we have left if we live until 90 years old.
#it will take your current age as the input and output a message with our
#time left in this format:
#where x, y, and z are replaced with the actual calculated numbers.
#warning your output should match the example output format exactlt,
#even the position of the commas and full stops.

#f-strings are known as Literal String Interpolation.
#makes interpolation simpler
#to create use prefix 'f'. it would be formatted the same way with
#str.format()

#365 days in a year, 52 weeks in a year, and 12 months in one year
#example input: 56
#example output: You have 12410 days, 1768 weeks, and 408 months left


#String input received from user
age = input("What is your current age?:\n")
#cast type age to integer
ag = int(age)

#calculating the number of days remaining until the user reaches 90. stores in 
#variable called ldays
ldays = (365 * 90) - (ag * 365)
#Calculating the number of weeks remaining until the user reaches 90. stores in 
#variable called lweeks
lweeks = (52 * 90) - (ag * 52)
#calculating the number of months remaining until the user reaches 90. stores in variable
#called lmonths
lmonths = (12 * 90) - (ag * 12)

#prints the statment using f-string, calling each variable
print(f"You have {ldays} days, {lweeks} weeks, and {lmonths} months left")


# int mnth
# int dy
# int wek;

# def age(a):
#      mnth = (12*90) - (a * 12)
#      dy = (365 * 90) - (a*365)
#      wek = (52 * 90) - (a * 52)


