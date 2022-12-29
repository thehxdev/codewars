#!/usr/bin/env python3

def arrayDiff(list1:list, list2:list) -> list:
    diff = []
    for i in list1:
        if i not in list2:
            diff.append(i)
    return diff

# CodeWars Solution
def array_diff(a:list, b:list) -> list:
    return [x for x in a if x not in b]
