ages = [20, 30, 40, 10, 12]
total = 0

for age in ages:
    total += age

total_people = len(ages)

avg_age = total / total_people

print(f"The average of the people is {avg_age}")


# - - - - - - - - - - - Using Enumerate to print index and value both - - - - - - - - - - - - -

for index, value in enumerate(ages):
    print(f"Index={index},Value={value}")


# Note : ages*2 will have a new list have ages appended 2 times : [20, 30, 40, 10, 12, 20, 30, 40, 10, 12]
