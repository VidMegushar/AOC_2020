import string

m = 0
group = []
with open('input6.txt') as f:
    for line in f.readlines():
        if line == '\n':
            s = 0
            for char in string.ascii_lowercase:
                if sum([char in g for g in group]) == len(group):
                    s += 1
            m += s
            group = []
        else:
            group.append(line.strip())

s = 0
for char in string.ascii_lowercase:
    if sum([char in g for g in group]) == len(group):
        s += 1
m += s
print(m)
