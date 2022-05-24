#build an automatic pizza order program
#baseed on the user's order work out their final bill

# small = 15
# medium = 20
# large = 25
# pep4Small = 2
# pep4Other = 3
# cheese = 1
# price = 0


from pickle import NONE
from queue import Empty
from types import NoneType


print("Welcome to Python Pizza Deliveries! ")
size = input("What size pizza would you like? Small, Medium or Large? ")



small = 15
medium = 20
large = 25
pep4Small = 2
pep4Other = 3
cheese = 1
price = 0
empty = None

#checks to make sure that the pizza option is not null
if(len(size.strip())):
    #Checks the size of the pizza the user intered
    #also prints the subtotal price for the user and starts their running balance
    if (size == 'small' or size =='s'):
        price = small
        print(f"Subtotal: ${price}")
    elif (size == 'medium' or size =='m'):
        price = medium
        print(f"Subtotal: ${price}")
    elif (size == 'large' or size == 'l'):
        price = large
        print(f"Subtotal: ${price}")
    # Checks size and asks if they want to add pep
    addPep = input("Would you like to add pepperoni? ")
    #also checks to make sure that the pizza size has a value and not null
    if(addPep == 'yes' or addPep == 'y' or addPep == 'yea'):
        if len(size.strip()) and size == 'small' or size == 's':
            price += pep4Small
            print(f"Subtotal: ${price}")
        else:
            price += pep4Other
            print(f"Subtotal: ${price}")
    else:
        print(f"Subtotal: ${price}")
    #checks if they want cheese
    extraCheese = input("Do you want to add extra cheese? ")
    if extraCheese == 'yes' or extraCheese == 'y' or extraCheese == 'yea':
            price += cheese
            print(f"Subtotal: ${price}")
    print(f"Your total Bill is: ${price}")
    print("Thank you come again!")
else:
    print(f"Your total Bill is: ${price}")
    print("Thank you come again!")
