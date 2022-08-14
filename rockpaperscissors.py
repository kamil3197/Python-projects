import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

pick = int(input("What do you choose? type 0 for rock, 1 for paper or 2 for scissors\n"))
enemy = random.randint(0,2)
if pick == 0:
    print(rock)
    if enemy == 0:
        print(f"enemy chose:\n{rock}")
        print('DRAW')
    elif enemy == 1:
        print(f"enemy chose:\n{paper}")
        print('You lose')
    else:
        print(f"enemy chose:\n{scissors}")
        print('You win')
elif pick == 1:
    print(paper)
    if enemy == 0:
        print(f"enemy chose:\n{rock}")
        print('You Win')
    elif enemy == 1:
        print(f"enemy chose:\n{paper}")
        print('DRAW')
    else:
        print(f"enemy chose:\n{scissors}")
        print('You lose')
elif pick == 2:
    print(scissors)
    if enemy == 0:
        print(f"enemy chose:\n{rock}")
        print('You Lose')
    elif enemy == 1:
        print(f"enemy chose:\n{paper}")
        print('You Win')
    else:
        print(f"enemy chose:\n{scissors}")
        print('Draw')
else:
    print('invalid number')
