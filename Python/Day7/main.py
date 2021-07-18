import random
import words
import ascii

word_list = words.word_list
# from words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
# from ascii import logo
print(ascii.logo)
print(chosen_word)

display = []
guessedChars = []
for _ in range(word_length):
    display += "_"

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess in guessedChars:
        print(f"You already guessed {guess}.")
    else:
        guessedChars += guess
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"Letter {guess} is not in the word. You lose a life")
            lives -= 1

        print(f"{' '.join(display)}")

        # from ascii import stages
        print(ascii.stages[lives])

        if lives == 0:
            print("You lose.")

        if "_" not in display:
            print("You win.")

