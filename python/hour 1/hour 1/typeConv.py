#Write a program that adds the digits in a 2 figit number
#e.g. if the input was 35 then the output should be 3+5
#warning do not change the code. your program should work
#for different inputs
#example input 39
#example output 3 + 9 = 12

#accepts user input
dig = input("input type a two digit number\n")
#prints the type of the user input
print(type(dig))

#takes the value of the user input at index 0 and assigns it to variable one
one = dig[0]
#creates variable ones which type casts variable one to an integer
ones = int(one)
#prints the type of variable one
print(type(one))
#takes the value of user input at index 1
two = dig[1]
#assigns and type casts the value of variable two to an interger to variable twos
twos = int(two)
#prints the type for two
print(type(two))
#assigns and type casts the sum of integers ones and twos to three
three = str(ones+twos)
#prints out the sum of the following addition
print(one," + "+two," = " +three)

