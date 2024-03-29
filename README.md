We had a special lesson on encryption prepared for you today in the file `bacon_binary.py`, but somebody encrypted it! Luckily, the culprit left us some clues so we can restore it.

Before you begin, follow the instructions in the `Setup` section below, so you can run the code on your local machine.

We know that for each of the encrypted messages in the trail of clues, the culprit used the [Vigenere cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher). The Vigenere cipher takes a string of letters as a key to encrypt a message, and can decrypt it using that same key. In today's mystery the Vigenere cipher is used three times, each with a different key and a different message. 

# Start Here
The trail of clues starts in the file `today.py`. It's a poem by Frank O'Hara that has been broken into nested lists of possible keys. You'll have to use your list indexing skills.
- Get the 6th item in the 2nd list of the 2nd list of the 3rd list of the 2nd list of `possible_keys` in `today.py`.
> Tip: Test the indexing as you go, and remember that Python is zero-indexed
- Uncomment line 9 of `decoded_messages.py` and pass the key as the second argument to `decrypt()`.
- This will decrypt the text in the file `regex_clue.py`, which will give you the second clue.

Good luck!

### Setup
- Clone this repository:

`git clone https://github.com/datastackacademy/treasure_hunt.git`

- Create a Python virtual environment:

`python3.7 -m venv venv`

- Activate it:

`source venv/bin/activate`

- Install the requirements in the `requirements.txt` file:

`pip install -r requirements.txt`

### References
- 'Today', by Frank O'Hara, 1950
- 'Cracking Codes with Python', by Al Sweigart, 2018
- 'Alice in Wonderland', by Lewis Carroll, 1865
- 'How to Make Anything Signify Anything', William Sherman for Cabinet Magazine, 2010
