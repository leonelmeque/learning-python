import random

print("Lets play rock, paper, scissors...")

player = input("Player 1, make your move: ").lower()

use_cases = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

computer = list(use_cases.keys())[random.randint(0,2)]

if player == computer:
    print("Draw")
elif use_cases[player] == computer:
    print("Human player won")
elif use_cases[computer] == player:
    print("Computer won")
else:
    print("Something went wrong")



