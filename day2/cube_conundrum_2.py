games_file = open('data.txt', 'r')
games = games_file.readlines()

power_sum = 0

for game in games:
	game.strip('\n')
	_, handfuls = game.split(':')

	rgb_max = [0,0,0]

	for cubes in handfuls.split(';'):
		for cube in cubes.split(','):
			amount = int(''.join(filter(str.isdigit, cube))) # https://stackoverflow.com/a/26825833
			if 'red' in cube:
				rgb_max[0] = max(rgb_max[0], amount)
			elif 'green' in cube:
				rgb_max[1] = max(rgb_max[1], amount)
			else:
				rgb_max[2] = max(rgb_max[2], amount)

	power_sum += rgb_max[0]*rgb_max[1]*rgb_max[2]

print(power_sum)