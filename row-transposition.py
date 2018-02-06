"""
Problem:
Design a program to simulate the row transposition cipher-decipher. The program
asks the user to enter the message (plain text) and the key (column permutation)
of length 7.
"""

def prune_text(plain_text):
    pruned_text = ''
    for char in plain_text:
        if char.isalpha():
            pruned_text += char
    if len(pruned_text) % 7 != 0:
        pruned_text += (7 - len(pruned_text) % 7) * 'x'
    return pruned_text

def encrypt(pruned_text, key):
    pruned_text = list(pruned_text)
    pruned_text = [pruned_text[x: x+7] for x in range(0, len(pruned_text), 7)]
    cipher_text = ''
    columns = []
    # find all the columns
    for i in range(len(pruned_text[0])):
        columns.append([row[i] for row in pruned_text])
    # create cipher text corresponding to ordering in columns
    for col_num in key:
        thisCol = int(col_num)
        for char in columns[thisCol - 1]:
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ''
    col_size = int(len(cipher_text) / 7)
    columns = [cipher_text[x: x+col_size] for x in range(0, len(cipher_text), col_size)]
    orderedCols = [0] * (int(len(cipher_text)/ col_size))
    for col_num in key:
        thisCol = columns[int(col_num) - 1]
        orderedCols[int(col_num) - 1] = thisCol
    ordered_rows = []
    for i in range(col_size):
        ordered_rows.append([col[i] for col in orderedCols])
    ordered_chars = [char for row in ordered_rows for char in row]
    plain_text = plain_text.join(ordered_chars)
    return plain_text

def main():
    print("Enter a message")
    plain_text = input()
    print("Enter a key:")
    # keyword needs to be lower case
    key = input().lower()
    # a valid keyword is alphabetic with no repeated chars
    if len(key) != 7:
        print('The key needs to be a permutation of 7 columns!! Exiting')
        sys.exit()
    if max(a) > '7' or min(a) < '1':
        print('The key needs to be a permutation of 7 columns!! Exiting')

    # encrypt
    cipher_text = encrypt(prune_text(plain_text), key)
    # decrpyt
    plain_text = decrypt(cipher_text, key)
    print('Cipher Text:', cipher_text)
    print('Plain Text:', plain_text)
