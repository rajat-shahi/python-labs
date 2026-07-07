person1_age = 22
person2_age = 17

if person1_age >= 18 and person2_age >= 18:
    print("You are both adult")
elif person1_age < 18 or person2_age < 18:
    print("One of you is adult and the other one is children")
else:
    print("Both of you are children")


is_hungry = False

if not is_hungry:
    print("I'm not hungry")
