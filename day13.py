from math import gcd
import time

data = []
with open('input13.txt') as f:
    for line in f.readlines():
        data.append(line.strip())

"""
ts = int(data[0])
buses = [int(x) for x in data[1].split(",") if x != 'x']

tss = [(ts // x) * (x) + x for x in buses]
minb = tss.index(min(tss))
"""
# Part 2
t = time.time()
buses2 = enumerate([int(x) if x != 'x' else 0 for x in data[1].split(",")])
buses2 = [x for x in buses2 if x[1] != 0]

def calc_match(a, b , pos, inc):
    k = 0
    while True:
        tmp_res = (a + k*inc + pos) % b
        if tmp_res == 0:
            return a + k*inc
        k += 1

a = buses2[0][1]
inc = a
for pos, b in buses2[1:]:
    a = calc_match(a, b, pos, inc)
    inc = inc*b
print(a)
print(round((time.time() - t)*1000, 3))

"""
first_bus = buses2[0][1]
fm_list = [first_match(first_bus, x[1], x[0]) for x in buses2]
print(fm_list)


lcm = fm_list[0]
for i in fm_list[1:]:
  lcm = lcm*i//gcd(lcm, i)

print(lcm)

max_bus = buses.index(max(buses))

def check_buses(buses, ts0):
    new_ts = [(ts0 // x[1]) * x[1] + (x[0] // x[1])*x[1] + x[1] - x[0] for x in buses]
    new_ts[0] =  new_ts[0] - buses[0][1]
    check = new_ts[0]
    if new_ts.count(check) == len(new_ts):
        return True, buses
    else:
        return False, buses

stop = False
ts0 = fm_list[max_bus] - buses2[max_bus][0]
increment = buses2[0][1]*buses2[max_bus][1]

i = 0
while not stop:
    i += 1
    ts0 += increment
    stop, bs = check_buses(buses2, ts0)
    if i % 100000 == 0:
        pass
        #print(ts0)

print(ts0)



i = 2
ch = True
while ch:
    if i % 20000 == 0: print(i)
    ts0 = buses2[max_bus][1]*i - buses2[max_bus][0]
    ch, lastb = check_buses(buses2, ts0)
    i += 1
print(ts0)
"""
# print(check_buses(buses2,1000000))"""