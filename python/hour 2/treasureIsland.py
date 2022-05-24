print("*******************************************************************************")
print("          |                   |                  |                     |")
print("\ _________|________________.=""_;=.______________|_____________________|_______")
print("|                   |  ,-\"_,=\"\"     \`\"=.|                  |")
print("|___________________|__\"=._o\`\"-._        \`\"=.______________|___________________")
print("          |                \`\"=._o\`\"=._      _\`\"=._                     |")
print(" _________|_____________________:=._o \"=._.\"_.-=\"\'\"=.__________________|_______")
print("|                   |    __.--\" , ; \`\"=._o.\" ,-\"\"\"-._ \".   |")
print("|___________________|_._\"  ,. .\` \` \`\` ,  \`\"-._\"-._   \". \'__|___________________")
print("          |           |o\`\"=._\` , \"\` \`; .\". ,  \"-._\"-._; ;              |")
print(" _________|___________| ;\`-.o\`\"=._; .\" \` \'\`.\"\` . \"-._ /_______________|_______")
print("|                   | |o;    \`\"-.o\`\"=._\`\`  \'\` \" ,__.--o;   |")
print("|___________________|_| ;     (#) \`-.o \`\"=.`_.--\"_o.-; ;___|___________________")
print("____/______/______/___|o;._    \"      \`\".o|o_.--\"    ;o;____/______/______/____")
print("/______/______/______/_\"=._o--._        ; | ;        ; ;/______/______/______/_")
print("____/______/______/______/__\"=._o--._   ;o|o;     _._;o;____/______/______/____")
print("/______/______/______/______/____\"=._o._; | ;_.--\"o.--\"_/______/______/______/_")
print("____/______/______/______/______/_____\"=.o|o_.--\"\"___/______/______/______/____")
print("/______/______/______/______/______/______/______/______/______/______/_____ /")
print("*******************************************************************************")

print(" ")
print("Welcome to treasure island.")
print("Your mission is to find the treasure.")

firstTest = input("You are at a cross road, which way do you want to go? Left or Right? ")

if firstTest == 'right' or firstTest == 'Right' or firstTest == 'r' or firstTest =='RIGHT':
    print("GAME OVER!")
#assuming left, doesn't check for any other value
else:
    secondTest = input("Swim or wait? ")
    if secondTest =='swim' or secondTest =='Swim' or secondTest == 's' or secondTest =='SWIM':
        print("GAME OVER!")
    #assuming wait, doesn't check for any other value
    else:
        thirdTest = input("Which door? ")
        if thirdTest == 'red' or thirdTest == 'Red' or thirdTest == 'r' or thirdTest == 'RED':
            print("GAME OVER!")
        elif thirdTest == 'blue' or thirdTest == 'Blue' or thirdTest == 'b' or thirdTest == 'BLUE':
            print("GAME OVER!")
        #assuming yellow, doesn't check for any other value
        else:
            print('You Win!')
