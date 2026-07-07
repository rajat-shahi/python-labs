countries = ["Brazil", "Japan", "India"]

print(countries[0])
print(countries[1])
print(f"Length of the list = {len(countries)}")

countries[1] = "China"
print(countries[1])

del countries[1]
print(f"New length of the list = {len(countries)}")

countries.append("United States")


for i in range(0, len(countries)):
    print(countries[i])

for i in range(-1, -len(countries) - 1, -1):  # range(start,end,inc/dec by)
    print(countries[i])

for country in reversed(countries):
    print(country)
