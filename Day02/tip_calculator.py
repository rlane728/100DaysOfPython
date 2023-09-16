#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to leave?  10, 12 or 15? ")) / 100
tip_read = int(tip_percent * 100)
number_guests = float(input("How many people to split the bill? "))

bill_plus_tip = round(total_bill + (total_bill * tip_percent), 2)
per_guest = round(bill_plus_tip / number_guests, 2)

print()
print(f"The total bill, plus {tip_read}% tip is: ${bill_plus_tip:.2f}")
print(f"Each person should pay: ${per_guest:.2f}")

# Another way to display the float to a certain decimal place is to pre-format a variable
decimal_float = "{:.2f}".format(per_guest)
print()
print(f"Formatting example: {decimal_float}")