#!/usr/bin/env python3

def lowest_product(nums: str):
    if len(nums) < 4:
        return 'Number is too small'

    nums_list = sorted(list(nums))

    if len(list(set(nums_list))) != len(nums_list):
        return 'Numbers should be consecutives'

    return int(nums_list[0]) * int(nums_list[1]) * int(nums_list[2]) * int(nums_list[3])

print(lowest_product('123456789'))

