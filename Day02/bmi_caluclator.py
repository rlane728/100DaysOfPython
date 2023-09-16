# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi_height = float(height)
bmi_weight = float(weight)
bmi_total = int(bmi_weight / (bmi_height ** 2))
bmi_str = str(bmi_total)
print(weight + " ÷ " + "( " + height + " x " + height + " )" + " = " + bmi_str )
print(bmi_total)