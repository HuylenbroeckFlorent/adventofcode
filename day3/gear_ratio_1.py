schematic = open('data.txt', 'r')
schematic_lines = schematic.readlines()

current_number = ''
current_number_adjacency = False
current_sum = 0

def check(char):
	return not (char.isdigit() or (char == '.') or (char == '\n'))

for i in range(len(schematic_lines)):
	schematic_line = schematic_lines[i]

	for j in range(len(schematic_line)):
		schematic_char = schematic_line[j]

		# Read character. Append to number if it's a digit. Treat the previously read whole number if it's not a digit.
		if schematic_char.isdigit():
			current_number += schematic_char

			if len(current_number) == 1:
				if i>0:
					if j>0:
						current_number_adjacency = current_number_adjacency or check(schematic_lines[i-1][j-1])
					current_number_adjacency = current_number_adjacency or check(schematic_lines[i-1][j])

				if j>0:
					current_number_adjacency = current_number_adjacency or check(schematic_lines[i][j-1])

				if i<len(schematic_lines)-1:
					if j>0:
						current_number_adjacency = current_number_adjacency or check(schematic_lines[i+1][j-1])
					current_number_adjacency = current_number_adjacency or check(schematic_lines[i+1][j])
			else:
				if i>0:
					current_number_adjacency = current_number_adjacency or check(schematic_lines[i-1][j])
				if i<len(schematic_lines)-1:
					current_number_adjacency = current_number_adjacency or check(schematic_lines[i+1][j])

		else:
			if len(current_number) > 0:
				if i>0:
					current_number_adjacency = current_number_adjacency or check(schematic_lines[i-1][j])

				current_number_adjacency = current_number_adjacency or check(schematic_char)

				if i<len(schematic_lines)-1:
					current_number_adjacency = current_number_adjacency or check(schematic_lines[i+1][j])

				if current_number_adjacency:
					print('ACCEPTED : '+current_number)
					current_sum += int(current_number)
				else:
					print('REJECTED : '+current_number)

			current_number = ''
			current_number_adjacency = False

print(current_sum)