# Dividing 8 by 3 gives us a float
# But if I try to convert it to int the decimal just gets chopped
# Instead, we can use round() to round to int
# ...or to float with a certain number of decimal places
# We can use the //  operator for floor division
print(8 / 3)
print(int(8 / 3))
print(round(8 / 3))
print(round(8 / 3, 2))
print(8 // 3)


# We can continue to manipulate numeric variables as below
# Shorthand operators for variable manipulation
result = 4 / 2
result /= 2
print(result)


# Thus far we have not been able to combine variable types in a single print (without casting).
score = 0
height = 1.8
isWinning = True
print("Your score is " + str(score) + "...")
# What we can do instead is use an f-String...
print(f"Your score is {score}...")
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")