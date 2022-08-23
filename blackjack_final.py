import random
from art import logo
from replit import clear

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21:
        print("you win, blackjacK!")
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "DRAW"
    elif computer_score == 0:
        return "you lose, computer has a blackjacK!"
    elif user_score == 0:
        return "YOU WIN ,BLACKJACK!"
    elif user_score > 21:
        return "you lose, score over"
    elif computer_score > 21:
        return "You win, computer score over"
    elif user_score > computer_score:
        return "you winn"
    else:
        return "you lose"


def play_game():
    user_cards = []
    computer_cards = []
    end_game = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not end_game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"user cards {user_cards}, and his score {user_score}")
        print(f"computer cards {computer_cards} and his score {computer_score}")
        if user_score == 0 or user_score > 21 or computer_score == 0:
            print(f"koniec gry")
            end_game = True
        else:
            ask = input(
                "Do you want to draw another card?(yes or no)\n").lower()
            if ask == 'yes':
                user_cards.append(deal_card())
            else:
                end_game = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final score is {user_score}")
    print(f"Computer final score is {computer_score}")

    print(compare(user_score, computer_score))


play_game()

while input("do you want to restart the game? (yes or no)\n").lower() == 'yes':
    clear()
    print(logo)
    play_game()
else:
    print("goodbye")
