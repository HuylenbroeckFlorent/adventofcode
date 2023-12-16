sequences = open('data.txt').readlines()

current_sum = 0

for sequence in sequences:
	sequence = [int(x) for x in sequence.strip('\n').split(' ')]

	diffs = [sequence]

	# We can't simple check sum(diffs[-1]) == 0 because you can have subsequences like [-2, -1, 0, 1, 2].
	while list(set(diffs[-1])) != [0]:
		diffs.append([diffs[-1][i+1] - diffs[-1][i] for i in range(len(diffs[-1])-1)])

	# Adding placeholders and filling them is actually the same as summing the last value for each subsequence
	# Except this time we need alterating plus and minus sign before the values because we are not adding a value to the previous one,
	# instead we are substracting a value from the previous one.
	# Having alteratin plus and minus simulates the accumulation of minus signs when iteratively substracting values from one subsequence to its parent sequence. 
	current_sum += sum([diffs[i][0]*((-1)**i) for i in range(len(diffs))])

print(current_sum)