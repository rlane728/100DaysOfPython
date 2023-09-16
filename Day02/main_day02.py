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
string_a = "123"
int_b = 456
swap_c = int(string_a)
string_a = str(int_b)
int_b = swap_c
print(string_a)
print(int_b)
print(type(string_a))
print(type(int_b))
