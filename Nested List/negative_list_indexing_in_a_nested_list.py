L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']

print(L[-3])
# Prints ['cc', 'dd', ['eee', 'fff']]

print(L[-3][-1])
# Prints ['eee', 'fff']

print(L[-3][-1][-2])
# Prints eee
