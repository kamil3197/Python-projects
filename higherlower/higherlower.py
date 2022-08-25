from art import logo, vs
from game_data import data
import random
from replit import clear

print(logo)
first_person = {}
second_person = {}

score = 0


#info about first person to print
def account_A(first_person):
    name = first_person["name"]
    description = first_person["description"]
    country = first_person["country"]
    return (f"compare A: {name}, a {description}, from {country}")


#info about second person to print
def account_B(second_person):
    name = second_person["name"]
    description = second_person["description"]
    country = second_person["country"]
    return (f"Against B: {name}, a {description}, from {country}")


def check_answer(ask, followers_A, followers_B):
    if followers_A > followers_B:
        return ask == 'a'
    else:
        return ask == 'b'


end_game = False
second_person = random.choice(data)

while not end_game:
    first_person = second_person
    second_person = random.choice(data)
    if first_person == second_person:
        second_person = random.choice(data)
    followers_A = first_person["follower_count"]
    followers_B = second_person["follower_count"]
    print(account_A(first_person))
    print(vs)
    print(account_B(second_person))

    ask = input("who has more followers? a or b \n").lower()

    is_correct = check_answer(ask, followers_A, followers_B)
    clear()
    if is_correct:
        score += 1
        print(f"you did well !you score is {score}")
    else:
        end_game = True
        print(f"you lose, final score {score}")
