from itertools import product

with open('input17.txt') as f:
    grid = [[l for l in line.strip()]for line in f.readlines()]

bot_layer = [["." for _ in range(len(grid))] for _ in range(len(grid))]
top_layer = [["." for _ in range(len(grid))] for _ in range(len(grid))]

grid = [bot_layer, grid, top_layer]

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
        
comb = list(product(set([-1,0,1]),repeat=3))[1:]

grid = expand_grid(grid)


for cycle in range(6):
    grid = expand_grid(grid)
    new_grid = [[[x for x in line] for line in layer] for layer in grid]
    l = len(grid[0])
    h = len(grid)
    for z in range(1,h-1):
        for x in range(1,l-1):
            for y in range(1,l-1):
                active_count = 0
                for i in comb:
                    tmp_x = x + i[0]
                    tmp_y = y + i[1]
                    tmp_z = z + i[2]
                    if grid[tmp_z][tmp_y][tmp_x] == '#':
                        active_count += 1
                if grid[z][y][x] == '.':
                    if active_count == 3:
                        new_grid[z][y][x] = '#'
                elif grid[z][y][x] == '#':
                    if active_count not in [2,3]:
                        new_grid[z][y][x] = '.'
    grid = new_grid


final_count = 0
l = len(grid[0])
h = len(grid)
for x in range(l):
    for y in range(l):
        for z in range(h):
            if grid[z][y][x] == '#':
                final_count += 1

print(final_count)