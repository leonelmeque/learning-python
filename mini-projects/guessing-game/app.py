import random

random_number = random.randint(1,10)

guess = input("Pick a number from 1 to 10: ")


while True:
    guess = int(guess)
    if guess == random_number:
        print("You got it!")
        play_again = input("Do you want to play again? (y/n)")
        if play_again == "y":
            random_number = random.randint(1, 10)
        else:
            print("Thank you for playing!")
            break
    elif guess < random_number:
        print("Too Low!")
    else:
        print("Too high!")

    guess = input("Pick a number from 1 to 10: ")

