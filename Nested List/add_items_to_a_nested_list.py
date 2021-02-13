L = ['a', ['bb', 'cc'], 'd']
L[1].append('xx')
print(L)
# Prints ['a', ['bb', 'cc', 'xx'], 'd']

L = ['a', ['bb', 'cc'], 'd']
L[1].insert(0, 'xx')
print(L)
# Prints ['a', ['xx', 'bb', 'cc'], 'd']

L = ['a', ['bb', 'cc'], 'd']
L[1].extend(['e', 'f', 'g'])
print(L)
# Prints ['a', ['bb', 'cc', 'e', 'f', 'g'], 'd']
