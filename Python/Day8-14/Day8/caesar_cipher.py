def caesar(text, shift, direction):
    text_list = list(text)
    if direction == 'decode':
        shift *= -1
    for i in range(len(text)):
        if text_list[i] in alphabet:
            text_list[i] = alphabet[(alphabet.index(text_list[i]) + shift) % len(alphabet)]
            # modulus for out of list index

    encoded_text = ''.join(text_list)
    print(f"The decoded text is {encoded_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode' or direction == 'decode':
    caesar(text, shift, direction)
else:
    print("Wrong input")
