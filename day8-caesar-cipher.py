character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(plain_text, shift_amount, direction="encode"):
    """
    Caesar Cipher return the cipher text in alphabetical order with specified shift and direction in alphabet character
    """
    code = ''
    if direction == 'decode':
        shift_amount *= -1

    for char in plain_text:
        if char in character:
            index = character.index(char)
            new_index = index + shift_amount
            new_char = character[new_index]
            code += new_char
        else:
            code += char

    return code

text_input = input('Password to encrypt: ').lower()
shift_input = int(input('Enter shift: '))
direction_input = input('Encode or decode: ').lower()
print(caesar_cipher(text_input, shift_input, direction_input))

