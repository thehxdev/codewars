#!/usr/bin/env python3

# My Solution
def binary(x:int=0) -> list:
    nums_binary = []
    if x == 0:
        return [0]
    while x > 0:
        y = int(x % 2)
        x = int(x / 2)
        nums_binary.append(y)
    return nums_binary[::-1]

def count_bits(n):
    n_bin = binary(n)
    return n_bin.count(1)

# ================== #

# CodeWars Solution
def countBits(n):
    return bin(n).count("1")

