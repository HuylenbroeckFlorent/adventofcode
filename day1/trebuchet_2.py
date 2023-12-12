calibration_document = open('data.txt', 'r')
calibration_document_lines = calibration_document.readlines()

calibration_values = []

text_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven' ,'eight', 'nine']

for calibration_line in calibration_document_lines:
	calibration_line = calibration_line.strip('\n')
	calibration_digits = []
	for i in range(len(calibration_line)):
		if calibration_line[i].isdigit():
			calibration_digits.append(calibration_line[i])
		else:
			for j in range(len(text_digits)):
				d = text_digits[j]
				if d in calibration_line[i:i+len(d)]:
					calibration_digits.append(str(j))
					break

	calibration_values.append(int(calibration_digits[0]+calibration_digits[-1]))

print(sum(calibration_values))