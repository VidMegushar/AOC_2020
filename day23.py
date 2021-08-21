import time

cup_num = 1000000
round_num = 10000000

cup_order = '247819356'

cup_order = [int(x) for x in cup_order]
new_cups = [int(x) for x in range(10, cup_num + 1)]
cup_order = cup_order + new_cups

next_dict = dict()

for i in range(len(cup_order)-1):
    next_dict[cup_order[i]] = cup_order[i+1]

next_dict[cup_order[-1]] = cup_order[0]

t = time.time()

def get_dest_cup(current_cup, removed):
    dest_cup = current_cup - 1
    if dest_cup == 0:
        dest_cup = cup_num
    while True:
        if dest_cup not in removed:
            return dest_cup
        else:
            dest_cup -= 1
            if dest_cup == 0:
                dest_cup = cup_num
    
def get_removed(current_cup):
    removed = []
    tmp_cup = next_dict[current_cup]
    removed.append(tmp_cup)
    tmp_cup = next_dict[tmp_cup]
    removed.append(tmp_cup)
    tmp_cup = next_dict[tmp_cup]
    removed.append(tmp_cup)
    return removed

current_cup = cup_order[0]
l = len(cup_order)



t = time.time()
for i in range(round_num):
    if i % 200000 == 0:
        print(str(round((i/10000000)*100, 2)), '%')
    removed = get_removed(current_cup)
    
    dest_cup = get_dest_cup(current_cup, removed)

    next_dict[current_cup] = next_dict[removed[2]]
    next_dict[removed[2]] = next_dict[dest_cup]
    next_dict[dest_cup] = removed[0]

    current_cup = next_dict[current_cup]


full_rt = time.time()-t

print(full_rt)

print(next_dict[1])
print(next_dict[next_dict[1]])
print(next_dict[1]*next_dict[next_dict[1]])