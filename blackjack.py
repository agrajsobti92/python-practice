from art import logo
import random


def deal_two_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    return [card1, card2]


def deal_one_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def play_game():
    print(logo)
    cards = deal_two_cards()
    comp_cards = [deal_one_card()]
    print(f"Your cards: {cards}, current score: {sum(cards)}")
    print(f"Computer's first card: {comp_cards}")
    deal = input("Type 'y' to get another card, type 'n' to pass: ")
    while deal == "y":
        cards.append(deal_one_card())
        print(f"Your cards: {cards}, current score: {sum(cards)}")
        if sum(cards) < 21:
            break
        deal = input("Continue? y or n: ")

    while sum(comp_cards) < 17:
        comp_cards.append(deal_one_card())

    print(f"Your cards: {cards}, current score: {sum(cards)}")
    print(f"Computer's cards: {comp_cards}")


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
