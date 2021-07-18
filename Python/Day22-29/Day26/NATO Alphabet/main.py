import pandas

name = input("What is your name?").upper()
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

name_nato = [nato_alphabet[nato_alphabet.letter == letter].code.item() for letter in name]
print(name_nato)

# or you can create a dictionary from csv, then use that

nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
name_nato = [nato_alphabet_dict[letter] for letter in name]
print(name_nato)

