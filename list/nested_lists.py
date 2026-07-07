matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[2][2])

# create a matrix of 5x5 with values [0,1,2,3,4] in each row
matrix_5x5 = []

for i in range(5):
    matrix_5x5.append([])

    for j in range(5):
        matrix_5x5[i].append(j)

print(matrix_5x5)


# create a matrix of 4 x 5 with values [0,1,2,3,4] in each row

matrix_4x5 = [[val for val in range(5)] for row in range(4)]
print(matrix_4x5)
