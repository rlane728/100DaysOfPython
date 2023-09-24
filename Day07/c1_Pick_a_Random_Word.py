#Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# NOTE - I generated a random int, but instructor used a better method - random.choice()
#  target_word = word_list[random.randint(0, 2)]
chosen_word = random.choice(word_list)
print(chosen_word) #DEBUG

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Please guess a letter: ").lower()
print(guess) #DEBUG

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# NOTE - Instructor used a FOR loop, I'm not going to use a FOR loop
#  I will note for later though that FOR will step through the elements of a string
my_bool = chosen_word.__contains__(guess)
print(my_bool) #DEBUG

for letter in chosen_word:
    print(letter)