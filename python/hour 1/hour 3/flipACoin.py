#virtual coin toss program. this will randomly tell the user heads or tails
#the first letter should be capitalised and spelt exactly like in the example
#there are many ways to do this but to pratice what we learnt in the last lesson
#you should generate a random number either 0 or 1. then use that number to print
#out heads or tails.
#1 should mean heads, 0 should mean tails
#hint: remember to import the random module first

#imports the random module
import random

#variable cointoss has random value of either 0 or 1
coinToss = random.randint(0,1)
#prints head or tails depending on the value
if coinToss == 0:
    print("Heads")
else:
    print("Tails")