import string

def get_row(row_word):
    row = 0
    for i in range(7):
        if row_word[i] == 'B':
            row += 2**(6-i)
    return row

def get_col(col_word):
    col = 0
    for i in range(3):
        if col_word[i] == 'R':
            col += 2**(2-i)
    return col

ids = []
with open('input5.txt') as f:
    for line in f.readlines():
        line = line.strip()
        row = get_row(line[:7])
        col = get_col(line[7:])
        ids.append(row * 8 + col)

print(max(ids))
print(sorted(ids))
print(get_row('FFFBBBF'))

