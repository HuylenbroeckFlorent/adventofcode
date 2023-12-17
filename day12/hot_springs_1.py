condition_records = [line.strip() for line in open('data.txt', 'r').readlines()]

# returns the compositions of integer i in n parts. Assume i > n.
def compositions(i, n):

	# Generate initial composition [1, 1, 1, ..., i-n+1]
	current_composition = [1] * n
	current_composition[-1] = i-n+1

	# Return first composition
	yield current_composition

	# From that initial composition, generate all the compositions until we reach [i-n+1, 1, 1, ..., 1]
	while current_composition[0] < i-n+1:

		# Find the highest index of element > 1
		index = max([i for i in range(n) if current_composition[i] > 1])

		# Update current composition
		tmp = current_composition[index]
		current_composition[index-1] += 1
		current_composition[index] = 1
		current_composition[-1] = tmp - 1 

		# Return next composition
		yield current_composition

# Build the string for debug purpose
def build_from(undamaged, damaged):
	_str = ''
	for i in range(len(undamaged)-1):
		_str+= '.'*undamaged[i]
		_str+= '#'*damaged[i]
	_str+= '.'*undamaged[-1]
	return _str

# For each condition record, find the number of undamaged spring and find the integer compositions for that number to generate all the possible 
# arrangment of undamaged springs in between the contiguous damaged spring groups.
# Then, compare these arrangment with the records arrangment too see if they are possible.
valid_arrangment_count = 0
for condition_record in condition_records:

	springs, damaged_arrangments = condition_record.split(' ')
	damaged_arrangments = [int(x) for x in damaged_arrangments.split(',')]

	undamaged_springs_len = len(springs) - sum(damaged_arrangments)
	damaged_arrangments_len = len(damaged_arrangments)

	undamaged_arrangments = []

	if undamaged_springs_len >= damaged_arrangments_len+1:
		for composition in compositions(undamaged_springs_len, damaged_arrangments_len+1):
			undamaged_arrangments.append([x for x in composition])

	if undamaged_springs_len >= damaged_arrangments_len:
		for composition in compositions(undamaged_springs_len, damaged_arrangments_len):
			left_arrangment = [0] + [x for x in composition]
			right_arrangment = [x for x in composition] + [0]
			undamaged_arrangments.append(left_arrangment)
			undamaged_arrangments.append(right_arrangment)

	if undamaged_springs_len >= damaged_arrangments_len-1:
		for composition in compositions(undamaged_springs_len, damaged_arrangments_len-1):
			undamaged_arrangments.append([0] + [x for x in composition] + [0])

	# Compare each arrangment to the condition record.
	for arrangment in undamaged_arrangments:

		valid = True
		current_index = 0
		for i in range(damaged_arrangments_len):
			if '#' in set(springs[current_index:current_index+arrangment[i]]):
				valid = False
			current_index += arrangment[i]
			if '.' in set(springs[current_index:current_index+damaged_arrangments[i]]):
				valid = False
			current_index += damaged_arrangments[i] 
		if '#' in set(springs[current_index:]):
			valid = False
		if valid:
			valid_arrangment_count += 1

print(valid_arrangment_count)