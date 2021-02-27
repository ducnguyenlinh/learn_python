# With list comprehension
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
L = [number for list in vector for number in list]
print(L)
# Prints [1, 2, 3, 4, 5, 6, 7, 8, 9]

# equivalent to the following plain, old nested loop:
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
L = []
for list in vector:
    for number in list:
        L.append(number)
print(L)
# Prints [1, 2, 3, 4, 5, 6, 7, 8, 9]


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
L = [[row[i] for row in matrix] for i in range(3)]
print(L)
# Prints [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
