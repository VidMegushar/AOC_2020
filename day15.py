import time

t = time.time()
start = [2,0,1,7,4,14,18]
# start = [19, 0, 5, 1, 10, 13]

spoken = dict()

for i, n in enumerate(start):
    spoken[n] = i+1

last = 0
turn = len(start) + 1

for turn in range(len(start)+1, 30000000):
    if last not in spoken:
        next_one = 0
        
    if last in spoken:
    # else:
        next_one = turn - spoken[last]

    

    spoken[last] = turn
    last = next_one


print(time.time() - t)
print(last)