ALPHA = "abcdefghijklmnopqrstuvwxyz"


def vigenere(direction: str, message: str, key: str) -> str: 
    """
    Encrypt or decrypt a message using a key.
    Adapted from 

    Args:
        direction (str): "encrypt", "e", "decrypt", or "d"
        message (str): text to alter
        key (str): decrypt a message with the same key that encrypted it

    Returns:
        str: encrypted or decrypted message
    """
    altered = ""
    current_index = 0

    for char in message:
        char_index = ALPHA.find(char)
        if char_index != -1:
            if direction == "encrypt" or direction == "e":
                char_index += ALPHA.find(key[current_index])
            elif direction == "decrypt" or direction == "d":
                char_index -= ALPHA.find(key[current_index])

            char_index %= len(ALPHA)

            altered += ALPHA[char_index]

            current_index += 1
            if current_index == len(key):
                current_index = 0
        else:
            altered += char
    
    return altered


def encrypt(message: str, key: str) -> str:
    """Vigenere encrypt a message using a key.

    Args:
        message (str): message to encrypt
        key (str): encryption key

    Returns:
        str: encrypted message
    """
    return vigenere('e', message, key)


def decrypt(message: str, key: str) -> str:
    """Vigenere decrypt a message using a key.

    Args:
        message (str): message to decrypt
        key (str): encryption key

    Returns:
        str: decrypted message
    """
    return vigenere('d', message, key) 
    