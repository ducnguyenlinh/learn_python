S = 'Hello, World!'
S[0] = 'J'
# Triggers TypeError: 'str' object does not support item assignment

S = 'Hello, world!'
new_S = 'J' + S[1:]
print(new_S)
# Prints Jello, world!
