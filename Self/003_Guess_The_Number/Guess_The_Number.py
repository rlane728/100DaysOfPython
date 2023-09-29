# Guess the number between 1 and 100
import random

max_num = 100
min_num = 1
number_guesses = 10
game_over = False

hidden_number = random.randint(min_num, max_num)
print(f"Guess a number between {min_num} and {max_num}")
#print(hidden_number)

while not game_over:
    print(f"You have {number_guesses} guess left.")
    player_guess = int(input("Guess a number: "))

    if player_guess == hidden_number:
        game_over = True
        print(f"You guessed {hidden_number}.  You win!")
    elif player_guess < hidden_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

    number_guesses -= 1
    if number_guesses == 0:
        game_over = True
        print(f"You failed to guess {hidden_number}.  You lose!")