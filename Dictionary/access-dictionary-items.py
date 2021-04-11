D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

print(D['name'])
# Prints Bob

# When key is present
print(D.get('name'))
# Prints Bob

# When key is absent
print(D.get('salary'))
# Prints None
