from itertools import product

with open('input17.txt') as f:
    grid = [[l for l in line.strip()]for line in f.readlines()]


hyper_cube = [[[["." for _ in range(24)] for _ in range(24)] for _ in range(15)] for _ in range(15)]

for x in range(len(grid)):
    for y in range(len(grid)):
        hyper_cube[7][7][7+x][7+y] = grid[x][y]

comb = list(product(set([-1,0,1]),repeat=4))[1:]

for _ in range(6):
    new_hcube = [[[[x for x in row] for row in layer] for layer in cube] for cube in hyper_cube]
    for cube in range(1,14):
        for layer in range(1,14):
            for x in range(1,23):
                for y in range(1,23):
                    count = 0
                    for c in comb:
                        if hyper_cube[cube+c[0]][layer+c[1]][x+c[2]][y+c[3]] == '#':
                            count += 1
                    if hyper_cube[cube][layer][x][y] == '#':
                        if count not in [2,3]:
                            new_hcube[cube][layer][x][y] = '.'
                    elif hyper_cube[cube][layer][x][y] == '.':
                        if count == 3:
                            new_hcube[cube][layer][x][y] = '#'
                    
    hyper_cube = new_hcube.copy()

final_count = 0
for cube in range(15):
    for layer in range(15):
        for x in range(24):
            for y in range(24):
                if hyper_cube[cube][layer][x][y] == '#':
                    final_count += 1

print(final_count)

"""
grid = [bot_layer, grid, top_layer]

empty_grid_1 = [[["." for _ in line] for line in layer] for layer in grid]
empty_grid_2 = [[["." for _ in line] for line in layer] for layer in grid]

hyper_grid = [empty_grid_1, grid, empty_grid_2]


def expand_grid(grid):
    l = len(grid[0])
    new_layer = [["." for _ in range(l + 2)] for _ in range(l + 2)]
    new_grid = [new_layer]
    for layer in grid:
        for i,line in enumerate(layer):
            layer[i] = ["."] + line + ["."]
        layer = [["." for _ in range(l + 2)]] + layer + [["." for _ in range(l + 2)]]
        new_grid.append(layer)
    new_grid.append([["." for _ in range(l + 2)] for _ in range(l + 2)])

    return new_grid
        


for grid in hyper_grid:
    grid = expand_grid(grid)

empty_grid_1 = [[["." for _ in line] for line in layer] for layer in hyper_grid[0]]
empty_grid_2 = [[["." for _ in line] for line in layer] for layer in hyper_grid[0]]

hyper_grid = [empty_grid_1] + hyper_grid + [empty_grid_2]

for grid in hyper_grid:
    print("")
    for layer in grid:
        for line in layer:
            print(line)


for cycle in range(1):
    for grid in hyper_grid:
        grid = expand_grid(grid)

    empty_grid_1 = [[["." for _ in line] for line in layer] for layer in hyper_grid[0]]
    empty_grid_2 = [[["." for _ in line] for line in layer] for layer in hyper_grid[0]]

    hyper_grid = [empty_grid_1] + hyper_grid + [empty_grid_2]

    new_grid = [[[[x for x in line] for line in layer] for layer in grid] for grid in hyper_grid]
    l = len(grid[0][0])
    h = len(grid[0])
    s = len(hyper_grid)
    for w in range(1,s-1):
        for z in range(1,h-1):
            for x in range(1,l-1):
                for y in range(1,l-1):
                    active_count = 0
                    for i in comb:
                        tmp_x = x + i[0]
                        tmp_y = y + i[1]
                        tmp_z = z + i[2]
                        tmp_w = w + i[3]
                        print(tmp_x, tmp_y, tmp_z, tmp_w)
                        if hyper_grid[tmp_w][tmp_z][tmp_y][tmp_x] == '#':
                            active_count += 1
                    if hyper_grid[w][z][y][x] == '.':
                        if active_count == 3:
                            new_grid[w][z][y][x] = '#'
                    elif hyper_grid[w][z][y][x] == '#':
                        if active_count not in [2,3]:
                            new_grid[w][z][y][x] = '.'
    hyper_grid = new_grid

for grid in hyper_grid:
    print("")
    for layer in grid:
        for line in layer:
            print(line)

final_count = 0
l = len(grid[0])
h = len(grid)
for x in range(l):
    for y in range(l):
        for z in range(h):
            if grid[z][y][x] == '#':
                final_count += 1

print(final_count)
"""