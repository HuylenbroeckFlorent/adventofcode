sequences = open('data.txt').readlines()

current_sum = 0

for sequence in sequences:
	sequence = [int(x) for x in sequence.strip('\n').split(' ')]

	diffs = [sequence]

	# We can't simple check sum(diffs[-1]) == 0 because you can have subsequences like [-2, -1, 0, 1, 2].
	while list(set(diffs[-1])) != [0]:
		diffs.append([diffs[-1][i+1] - diffs[-1][i] for i in range(len(diffs[-1])-1)])

	# Adding placeholders and filling them is actually the same as summing the last value for each subsequence.
	current_sum += sum([diff[-1] for diff in diffs])

print(current_sum)