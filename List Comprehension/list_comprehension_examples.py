# Basic Example
#
#
L = []
L.append(0)
L.append(1)
L.append(4)
L.append(9)
L.append(16)
print(L)
# Prints [0, 1, 4, 9, 16]

L = []
for x in range(5):
    L.append(x**2)
print(L)
# Prints [0, 1, 4, 9, 16]

L = [x**2 for x in range(5)]
print(L)
# Prints [0, 1, 4, 9, 16]


# Example 1
#
#
L = [x*3 for x in 'RED']
print(L)
# Prints ['RRR', 'EEE', 'DDD']

# Example 2
#
#
# Convert list items to absolute values
vec = [-4, -2, 0, 2, 4]
L = [abs(x) for x in vec]
print(L)
# Prints [4, 2, 0, 2, 4]

# Example 3
#
#
# Remove whitespaces of list items
colors = ['  red', '  green ', 'blue  ']
L = [color.strip() for color in colors]
print(L)
# Prints ['red', 'green', 'blue']

# Example 4
#
#
L = [(x, x**2) for x in range(4)]
print(L)
# Prints [(0, 0), (1, 1), (2, 4), (3, 9)]
