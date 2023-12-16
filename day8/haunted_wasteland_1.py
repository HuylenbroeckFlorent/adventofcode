_map = open('data.txt', 'r').readlines()

sequence = _map[0].strip('\n')
nodes = _map[2::]

network = {}
# The first and second nodes are always AAA and ZZZ... Found it the hard way.
current = 'AAA' 
last = 'ZZZ'

for i in range(len(nodes)):
	node_name, node_next = nodes[i].split(' = ')
	node_next = node_next.strip('()\n')
	network[node_name] = node_next.split(', ')

steps = 0
while current != last:
	for step in sequence:
		steps += 1
		if step == 'L':
			current = network[current][0]
		else:
			current = network[current][1]

		if current == last:
			break;

print(steps)
