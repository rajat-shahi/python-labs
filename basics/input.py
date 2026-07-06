# for taking inputs we use input() function
# whatever the user input, we get it as a string in the program
# to convert to our desired data type we use typecasting : int(), float()


input("What is your name ?")

name = input("What is your name ?")
age = input("What's your age?")

age = int(age) + 1
print(type(age))
print(f"Age of the person is {age}")

phone_number = int(input("Enter your phone number"))
pi = float(input("Enter value of PI"))

print(type(phone_number))
print(type(pi))
