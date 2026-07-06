"""
while True :
    ...
else :
    ....

"""

secret_number = 3
guessed_number = int(input("Enter the number :"))

while secret_number != guessed_number:
    print("Oops! Wrong Guess")
    guessed_number = int(input("Enter the number :"))
else:
    print("Congratulations! You got it")
