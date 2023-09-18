######################
# Randoms and Modules
######################
# We can import the random module here
# Along with others, even custom modules that we create
import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

# Use print to call float pi from my_module.py
print(my_module.pi)

# The random module contains a function that allows us to
# create a float between 0.0 and 0.999999999...
random_float = random.random()
print(random_float)

# Quick Exercise - How do we create a random float between 0 and 5?
# My answer...
my_random = (random.randint(0, 4) + random.random())
print(my_random)

# For fun, format it to 3 decimals...
print(f"{my_random:.3f}")

# Well, her answer was easier...
# And probably a little more correct
her_random = (random.random() * 5)
print(her_random)

print()
###########################
# Lists
###########################
fruit = ["item1", "item2"]
print(fruit[0])
print(fruit[1])

fruit = [random.random(), random.random(), random.random()]
print(fruit[0])
print(fruit[1])
print(fruit[2])

fruit = ["hello", 21, False, my_module.pi]
print(type(fruit[0]))
print(type(fruit[1]))
print(type(fruit[2]))
print(type(fruit[3]))

# We can go backwards...
print(fruit[-1])

# We can change elements of a list by calling their index
fruit = ["value_one", "value_two"]
print(fruit[0])
fruit[0] = "value_three"
print(fruit[0])

# Oh, badass... I discovered this by accident.
# Pull the index of an index...
fruit = ["v_A_lue_one"]
print(fruit[0][2])

# Add an item to a list
fruit = ["value_one", "value_two"]
print(fruit[-1])
fruit.append("value_three")
print(fruit[-1])

print()
# Nested Lists
fruits = ["Apple", "Pear", "Banana"]
vegetables = ["Onion", "Carrots", "Celery"]
fungi = ["mush_R_ooms"]
produce = [fruits, vegetables, fungi]
print(produce)
print(produce[1])
print(produce[1][1])
print(produce[0][1])
print(produce[2][0][5])