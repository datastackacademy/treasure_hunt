# Python Treasure Hunt

## Overview

We had a special lesson on encryption prepared for you today in the file `bacon_binary.py`, but somebody encrypted it! Luckily, the culprit left us some clues so we can restore it.

Before you begin, follow the instructions in the `Setup` section below, so you can run the code on your local machine.

We know that for each of the encrypted messages in the trail of clues, the culprit used the [Vigenere cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher). The Vigenere cipher takes a string of letters as a key to encrypt a message, and can decrypt it using that same key. In today's mystery the Vigenere cipher is used three times, each with a different key and a different message. 

## Setup

1. Clone this repository on to your local computer:

    ```bash
    git clone https://github.com/datastackacademy/treasure_hunt.git
    ```

1. Create a Python virtual environment & active it:

    ```bash
    cd treasure_hunt
    python3 -m venv venv
    source venv/bin/activate
    ```

1. Install the requirements in the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

1. Open the `treasure_hunt.ipynb` notebook and follow the instructions.


Good luck! 🍀🌠🤞

### References

The code in `vigenere.py` was closely adapted from Sweigart's book 'Cracking Codes with Python'.

- 'Today', by Frank O'Hara, 1950
- 'Cracking Codes with Python', by Al Sweigart, 2018
- 'Alice in Wonderland', by Lewis Carroll, 1865
- 'How to Make Anything Signify Anything', William Sherman for Cabinet Magazine, 2010
