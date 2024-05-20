import random

t = 5
m = [[random.randint(0,9) for i in range(t)] for i in range(t)]
s = 0

for i in range (t):
    print(m[i])

for i in range (t):
    for j in range (t):
        s += m[j][i]
    r = s / t
    print("A media da coluna é:",r)
    s = 0