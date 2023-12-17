scratchcards = open('data.txt', 'r').readlines()

current_sum = 0

for scratchcard in scratchcards:
	_, scratchcard_numbers = scratchcard.split(':')
	winning_numbers, candidate_numbers = scratchcard_numbers.split('|')

	winning_numbers = [int(x) for x in winning_numbers.strip('\n').split(' ') if x.strip(' ').isdigit()]
	candidate_numbers = [int(x) for x in candidate_numbers.strip('\n').split(' ') if x.strip(' ').isdigit()]

	match = -1
	for candidate_number in candidate_numbers:
		if candidate_number in winning_numbers:
			match += 1
			winning_numbers.remove(candidate_number)

	if match >= 0:
		current_sum += 2**match 

print(current_sum)