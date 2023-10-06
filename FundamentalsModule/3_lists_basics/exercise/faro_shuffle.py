cards_for_shuffling = input().split()
count_of_shuffling = int(input())

for shuffle in range(count_of_shuffling):
    shuffled_cards = []
    for cards in range(len(cards_for_shuffling) // 2):
        right_side = cards_for_shuffling[:len(cards_for_shuffling) // 2:]
        left_side = cards_for_shuffling[len(cards_for_shuffling) // 2::]
        shuffled_cards.append(right_side[cards])
        shuffled_cards.append(left_side[cards])
    cards_for_shuffling = shuffled_cards

print(shuffled_cards)
