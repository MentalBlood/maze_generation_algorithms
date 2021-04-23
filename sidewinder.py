import random

def generate(width, height, wall_symbol='█', clear_symbol=' '):
	height //= 2
	width //= 2
	grid = [[{
		'bottom_wall': True,
		'right_wall': True
	} for i in range(width)] for j in range(height)]

	cx = 0
	for y in range(height):
		for x in range(width):
			if y != 0:
				if random.randint(0, 1) and (x != width):
					grid[y][x]['right_wall'] = False
				else:
					if cx == x:
						random_x = cx
					else:
						random_x = random.randint(min(x, cx), max(x, cx)-1)
					grid[y-1][random_x]['bottom_wall'] = False
					if x != width:
						cx = x + 1
					else:
						cx = 0
			else:
				if x != width:
					grid[y][x]['right_wall'] = False

	return convert(grid, wall_symbol, clear_symbol)

def convert(grid, wall_symbol, clear_symbol):
	new_grid = [[clear_symbol for i in range(len(grid[0]) * 2)] for j in range(len(grid) * 2)]
	current_coords = [0, 0]
	for row in grid:
		for cell in row:
			if cell['bottom_wall']:
				new_grid[current_coords[1] + 1][current_coords[0]] = wall_symbol
			if cell['right_wall']:
				new_grid[current_coords[1]][current_coords[0] + 1] = wall_symbol
			current_coords[0] += 2
		current_coords[0] = 0
		current_coords[1] += 2
	buf = '\n'.join([''.join(row) for row in new_grid[1:-1]])
	return buf