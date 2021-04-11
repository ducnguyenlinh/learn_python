L = ['red', 'green', 'blue']
D = {k:v for k,v in enumerate(L)}
print(D)
# Prints {0: 'red', 1: 'green', 2: 'blue'}

D = {ix: line for ix, line in enumerate(open('myFile.txt'))}
print(D)
# {0: 'First line\n',
#  1: 'Second line\n',
#  2: 'Third line\n'}
