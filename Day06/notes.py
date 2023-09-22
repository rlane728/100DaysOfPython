# print() is built-in function
print("Hello World")

# len() is a built-in function
print(len("four"))

# We can create our own functions...
def my_function():
    print("\nRun your own function")
    print("Hello")
    print("Bye")

# Then call our functions...
my_function()

# OK, this is noteworthy
# Two ways of working...
true_false = True
while true_false != True:
    print(False)
else:
    print(True)

while not true_false:
    print(False)
else:
    print(True)