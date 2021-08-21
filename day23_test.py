import time

cup_order = '389125467'
cup_order = [int(x) for x in cup_order]
print(len(cup_order))
t = time.time()

def get_dest_cup(ccp, ccl, cup_order, removed):
    dest_cup_label = ccl
    dest_cup_label = (dest_cup_label - 1)
    if dest_cup_label == 0:
        dest_cup_label = 9
    while True:
        if dest_cup_label not in removed:
            return(dest_cup_label, cup_order.index(dest_cup_label))
        else:
            dest_cup_label = (dest_cup_label - 1)
            if dest_cup_label == 0:
                dest_cup_label = 9
    


current_cup_pos = 0
l = len(cup_order)
current_cup_label = cup_order[current_cup_pos]
t = time.time()
for i in range(100):
    
    removed = []
    removed.append(cup_order[(current_cup_pos + 1) % l])
    removed.append(cup_order[(current_cup_pos + 2) % l])
    removed.append(cup_order[(current_cup_pos + 3) % l])
    for i in removed:
        cup_order.remove(i)
    

    
    dest_cup_label, dest_cup_pos = get_dest_cup(current_cup_pos, current_cup_label, cup_order, removed)

    # cup_order = cup_order[:(dest_cup_pos+1) % l] + removed + cup_order[(dest_cup_pos + 1) % l:]
    cup_order[(dest_cup_pos+1) % l:(dest_cup_pos+1) % l] = removed
    current_cup_pos = (cup_order.index(current_cup_label) + 1) % l
    current_cup_label = cup_order[current_cup_pos]


first_ind = cup_order.index(1)
result = cup_order[(first_ind+1)%9] + cup_order[(first_ind+2)%9]
print(result)
#print("".join([str(x) for x in final_list]))


    