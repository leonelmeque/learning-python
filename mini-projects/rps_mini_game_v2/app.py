from random import randint

player_wins = 0
computer_wins = 0


while player_wins < 2 and computer_wins < 2:
    print("...rock...")
    print("...paper...")
    print("...scissors...")
    print("Go!")

    player = input("Enter your choice (enter q/quit to stop the game): ").lower()
    random_num = randint(0,2)

    if player == "q" or player == "quit":
        computer_wins = None
        player_wins = None
        break

    if random_num == 0:
        computer = "rock"
    elif random_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"The computer plays: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer wins :( ")
            computer_wins += 1
        else:
            print("Player wins!")
            player_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    elif  player == "scissors":
        if computer == "rock":
            print("Computer wins!")
            computer_wins += 1
        else:
            print("You win!")
            player_wins += 1


if player_wins is not None and computer_wins is not None:
    print(f"The score is\nPlayer: {player_wins}\nComputer: {computer_wins}")