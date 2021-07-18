with open("Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter = letter_file.read()

with open("Input/Names/invited_names.txt", mode="r") as names_file:
    name = names_file.readline().strip()  # can change to names = names_file.readlines(), for name in names:
    while len(name) != 0:
        with open(f"Output/ReadyToSend/{name}.txt", mode="w") as send_letter_file:
            send_letter_file.write(letter.replace("[name]", name))
        name = names_file.readline().strip()
