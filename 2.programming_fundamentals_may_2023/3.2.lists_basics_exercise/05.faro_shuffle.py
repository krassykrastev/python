# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half.
# Then the cards in the two halves are perfectly interleaved, such that the original bottom card is still on the bottom and the original top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second line receives a count of faro shuffles that should be made.
# Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.
#
# Input1:
# a b c d e f g h
# 5
#
# Output1: ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']
#
# Input2:
# one two three four
# 3
#
# Output2: ['one', 'three', 'two', 'four']

deck_of_cards = input().split()
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):
    final_deck = []
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]

    for card_index in range(len(right_part)):
        final_deck.append(left_part[card_index])
        final_deck.append(right_part[card_index])

    deck_of_cards = final_deck

print(final_deck)