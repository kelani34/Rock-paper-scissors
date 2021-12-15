rock = '''

ROCK
ROCK
ROCK
'''

paper = '''

PAPER
PAPER
PAPER
'''

scissors = '''

SCISSORS
SCISSORS
SCISSORS
'''

import random
#  0 == rock
#  1 == paper
#  2 == scissors

images = [rock, paper,  scissors]

user_input = int(input("What do you choose? Type 0 for 'Rock', 1 for 'Paper'and 2 for 'Scissors' : \n"))

if user_input >= 3 or user_input < 0:
    print("INVALID: You Lose")
    
else:
    print(images[user_input])
    comp_input = random.randint(0, 2)
    print("Computer chose:")
    print(images[comp_input])

    if comp_input == 0 and user_input == 2:
        print("You lose")
    elif user_input == 0 and comp_input == 2:
        print("You Win!")
    elif user_input == comp_input:
        print("Its a draw!")     
    elif user_input > comp_input:
        print("You Win")    
    elif comp_input > user_input:
        print("You Win")
        

    