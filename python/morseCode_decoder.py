#!/usr/bin/env python3

sample_morse = '.... --- ... ... . .. -.'

MORSE_CODE = {
    '.-'    : 'A', '-...'  : 'B', '-.-.'  : 'C',
    '-..'   : 'D', '.'     : 'E', '..-.'  : 'F',
    '--.'   : 'G', '....'  : 'H', '..'    : 'I',
    '.---'  : 'J', '-.-'   : 'K', '.-..'  : 'L',
    '--'    : 'M', '-.'    : 'N', '---'   : 'O',
    '.--.'  : 'P', '--.-'  : 'Q', '.-.'   : 'R',
    '...'   : 'S', '-'     : 'T', '..-'   : 'U',
    '...-'  : 'V', '.--'   : 'W', '-..-'  : 'X',
    '-.--'  : 'Y', '--..'  : 'Z', '.----' : '1',
    '..---' : '2', '...--' : '3', '....-' : '4',
    '.....' : '5', '-....' : '6', '--...' : '7',
    '---..' : '8', '----.' : '9', '-----' : '0'
}

# My Solution
def decode_morse_1(morse_code:str):
    morse_code = morse_code.strip()
    split_words = morse_code.split('   ')
    sentence = []
    for word in split_words:
        words = []
        current_word = word.split(' ')
        for char in current_word:
            words.append(MORSE_CODE[char])
        complete_word = ''.join(words)
        sentence.append(complete_word)
    return ' '.join(sentence)

# CodeWars Solution
def decode_morse_2(morse_code:str):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morse_code.strip().split('   '))

# test
print(decode_morse_1(sample_morse))

