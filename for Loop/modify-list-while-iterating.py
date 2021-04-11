# infinite loop
colors = ['red', 'green', 'blue']
for x in colors:
    if x == 'red':
        colors.insert(0, 'orange')
        print(colors)

colors = ['red', 'green', 'blue']
for x in colors[:]:
	if x == 'red':
		colors.insert(0, 'orange')
print(colors)
# Prints ['orange', 'red', 'green', 'blue']
