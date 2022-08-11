import random

# dirtyDozen = ["strawberries", "nectarines", "apples", "grapes", "peaches", 
# "cherries", "pears", "tomatoes", "celery", "potatoes"]

fruits = ["strawberries", "nectarines", "apples", "grapes", "peaches", 
"cherries", "pears", "tomatoes"]

vegetables = ["spinach", "kale", "celery", "potatoes"]

#a list that contains 2 list
dirtyDozen = [fruits, vegetables]

#prints the value fot he list
#technically three yes list nested.
#fruits is a list
#vegetables is a list
#dirty dozen is a list that contains two elements which are the list of fruits
#and the list of vegetables
print(dirtyDozen)
print(dirtyDozen[1][1])