#write a program that interprets the body mass index based on a user's weight and
#height. it should tell the interpretation of their bmi based on the bmi value
#under 18.5 they are underweight
#over 18.5 but below 25 they have normal weight
# over 25 but below 30 they are oberweight1
# over 30 but below 35 they are obese
# above 35 they are clinically obese

height = float(input("Enter your height in m: \n"))
weight = float(input("Enter your weight in kg: \n"))

bmi = float('{0:.2f}'.format(round((weight/(height*height)),2)))

if bmi < 18.5:
    print(f"You're total BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"You're total BMI is {bmi}, you have normal weight.")
elif bmi > 25 and bmi < 30:
    print(f"You're total BMI is {bmi}, you are overweight.")
elif bmi > 30 and bmi < 35:
    print(f"You're total BMI is {bmi}, you are obese.")
else:
    print(f"You're total BMI is {bmi}, you clinically obese.")