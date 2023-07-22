# The program is to cipher and decipher words or messages.

import os
                       
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# The function is to decrypt or encrpyt text according to what the user wants and how many positions the letters should be moved
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    # we will first decide what direction between decoding and encoding the user would like to take.
    if cipher_direction == "decode":
        shift_amount *= -1
       # the above is to ensure that if the program receives a message as input and not a singular word, we keep the spacing for the text as is
    # the below is to ensure if the program gets symbols and numbers in the text types, such is ignored and the focus is only on the letters
    for char in start_text:
        if char in alphabet: 
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The cipher direction is {cipher_direction}, the result is: {end_text}")

from caesar_cipher_art import logo
print(logo)

# the program should loop for as long as the user wants to use it

should_continue = True
while should_continue:

        
    direction = input("Type 'encode' to encrypt, type 'decode' to decrpyt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    
    shift = shift % 26
    # the above is to ensure the shift amounts never go beyond the number of letters contained in the alphabet list
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

    result = input("Type 'yes' if you wish to run the program again, otherwiser, type 'no' \n").lower()
    if result == "yes":
        os.system("cls")  
    elif result == "no":
        should_continue = False
        print("Goodbye") 


    
"""#The function encrypt is to take in a text or word from the user, then shifting the letters according to the amount the user inputs to produce an outcome that is jumbled
def encrypt(plain_text, shift_amount):
    cipher_text = ""
        #using a for-loop, we will go through each word or sentence and shift each letter in the input
    for letter in plain_text:
            # the position will look at where the input is currently located by using the index function and that will be the starting point for the program
        position = alphabet.index(letter)
            # to find the output of each letter, we take the starting point according to the alphabet list then shift forward by the number of letters the user has chosen and inputed
        new_position = position + shift_amount
            #the below is to ensure that we bring all the letters back to make one singular word or make up the sentence as it was inputed. This is by taking each letter and combining them
            # in the same way it previously was
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The decoded text is {plain_text}")

# This is to call the different functions according to if the user wants an encrypted message or a decrypted message
if direction == "encode":
    encrypt(plain_text = text, shift_amount = shift)
elif direction == "decode":
    decrypt(cipher_text = text, shift_amount = shift)
"""
