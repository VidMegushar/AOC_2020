with open('input19_rules.txt') as f:
    rules = dict()
    for line in f.readlines():
        i, rule = line.split(':')
        rule = rule.strip().split("|")
        rule = [[i.strip('"') for i in r.strip().split(" ")] for r in rule]
        rules[i] = rule

rules['a'] = [['a']]
rules['b'] = [['b']]

with open('input19_string.txt') as f:
    strings = [line.strip() for line in f.readlines()]


def update_rules(rule):
    new_rule = [[]]
    for i in rule:
        temp_rule = rules[i]
        if len(temp_rule) == 1:
            new_rule = [l + temp_rule[0] for l in new_rule]
        else:
            rules_list = [i for i in new_rule]
            new_rule = []
            for r in rules_list:
                new_rule.append(r + temp_rule[0])
                new_rule.append(r + temp_rule[1])
    return new_rule


rules42 = []

finished_rules_42 = []
all_rules = rules['42']

def get_rules(all_rules):
    finished_rules = []
    while len(all_rules) > 0:
        new_all_rules = []
        for r in all_rules:
            new_all_rules += update_rules(r)
        all_rules = []
        for i,r in enumerate(new_all_rules):
            if r.count('a') + r.count('b') == len(r):
                finished_rules.append("".join(r))
            else:
                all_rules.append(r)
    return finished_rules

finished_rules_42 = get_rules(rules['42'])
finished_rules_31 = get_rules(rules['31'])

print(finished_rules_42[:5])
print(finished_rules_31[:5])



finished_rules_42 = set(finished_rules_42)
finished_rules_31 = set(finished_rules_31)
correct_strings = 0

def check_string(s):
    v = 42
    count42 = 0
    count31 = 0
    for i in range(len(s)//8):
        if v == 42:
            if s[i*8:(i+1)*8] in finished_rules_42:
                count42 += 1
            else:
                v = 31
                if s[i*8:(i+1)*8] in finished_rules_31:
                    count31 += 1
        else:
            if s[i*8:(i+1)*8] in finished_rules_31:
                    count31 += 1
    if count31 + count42 == len(s)//8 and count31 < count42 and count31 > 0:
        return True
    return False

for s in strings:
    if check_string(s):
        correct_strings += 1


print('correct_strings')
print(correct_strings)
