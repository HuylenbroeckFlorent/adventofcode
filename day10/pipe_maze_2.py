import sys

pipe_maze = open('data.txt', 'r').readlines()

# Pipe connections will be stored as a list of 4 directions [NORTH, EAST, SOUTH, WEST]
connections_map = {
	'.': [0, 0, 0, 0],
	'|': [1, 0, 1, 0],
	'-': [0, 1, 0, 1],
	'L': [1, 1, 0, 0],
	'J': [1, 0, 0, 1],
	'7': [0, 0, 1, 1],
	'F': [0, 1, 1, 0],
	'S': [1, 1, 1, 1]
}

# Build the maze
connections = []
start = (0, 0)
for i in range(len(pipe_maze)):
	row = pipe_maze[i].strip('\n')
	connection_row = []
	maze_row = []
	for j in range(len(row)):
		pipe = row[j]
		if pipe == 'S':
			start = (i, j)
		connection_row.append(connections_map[pipe])
	connections.append(connection_row)

# Since every pipe connects exactly two other pipe (otherwise the loop wouldn't be complete), we don't have to worry about deadends.
# There's no need for Floyds nor Dijkstra in such a simple case. We can simply start from both entries and see when they join.

# Also we cheat to allow for a recursive algorithm.
sys.setrecursionlimit(len(connections)*len(connections[0]))

loop_tiles = [[0 for _ in  connections[i]] for i in range(len(connections))]

# This time we don't need the distances, we only need to know which tiles are walls (pipe from the loop) or not.
def mark_loop(x, y, entered_from=5):
	if (x, y) == start and loop_tiles[x][y] == 1:
		return
	else:
		loop_tiles[x][y] = 1
		entered_from = (entered_from+2)%4
		for i in range(4):
			if connections[x][y][i] and i != entered_from:
				if i == 0 and x > 0:
					mark_loop(x-1, y, i)
				elif i == 1 and y < len(connections[x])-1:
					mark_loop(x, y+1, i)
				elif i==2 and x < len(connections)-1:
					mark_loop(x+1, y, i)
				elif i==3 and y>0:
					mark_loop(x, y-1, i)

for i in connections[start[0]][start[1]]:
	if i:
		mark_loop(*start)

enclosed_tiles_counter = 0

# To count the enclosed tiles, we traverse the maze row by row, keeping track of how many ground tiles were traversed.
# When we encounter a wall, we have to determine if crossing it makes us enter (resp. exit) the loop or stay outside (resp. inside).
# To do so, we compare the number of pipe from that wall that exits to the north and to the south.
# Having one of each would mean that crossing that wall makes un enter (resp. exit) inside the loop.
# Having two of one type would not make us enter (resp. exit) the loop.
# Whenever we cross a wall and we were inside the loop, we add the traversed ground tiles since the last wall to the counter. 
for i in range(len(loop_tiles)):
	row = loop_tiles[i]

	# We track how many ground tiles were passed since last wall.
	tiles_since_last_wall = 0

	# We track whether if we're currently inside ou outside the loop.
	inside = False

	# Track the amount of north/south exits.
	norths = 0
	souths = 0

	for j in range(len(row)):
		tile = row[j]

		# We are on a ground tile, increment the current tile counter.
		if tile == 0:
			tiles_since_last_wall += 1
		else:
			# We are on a wall tile, we count the number of south and north exits.
			norths += connections[i][j][0]
			souths += connections[i][j][2]

			# When the total of north and south exits reaxches 2, a wall was completed (two walls can be directly in contact so we don't wait for a ground tile).
			if norths+souths == 2:
				if inside:
					enclosed_tiles_counter += tiles_since_last_wall
				if norths == souths:
					inside = not inside
				norths = 0
				souths = 0
				tiles_since_last_wall = 0
	
print(enclosed_tiles_counter)
