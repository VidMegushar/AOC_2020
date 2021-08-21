import string

def get_number(value, mask):
    mask = mask[::-1]
    value = value[::-1]
    new_val = [int(value[i])*(2**i) if n == 'X' else int(n)*(2**i) for i,n in enumerate(mask)]
    new_val = sum(new_val)
    return new_val

def part2(mask, mem_pos):
    all_memory = [""]
    new_val = [mem_pos[i] if n == '0' else n for i,n in enumerate(mask)]
    for v in new_val:
        if v != 'X':
            all_memory = [i+v for i in all_memory]
        else:
            all_memory = [i +'1' for i in all_memory] + [i +'0' for i in all_memory]

    all_memory = [int(i,2) for i in all_memory]

    return all_memory

memory = dict()
with open('input14.txt') as f:
    for line in f.readlines():
        if line.split(" ")[0] == 'mask':
            mask = line.strip().split(" ")[2]
        else:
            line = line.split("[")[1]
            mem_pos = int(line.split("]")[0])
            value = int(line.split(" ")[2])
            # value = "{0:b}".format(value)
            # pad = "0"*(36 - len(value))
            # value = pad + value

            # Part 1
            # new_val = get_number(value, mask)
            # memory[mem_pos] = new_val

            # Part 2
            mem_pos = "{0:b}".format(mem_pos)
            pad = "0"*(36 - len(mem_pos))
            mem_pos = pad + mem_pos
            all_memory = part2(mask, mem_pos)
            for m in all_memory:
                memory[m] = value



print(sum(memory.values()))
