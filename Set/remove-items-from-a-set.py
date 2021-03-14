# with remove() method
#
#
S = {'red', 'green', 'blue'}
S.remove('red')
print(S)
# Prints {'blue', 'green'}

# with discard() method
#
#
S = {'red', 'green', 'blue'}
S.discard('red')
print(S)
# Prints {'blue', 'green'}

# with pop() method
#
#
S = {'red', 'green', 'blue'}
x = S.pop()
print(S)
# Prints {'green', 'red'}

# removed item
print(x)
# Prints blue

S = {'red', 'green', 'blue'}
S.clear()
print(S)
# Prints set()
