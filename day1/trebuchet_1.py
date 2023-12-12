calibration_document = open('data.txt', 'r')
calibration_document_lines = calibration_document.readlines()

calibration_values = []

for calibration_line in calibration_document_lines:
	calibration_line = calibration_line.strip('\n')
	calibration_digits = []
	for calibration_char in calibration_line:
		if calibration_char.isdigit():
			calibration_digits.append(calibration_char)
	calibration_values.append(int(calibration_digits[0]+calibration_digits[-1]))

print(sum(calibration_values))