#!/usr/bin/env python3

# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/python

# My Solution
def find_nb_1(m:int) -> int:
    start_num = 0
    current_cube_vol = start_num ** 3
    current_vol = m
    while current_vol >= 0:
        start_num += 1
        current_cube_vol = start_num ** 3
        current_vol -= current_cube_vol

    if abs(current_vol) != current_cube_vol:
        return -1
    return start_num - 1

# CodeWars Solution
def find_nb_2(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n**3
        if volume == m:
            return n
        n += 1
    return -1
