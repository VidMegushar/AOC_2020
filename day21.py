ingridients = []
allergens = []
with open('input21.txt') as f:
    for line in f.readlines():
        ing, alg = line.split('(')
        ingridients.append(ing.strip().split(" "))
        allergens.append([x.strip()[:-1] for x in alg.split(" ")[1:]])


allergens_list = []
for a in allergens:
    allergens_list += a

allergens_list = list(set(allergens_list))

ingridients_list = []
for i in ingridients:
    ingridients_list += i


candidates = dict()
for i in allergens_list:
    check_ings = []
    for j, al in enumerate(allergens):
        if i in al:
            check_ings.append(ingridients[j])

    candidates[i] = set(check_ings[0]).intersection(*check_ings)
    
todo_alls = [x for x in candidates]
finished_list = []
fl = set()
while todo_alls:
    temp_all = todo_alls.pop()
    if len(candidates[temp_all]) == 1:
        temp_ing = list(candidates[temp_all])[0]
        finished_list.append((temp_all, temp_ing))
        fl.add(temp_ing)
        for x in candidates:
            if temp_ing in candidates[x]:
                candidates[x].remove(temp_ing)
    else:
        todo_alls = [temp_all] + todo_alls

not_alergic = []
for i in ingridients_list:
    if i not in fl:
        not_alergic.append(i)

print(not_alergic)
print(len(not_alergic))

final_str = ""
finished_list = sorted(finished_list)
for i in finished_list:
    final_str += i[1] + ","

print(final_str[:-1])