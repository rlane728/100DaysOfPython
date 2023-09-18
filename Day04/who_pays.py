# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
guest_count = (len(names) - 1)
#print(guests) #DEBUG

rand_choice = random.randint(0, guest_count)
#print(rand_choice) #DEBUG

who_pays = names[rand_choice]
print(f"{who_pays} is going to buy the meal today!")

# Alternatively, we can use the random.choice() function
print(f"{random.choice(names)} is going to buy the meal today!")