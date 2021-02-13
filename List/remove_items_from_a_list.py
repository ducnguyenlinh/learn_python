# Remove an Item by Index
#
#
L = ['red', 'green', 'blue']
x = L.pop(1)
print(L)
# Prints ['red', 'blue']

# removed item
print(x)
# Prints green

L = ['red', 'green', 'blue']
del L[1]
print(L)
# Prints ['red', 'blue']


# Remove an Item by Value
#
#
L = ['red', 'green', 'blue']
L.remove('red')
print(L)
# Prints ['green', 'blue']


L = ['red', 'green', 'blue', 'red']
L.remove('red')
print(L)
# Prints ['green', 'blue', 'red']


# Remove Multiple Items
#
#
L = ['red', 'green', 'blue', 'yellow', 'black']
del L[1:4]
print(L)
# Prints ['red', 'black']

# Remove all Items
#
#
L = ['red', 'green', 'blue']
L.clear()
print(L)
# Prints []
