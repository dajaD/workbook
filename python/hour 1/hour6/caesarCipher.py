from art import logo

#imports and uses the logo from the art file
print(logo)

#array that holds all the letters in the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
# def caesar(text, shift, direction):
#     cipherText = ""
#     if direction == 'decode':
#             shift *= -1
#     for letter in text:
#         #TODO-3: What happens if the user enters a number/symbol/space?
#         #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#         #e.g. start_text = "meet me at 3"
#         #end_text = "•••• •• •• 3"
#         position = alphabet.index(letter)
#         cipherText += alphabet[position + shift]
#     print(f"The {direction}d text is {cipherText}")

def caesar():
    #variable for the new text
    cipherText = ""
    #direction of the shift
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    #text that will be shifted
    text = input("Type your message:\n").lower()
    #amount to shift
    shift = int(input("Type the shift number:\n"))
    #ensures that if the number of shifts exceeds 26 it will find the next letter still and not break
    shift = shift % 26
    #checks the direction of the shift
    if (direction) == 'encode':
#for loop goes through the text that was provided by the user
        for letter in text:
#checks to see if the 'letter' is identified by the array of letters given and not another character
            if letter in alphabet:
                position = alphabet.index(letter)
                cipherText += alphabet[position + shift]
            else:
                cipherText += letter
    else:
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                cipherText += alphabet[position - shift]
            else:
                cipherText += letter
    print(f"Your new message is {cipherText}")
    #while loop reruns if the
    while(True):
        redo = input("Do you want to try it again? ")
        if (redo == 'yes'):
            print('Ok here we go!')
            caesar()
        else:
            print('Ok! Good bye')
            break

caesar()
# #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values



# #Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(pText, shiftA):
#     cipherText = ""
# #     # Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
# #     #e.g. 
# #     #plain_text = "hello"
# #     #shift = 5
# #     #cipher_text = "mjqqt"
# #     #print output: "The encoded text is mjqqt"
# #     #for loop goes through the text entered by the user 
#     for letter in pText:
#         #variable position, gets the index of variable letter
#         position = alphabet.index(letter)
#         #variable newLetter gets the value of the index at the original position added to the shift amount
#         #adds the letters into the variable ciphertext
#         cipherText += alphabet[position + shiftA]
# #     #prints the new text
#     print(f"Your new encoded text is {cipherText}")
# #     ##HINT: How do you get the index of an item in a list:
# #     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# #     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# # #Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(pText, shiftA):
#     cipherText = ""
#   #Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#   #e.g. 
#   #cipher_text = "mjqqt"
#   #shift = 5
#   #plain_text = "hello"
#   #print output: "The decoded text is hello"
#     for letter in pText:
#         position = alphabet.index(letter)
#         cipherText += alphabet[position - shiftA]
#     print(f"The decoded text is {cipherText}")


# # #Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable.
# # # You should be able to test the code to encrypt *AND* decrypt a message.
# if direction == 'encode':
#     # Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)

