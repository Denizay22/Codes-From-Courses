# kinda messy and might not work rn, need to be revised

import random


def draw_card(hand):
    hand.append(random.choice(cards))


def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        score -= 10
        hand[hand.index(11)] = 1
    return score


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playerHand = []
computerHand = []

playerHand.append(random.choice(cards))
playerHand.append(random.choice(cards))
computerHand.append(random.choice(cards))
computerHand.append(random.choice(cards))

playerScore = calculate_score(playerHand)
computerScore = calculate_score(computerHand)

isGameEnded = False
while not isGameEnded:
    print(f"Your hand: {playerHand}, Your score: {playerScore}\nComputer's cards: {computerHand[0]}, ?")

    if playerScore == 0 or playerScore == 21:
        print("Congrats! You hit 21! You win!")
    elif playerScore > 21:
        print("You lose! Git gud.")
        isGameEnded = True
        break
    playerChoice = input("Type 'draw' to draw another card, 'stand' to hold on to your cards.\n")

    if playerChoice == 'draw':
        draw_card(playerHand)
        playerScore = calculate_score(playerHand)

    elif playerChoice == 'stand':
        while computerScore < 22 and playerScore > computerScore:
            draw_card(computerHand)
            calculate_score(computerHand)
            isGameEnded = True
        print(f"Your final hand: {playerHand}, Your final score: {playerScore}\nComputer's final hand: {computerHand},"
              f" Computer's final score: {computerScore}")

        if computerScore > 21:
            print("Computer bursts. You win!")
        elif computerScore > playerScore:
            print("You lose! Git gud.")
        elif computerScore == playerScore:
            print("It's a draw.")
