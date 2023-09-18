# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇
import random

coin_toss = random.randint(0, 1)

if coin_toss == 0:
    print("Heads")
else:
    print("Tails")

# I suppose you could write it like this
# But there would be no way to debug it
if random.randint(0, 1) == 0:
    print("Heads")
else:
    print("Tails")