### The idea for the second part is to tread seeds as ranges.
# Each seed range will be stored as a tuple (seed_start, seed_length)
# Successive mappings will be treated similarly as the part 1, replacing their value from the old mapping with those from the resulting
# mapping iteratively. Except this time, seed range might be split into more smaller ranges to respect the mappings.
# e.g. a mapping '50 98 10' will split the seed range (95, 10) into the two seed ranges (95, 3) and (50, 7).
#
# Storing only the first value of each range is sufficient since the mapping is always ascending, so the first value of any range will
# be the lowest one for that range.

almanac = open('data.txt', 'r').readlines()

# Extract almanac data
# This time, seeds will be treated as tuple (seed_start, seed_length)
seeds_data = [int(x) for x in almanac[0].strip('\n').split(' ')[1::]]
seeds = []
for i in range(0, len(seeds_data), 2):
	seeds.append((seeds_data[i], seeds_data[i+1]))

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
current_map = [seed for seed in seeds]

# Similar as part 1, we treat each mapping iteratively
for _map in maps:

	# This time we are not aplying a diff_map but replacing current_map with next_map.
	next_map = []

	# For each mapping, each map in treated separately, creating a 'next_map' that will replace the current map.
	for dest_start, source_start, length in _map:

		# Residual seed ranges that do not fit any mapping.
		unmapped = []

		# We need to check for total or partial overlaps between 
		# mapping range : [source_start, source_start + length] 
		# and 
		# seed range : [seed_start, seed_start + seed_length]
		# Any overlap would go in the 'next_map' with its updated range, and the remaining non-overlapping range will be put in 'unmapped'
		# for the following iterations of the current mapping.
		for seed_start, seed_length in current_map:
			# CASE 1 : seed range is completely contained in mapping range
			# -> The whole seed range gets offset
			if seed_start >= source_start and seed_start + seed_length <= source_start + length:
				next_map.append((dest_start + seed_start - source_start, seed_length))

			# CASE 2 : seed range overlaps only the lower values of the mapping range. 
			# -> Offset the lower values and put the remaining values in the unmapped list.
			elif 	seed_start <= source_start \
					and seed_start + seed_length <= source_start + length \
					and seed_start + seed_length >= source_start:
				overlap_length = seed_length - (source_start - seed_start)
				next_map.append((dest_start, overlap_length))
				unmapped.append((seed_start, seed_length - overlap_length))

			# CASE 3 : seed range overlaps only the highest values of the mapping range.
			# -> Offset the higher values and put the remaining values in the unmapped list.
			elif 	seed_start >= source_start \
					and seed_start + seed_length >= source_start + length \
					and seed_start <= source_start + length:
				overlap_length = source_start + length - seed_start
				next_map.append((dest_start + length - overlap_length, overlap_length))
				unmapped.append((source_start + length, seed_length - overlap_length))

			# CASE 4 : mapping range is completely contained in seed range.
			# -> Offset all of the mapping range and add both extremities to unmapped list.
			elif seed_start <= source_start and seed_start + seed_length >= source_start + length:
				next_map.append((dest_start, length))
				unmapped.append((seed_start, source_start - seed_start))
				unmapped.append((source_start + length, (seed_start + seed_length) - (source_start + length)))

			# CASE 5 : no overlap.
			# -> No offset, seed range goes into unmapped list.
			else:
				unmapped.append((seed_start, seed_length))

		# We only need to look at unmapped seed ranges for the rest of the iteration.
		current_map = [x for x in unmapped]

	# Update current map for next iteration.
	current_map = current_map + next_map

print(min([x[0] for x in current_map]))