#!/usr/bin/env python3
# NOTE - Stepping through e1-e5 made the flow of everything quite confusing, especially since it was someone else's code
#  and I was only modifying small portions of it.
#  So this is my own hangman, using the art and words modules provided by the instructor
import os
import random
import hangman_words
import hangman_art

# Begin by clearing the screen and printing the logo
os.system('clear')
print(hangman_art.logo)
input("            Press Enter to start...")

player_lives = 6
guess_list = []
game_over = False

# Get the hidden and display words
hidden_word = list(random.choice(hangman_words.word_list))
display_word = []
for count in hidden_word:
    display_word.append("_")

# Play the game
while not game_over:
    os.system('clear')
    print(hangman_art.stages[player_lives])
    print(f"{' '.join(display_word)}")
    #print(f"{' '.join(hidden_word)}") #DEBUG

    guess = input("Guess a letter: ")

    # Make sure the letter has not already been guessed
    if guess not in guess_list:
        guess_list.append(guess)
    else:
        print(f"You already guessed the letter \"{guess}\"")
        input()
        continue

    # Check to see if the player made a correct guess
    if guess in hidden_word:
        for position in range(len(hidden_word)):
            if guess == hidden_word[position]:
                display_word[position] = guess
    else:
        player_lives -= 1

    # Check to see if the players has won or lost
    if "_" not in display_word:
        os.system('clear')
        print(hangman_art.stages[player_lives])
        print("You win!")
        print(f"{' '.join(hidden_word)}")
        game_over = True
    elif player_lives == 0:
        os.system('clear')
        print(hangman_art.stages[player_lives])
        print("You lose!")
        print(f"{' '.join(hidden_word)}")
        game_over = True
    else:
        continue
