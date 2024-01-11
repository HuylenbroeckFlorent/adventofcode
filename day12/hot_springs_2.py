# For this part, we start by only considering the last group of damaged springs.
# G <- last group of damged springs
# We go trough the list of springs S, keeping track of how many way there are to arrange that group starting from each index of S.
# We obtain a list M of length len(springs)+1 which value at index i indicates the number of way we can arrange G damaged springs starting at index i in S.
# Then, we consider the previous group of damaged springs
# G <- previous group of damaged springs 
# and update list M by creating a temprorary list M_tmp and filling that list while reading S from its end. 
# If we encounter a '.' in S at index j, we simply copy the value from the previous cell M_tmp[i] <- M_tmp[i+1]
# If we encounter a '#' in S at index j and the substring in S of length G_n-1 starting at j is a group of damaged springs, then M_tmp[j] = M[j+G+1]
# If we encounter a '?' in S at index j, we sum both of the above cases.
# When S is completely read, with update M with M_tmp and proceed with the previous group of damaged springs. 
# When all the groups of damaged springs are processed, the value in the first cell of M gives the total amount of arrangment.
condition_records = [line.strip() for line in open('data.txt', 'r').readlines()]

valid_arrangment_count = 0
for condition_record in condition_records:

	springs, damaged_groups = condition_record.split(' ')
	damaged_groups = [int(x) for x in damaged_groups.split(',')]

	springs = '?'.join([springs] * 5)
	damaged_groups *= 5

	# Add a padding '.' if springs does not end in a '.' already.
	springs += '' if springs[-1] == '.' else '.	'

	# Initialize M of length len(springs)+1 filled with 1 starting from the end until we encounter a spring.
	matcher = [0] * (len(springs)+1)
	matcher[-1] = 1
	tail = len(springs)-1
	while springs[tail] != '#' and tail >= 0:
		matcher[tail] = 1
		tail -= 1

	# Proceed each group individually starting from the last one.
	for i in range(len(damaged_groups)-1,-1,-1):
		current_group = damaged_groups[i]
		matcher_tmp = [0] * len(matcher)

		for j in range(len(springs)-1,-1,-1):
			if springs[j] in '#?':
				try:
					if '.' not in springs[j:j+current_group] and springs[j+current_group] != '#':
						try:
							matcher_tmp[j] += matcher[j+current_group+1]
						except IndexError:
							matcher_tmp[j] += matcher[-1]
				except IndexError:
					pass

			if springs[j] in '.?':
				matcher_tmp[j] += matcher_tmp[j+1]

		matcher = matcher_tmp

	valid_arrangment_count += matcher[0]

print(valid_arrangment_count)
