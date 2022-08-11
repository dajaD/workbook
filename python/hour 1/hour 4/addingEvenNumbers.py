#write a program that calculates the sum of all the even numbers from 1 to 100 including 1 and 100
#there should only be 1 print statement in the console output. It should just print the firal total
#and not every step of the calculation.
#hint: there are quite a few ways of solving this problem but you will need to use the range() function in 
#any of the solutions


#creates a variable total that has an inital value of 0
total = 0
#for loop that counts from 1 to 100, and skips every other number
for num in range(1,101,2):
    #adds the value to the total variable
    total += num
#prints the total
print (total)