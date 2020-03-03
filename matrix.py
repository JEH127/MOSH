matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# afficher élément matrice
print(matrix[0][2])  # => 3
print('*'*10)
for row in matrix:
    for item in row:
        print(item)
