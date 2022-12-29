#!/usr/bin/env python3

# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

# My solution
def high_and_low(numbers:str) -> str:
    str_nums = numbers.split(" ")
    nums = []
    for i in str_nums:
        nums.append(int(i))
    return " ".join([str(max(nums)), str(min(nums))])


# Codewars Solution
def high_and_low_2(numbers:str) -> str:
    nn = [int(s) for s in numbers.split(" ")]
    return "{} {}".format(max(nn),min(nn))
    
print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
print(high_and_low_2("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
