almanac = open('test.txt', 'r').readlines()

# Extract almanac data
seeds = [int(x) for x in almanac[0].strip('\n').split(' ')[1::]]
almanac = almanac[1::]

maps = []
current_map = []

for line in almanac:
	if line == '\n':
		continue

	elif line[0].isalpha():
		if current_map:
			maps.append(current_map)
			current_map = []

	else:
		current_map.append([int(x) for x in line.strip('\n').split(' ')])
if current_map:
	maps.append(current_map)


### Process almanac data
# The goal is to know which seed correspond to which location, we don't care about the intermediary mapping.
current_map = [seed for seed in seeds]
n_seeds = len(seeds)

for _map in maps:

	# For each mapping, create a 'difference' map that will have to be applied to the current map.
	diff_map = [0 for x in current_map]

	for dest_start, source_start, length in _map:

		# Instead of permutations, the difference between source and destination range can be seen as an offet. 
		# If source range [98, 99] becomes [50, 51], it's the same as applying an offset of -48 to the source values. 
		diff = source_start - dest_start
		diff_map = [diff if (current_map[x] in range(source_start, source_start+length)) else diff_map[x] for x in range(n_seeds)]

	# Once all the ranges of a mapping are processed, we apply the offset to our current map and proceed to the next mapping.
	current_map = [current_map[x]-diff_map[x] for x in range(n_seeds)]

print(min(current_map))