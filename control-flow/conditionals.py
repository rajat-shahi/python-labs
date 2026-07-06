"""
if True:
    ...
else:
    ...
"""

age = int(input("How old are you?"))

if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")


"""
    if True:
        ...
    elif True:
        ...
    else:
        ...
"""

if age <= 25:
    print("Young")
elif age > 25 and age <= 60:
    print("Mid Age")
else:
    print("Old")
