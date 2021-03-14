T = ('red', 'green', 'blue')
T[0] = 'black'
# Triggers TypeError: 'tuple' object does not support item assignment

T = (1, [2, 3], 4)
T[1][0] = 'xx'
print(T)
# Prints (1, ['xx', 3], 4)
