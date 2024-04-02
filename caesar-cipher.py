character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']


def caesar_cipher(text="abc", shift=1):
    """
    Caesar Cipher return the cipher text in alphabetical order with specified shift
    """
    text = text.lower()
    shift = shift % len(character)
    shift_char = character[shift:] + character[:shift]
    # maketrans argument must be str not list
    table = str.maketrans(''.join(character), ''.join(shift_char))
    text = text.translate(table)
    return text


text = input('Password to encrypt: ')
shift = int(input('Enter shift: '))
print(caesar_cipher(text, shift))

