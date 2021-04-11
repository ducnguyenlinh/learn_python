D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

print('name' in D)
# Prints True
print('salary' in D)
# Prints False

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

print('Bob' in D.values())
# Prints True
print('Sam' in D.values())
# Prints False
