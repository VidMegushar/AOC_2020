import string

with open('input4.txt') as f:
    data = [i.strip() for i in f.readlines()]

valid_pass = 0
passport = []
for line in data:
    if len(line) < 3:
        passport = set(passport)
        if len(passport) == 7:
            valid_pass += 1
        passport = []
    else:
        for i in line.split(" "):
            code, value = i.split(':')
            if code == 'byr':
                if value.isnumeric():
                    if int(value) >= 1920 and int(value) <= 2002:
                        passport.append(code)
            elif code == 'iyr':
                if value.isnumeric():
                    if int(value) >= 2010 and int(value) <= 2020:
                        passport.append(code)
            elif code == 'eyr':
                if value.isnumeric():
                    if int(value) >= 2020 and int(value) <= 2030:
                        passport.append(code)
            elif code == 'hgt':
                if value[-2:] == 'cm':
                    if int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
                        passport.append(code)
                elif value[-2:] == 'in':
                    if int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
                        passport.append(code)
            elif code == 'hcl':
                if len(value) == 7:
                    if value[0] == '#':
                        if all(c in string.hexdigits for c in value[1:]):
                            passport.append(code)
            elif code == 'ecl':
                if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    passport.append(code)
            elif code == 'pid':
                if value.isnumeric() and len(value) == 9:
                    passport.append(code)

passport = set(passport)
if len(passport) == 7:
    valid_pass += 1
passport = []

print(valid_pass)