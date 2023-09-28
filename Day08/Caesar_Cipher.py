# NOTE - My Caesar Cipher
#  To encode user's message, shift right n positions in the alphabet, looping around
#  To decode user's message, shift left n positions in the alphabet, looping around
#  I'll challenge myself to use a single alphabet list

import os
import caesar_art


# Set up our alphabet list.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Initialize the game with title screen
def gamestart():
    os.system('clear')
    print(caesar_art.logo)
    print()


def userinput():
    input_choice = ""
    while input_choice != "E" and input_choice != "D":
        input_choice = input("Would you like to [E]ncode or [D]ecode your message? ")
    input_message = input("Please enter the message: \n")
    input_shift = input("Please enter the shift amount: ")
    return input_choice, input_message, input_shift


def cipher():
    continue_game = True
    while continue_game:
        choice, message, shift = userinput()

        final_text = ""
        for character in message:
            is_alpha = character.isalpha()
            is_upper = character.isupper()
            character = character.lower()
            char_shift = int(shift)
            if not is_alpha:
                final_text += character
            elif choice == "E":
                position = alphabet.index(character)
                if position + char_shift > 25:
                    char_shift = (position + char_shift) % 26
                    translation = alphabet[0 + char_shift]
                else:
                    translation = alphabet[position + char_shift]

                if is_upper:
                    final_text += translation.upper()
                else:
                    final_text += translation
            else:
                position = alphabet.index(character)
                if position - char_shift < 0:
                    char_shift = (char_shift - position) % 26
                    translation = alphabet[26 - char_shift]
                else:
                    translation = alphabet[position - char_shift]

                if is_upper:
                    final_text += translation.upper()
                else:
                    final_text += translation

        if choice == "E":
            print("Your encoded message is:")
            print(final_text)
        else:
            print("Your decoded message is:")
            print(final_text)

        game_on = input("Would you like to try another message? [Y] or [N]: \n")
        if game_on == "N":
            continue_game = False

        os.system('clear')


gamestart()
cipher()
