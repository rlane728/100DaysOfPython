# Password Generator Project
# This is the end of Day05 assignment, not to be confused with the password generator in /Self
# This is the "Easy" version
# I'm going to forego using while statements as the training hasn't gotten us there yet
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

pass_list = []

# Doing this here for readability
nr_letters = (nr_letters + 1)
nr_symbols = (nr_symbols + 1)
nr_numbers = (nr_numbers + 1)

# Generate the letters, captialization randomized
for count in range(1, nr_letters):
    let_n = random.randint(0,25)
    up_low = random.randint(0,1)
    if up_low == 0:
        pass_list.append(letters[let_n].upper())
    else:
        pass_list.append(letters[let_n])
#print(pass_list) #DEBUG

# Generate the symbols
for count in range(1, nr_symbols):
    sym_n = random.randint(0,8)
    pass_list.append(symbols[sym_n])
#print(pass_list) #DEBUG

# Generate the numbers (convert them to string)
for count in range(1, nr_numbers):
    num_n = random.randint(0,9)
    pass_list.append(str(numbers[num_n]))
#print(pass_list) #DEBUG

#print(len(pass_list)) #DEBUG

# Create the final password
length = len(pass_list)
final_pass = ""
count = 0
for count in range(0, length):
    final_pass = final_pass + pass_list[count]
print(final_pass)