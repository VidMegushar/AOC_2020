from collections import deque
import time

t = time.time()

player1 = []
player2 = []

with open('input22.txt') as f:
    lines = f.read()
    p1, p2 = lines.split("\n\n")
    player1 = [int(i) for i in p1.split("\n")[1:]]
    player2 = [int(i) for i in p2.split("\n")[1:]]


def create_state_word(player1, player2):
    return "".join([str(x) + '.' for x in list(player1)])


def game(player1, player2):
    all_games = set()
    while True:
        game_word = create_state_word(player1, player2)
        if game_word in all_games:
            return ('p1', player1)
        else:
            all_games.add(game_word)

        if len(player1) == 0:
            return ('p2', player2)

        if len(player2) == 0:
            return ('p1', player1)

        c1, player1 = player1[0], player1[1:]
        c2, player2 = player2[0], player2[1:]

        if c1 <= len(player1) and c2 <= len(player2):
            winner, _ = game(player1[:c1], player2[:c2])
            if winner == 'p1':
                player1.append(c1)
                player1.append(c2)
            else:
                player2.append(c2)
                player2.append(c1)
        else:
            if c1 > c2:
                player1.append(c1)
                player1.append(c2)
            else:
                player2.append(c2)
                player2.append(c1)


_ , winner = game(player1, player2)

res = 0
l = len(winner)
for i in range(l):
    x = winner.pop()
    res += (i+1)*x

print(res)
print(time.time() - t)