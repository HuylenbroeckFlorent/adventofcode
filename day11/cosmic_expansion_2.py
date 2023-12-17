# For the second part, we mark the index to be expanded, and add 1000000 to the sum for each of these index in between each two pairs along both axis.
expansion_factor = 1000000

image = [line.strip() for line in open('data.txt', 'r').readlines()]

# Vertical expansion
vertical_expansion_index = [i for i in range(len(image)) if list(set(image[i])) == ['.']]

# Horizontal expansion
horizontal_expansion_index = [j for j in range(len(image[0])) if list(set([image[i][j] for i in range(len(image))])) == ['.']]

# Retrieve galaxies indexes
galaxies = []
for i in range(len(image)):
	for j in range(len(image[i])):
		if image[i][j] == '#':
			galaxies.append((i, j))

# Compute distances for each unique pair.
# We are computing the manhattan distance. We don't have to bother with steps, we can just look at the horizontal and vertical distance and sum them.
sum_of_distances = 0
while len(galaxies) > 0:
	current = galaxies[0]
	galaxies = galaxies[1:]

	for galaxie in galaxies:

		sum_of_distances += abs(current[0] - galaxie[0])
		for v in vertical_expansion_index:
			if v<=current[0] and v<=galaxie[0]:
				continue
			elif v>=current[0] and v>=galaxie[0]:
				break
			else:
				sum_of_distances += expansion_factor - 1

		sum_of_distances += abs(current[1] - galaxie[1])
		for h in horizontal_expansion_index:
			if h<=current[1] and h<=galaxie[1]:
				continue
			elif h>=current[1] and h>=galaxie[1]:
				break
			else:
				sum_of_distances += expansion_factor - 1

print(sum_of_distances)