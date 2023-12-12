MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

games_file = open('data.txt', 'r')
games = games_file.readlines()

game_id_sum = 0

def validate_handful(handful):
	cubes = handful.split(',')
	for cube in cubes:
		amount = int(''.join(filter(str.isdigit, cube))) # https://stackoverflow.com/a/26825833
		if ('red' in cube and amount > MAX_RED) \
		or ('green' in cube and amount > MAX_GREEN) \
		or ('blue' in cube and amount > MAX_BLUE):
			return False
	return True 

for game in games:
	game.strip('\n')
	game_id, game_data = game.split(':')
	id = int(''.join(filter(str.isdigit, game_id)))

	handfuls = game_data.split(';')
	valid_game = True
	for handful in handfuls:
		valid_game &= validate_handful(handful)
		if not valid_game:
			break

	if valid_game:
		game_id_sum += id

print(game_id_sum)