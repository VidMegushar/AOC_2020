import time
t = time.time()

data = []
with open('input11.txt') as f:
    for line in f.readlines():
        line = ["."] + [l for l in line.strip()] + ["."]
        data.append(line)

data = [["." for _ in data[0]]] + data + [["." for _ in data[0]]]

dirs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]

def check_occ(data, d, i, j):
    i += d[0]
    j += d[1]

    while j < len(data) and j > 0 and i < len(data[0]) and i > 0:
        if data[j][i] == '#':
            return True
        elif data[j][i] == 'L':
            return False
        i += d[0]
        j += d[1]
    return False


def one_step(data):
    tmp_data = [[i for i in line] for line in data]

    for i in range(1,len(data[0])-1):
        for j in range(1, len(data)-1):
            if data[j][i] == "L":
                occ = 0
                for seat in dirs:
                    if check_occ(data, seat, i, j):
                        occ += 1
                if occ == 0:
                    tmp_data[j][i] = '#'

            if data[j][i] == '#':
                occ_count = 0
                for seat in dirs:
                    if check_occ(data, seat, i, j):
                        occ_count += 1
                if occ_count >= 5:
                    tmp_data[j][i] = 'L'
    return tmp_data

def count(data):
    occ_seats = 0
    for i in range(1,len(data[0])-1):
        for j in range(1, len(data)-1):
            if data[j][i] == '#':
                occ_seats += 1
    return occ_seats

eq = 0
old_count = 0
while eq < 4:
    data = one_step(data)
    new_count = count(data)
    if new_count == old_count:
        eq += 1
    else:
        old_count = new_count


print(new_count)
print(time.time() - t)
