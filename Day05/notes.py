import random


# FOR loops
# They're FOR loops, what do you expect?
print("\nFor Loop...")
list_of_items = ["Apple", "Peach", "Pear"]
for item in list_of_items:
    print(item)
    print(f"{item} Pie.")


# The range() function
# Operate on a range
print("\nFor loop with range()...")
for number in range(1, 10):
    print(number)


# Add a step to the range() function
print("\nFor loop, ranged, with step function...")
for number in range(0, 31, 3):
    print(number)


# Add all of the numbers from 1 to 100
print("\nThe sum of all numbers from 1 to 100")
total = 0
for number in range(1, 101):
    total += number
print(total)


# There was a little Easter egg in the password_generator instructions... random.choice()
print("\nUse random.choice()")
mylist = ["poo", "foo", "goo", "noo"]
print(mylist)
print(random.choice(mylist))


# What I used was random.shuffle(), which shuffles the final list
# Then I just added each element of the shuffled list to a string
# Which is still pretty good (see the password generators for full example)
# Actually, turned out to be the instructor's preferred method.
print("\nUse random.shuffle()")
mylist = ["poo", "foo", "goo", "noo"]
random.shuffle(mylist)
print(mylist)