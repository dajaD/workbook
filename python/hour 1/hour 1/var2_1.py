#Write a program that switches the values stored in 
#the variables a and b
#warning do not change the code. Your program should
#work for different inputs e.g. any value of a and b
#example Input
#a: 3
#b: 5
#an easy solution would be to print
#"a = " + b
#"a = " + a
#but not the solution were looking for


#accepts input from user for values a & b using input()
a = input("a: ")
b = input("b: ")

#creates variable c and assigns the value of a to c
c = a
#reassigns the value of a to the value of b
a = b
#reassigns the value of b to c
b = c

#printing out the switch of the values
print("a = "+a)
print("b = "+b)