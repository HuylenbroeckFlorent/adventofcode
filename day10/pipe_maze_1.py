import sys

pipe_maze = open('data.txt', 'r').readlines()

# Pipe connections will be stored as a list of 4 directions [NORTH, EAST, SOUTH, WEST]
connections = {
	'.': [0, 0, 0, 0],
	'|': [1, 0, 1, 0],
	'-': [0, 1, 0, 1],
	'L': [1, 1, 0, 0],
	'J': [1, 0, 0, 1],
	'7': [0, 0, 1, 1],
	'F': [0, 1, 1, 0],
	'S': [1, 1, 1, 1]
}

# build the maze
maze = []
start = (0, 0)
for i in range(len(pipe_maze)):
	row = pipe_maze[i].strip('\n')
	maze_row = []
	for j in range(len(row)):
		pipe = row[j]
		if pipe == 'S':
			start = (i, j)
		maze_row.append(connections[pipe])
	maze.append(maze_row)

# Since every pipe connects exactly two other pipe (otherwise the loop wouldn't be complete), we don't have to worry about deadends.
# Also there's no need for Floyds nor Dijkstra in such a simple case. We can simply start from both entries and see when they join.

# Also we cheat to allow for a recursive algorithm.
sys.setrecursionlimit(len(maze)*len(maze[0]))

distances = [[0 for _ in  maze[i]] for i in range(len(maze))]

def mark_loop(x, y, current_distance, entered_from=5):
	if (x, y) == start and current_distance > 1:
		return
	elif distances[x][y] < current_distance and distances[x][y] > 0:
		return
	else:
		current = maze[x][y]
		distances[x][y] = min(distances[x][y], current_distance) if distances[x][y] != 0 else current_distance
		entered_from = (entered_from+2)%4
		for i in range(4):
			if maze[x][y][i] and i != entered_from:
				if i == 0 and x > 0:
					mark_loop(x-1, y, current_distance+1, i)
				elif i == 1 and y < len(maze[x])-1:
					mark_loop(x, y+1, current_distance+1, i)
				elif i==2 and x < len(maze)-1:
					mark_loop(x+1, y, current_distance+1, i)
				elif i==3 and y>0:
					mark_loop(x, y-1, current_distance+1, i)

for i in maze[start[0]][start[1]]:
	if i:
		mark_loop(*start, 1)

# print('\n'.join([str(distances[i]) for i in range(len(distances))]))
print(max([max(row) for row in distances]))