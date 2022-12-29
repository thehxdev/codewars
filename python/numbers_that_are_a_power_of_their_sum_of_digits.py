#!/usr/bin/env python3

def powerOfSum(number:int) -> bool:
    str_number = str(number)
    sum_of_digits = sum(int(str_number[x]) for x in range(len(str_number)))
    powerOfSum = sum_of_digits ** len(str_number)
    return number == powerOfSum

