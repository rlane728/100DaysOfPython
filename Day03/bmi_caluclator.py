# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi_height = float(height)
bmi_weight = float(weight)
bmi_total = round(bmi_weight / (bmi_height ** 2))

if bmi_total < 18.5:
    print(f"Your BMI is {bmi_total}, you are underweight.")
elif bmi_total < 25:
    print(f"Your BMI is {bmi_total}, you have a normal weight.")
elif bmi_total < 30:
    print(f"Your BMI is {bmi_total}, you are slightly overweight.")
elif bmi_total < 35:
    print(f"Your BMI is {bmi_total}, you are overweight.")
else:
    print(f"Your BMI is is {bmi_total}, you are clinically obese.")
