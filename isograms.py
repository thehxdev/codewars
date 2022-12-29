#!/usr/bin/env python3

# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.

t = input("Enter a string: ")

# My Solution
def is_isogram(string:str):
    isogram = True
    # Ignore lower case.
    string = string.lower()
    for i in range(len(string)):
        if string.count(string[i]) > 1:
            isogram = False
            break

    return isogram

# CodeWars Solution
def is_isogram_2(string):
    return len(string) == len(set(string.lower()))

print(is_isogram(t))
print(is_isogram_2(t))

