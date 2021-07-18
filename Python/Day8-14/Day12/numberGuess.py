# can separate code to functions like checkLives, checkGuess, etc but for such a small code not needed.
# can set live constants for easy and hard mode ----> EASY_LIVES = 5  HARD_LIVES = 10
import random

number = random.randint(0, 100)
difficulty = input("Choose your difficulty. 'easy' or 'hard'\n")
# check might be needed for wrong input on other projects
live = -1
if difficulty == 'easy':
    live = 10
elif difficulty == 'hard':
    live = 5

gameover = False

while not gameover and live > 0:

    print(f"You have {live} attempts to guess the number.")

    guess = int(input("Make a guess.\n"))

    if guess == number:
        print(f"Right! The number was {number}")
        gameover = True  # if you don't want to hold an extra variable for this, just set live = 0
    else:
        if guess < number:
            print("Too low.\n")
            live -= 1
        elif guess > number:
            print("Too high.\n")
            live -= 1
        if live == 0:
            print(f"You are out of lives. You lose. Number was {number}")
