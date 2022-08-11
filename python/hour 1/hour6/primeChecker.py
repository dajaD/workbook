#prime numbers are numbers that can only be cleanly divided by itself and 1. 
#write a function that checks whether if the number passed into it is a prime number or not. 
#e.g. 2 is a prime number, because it is only divisible by 1 and 2.
#but 4 is not a prime number because you can divide it by 1,2, or 4.
#
def primeChecker(number):
    prime = True
    #checks through all the numbers starting at 2, until 'number' to see if it has clean division
    for num in range(2, number):
        if number % num == 0:
           prime = False
    #checks to see if the number input by the user is a prime number
    if prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
            
    

n = int(input("Check this number: "))
primeChecker(number = n)