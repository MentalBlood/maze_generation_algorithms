import random

width = 150
height = 20

wall = '█'
clear = ' '

m = [[wall for i in range(width)] for j in range(height)]

x = random.randrange(0, width // 2) * 2 + 1
y = random.randrange(0, height // 2) * 2 + 1

m[y][x] = ' '

to_check = []
if y - 2 >= 0:
	to_check.append((x, y - 2))
if y + 2 < height:
	to_check.append((x, y + 2))
if x - 2 >= 0:
	to_check.append((x - 2, y))
if x + 2 < width:
	to_check.append((x + 2, y))

while len(to_check) > 0:
	i = random.randrange(len(to_check))
	x, y = to_check[i]
	m[y][x] = clear
	del to_check[i]

	directions = [
		(y - 2 >= 0, 0, -1),
		(y + 2 < height, 0, 1),
		(x - 2 >= 0, -1, 0),
		(x + 2 < width, 1, 0)
	]
	random.shuffle(directions)
	for d in directions:
		if d[0]:
			if m[y + d[2] * 2][x + d[1] * 2] == clear:
				m[y + d[2]][x + d[1]] = clear
				break

	for d in directions:
		if d[0]:
			if m[y + d[2] * 2][x + d[1] * 2] == wall:
				to_check.append((x + d[1] * 2, y + d[2] * 2))

	if len(to_check) > 1:
		to_check.pop()

	# buf = '\n'.join([''.join(row) for row in m]) 
	# print(buf)
	# input()

buf = '\n'.join([''.join(row) for row in m]) 
print(buf)