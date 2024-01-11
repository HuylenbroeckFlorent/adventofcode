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

# Returns index of the first two successives identical lines starting from 'start'. Returns 0 if no such lines are found.
def find_next_incidence_index(pattern, start=0):
	previous_line = pattern[start]
	for i in range(start+1, len(pattern)):
		if pattern[i] == previous_line:
			return i
		previous_line = pattern[i]
	return 0

# Check that strings are mirrored around certain index.
def check_reflection(pattern):
	incidence_index = find_next_incidence_index(pattern)
	while incidence_index > 0:
		reflection_length = min(incidence_index, len(pattern)-incidence_index)

		mirrored = True
		for incidence_length in range(1,reflection_length):
			mirrored = mirrored and (pattern[incidence_index-incidence_length-1] == pattern[incidence_index+incidence_length])
			if not mirrored:
				incidence_index = find_next_incidence_index(pattern, incidence_index)
				break

		if mirrored:
			return incidence_index
	return 0

def transpose(pattern):
	return [''.join([x[i] for x in pattern]) for i in range(len(pattern[0]))]

notes_total = 0
for pattern in patterns:
	notes_total += 100*check_reflection(pattern)
	notes_total += check_reflection(transpose(pattern))

print(notes_total)
