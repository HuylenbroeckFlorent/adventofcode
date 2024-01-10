condition_records = [line.strip() for line in open('data.txt', 'r').readlines()]

# invariant : springs[0:current] is treated and complies with the damaged arrangment
def breath_first_search(springs, current, damaged_arrangments):

	# print(springs)
	# print(current)
	# print(damaged_arrangments)
	# print()

	# Base case
	if damaged_arrangments == [0] and '#' not in set(list(springs[current::])):
		return 1

	# We reached the end without encountering the base case
	if current == len(springs):
		return 0

	# Too long group of damaged springs
	if (not damaged_arrangments) or damaged_arrangments[0] < 0:
		return 0

	total = 0

	current_spring = springs[current]
	previous_spring = springs[current-1] if current > 0 else '.'

	if current_spring in ('#', '.'):
		return total + breath_first_search(springs, current + 1, update_damaged_arrangments(previous_spring, current_spring, damaged_arrangments))
	else:
		treated_springs = springs[0:current]
		sprints_to_treat = springs[current+1::]
		total += breath_first_search(treated_springs + '.' + sprints_to_treat, current + 1, update_damaged_arrangments(previous_spring, '.', damaged_arrangments))
		total += breath_first_search(treated_springs + '#' + sprints_to_treat, current + 1, update_damaged_arrangments(previous_spring, '#', damaged_arrangments))
		return total



# We update the damaged arrangments by substracting one to the leftmost value whenever we encounter a spring.
# When it reaches 0, the 0 is left until another group of damaged spring is met then we remove it and continue substracting to the new leftmost value.
def update_damaged_arrangments(previous, current, damaged_arrangments):
	new_damaged_arrangments = [x for x in damaged_arrangments]
	if current == '#':
		if previous == '.':
			if new_damaged_arrangments[0] == 0:
				new_damaged_arrangments = new_damaged_arrangments[1:]
			else:
				return []
		if new_damaged_arrangments:
			new_damaged_arrangments[0] -=1
		return new_damaged_arrangments
	else:
		if previous == '#' and new_damaged_arrangments[0] != 0:
			return []
		else:
			return new_damaged_arrangments

			


valid_arrangment_count = 0
for condition_record in condition_records:

	springs, damaged_arrangments = condition_record.split(' ')
	damaged_arrangments = [int(x) for x in damaged_arrangments.split(',')]

	springs *= 5
	damaged_arrangments *= 5
	damaged_arrangments = [0] + damaged_arrangments

	print(springs)
	print(damaged_arrangments)

	ret = breath_first_search(springs, 0, damaged_arrangments)

	print(ret)

	valid_arrangment_count += ret

	print()

print(valid_arrangment_count)

	