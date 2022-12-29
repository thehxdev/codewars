#!/usr/bin/env python3

# Return shortes word(s) length in given string.

# My Solution
def find_short_1(s:str) -> int:
    x = s.split(' ')
    word_len_list = []
    for i in x:
        i_len = len(i)
        word_len_list.append(i_len)
    return len(x[word_len_list.index(min(word_len_list))])

# CodeWars Solution 1
def find_short_2(s:str) -> int:
    return min(len(x) for x in s.split())

# CodeWars Solution 2
def find_short_3(s:str) -> int:
    return len(min(s.split(' '), key=len))
