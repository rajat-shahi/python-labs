# comparison operators : == , != , > , >= , < , <=
# python evaluates both type and value while comparing values
# while comparing strings, python compares strings lexicographically so unicode values of the characters comes into picture

print(2 == 2)
print(4 == 2)
print("2" == 2)

print(4 > 2)
print(2 > 2)

print(4 > 2)
print(2 >= 2)

print(4 < 2)
print(2 < 2)

print(4 <= 2)
print(2 <= 2)

print("python" > "Python")  # True because unicode value of 'p' is 112 and 'P' is 80

print(ord("p"))
print(ord("P"))
