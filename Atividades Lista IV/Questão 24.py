import random

t = 5
m = [[random.randint(0,9) for i in range(t)] for i in range(t)]
s = 0

for i in range(t):
    print(m[i])

print()

for i in range(t):
    for j in range(t):
        s += m[i][j]
    print("A soma da linha",i+1,"é:",s)
    s = 0

print()

for i in range(t):
    for j in range(t):
        s += m[j][i]
    print("A soma da coluna",i+1,"é:",s)
    s = 0