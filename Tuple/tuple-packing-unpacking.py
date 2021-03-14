T = ('red', 'green', 'blue', 'cyan')
print(T)
# Prints ('red', 'green', 'blue', 'cyan')

# Tuple Unpacking
#
#
T = ('red', 'green', 'blue', 'cyan')
(a, b, c, d) = T

print(a)
# Prints red

print(b)
# Prints green

print(c)
# Prints blue

print(d)
# Prints cyan


# Common errors in tuple unpacking

T = ('red', 'green', 'blue', 'cyan')
(a, b) = T
# Triggers ValueError: too many values to unpack

T = ('red', 'green', 'blue')
(a, b, c, d) = T
# Triggers ValueError: not enough values to unpack (expected 4, got 3)
