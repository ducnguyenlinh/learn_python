D1 = {'name': 'Bob',
      'age': 25,
      'job': 'Dev'}

D2 = {'age': 30,
      'city': 'New York',
      'email': 'bob@web.com'}

D1.update(D2)
print(D1)
# Prints {'name': 'Bob', 'age': 30, 'job': 'Dev',
#         'city': 'New York', 'email': 'bob@web.com'}
