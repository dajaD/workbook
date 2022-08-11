# ############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   #for item i in range inclusive:1, exclusive:20
#   #changed the end to 21, so that 20 is included in the range of numbers
#   for i in range(1, 21):
#     #check to see if i is equal to 20
#     if i == 20:
#       #if equal to 20, will print statement
#       print("You got it")
#     #otherwise exists loop
# #calls function
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# #original range was not correct
# #list starts at 0 index, 
# #randint() has start/stop inclusive
# dice_num = randint(0, 5)
# #prints the image of the dice, for given random index position
# print(dice_imgs[dice_num])
#error continues when trying to reach the sixth index, as it does not exist. 

# # Play Computer
# year = int(input("What's your year of birth? "))
# #added an equal sign so that the year is included with millenials
# if year > 1980 and year <= 1994:
#   print("You are a millenial. ")
# elif year > 1994:
#   print("You are a Gen Z. ")
# #has an error as 1994 is not a year you can access technically with this limitation

# # Fix the Errors
# #need to cast age to the data type integer
# age = int(input("How old are you? "))
# if age >= 18:
#   #added the f before the " " so the reference works properly
#   print(f"You can drive at age {age}.")
#   #added an else statement when the user is less than 18 years old
# else:
#   print(f"You can not drive at age {age}")

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
#should only have one '='
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     #needed to fix indentatation so that the list prints correctly
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])