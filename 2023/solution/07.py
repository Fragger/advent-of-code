import sys
from collections import Counter

scores = [(1,1,1,1,1), (2,1,1,1), (2,2,1), (3,1,1), (3,2), (4,1), (5,)]

def p1key(hand):
    cards, _ = hand
    score = scores.index(tuple(count[1] for count in Counter(cards).most_common()))
    order = tuple('23456789TJQKA'.index(card) for card in cards)
    return (score, order)

def p2key(hand):
    cards, _ = hand
    order = tuple('J23456789TQKA'.index(card) for card in cards)

    cards = Counter(cards)
    j = cards.pop('J',0) if cards['J']<5 else 0
    score = [count[1] for count in cards.most_common()]
    score[0] += j
    score = scores.index(tuple(score))

    return (score, order)

hands = []
with open(sys.argv[1] if len(sys.argv) > 1 else '../input/07') as f:
    for line in f:
        cards, bid = line.split()
        hands.append((cards, int(bid)))

hands.sort(key=p1key)
print(sum((i+1)*bid for i, (_, bid) in enumerate(hands)))

hands.sort(key=p2key)
print(sum((i+1)*bid for i, (_, bid) in enumerate(hands)))
