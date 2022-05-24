print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))


if height >= 120:
    print('You can ride')
    age = int(input("How old are you?\n"))
    price = 5
    if age < 12:
        print(f"Your total is ${price} for a child ticket")
    elif age <= 18:
        price = price + 2
        print(f"your total is ${price} for a youth ticket")
    elif (age >= 18 and age >= 45 and age <= 55):
        price = 0
        print(f"Your total is ${price} your ticket is on us!")
    elif (age >= 18):
        price = price + 7
        print(f"Your total is ${price} for an adult ticket")
    photo = input("Do you want to take photos? ")
    if(photo == 'yes' or photo == 'y'):
        price += 3
        print(f"That will be ${price}")
    print(f"The total bill is: ${price}")
else:
    print('can\'t ride')

    #added f string to use to keep track of each individuals bill