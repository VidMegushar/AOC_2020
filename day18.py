import re

with open('input18.txt') as f:
    data = [line.strip() for line in f.readlines()]

def search_bracket(eq):
    in1 = 0
    for i, letter in enumerate(eq):
        if letter == '(':
            in1 = i
        elif letter == ')':
            return in1, i

def solve_simple(eq):
    eq_list = eq.strip().split(" ")
    res = int(eq_list[0])
    i = 1
    while i < len(eq_list) - 1:
        if eq_list[i] == '+':
            res += int(eq_list[i+1])
        elif eq_list[i] == '*':
            res *= int(eq_list[i+1])
        i += 2
    return res

def solve_part2(eq):
    eq_list = eq.strip().split(" ")
    while eq_list.count('+') > 0:
        plus_index = eq_list.index('+')
        eq_list = eq_list[:plus_index - 1] + [str(int(eq_list[plus_index - 1]) + int(eq_list[plus_index + 1]))] + eq_list[plus_index + 2:]
    res = int(eq_list[0])
    i = 2
    while i < len(eq_list):
        res *= int(eq_list[i])
        i += 2
    return res

result = 0
for eq in data:
    while eq.count('(') > 0:
        in1, in2 = search_bracket(eq)
        eq = eq[:in1] + str(solve_part2(eq[in1+1:in2])) + eq[in2+1:]
    result += solve_part2(eq)

print(result)