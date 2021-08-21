import time
t = time.time()

data = [[],[],[]]
pos = 0
with open('input16.txt') as f:
    for line in f.readlines():
        if line == '\n':
            pos += 1
        else:
            data[pos].append(line.strip())

format_t, your_t, nearby_t = data
possible_values = set()
# First part
format_dict = {}
for l in format_t:
    tmp_set = set()
    tmp_f = l.split(":")
    name = tmp_f[0]
    values = tmp_f[1].strip().split(' or ')
    value1 = values[0].split("-")
    value2 = values[1].split("-")
    for i in range(int(value1[0]), int(value1[1])+1):
        possible_values.add(i)
        tmp_set.add(i)
    for i in range(int(value2[0]), int(value2[1])+1):
        possible_values.add(i)
        tmp_set.add(i)
    format_dict[name] = tmp_set

"""
new_format = []
for l in format_t:
    tmp_f = l.split(" ")
    name = tmp_f[0][:-1]
    value1 = tmp_f[1].split("-")
    value2 = tmp_f[3].split("-")
    new_format.append([(int(value1[0]), int(value1[1])), (int(value2[0]), int(value2[1]))]) 
"""
your_t = [int(i) for i in your_t[1].split(",")]

def part1(ticket, pos_values):
    tmp_sum = 0
    for i in ticket:
        if i not in pos_values:
            tmp_sum += i
    return tmp_sum

def part2(ticket, pos_values):
    for i in ticket:
        if i not in pos_values:
            return False
    return True

valid_tickets = []
for ticket in nearby_t[1:]:
    ticket = [int(i) for i in ticket.split(",")]
    if part2(ticket, possible_values):
        valid_tickets.append(ticket)

fields = {}
for i in range(len(valid_tickets[0])):
    fields[i] = set()
    field = set([ticket[i] for ticket in valid_tickets])
    for fn in format_dict:
        if field.issubset(format_dict[fn]):
            fields[i].add(fn)

lens = len(fields) + 1
while lens > len(fields):
    for i in fields:
        if len(fields[i]) == 1:
            val = list(fields[i])[0]
            for j in fields:
                if i != j:
                    if val in fields[j]:
                        fields[j].remove(list(fields[i])[0])
    lens = sum([len(fields[s]) for s in fields])

final_val = 1
for i in fields:
    val = list(fields[i])[0]
    if val[:9] == 'departure':
        final_val = final_val*your_t[i]

print(final_val)
print(time.time() - t)