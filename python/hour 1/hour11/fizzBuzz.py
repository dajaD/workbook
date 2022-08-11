# Debug FizzBuzz

# Instructions
# Read this the code in main.py
# Spot the problems 🐞.
# Modify the code to fix the program.
# No shortcuts - don't copy-paste to replace the code entirely with a working solution.
# The code needs to print the solution to the FizzBuzz game.

# Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# `When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#   `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

# Hint
# There is more than one fix required.

#added () to visuals to make it easier to read
for number in range(1, 101):
  #changed from 'or' to 'and' to be inclusive
  if (((number % 3) == 0) and ((number % 5) == 0)):
    print("FizzBuzz")
    #changed from 'if' to 'elif'
  elif ((number % 3) == 0):
    print("Fizz")
  elif ((number % 5) == 0):
    print("Buzz")
  else:
    #removed [] to make sure that it does not print the value of number in a list
    print(number)