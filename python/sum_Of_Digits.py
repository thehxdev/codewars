#!/usr/bin/env python3

# https://www.codewars.com/kata/541c8630095125aba6000c00/python

# My Solution
def digital_root_1(n:int):
    current_num = n
    sum_n = 0
    while len(str(current_num)) > 1:
        for num in list(str(current_num)):
            sum_n += int(num)
        current_num = sum_n
        sum_n = 0
    return int(current_num)

# CodeWars Solution 1
def digital_root_2(n):
    return n if n < 10 else digital_root_2(sum(map(int,str(n))))

# CodeWars Solution 2
def digital_root_3(n):
    return n%9 or n and 9
