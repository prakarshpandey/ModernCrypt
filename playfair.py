"""
Design a program to simulate the playfair cipher-decipher. The program
asks the user to enter the message and the keyword. The program should show the
cipher text and plain text after decryption.
"""
import sys
import numpy as np

plain_alpha = 'abcdefghjklmnopqrstuvwxyz'
cipher_alpha = 'ABCDEFGHJKLMNOPQRSTUVWXYZ'

def keyword_is_valid(keyword):
    for char in keyword:
        # make sure all chars are alphabetic
        if not char.isalpha():
            return False
    # make sure there are no repeated chars
    return len(keyword) == len(set(keyword))

def create_key(keyword):
    # generate key
    key = list(keyword)
    for char in plain_alpha:
        if char not in key:
            key.append(char)
    key = [key[x: x+5] for x in range(0, len(key), 5)]
    return key

def pruneMessage(plain_text):
    # make sure we don't have any single character digrams
    digram_list = [plain_text[x: x+2] for x in range(0, len(plain_text), 2)]
    pruned_text = ''
    print(digram_list)
    correction_made = False
    for digram in digram_list:
        if len(digram) >= 2:
            if digram[0] == digram[1] and not correction_made:
                pruned_text += digram[0] + 'x' + digram[1]
                correction_made = True
            else:
                pruned_text += digram
        else:
            pruned_text += digram
    if len(pruned_text) % 2 != 0:
        pruned_text += 'x'
    return pruned_text

def encrypt(pruned_text, key):
    # encryption algorithm
    digram_list = [pruned_text[x: x+2] for x in range(0, len(pruned_text), 2)]
    cipher_text = ''

    for digram in digram_list:
        char1, char2 = digram
        row1 = 0
        row2 = 0
        col1 = 0
        col2 = 0
        for row in range(5):
            for col in range(5):
                if key[row][col] == char1:
                    row1 = row
                    col1 = col
                elif key[row][col] == char2:
                    row2 = row
                    col2 = col
        if row1 == row2:
            cipher_text += key[row1][(col1 + 1) % 5]
            cipher_text += key[row2][(col2 + 1) % 5]

        elif col1 == col2:
            cipher_text += key[(row1 + 1) % 5][col1]
            cipher_text += key[(row2 + 1) % 5][col2]

        else:
            cipher_text = cipher_text + key[row1][col2] + key[row2][col1]

    return cipher_text

def decrypt(cipher_text, key):
    # decryption algorithm
    digram_list = [cipher_text[x: x+2] for x in range(0, len(cipher_text), 2)]
    plain_text = ''

    for digram in digram_list:
        char1, char2 = digram
        row1 = 0
        row2 = 0
        col1 = 0
        col2 = 0
        for row in range(5):
            for col in range(5):
                if key[row][col] == char1:
                    row1 = row
                    col1 = col
                elif key[row][col] == char2:
                    row2 = row
                    col2 = col
        if row1 == row2:
            plain_text += key[row1][(col1 - 1) % 5]
            plain_text += key[row2][(col2 - 1) % 5]

        elif col1 == col2:
            plain_text += key[(row1 - 1) % 5][col1]
            plain_text += key[(row2 - 1) % 5][col2]

        else:
            plain_text = plain_text + key[row1][col2] + key[row2][col1]

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
    cipher_text = encrypt(pruneMessage(plain_text.lower()), key)
    # decrpyt
    plain_text = decrypt(cipher_text, key)
    print('Cipher Text:', cipher_text)
    print('Plain Text:', plain_text)


"""
Sample Output:

Enter a message
balloon
Enter a key:
monarchy
['ba', 'll', 'oo', 'n']
Cipher Text: jbsupmna
Plain Text: balxloon

Enter a message
ball
Enter a key:
monarchy
['ba', 'll']
Cipher Text: jbsusu
Plain Text: balxlx
"""
