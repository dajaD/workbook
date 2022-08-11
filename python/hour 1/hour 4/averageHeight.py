#you are going to write a program that calculates the average student height from a list of heights.
#e.g. studentHeight = [100,124,165,173,189,169,146]
#the average height can be calculated by adding all the heights together and dividing by the total number of heights.

#you should not use the sum() or len() functions in your answer
#you should try to replicate their functionality using what you lesrnt about for loops

studentHeight = input("Input a list of student heights ").split()
for student in range(0, len(studentHeight)):
    studentHeight[student] = int(studentHeight[student])
print(studentHeight)

counter = 0
total = 0
for s in studentHeight:
    counter += 1
    total += s
print(f"There is a total of {counter} heights in studentHeights")
avg = total / counter
print(f"{total} divided by {counter} = {avg}")
avg = round(avg)
print(f"The avgera age rounded to the nearest whole number = {avg}")