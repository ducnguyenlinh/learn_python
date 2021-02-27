# With list comprehension
L = [ord(x) for x in 'foo']
print(L)
# Prints [102, 111, 111]

# With map() function
L = list(map(ord, 'foo'))
print(L)
# Prints [102, 111, 111]

# With list comprehension
L = [x ** 2 for x in range(5)]
print(L)
# Prints [0, 1, 4, 9, 16]

# With map() function
L = list(map((lambda x: x ** 2), range(5)))
print(L)
# Prints [0, 1, 4, 9, 16]
