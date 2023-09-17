# Determine if any given year is a leap year based on the following rules...
# on every year that is evenly divisible by 4
# **except** every year that is evenly divisible by 100
# **unless** the year is also evenly divisible by 400
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if (year % 4) > 0:
    print(f"{year} is not a leap year.")
elif (year % 100) == 0:
    if (year % 400) == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print(f"{year} is a leap year.")

