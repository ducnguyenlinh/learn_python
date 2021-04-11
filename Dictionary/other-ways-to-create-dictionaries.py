# Create a dictionary with list of zipped keys/values
keys = ['name', 'age', 'job']
values = ['Bob', 25, 'Dev']

D = dict(zip(keys, values))

print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}

# Initialize dictionary with default value '0' for each key
keys = ['a', 'b', 'c']
defaultValue = 0

D = dict.fromkeys(keys,defaultValue)

print(D)
# Prints {'a': 0, 'b': 0, 'c': 0}
