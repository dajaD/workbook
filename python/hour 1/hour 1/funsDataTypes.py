#
#len() doesn't use integers
num = len(input("What is your name: "))

#can only concatenate strings and not integers
#will return an error
# print("Your name has "+num+" characters")

#type() will check what you have in parathensis
#and will return data type
print(type(num))

#type cast the type of num (int) to string and stores
#in value newNum
#uses str() to convert
newNum = str(num)
print("Your name has "+newNum+" characters")

a = float(123)
print(type(a))

print(str(70)+str(100))

# 3 + 5 = 8 --- addition
# 7 - 4 = 3 --- subtraction
# 3 * 2 = 6 --- multiplication
# 6 / 3 = 2 --- division
# 2 ** 4 = 8 --- power

# PEMDASLR:
# ()
# **
# * /
# + -
#

print(3 * 3 + 3 / 3 - 3)