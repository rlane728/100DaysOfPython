#Write your code below this row 👇

# The challenge is to total all even numbers between 1 and 100
# There should only be one print statement in the console
total = 0
for i in range(2, 101, 2):
    total += i
print(total)

# Here is another way to do it
total2 = 0
for i in range(1, 101):
    if (i % 2) == 0:
        total2 += i
print(total2)

