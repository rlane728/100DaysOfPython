# Write your code below this line 👇

# NOTE - lol, I kinda over-engineered this.  Look how easy...
#  for i in range(2,number)
#   if number % i == 0:
#    is_prime = False

def prime_checker(number):
    prime = True
    divisors = "235"
    if str(number) not in divisors:
        for num in divisors:
            if number % int(num) == 0:
                prime = False
                break
    if prime is True:
        print("It's a prime number.")
    else:
        print("It's not a prime number")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
