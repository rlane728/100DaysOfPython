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

