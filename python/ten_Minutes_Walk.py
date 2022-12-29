#!/usr/bin/env python3

# https://www.codewars.com/kata/54da539698b8a2ad76000228/python

# My Solution
def is_valid_walk(walk:list):
    return True if len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w') else False

