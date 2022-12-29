#!/usr/bin/env python3

def valid_parentheses(chars:str) -> bool:
    x = []
    par = ["(", ")"]
    for char in chars:
        if char in par:
            x.append(char)
        if len(x) >= 2 and x[-2] == "(" and x[-1] == ")":
            x.pop(-1)
            x.pop(-1)
    return True if len(x) == 0 else False
            
# CodeWars Solution
def valid_parentheses_2(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
