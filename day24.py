def get_direction_list(direction):
    i = 0
    dir_list = []
    while i < len(direction):
        if direction[i] in ['e', 'w']:
            dir_list.append(direction[i])
            i += 1
        else:
            dir_list.append(direction[i:i+2])
            i += 2
    return dir_list


direction_dict = {
    'e': (2,0),
    'w': (-2,0),
    'ne': (1,-1),
    'nw': (-1,-1),
    'se': (1,1),
    'sw': (-1,1)
}

with open('input24.txt') as f:
    directions = [get_direction_list(line.strip()) for line in f.readlines()]

max_dir = max([len(c) for c in directions])

hex_grid = [[0 for i in range(4*max_dir + 400)] for j in range(4*max_dir + 400)]

start_pos = (2*max_dir + 200, 2*max_dir + 200)

for direction in directions:
    tmp_posx = start_pos[0]
    tmp_posy = start_pos[1]
    for smer in direction:
        smer_x = direction_dict[smer][0]
        smer_y = direction_dict[smer][1]
        tmp_posx += smer_x
        tmp_posy += smer_y
    hex_grid[tmp_posy][tmp_posx] = 1 - hex_grid[tmp_posy][tmp_posx]


for day in range(100):
    new_hg = [[x for x in line] for line in hex_grid]
    for y in range(2,len(hex_grid)-2):
        for x in range(2,len(hex_grid[0])-2):
            if (x+y) % 2 == 0:
                black_neighbours = 0
                for d in direction_dict.values():
                    if hex_grid[y+d[1]][x+d[0]] == 1:
                        black_neighbours += 1
                if hex_grid[y][x] == 1:
                    if black_neighbours not in [1,2]:
                        new_hg[y][x] = 0
                else:
                    if black_neighbours == 2:
                        new_hg[y][x] = 1
    hex_grid = new_hg

print(sum([sum(x) for x in hex_grid]))



