# Set Union
#
#
A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}

# by operator
print(A | B)
# Prints {'blue', 'green', 'yellow', 'orange', 'red'}

# by method
print(A.union(B))
# Prints {'blue', 'green', 'yellow', 'orange', 'red'}

# Set Intersection
#
#
A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}

# by operator
print(A & B)
# Prints {'red'}

# by method
print(A.intersection(B))
# Prints {'red'}

# Set Difference
#
#
A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}

# by operator
print(A - B)
# Prints {'blue', 'green'}

# by method
print(A.difference(B))
# Prints {'blue', 'green'}

# Set Symmetric Difference
#
#
A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}

# by operator
print(A ^ B)
# Prints {'orange', 'blue', 'green', 'yellow'}

# by method
print(A.symmetric_difference(B))
# Prints {'orange', 'blue', 'green', 'yellow'}

# python-frozenset
#
#
S = frozenset({'red', 'green', 'blue'})
print(S)
# Prints frozenset({'green', 'red', 'blue'})

# finding size
S = frozenset({'red', 'green', 'blue'})
print(len(S))
# Prints 3

# performing union
S = frozenset({'red', 'green', 'blue'})
print(S | {'yellow'})
# Prints frozenset({'blue', 'green', 'yellow', 'red'})

# removing an item
S = frozenset({'red', 'green', 'blue'})
S.pop()
# Triggers AttributeError: 'frozenset' object has no attribute 'pop'

# adding an item
S = frozenset({'red', 'green', 'blue'})
S.add('yellow')
# Triggers AttributeError: 'frozenset' object has no attribute 'add'
