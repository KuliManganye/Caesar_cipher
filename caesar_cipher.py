# The program is to cipher and decipher words or messages.

import os
                       
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# The function is to decrypt or encrypt text according to what the user wants and how many positions the letters should be moved
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    # We will first decide what direction between decoding and encoding the user would like to take.
    if cipher_direction == "decode":
        shift_amount *= -1
       # The above is to ensure that if the program receives a message as input and not a singular word, we keep the spacing for the text as is
    # The below is to ensure if the program gets symbols and numbers in the text types, such is ignored and the focus is only on the letters
    for char in start_text:
        if char in the alphabet: 
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

        
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    
    shift = shift % 26
    # the above is to ensure the shift amounts never go beyond the number of letters contained in the alphabet list
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

    result = input("Type 'yes' if you wish to run the program again, otherwise, type 'no' \n").lower()
    if result == "yes":
        os.system("cls")  
    elif result == "no":
        should_continue = False
        print("Goodbye") 



