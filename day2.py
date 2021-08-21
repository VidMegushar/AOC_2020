with open('input2.txt') as f:
    data = [i for i in f.readlines()]

cor = 0
for line in data:
    n, l, password = line.split(" ")
    n1, n2, = n.split("-")
    l = l.strip(":")

    num = password.count(l)

    if (password[int(n1)-1] == l) ^ (password[int(n2)-1] == l):      
        cor += 1

print(cor)
