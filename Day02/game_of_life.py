# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
user_months_remaining = (90 * 12) - (int(age) * 12)
user_weeks_remaining = (90 * 52) - (int(age) * 52)
user_days_remaining = (90 * 365) - (int(age) * 365)

print(f"You have {user_days_remaining} days, {user_weeks_remaining} weeks, and {user_months_remaining} months left.")

# We can make the output a little more elegant by doing the following
message = f"You have {user_days_remaining} days, {user_weeks_remaining} weeks, and {user_months_remaining} months left."
print(message)