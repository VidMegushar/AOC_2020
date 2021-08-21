import time


with open('input1.txt') as f:
    data = [int(i) for i in f.readlines()]

t1 = time.time()

data.sort()

for i in range(len(data)-2):
    for j in range(i+1, len(data)-1):
        for k in range(j+1, len(data)):
            if data[i] + data[j] + data[k]== 2020:
                print(data[i] * data[j] * data[k])
                t2 = time.time()
                print(t2-t1)



