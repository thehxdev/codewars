#!/usr/bin/env python3

# https://www.codewars.com/kata/5287e858c6b5a9678200083c

def narcissistic(value:int) -> bool:
    str_value = str(value)
    digits    = len(str_value)
    nums      = []
    
    for i in str_value:
        nums.append(int(i) ** digits)

    return sum(nums) == value


# Codewars Solution
def narcissistic_2(value:int) -> bool:
    return value == sum(int(x) ** len(str(value)) for x in str(value))

