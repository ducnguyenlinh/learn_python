# Create a dictionary with a list of two-item tuples
L = [('name', 'Bob'),
     ('age', 25),
     ('job', 'Dev')]

D = dict(L)
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}

# Create a dictionary with a tuple of two-item lists
T = (['name', 'Bob'],
     ['age', 25],
     ['job', 'Dev'])

D = dict(T)
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}

D = {'name': 'Bob', 'age': 25, 'job': 'Dev'}

print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}
