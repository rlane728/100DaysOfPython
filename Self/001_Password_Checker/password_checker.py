# Password Checker
# 1. Prompt the user to enter a password.
# 2. Check if the password meets the following criteria:
#       At least 8 characters long.
#       Contains both uppercase and lowercase letters.
#       Contains at least one digit (0-9).
# 3. Display a message indicating whether the password is strong or weak based on the criteria.
print("Welcome to Password Checker!")
print("To pass the test, your password must:")
print("   - Be at least 8 characters in length")
print("   - Contain at least on lowercase and one uppercase letter")
print("   - Contain at least one number")
print()
user_passwd = input("Please enter your password: ")

if len(user_passwd) >= 8:
    if user_passwd.isupper() == False:
        if user_passwd.islower() == False:
            if user_passwd.isalpha() == False:
                print("Success - Your password has passed the test!")
            else:
                print("Fail - Your password must contain at least one number.")
        else:
            print("Fail - Your password must contain at least one uppercase letter.")
    else:
        print("Fail - Your password must contain at least one lowercase letter.")
else:
    print("Fail - Your password must be at least eight characters long.")

############################################################################
##After checking my work, chatGPT gave me the following simplified version.
############################################################################
#    user_passwd = input("Please enter your password: ")
#
#    # Initialize variables to track criteria fulfillment
#    has_length = len(user_passwd) >= 8
#    has_lowercase = any(char.islower() for char in user_passwd)
#    has_uppercase = any(char.isupper() for char in user_passwd)
#    has_digit = any(char.isdigit() for char in user_passwd)
#
#    # Check and provide feedback
#    if has_length and has_lowercase and has_uppercase and has_digit:
#        print("Success - Your password has passed the test!")
#    else:
#        print("Fail - Your password does not meet all the criteria:")
#        if not has_length:
#            print("   - It must be at least eight characters long.")
#        if not has_lowercase:
#            print("   - It must contain at least one lowercase letter.")
#        if not has_uppercase:
#            print("   - It must contain at least one uppercase letter.")
#        if not has_digit:
#            print("   - It must contain at least one number.")
