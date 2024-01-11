notes = open('data.txt', 'r').readlines()

patterns = []
tmp_pattern = []
for line in notes:
	if tmp_pattern and line == '\n':
		patterns.append(tmp_pattern)
		tmp_pattern = []
	else:
		tmp_pattern.append(line.strip())
patterns.append(tmp_pattern)

# Instead of using equality, we check the number of different characters between two lines
def compare_lines(line_1, line_2):
	diff = 0
	for i in range(len(line_1)):
		diff += line_1[i] != line_2[i]

	return diff

# Returns index of the first two successives identical (or 1-off) lines starting from 'start'. Returns 0 if no such lines are found.
def find_next_incidence_index(pattern, start=0):
	previous_line = pattern[start]
	for i in range(start+1, len(pattern)):
		if compare_lines(pattern[i], previous_line) <= 1:
			return i
		previous_line = pattern[i]
	return 0

# Check that strings are mirrored starting from a given index.
def check_reflection(pattern):
	incidence_index = find_next_incidence_index(pattern)
	while incidence_index > 0:
		reflection_length = min(incidence_index, len(pattern)-incidence_index)

		# Instead of checking for perfect reflexion, we check the number of smudges.
		reflection_score = 0
		for incidence_length in range(0,reflection_length):
			reflection_score += compare_lines(pattern[incidence_index-incidence_length-1], pattern[incidence_index+incidence_length])

		# If that number is exactly one, we found our reflection.
		if reflection_score == 1:
			return incidence_index
		else:
			incidence_index = find_next_incidence_index(pattern, incidence_index)
	return 0

def transpose(pattern):
	return [''.join([x[i] for x in pattern]) for i in range(len(pattern[0]))]

notes_total = 0
for pattern in patterns:
	notes_total += 100*check_reflection(pattern)
	notes_total += check_reflection(transpose(pattern))

print(notes_total)
