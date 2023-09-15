#######################################
# Write your first Hello World
#######################################
print("Hello World!")


#######################################
# Add some user input to Hello World
#######################################
first = input("What is your name? ")
print("Hello, " + first + "nice to meet you!")
last = input("What is your last name? ")
print("Hello " + first + " " + last + "!")
print("The length of your last name is " + str(len(last)) + " characters!")


#################################
# Switching variables section
#################################

# Switching variables
a = input("Enter a value for a: ")
b = input("Enter a value for b: ")

# My Answer
# Below was my answer, which does work...
y = a
z = b
b = y
a = z
print("a is now: " + a)
print("b is now: " + b)

# However the teacher's answer was simplified
# c = a
# a = b
# b = c


#################################
# This next sesction applies some of the principles from above
# as well as introducing newline operators
#################################

# Band Name Generator
# 1. Create a greeting for your program.
print("Hi there!  Welcome to Band name generator!")
# 2. Ask the user for the city that they grew up in.
user_city = input("What city did you grow up in? \n")
# 3. Ask the user for the name of a pet.
user_pet = input("What is the name of your favorite pet? \n")
# 4. Combine the name of their city and pet and show them their band name.
print("Your band name is " + user_city + " " + user_pet + "!")
# 5. Make sure the input cursor shows on a new line:

