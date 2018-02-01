"""
Problem 2:
Design a program to simulate the monoalphabetic cipher-decipher. The program
asks the user to enter the message and the keyword. The program should show the
cipher text and plain text after decryption. 
"""

import sys

plain_alpha = 'abcdefghijklmnopqrstuvwxyz'
cipher_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def keyword_is_valid(keyword):
    for char in keyword:
        # make sure all chars are alphabetic
        if not char.isalpha():
            return False
    # make sure there are no repeated chars
    return len(keyword) == len(set(keyword))

def create_key(keyword):
    # add all letters of the keyword
    key = keyword.upper()
    for char in cipher_alpha:
        # add the rest of the characters in alphabetic order
        if char not in key:
            key += char
    return key

def encrypt(plain_text, key):
    cipher_text = ''
    for char in plain_text:
        if char.isalpha():
            # encyrpt the character
            char_number = plain_alpha.find(char)
            cipher_text += key[char_number]
        else:
            # we don't encrypt non-alphabetic chars
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ''
    for char in cipher_text:
        if char.isalpha():
            # decrypt the char
            char_number = key.find(char)
            plain_text += plain_alpha[char_number]
        else:
            # we don't decrypt non-alphabetic chars
            plain_text += char
    return plain_text

def main():
    print("Enter a message")
    plain_text = input()
    print("Enter a key:")
    # keyword needs to be lower case
    keyword = input().lower()
    # a valid keyword is alphabetic with no repeated chars
    if not keyword_is_valid(keyword):
        print("Keyword needs to be alphabetic with no repeated characters.",
                "Exiting")
        sys.exit()
    # create a key
    key = create_key(keyword)
    # encrypt
    cipher_text = encrypt(plain_text.lower(), key)
    # decrpyt
    plain_text = decrypt(cipher_text, key)
    print('Key:', key)
    print('Cipher Text:', cipher_text)
    print('Plain Text:', plain_text)

"""
Sample Output:

>>> main()
Enter a message
hello!! World,,?!
Enter a key:
monarchy
Key: MONARCHYBDEFGIJKLPQSTUVWXZ
Cipher Text: YRFFJ!! VJPFA,,?!
Plain Text: hello!! world,,?!

>>> main()
Enter a message
this is a secret message
Enter a key:
crypto
Key: CRYPTOABDEFGHIJKLMNQSUVWXZ
Cipher Text: QBDN DN C NTYMTQ HTNNCAT
Plain Text: this is a secret message

>>> main()
Enter a message
i love cs
Enter a key:
democracy
Keyword needs to be alphabetic with no repeated characters. Exiting
"""
