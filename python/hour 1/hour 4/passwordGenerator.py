import random

lttrs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nmbrs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
smbls = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator! ")
letters = int(input("How many letters would you like your password?\n "))
symbs = int(input("How many symbols would you like?\n "))
nums = int(input("How many numbers would you like?\n "))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#empty list called password, which will accept the user input
password = []
#function to get the letters that will be in the password
def alpha(numbers):
    #for loop goes through the index starting at 0, and ends at the last number
    for num in range(0, numbers):
        #adds the randomly generated choices from the list to the empty password list
        password.append(random.choice(lttrs))

def nus(numbers):
    for num in range(0, numbers):
        password.append(random.choice(nmbrs))
        
def syms(numbers):
    for num in range(0, numbers):
        password.append(random.choice(smbls))

#calls all the functions to create the password
def generate():
    alpha(letters)
    syms(symbs)
    nus(nums)
    
generate()
#join() converts the list to a string
#can use this as all the elements are strings. 
passwor = ''.join(password)
print(f"Here is your password: {passwor}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#uses the random() function and the shuffle method which takes a list and shuffles the order
random.shuffle(password)
#changes it to a str from list
passwo = ''.join(password)
print(passwo)