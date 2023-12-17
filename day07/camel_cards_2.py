games = open('data.txt', 'r').readlines()

order = 'J23456789TQKA'

scores_and_bids = []

for cards, bid in [game.split(' ') for game in games]:
	hand = []
	jokers = 0
	for card in list(set(cards)):
		if card == 'J':
			jokers = cards.count(card)
		else:
			hand.append(cards.count(card))

	# We can score the hands simply using the number of unique card in them.
	# This works as well as part 1 since it's awlays having the maximum amount of the same
	# card that wins the more point, so jokers will all be counted as the same card.
	# Only the case when there's 5 jokers in hand is checked separately.
	score = 4 if jokers == 5 else 5-len(hand)

	# Exceptions:
	# A triple and two pairs that have the same number of unique card.
	# Tie-break by looking if there's 3 of the same card + jokers and score accordingly.
	if len(hand) == 3 and (3-jokers) in hand:
		score += 0.5

	# A full house and four of a kind too,
	# Tie-break looking for 4 of the same card + jokers.
	if len(hand) == 2 and (4-jokers) in hand:
		score += 0.5 

	scores_and_bids.append(((score, *[order.index(card) for card in cards]), int(bid.strip('\n'))))

scores_and_bids = sorted(scores_and_bids, key=lambda x: x[0])

print(sum([(i+1)*scores_and_bids[i][1] for i in range(len(scores_and_bids))]))