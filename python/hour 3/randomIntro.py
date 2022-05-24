from cmath import pi
import random
from tokenize import Double

#importing the value from a different module
import myModule

#variable randomInt will have a value between 1 and 10 (whole numbers)
randomInt = random.randint(1,10)
print(randomInt)

#prints the value of pi from the other module that was imported
print(myModule.pi)

#generating a random float from 0.0 to 1.0 exclusive
randomtFloat = random.random()
print(randomtFloat)

#generate and print a random decimal between 0 and 5 inclusive
randomChallenge = float(random.randint(0,5))
print (randomChallenge)

#generates and prints a random decimal between 0 and 5 exclusive
randomChallenge1 = 5 * (random.random())
print (randomChallenge1)

