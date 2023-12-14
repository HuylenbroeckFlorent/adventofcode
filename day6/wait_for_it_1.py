races = open('data.txt', 'r').readlines()
times = [int(x) for x in races[0].split(':')[1].strip('\n').split(' ') if x.isdigit()]
distances = [int(x) for x in races[1].split(':')[1].strip('\n').split(' ') if x.isdigit()]

current_product = 1
for i in range(len(times)):
	time = times[i]
	distance = distances[i]
	ways_to_win = 0
	for press_time in range(1, time-1):
		if press_time*(time-press_time) > distance:
			ways_to_win += 1
	if ways_to_win > 0:
		current_product *= ways_to_win

print(current_product)
