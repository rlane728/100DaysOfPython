# This is a string
string_hello = "Hello"
print(type(string_hello))

# This is an int
int_123 = 123
print(type(int_123))

# This is a float
float_12567 = 12.567
print(type(float_12567))

# This is a bool
bool_true = True
bool_false = False
print(type(bool_true))
print(type(bool_false))

# len() can be used to return the length of a string
print(len("Hello"))

# But will fail to return the length ogf int
# print(len(12345)) produces an error

# Strings themselves can be indexed
# This is called "subscripting"
print("Robert"[2])

# Large integers use underscores instead of comma separators
# print(int(100,000,000)) ... This throws an error
print(int(100_000_000))

# Strings can be cast to int and vice versa
# I'm sure this can be done with the others, too
string_a = "123"
int_b = 456
swap_c = int(string_a)
string_a = str(int_b)
int_b = swap_c
print(string_a)
print(int_b)
print(type(string_a))
print(type(int_b))

# A print statement by default can only concatenate equivalent data types
string_print1 = "Hello"
int_print1 = 12345
print (string_print1 + " User!")

# The following will throw an error because the data types differ
# print (int_print1 + string_print1)

# ints and floats can be combined
int_float = 100
float_int = 23.3
print(int_float + float_int)
intf_out = print(int_float + float_int)
print(type(intf_out))
intf_plus = int_float + float_int
print(type(intf_plus))


# Mathematical operators
# Normal orders of operation apply
# PEMDASLR (paren, exp, mult, div, add, sub, left/right)
print(3 + 5)    # addition
print(3 - 5)    # subtraction
print(3 * 5)    # multiplication
print(6 / 3)    # division
print(6 ** 3)   # exponent
print(3 + 3 * 3 - 5)
print((3 + 3) * (3 - 5))
print(3 + (3 * (3 / 5)))