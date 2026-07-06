# - - - - - - - - - - NUMBERS - - - - - - - - - - - #

num_dec = 123  # decimal
num_octal = 0o123  # octal
num_hex = 0x123  # hexadecimal
num_float = 1e-2  # float
num_big = 1_000_000

print("num_dec :", num_dec)
print("num_octal :", num_octal)
print("num_hex :", num_hex)
print("num_float :", num_float)
print("num_big", num_big)
print(type(num_dec), type(num_octal), type(num_hex), type(num_float), type(num_big))

# - - - - - - - - - - STRINGS - - - - - - - - - - - #

str1 = "Hi, I am Rajat"
str2 = "Hi, I am 'Rajat'"
str3 = 'Hi, I am "Rajat"'
str4 = 'Hi, I am "Rajat"'

print(str1, str2, str3, str4, sep="\n")
print(type(str3))


# - - - - - - - - - - BOOLEAN - - - - - - - - - - - #
val1 = True
val2 = False
val3 = 1
val4 = 0

print(val1, val2, val3, val4)
print(type(val2))
