import math

bag_dict = {}
bag_dict["other bags."] = []

with open('test.txt') as f:
    for line in f.readlines():
        bag, contents = line.strip().split("contain")
        bag = bag[:-6]
        contents = [i.strip() for i in contents.split(",")]
        contents = [(con.split(" ")[0], con.split(" ")[1] + " " + con.split(" ")[2]) for con in contents]
        if bag not in bag_dict:
            bag_dict[bag] = []
        for c in contents:
            bag_dict[bag].append(c)

print(bag_dict)

def check_shiny(bag, count=0):
    if bag_dict[bag][0][1] == 'other bags.':
        return 0

    tmp_count = 0
    for i in bag_dict[bag]:
        tmp_count += int(i[0]) + int(i[0]) * check_shiny(i[1], count)
    return count + tmp_count


print(check_shiny('shiny gold'))

"""
contains_gold = set()

def check_bag(bag):
    if bag in contains_gold:
        return True
    elif 'shiny gold' in bag_dict[bag]:
        contains_gold.add(bag)
        return True
    for c in bag_dict[bag]:
        if check_bag(c):
            return True
    return False

for key in bag_dict:
    if check_bag(key):
        contains_gold.add(key)

print(len(contains_gold))
"""

