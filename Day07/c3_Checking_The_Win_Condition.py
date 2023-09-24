#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed
# all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# NOTE - It's probably cheating (because we never learned it), but I used a break function here...
#  So at any point if we find a "_" we declare no win and break the FOR loop, which iterates the WHILE loop.
player_win = False

while player_win == False:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter - This is Instructor code
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    # Check guessed letter - This is Instructor code

    for letter in display:
        if letter == "_":
            player_win = False
            break
        else:
            player_win = True
    print(display)
else:
    print("You Win!")

# NOTE - These are equivalent.  The instructor says the latter is more human readable... I disagree
#  while player_win == False
#  while not player_win

# NOTE - This is a much better way to search display, and we can use it to break the while loop
#  if "_" not in display:
#       print("You Win!")
#       player_win = True

# NOTE - Another option that I explored was first sorting the list, because "_" will occur first alphabetically
#  We could then compare just the first character.
#  I considers using the list.sort() function, but it would require a whole new list
#  I then stumbled upon the sorted() function... which is a cool little function
#    mylist_a = ["a", "b", "_", "c"]
#    if sorted(mylist_a)[0] == "_":
#       print("Player has not won")
#    else:
#       print("Player has won")
