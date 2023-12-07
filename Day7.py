rankings = {
    'A': 12,
    'K': 11,
    'Q': 10,
    'J': 9,
    'T': 8,
    '9': 7,
    '8': 6,
    '7': 5,
    '6': 4,
    '5': 3,
    '4': 2,
    '3': 1,
    '2': 0,
    '1': -1  # Joker
}


# Returns hand as a 5-tuple where each element is that card's 'ranking'
def hand_to_ranking(hand: str):
    return rankings[hand[0]], \
           rankings[hand[1]], \
           rankings[hand[2]], \
           rankings[hand[3]], \
           rankings[hand[4]]


def task1(path, part2=False):
    with open(path, 'r') as file:
        # The buckets of each hand, holds tuples of (hand, bid)
        five_oak = []
        four_oak = []
        full_house = []
        three_oak = []
        two_pair = []
        one_pair = []
        high_card = []
        all_buckets = [high_card, one_pair, two_pair, three_oak, full_house, four_oak, five_oak]
        for line in file.readlines():
            line = line.rstrip()
            hand, bid = line.split(' ')

            if part2:
                hand = hand.replace('J', '1')

            # Check what kind of hand we have. We can deduce our hand using the number of
            # unique keys we have. For example, high card will have 5 keys, five_oak will have 1,
            # two pair will have 3 keys, one pair will have 4 keys, four_oak will have 2 keys, three_oak will have
            # 3 keys, full house has 2 keys. As you can see, we must distinguish between 3 keys and 2 keys, since both
            # have 2 cases.
            card_map = {}
            joker_occurrences = 0
            for c in hand:
                if c == '1': # Joker
                    joker_occurrences += 1
                    continue
                if c in card_map:
                    card_map[c] += 1
                else:
                    card_map[c] = 1

            if part2:
                if joker_occurrences == 5:
                    card_map['1'] = 5
                elif joker_occurrences > 0:
                    sorted_cards = sorted(card_map.items(), key=lambda pair: pair[1], reverse=True)
                    highest_key = sorted_cards[0][0]
                    card_map[highest_key] += joker_occurrences

            match len(card_map):
                case 5:
                    high_card.append((hand, bid))
                case 4:
                    one_pair.append((hand, bid))
                case 3:
                    # two pair will have a structure of (2, 2, 1), three_oak will be (3, 1, 1)
                    if 2 in card_map.values():
                        two_pair.append((hand, bid))
                    else:
                        three_oak.append((hand, bid))
                case 2:
                    if 4 in card_map.values():
                        four_oak.append((hand, bid))
                    else:
                        full_house.append((hand, bid))
                case 1:
                    five_oak.append((hand, bid))

        # Sort all of our buckets. Note this results in an ascending order, so our highest value
        # card are at the end of the bucket, which just makes ranking below easier, since we start at 1.
        for bucket in all_buckets:
            bucket.sort(key=lambda tupl: hand_to_ranking(tupl[0]))

        # Now get our result by multiplying bid by rank
        rank = 1
        solution = 0
        for bucket in all_buckets:
            for hand, bid in bucket:
                solution += int(bid) * rank
                rank += 1
        return solution


print('Answer 1:', task1('Day7.txt'))

# For part 2, combine with part 1 since minimal things change. Instead, if we have a joker card, we want to
# append 1 to count of the highest card occurrence, which we'll have to do at the end, since if J appears first,
# (for example, JKQ11) we won't know the highest occurrence. Also, there's the case of JJJJJ, in which no card
# is the highest occurence. In that case, if Joker_occurrences = 5, then just make it a 5 of a kind.
# After we determine the hand, we can replace all jokers with the value of '1' which will have the lowest
# value.
print('Answer 1:', task1('Day7.txt', True))

