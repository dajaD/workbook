from ntpath import join
import random
from hangmanArt import stages
from hangmanArt import logo
from hangmanWords import wordList

#TODO-1: - Update the word list to use the 'wordList' from hangmanWords.py
#Delete this line: wordList = ["ardvark", "baboon", "camel"]

#randomly choose a word from the wordlist and assign it to a variable called chosen word.
chosenWord = random.choice(wordList)

#Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#TODO-3: - Import the logo from hangmanArt.py and print it at the start of the game.
print(logo)

print(chosenWord)

#Create an empty List called display.
display = []
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
for letter in chosenWord:
    display.append('_')


# Use a while loop to let the user guess again. 
# #The loop should only stop once the user has guessed all the letters in 
# the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

end = False

while not end:

    #ask the user to guess a letter and assign their answer to a variible called guess. make guess 
    #lowercase
    guess = input("Guess a letter in the puzzle: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"You already guessed {guess} try again! ")

    #Loop through each position in the chosenWord;
    # #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    # #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

    for pos in range(len(chosenWord)):
        letter = chosenWord[pos]
        if letter == guess:
            display[pos] = letter

    #check if the letter the user guessed is one of the letters in the chosen word.
    # for letter in chosenWord:
    #     if guess == letter:
    #         print('Right')
    #     else:
    #         print('Wrong')

    #Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
    #joins all the elements in the list and converts it to a string instead. more visually appealing
    print(f"{ ' '.join(display)}")

    #checks to see if the game is finished
    if "_" not in display:
        end = True
        print("You Win! ")
    #If guess is not a letter in the chosenWord,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    elif guess not in chosenWord:
       #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"{guess} is not in the puzzle. ")
       #TODO-2: - Import the stages from hangman_art.py and make this error go away.
        print(stages[lives-1])
        lives -= 1
        if lives == 0:
            end = True
            print("You Lose!")