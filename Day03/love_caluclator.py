# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

t_count = name1.count("t") + name2.count("t")
r_count = name1.count("r") + name2.count("r")
u_count = name1.count("u") + name2.count("u")
e1_count = name1.count("e") + name2.count("e")
true_count = (t_count + r_count + u_count + e1_count)
str_true = str(true_count)

l_count = name1.count("l") + name2.count("l")
o_count = name1.count("o") + name2.count("o")
v_count = name1.count("v") + name2.count("v")
e2_count = name1.count("e") + name2.count("e")
love_count = (l_count + o_count + v_count + e2_count)
str_love = str(love_count)

true_love = int(str_true + str_love)

if (true_love < 10) or (true_love > 90):
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif (true_love >= 40) and (true_love <= 50):
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")
