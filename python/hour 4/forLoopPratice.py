#using the for loop with python lists

#variable fruits hold a list that contains 3 elements of strings
fruits = ["Apples", "oranges", "pears"]

#for loop
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")


#for loop with raange
for num in range(1,11,3):
    print(num)

#for loop using range(start, stop, step)
#inclusive start, exclusive stop
total = 0
for num in range(1,101,1):
    print(num)
    total += num
print (total)