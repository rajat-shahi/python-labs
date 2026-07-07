# slicing list => list[start:stop:step]

letters = ["A", "B", "C", "D", "E"]
print(letters[0:2])

print(letters[1:])
print(letters[:3])
print(letters[1:-1])
print(letters[:])
print(letters[::-1])

del letters[1:3]
print(letters)

del letters[:]
print(letters)
