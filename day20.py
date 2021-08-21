from itertools import permutations

tiles = dict()
tile = []
with open('input20.txt') as f:
    for line in f.readlines():
        if len(line) == 1:
            tiles[name] = tile
            tile = []
        elif line[0] == 'T':
            name = int(line.strip().split(" ")[1][:-1])
        else:
            tile.append([x for x in line.strip()])

def rotate(tile):
    new_tile = [[None for _ in range(len(tile))] for _ in range(len(tile))]

    l = len(tile)
    for i in range(l):
        for j in range(l):
            elt = tile[i][j]
            new_tile[j][l-i-1] = elt
    return new_tile

def flip(tile):
    new_tile = []

    for line in tile:
        new_tile.append(line[::-1])
    return new_tile

def compare_ud(up, down):
    if up[-1] == down[0]:
        return True
    return False

def compare_lr(left, right):
    for i in range(len(left)):
        if left[i][-1] != right[i][0]:
            return False
    return True

def compare_two_tiles(tile1, tile2):
    for side in range(4):
        tile1 = rotate(tile1)
        for fl in range(2):
            tile2 = flip(tile2)
            for rotation in range(4):
                tile2 = rotate(tile2)
                if compare_lr(tile1, tile2):
                    return True
    return False

tiles_list = [x for x in tiles]

matches = {i:[] for i in tiles_list}

for i in matches:
    for j in matches:
        if i != j:
            if compare_two_tiles(tiles[i],tiles[j]):
                matches[i].append(j)


for i in matches:
    if len(matches[i]) == 4:
        middle = i
        break


big_picture = [[None for _ in range(25)] for _ in range(25)]

todo = [(middle, 12, 12)]
big_picture[12][12] = middle
checked = set()
checked.add(middle)
# dirs = [(1,0), (0,1), (-1,0), (0,-1)]
dirs = ['up', 'down', 'left', 'right']
while todo:
    tile_name, x, y = todo.pop()
    tile = tiles[tile_name]
    for neigh in matches[tile_name]:
        if neigh not in checked:
            checked.add(neigh)
            neigh_tile = tiles[neigh]
            for fl in range(2):
                neigh_tile = flip(neigh_tile)
                for rotation in range(4):
                    neigh_tile = rotate(neigh_tile)
                    for direction in dirs:
                        if direction == 'up':
                            if compare_ud(neigh_tile, tile):
                                todo.append([neigh, x, y-1])
                                tiles[neigh] = neigh_tile
                                big_picture[y-1][x] = neigh
                        elif direction == 'down':
                            if compare_ud(tile, neigh_tile):
                                todo.append([neigh, x, y+1])
                                tiles[neigh] = neigh_tile
                                big_picture[y+1][x] = neigh
                        elif direction == 'left':
                            if compare_lr(neigh_tile, tile):
                                todo.append([neigh, x-1, y])
                                tiles[neigh] = neigh_tile
                                big_picture[y][x-1] = neigh
                        elif direction == 'right':
                            if compare_lr(tile, neigh_tile):
                                todo.append([neigh, x+1, y])
                                tiles[neigh] = neigh_tile
                                big_picture[y][x+1] = neigh

final_picture = []

for i in big_picture:
    if len(i) != i.count(None):
        final_picture.append([x for x in i if x is not None])


scaled_pic_side = (len(tile) - 2) * len(final_picture)

scaled_picture = [[None for _ in range(scaled_pic_side)] for _ in range(scaled_pic_side)]

for i, line in enumerate(final_picture):
    for j, tile_name in enumerate(line):
        for y in range(1, len(tile)-1):
            for x in range(1, len(tile)-1):
                scaled_picture[i*(len(tile)-2) + y - 1][j*(len(tile)-2) + x - 1] = tiles[tile_name][y][x]



sea_monster = []
with open('sea_monster.txt') as f:
    for line in f.readlines():
        sea_monster.append(['#' if x == '#' else 'o' for x in line])

new_scaled_pic = [[x for x in line] for line in scaled_picture]

drakes = 0

for fl in range(2):
    scaled_picture = flip(scaled_picture)
    new_scaled_pic = flip(new_scaled_pic)
    for rotation in range(4):
        scaled_picture = rotate(scaled_picture)
        new_scaled_pic = rotate(new_scaled_pic)
        for y in range(len(new_scaled_pic) - len(sea_monster) + 1):
            for x in range(len(new_scaled_pic) - len(sea_monster[0]) + 1):
                drake = 0
                br = False
                for i, line in enumerate(sea_monster):
                    if br: break
                    for j, znak in enumerate(line):
                        if znak == '#':
                            if scaled_picture[y+i][x+j] == '#':
                                drake += 1
                            else:
                                br = True
                                break
                if drake == 15:
                    for i, line in enumerate(sea_monster):
                        for j, znak in enumerate(line):
                            if znak == '#':
                                new_scaled_pic[y+i][x+j] = 'O'


new_scaled_pic = rotate(new_scaled_pic)

res = 0
for i in new_scaled_pic:
    for j in i:
        if j == '#':
            res += 1

print(res)

for i in new_scaled_pic:
    print("".join(i))

