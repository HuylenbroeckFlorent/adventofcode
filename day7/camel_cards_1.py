games = open('data.txt', 'r').readlines()

order = '23456789TJQKA'

scores_and_bids = []

for cards, bid in [game.split(' ') for game in games]:
	hand = []
	for card in list(set(cards)):
		hand.append(cards.count(card))

	# We can score the hands simply using the number of unique card in them.
	score = 5-len(hand)

	# Exceptions:
	# A triple and two pairs that have the same number of unique card.
	# Tie-break by looking if there's 3 of the same card and score accordingly.
	if len(hand) == 3 and 3 in hand:
		score += 0.5

	# A full house and four of a kind too,
	# Tie-break looking for 4 of the same card.
	if len(hand) == 2 and 4 in hand:
		score += 0.5 

	scores_and_bids.append(((score, *[order.index(card) for card in cards]), int(bid.strip('\n'))))

scores_and_bids = sorted(scores_and_bids, key=lambda x: x[0])

print(sum([(i+1)*scores_and_bids[i][1] for i in range(len(scores_and_bids))]))