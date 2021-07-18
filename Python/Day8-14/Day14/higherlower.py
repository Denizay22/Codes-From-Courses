# might write a function for deciding winner and check if guess is right or not
from art import logo, vs
from gamedata import data
import random

score = 0

game_end = False
competitors = {
    "A": random.choice(data)
}
print(logo)
while not game_end:
    competitors["B"] = random.choice(data)
    if competitors["A"]["follower_count"] > competitors["B"]["follower_count"]:
        winner = "A"
    else:
        winner = "B"
    print(f"Compare A: {competitors['A']['name']}, a {competitors['A']['description']}, from {competitors['A']['country']}")
    print(vs)
    print(f"Against B: {competitors['B']['name']}, a {competitors['B']['description']}, from {competitors['B']['country']}")
    player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if player_choice == winner:
        score += 1
        print(f"You're right! Current score: {score}")
        competitors["A"] = competitors[winner]
        del competitors["B"]  # will produce error if the key not found. can use dict[key].pop('key') instead.
    else:
        print(f"You're wrong! Your final score: {score}")
        game_end = True
