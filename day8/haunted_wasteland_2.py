import math

_map = open('data.txt', 'r').readlines()

sequence = _map[0].strip('\n')
nodes = _map[2::]

network = {}
starting_nodes = []

for i in range(len(nodes)):
	node_name, node_next = nodes[i].split(' = ')
	node_next = node_next.strip('()\n')
	network[node_name] = node_next.split(', ')
	if node_name[-1] == 'A':
		starting_nodes.append(node_name)

path_lengths = []

# We just need to find the length from each individual starting point to their respective end point.
for current in starting_nodes:
	steps = 0
	while current[-1] != 'Z':
		for step in sequence:
			steps += 1
			if step == 'L':
				current = network[current][0]
			else:
				current = network[current][1]

			if current[-1] == 'Z':
				path_lengths.append(steps)
				break;

# Then find the least common multiple between all of these lengths.
print(math.lcm(*path_lengths))