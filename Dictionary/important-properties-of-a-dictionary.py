# Keys must be unique:
#
#
D = {'name': 'Bob',
     'age': 25,
     'name': 'Jane'}
print(D)
# Prints {'name': 'Jane', 'age': 25}

# Key must be immutable type:
#
#
D = {(2,2): 25,
     True: 'a',
     'name': 'Bob'}


# Value can be of any type:
#
#
# values of different datatypes
D = {'a':[1,2,3],
     'b':{1,2,3}}

# duplicate values
D = {'a':[1,2],
     'b':[1,2],
     'c':[1,2]}
