T = ('cc', 'aa', 'dd', 'bb')
print(tuple(sorted(T)))
# Prints ('aa', 'bb', 'cc', 'dd')

T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)    # convert tuple to list
tmp.sort()       # sort list
T = tuple(tmp)   # convert list to tuple
print(T)         # Prints ('aa', 'bb', 'cc', 'dd')
