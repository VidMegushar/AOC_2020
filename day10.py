with open('input10.txt') as f:
    data = [0] + [int(line.strip()) for line in f.readlines()]

data = sorted(data)

ones = 0
threes = 0
for i in range(len(data)-1):
    if data[i+1] - data[i] == 1:
        ones += 1
    elif data[i+1] - data[i] == 3:
        threes += 1

print(ones, threes+1, ones*(threes+1))
    

# PART 2
data.reverse()
calculated = dict()


def calculate(data):
    if data[0] in calculated:
        return calculated[data[0]]
    if len(data) == 1:
        calculated[data[0]] = 1
        return 1
    elif len(data) == 2:
        calculated[data[0]] = 1
        return 1
    elif len(data) == 3:
        if data[0] - data[2] <= 3:
            calculated[data[0]] = calculate(data[1:]) + calculate(data[2:])
        else:
            calculated[data[0]] = calculate(data[1:])
        return calculated[data[0]]
    else:
        if data[0] - data[3] <= 3:
            calculated[data[0]] = calculate(data[1:]) + calculate(data[2:]) + calculate(data[3:])
        elif data[0] - data[2] <= 3:
            calculated[data[0]] = calculate(data[1:]) + calculate(data[2:])
        else:
            calculated[data[0]] = calculate(data[1:])
        return calculated[data[0]]

print(calculate(data))
