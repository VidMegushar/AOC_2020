with open('input8.txt') as f:
    inst = [line.strip().split(" ") for line in f.readlines()]

pos = 0
acc = 0
all_pos = set()

def try_run(inst):
    pos = 0
    acc = 0
    all_pos = set()
    run = True
    while pos < len(inst):
        if pos in all_pos:
            run = False
            break
        all_pos.add(pos)

        tmp_inst = inst[pos][0]
        tmp_ammount = int(inst[pos][1])

        if tmp_inst == 'nop':
            pos += 1
        elif tmp_inst == 'acc':
            pos += 1
            acc += tmp_ammount
        elif tmp_inst == 'jmp':
            pos += tmp_ammount
    
    if run:
        print("try_run: " + str(acc))


for i, val in enumerate(inst):
    if val[0] == 'nop':
        tmp_inst = inst.copy()
        tmp_inst[i] = ['jmp', val[1]]
        try:
            try_run(tmp_inst)
        except:
            continue
    elif val[0] == 'jmp':
        tmp_inst = inst.copy()
        tmp_inst[i] = ['nop', val[1]]
        try:
            try_run(tmp_inst)
        except:
            continue
    
        