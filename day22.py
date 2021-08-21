from collections import deque
import time

t = time.time()

player1 = deque()
player2 = deque()

with open('input22.txt') as f:
    lines = f.read()
    p1, p2 = lines.split("\n\n")
    p1 = [int(i) for i in p1.split("\n")[1:]]
    p2 = [int(i) for i in p2.split("\n")[1:]]

for i in p1:
    player1.append(i)

for j in p2:
    player2.append(j)

all_games = set()




while len(player1) > 0 and len(player2) > 0:
    c1 = player1.popleft()
    c2 = player2.popleft()

    if c1 > c2:
        player1.append(c1)
        player1.append(c2)
    else:
        player2.append(c2)
        player2.append(c1)
    i += 1
    if i % 50000 == 0:





res = 0
if len(player1) == 0:
    l = len(player2)
    for i in range(l):
        x = player2.popleft()
        res += (l-i)*x

else:
    l = len(player1)
    for i in range(l):
        x = player1.popleft()
        res += (l-i)*x

print(res)
print(time.time() - t)