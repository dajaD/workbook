#Write a program that calculates the body mass index from a user's weight and
#and height. The BMI is a measure of someone's weight taking into account
#their height. e.g. If a tall person and a short person both weigh the same
#amount, the short person is usally more overweight.
#The BMI is calculated by diving a person's weight (in kg) by the square of
#their height (in m):

#variable 'weightKG' accepts user input for the weight ---type string
weightKG = input("What is your weight in kg: \n")
#variable 'heightm' acepts user input for the height ---type string
heightm = input("What is your height in m: \n")

#type cast for weightKG assigns to variable to weight
weight = int(weightKG)
#type cast for heightm assigns to variable height
height = float(heightm)

#equation to determine the bmi and assigns it to the variable bmi
bmi = weight / (height*height)

#print the value for bmi after type casting 
print(int(bmi))