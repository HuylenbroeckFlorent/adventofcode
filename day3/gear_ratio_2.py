schematic = open('data.txt', 'r')
schematic_lines = schematic.readlines()

def extract_numbers_around_index(line, j):

	current_number = ''
	numbers = []
	is_elligible = False

	for i in range(len(line)):
		
		# If at one point while parsing the number we're at indexes around j, then the number is elligible for extraction
		if i>=j and i<=j+1:
			is_elligible = True

		if line[i].isdigit():
			current_number += line[i]
		else:
			if is_elligible and current_number != '':
				numbers.append(int(current_number))
			current_number = ''
			is_elligible = False

	return numbers


current_sum = 0

for i in range(len(schematic_lines)):
	schematic_line = schematic_lines[i]

	for j in range(len(schematic_line)):
		schematic_char = schematic_line[j]

		if schematic_char == '*':

			gear_numbers = []
			if i>0:
				gear_numbers += extract_numbers_around_index(schematic_lines[i-1], j)
			gear_numbers += extract_numbers_around_index(schematic_lines[i], j)
			if i<len(schematic_lines)-1:
				gear_numbers += extract_numbers_around_index(schematic_lines[i+1], j)

			if len(gear_numbers) == 2:
				current_sum += gear_numbers[0] * gear_numbers[1]

print(current_sum)




