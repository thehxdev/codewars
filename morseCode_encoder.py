#!/usr/bin/env python3


MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----'
}

def encodeToMorse(sentence:str):
    words = (sentence.upper()).split(" ")
    encodedMorseCode = []

    for word in words:
        currentWord = []
        for char in word:
            currentWord.append(MORSE_CODE[char])

        encodedMorseCode.append(currentWord)

    return encodedMorseCode


userInput = input("Enter your sentence: ")

print(encodeToMorse(userInput))
