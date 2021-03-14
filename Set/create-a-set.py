# A set of strings
S = {'red', 'green', 'blue'}

# A set of mixed datatypes
S = {1, 'abc', 1.23, (3+4j), True}

S = {'red', 'green', 'blue', 'red'}
print(S)
# Prints {'blue', 'green', 'red'}

S = {1, 'abc', ('a', 'b'), True}

S = {[1, 2], {'a': 1, 'b': 2}}
# Triggers TypeError: unhashable type: 'list'
