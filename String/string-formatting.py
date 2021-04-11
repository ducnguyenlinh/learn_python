# printf-style % string formatting
S = '%s is %d years old.' % ('Bob', 25)
print(S)
# Prints Bob is 25 years old.

# format() Built-in Method
S = '{1} is {0} years old.'.format(25, 'Bob')
print(S)
# Prints Bob is 25 years old.

# f-String Formatter
name = 'Bob'
age = 25
S = f"{name} is {age} years old."
print(S)
# Prints Bob is 25 years old.
