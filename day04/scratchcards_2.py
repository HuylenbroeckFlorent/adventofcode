scratchcards = open('data.txt', 'r').readlines()

copies = [1] * len(scratchcards)

# Processing the cards is the same, the score we compute is different. 
# If a card has N matching numbers, we add the number of copy of that card to the N following cards counters.  
for i in range(len(scratchcards)):
	scratchcard = scratchcards[i]

	_, scratchcard_numbers = scratchcard.split(':')
	winning_numbers, candidate_numbers = scratchcard_numbers.split('|')

	winning_numbers = [int(x) for x in winning_numbers.strip('\n').split(' ') if x.strip(' ').isdigit()]
	candidate_numbers = [int(x) for x in candidate_numbers.strip('\n').split(' ') if x.strip(' ').isdigit()]

	match = 0
	for candidate_number in candidate_numbers:
		if candidate_number in winning_numbers:
			match += 1
			winning_numbers.remove(candidate_number)

	for j in range(match):
		if i+j < len(scratchcards):
			copies[i+j+1] += copies[i]

print(sum(copies))