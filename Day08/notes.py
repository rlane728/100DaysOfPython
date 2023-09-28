# Define a function and call it
def greet():
    print()
    print("Hello World.")
    print("The Sky is Blue.")
    print("The Grass is Green.")

greet()


# Make the function take a variable
def greet2(name):
    print()
    print(f"Hello, {name}.")
    print("The Sky is Blue.")
    print("The Grass is Green.")

greet2("Rob")
# The parameter:data pair is name:Rob


# Make a function that takes multiple inputs
def greet_with(name, location):
    print()
    print(f"Hello, {name}.")
    print(f"{location} sure is a fine town.")
    print("The grass is green.")

greet_with("Rob", "London")
greet_with("France", "Henry")
greet_with(location="Beijing", name="Wilson")  # NOTE - This is a key=value argument