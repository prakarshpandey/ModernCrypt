"""
Prakarsh Pandey, Harvey Mudd College
Problem: Design a program to act as a general Caesar cipher-decipher.
The program asks the user to enter the message and the keyword.
The program should show the cipher text and plain text after decryption. 
"""

import sys

plain_alpha = 'abcdefghijklmnopqrstuvwxyz'
cipher_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plain_text, k):
    cipher_text = ''
    for char in plain_text:
        if char.isalpha():
            # encyrpt the character
            char_number = plain_alpha.find(char)
            char_number = (char_number + k) % 26
            cipher_text += cipher_alpha[char_number]
        else:
            # we don't encrypt non-alphabetic chars
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, k):
    plain_text = ''
    for char in cipher_text:
        if char.isalpha():
            # decrypt the char
            char_number = cipher_alpha.find(char)
            char_number = (char_number - k) % 26
            plain_text += plain_alpha[char_number]
        else:
            # we don't decrypt non-alphabetic chars
            plain_text += char
    return plain_text

def main():
    print("Enter a message")
    plain_text = input()
    print("Enter a key:")
    try:
        k = int(input())
    except ValueError:
        print("Needs to be an integer greater than 0. Exiting.")
        sys.exit()
    if k < 0:
        print("Needs to be an integer greater than 0. Exiting.")
        sys.exit()
    cipher_text = encrypt(plain_text.lower(), k)
    plain_text = decrypt(cipher_text, k)
    print('Cipher Text:', cipher_text)
    print('Plain Text:', plain_text)

"""
Sample Output:
Enter a message
Hello? is any1 there!!
Enter a key:
4
Cipher Text: LIPPS? MW ERC1 XLIVI!!
Plain Text: hello? is any1 there!!

Enter a message
hellpo
Enter a key:
-3
Needs to be an integer greater than 0. Exiting.
"""
