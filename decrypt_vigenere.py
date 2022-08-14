from regex_clue import regex_clue
from site_address import site_address
from bacon_binary import bacon_binary


ALPHA = "abcdefghijklmnopqrstuvwxyz"

def decrypt(coded_message, key):
    decrypted = ""
    current_index = 0

    for char in coded_message:
        char_index = ALPHA.find(char)
        if char_index != -1:
            char_index -= ALPHA.find(key[current_index])

            char_index %= len(ALPHA)

            decrypted += ALPHA[char_index]

            current_index += 1
            if current_index == len(key):
                current_index = 0
        else:
            decrypted += char
    
    return decrypted


