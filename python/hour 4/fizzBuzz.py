#write a program that automatically prints the solution to the fizzbuzz game
#program should print each number from 1 to 100 in turn
#when the number is divisible by 3 then instead of printing the number it should
#print "Fizz"
#when divisible by 5, it should print "buzz"
#when divisible by both 3 and 5 print fizzbuzz

for num in range(1,101):
    if ((num % 3 == 0) and (num % 5 == 0)) :
        print("FizzBuzz")
    elif((num % 3 == 0)):
        print("Fizz")
    elif((num % 5 == 0)):
        print("Buzz")
    else:
        print(num)