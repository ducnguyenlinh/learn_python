L = ['a', ['bb', 'cc', 'dd'], 'e']
x = L[1].pop(1)
print(L)
# Prints ['a', ['bb', 'dd'], 'e']

# removed item
print(x)
# Prints cc

L = ['a', ['bb', 'cc', 'dd'], 'e']
del L[1][1]
print(L)
# Prints ['a', ['bb', 'dd'], 'e']


L = ['a', ['bb', 'cc', 'dd'], 'e']
L[1].remove('cc')
print(L)
# Prints ['a', ['bb', 'dd'], 'e']
