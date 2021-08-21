with open('input9.txt') as f:
    data = [int(line.strip()) for line in f.readlines()]

def check_sum(i, tmp_data):
    tmp_data = sorted(tmp_data)
    for a in range(len(tmp_data)-1):
        for b in range(a+1, len(tmp_data)):
            if tmp_data[a] + tmp_data[b] == i:
                return True
    return False

for i in range(25,len(data)):
   if not check_sum(data[i], data[i-25:i]):
       print(data[i])
       break


for i in range(len(data)):
    tmp_list = [data[i]]
    tmp_val = data[i]
    for j in range(i+1, len(data)):
        tmp_val += data[j]
        tmp_list.append(data[j])
        if tmp_val == 133015568:
            print(max(tmp_list), min(tmp_list), max(tmp_list) + min(tmp_list))
        if tmp_val > 133015568:
            break