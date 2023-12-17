image = [line.strip() for line in open('data.txt', 'r').readlines()]

# Vertical expansion
i=0
while i < len(image):
	row = image[i]
	if list(set(row)) == ['.']:
		image.insert(i, row)
		i+=1
	i+=1

# Horizontal expansion
j=0
while j < len(image[0]):
	column = [row[j] for row in image]
	if list(set(column)) == ['.']:
		for i in range(len(image)):
			image[i] = image[i][:j] + '.' + image[i][j:]
		j+=1
	j+=1

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
		sum_of_distances += abs(current[1] - galaxie[1])

print(sum_of_distances)