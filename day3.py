import math

with open('input3.txt') as f:
    data = [[j for j in i.strip()] for i in f.readlines()]


right = 3
down = 1

posx = 0
posy = 0

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

height = len(data)

trees = []
for slope in slopes:
    posx = 0
    posy = 0

    right = slope[0]
    down = slope[1]
    tmp_trees = 0

    while posy < height -1:
        posx += right
        posy += down
        if posx >= len(data[0]):
            posx = posx - len(data[0])
        if data[posy][posx] == '#':
            tmp_trees += 1
    trees.append(tmp_trees)

print(trees)
print(math.prod(trees))