# Remove an Item by Key
#
#
D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

x = D.pop('age')
print(D)
# Prints {'name': 'Bob', 'job': 'Dev'}

# get removed value
print(x)
# Prints 25

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

del D['age']
print(D)
# Prints {'name': 'Bob', 'job': 'Dev'}


# Remove Last Inserted Item
#
#
D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

x = D.popitem()
print(D)
# Prints {'name': 'Bob', 'age': 25}

# get removed pair
print(x)
# Prints ('job', 'Dev')

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

D.clear()
print(D)
# Prints {}


# Remove all Items
#
#
D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

D.clear()
print(D)
# Prints {}
